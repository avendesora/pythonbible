use regex::Regex;
use std::collections::HashMap;

use crate::books::Book;
use crate::normalized_reference::NormalizedReference;
use crate::regular_expressions::SCRIPTURE_REFERENCE_REGULAR_EXPRESSION;
use crate::roman_numeral_util::convert_all_roman_numerals_to_integers;
use crate::validator::is_valid_reference;
use crate::verses::{get_number_of_chapters, get_number_of_verses, is_single_chapter_book};

const COLON: &str = ":";
const COMMA: &str = ",";
const DASH: &str = "-";
const HTML_MDASH: &str = "&mdash;";
const HTML_NDASH: &str = "&ndash;";
const PERIOD: &str = ".";

pub fn get_references(text: &str, book_groups: Option<&HashMap<&str, Vec<Book>>>, bible: Option<&crate::bible::Bible>) -> Vec<NormalizedReference> {
    let mut references: Vec<NormalizedReference> = Vec::new();

    // Replace roman numerals and HTML dashes
    let mut clean_text = convert_all_roman_numerals_to_integers(text);
    clean_text = clean_text.replace(HTML_NDASH, DASH).replace(HTML_MDASH, DASH);

    let scripture_re = Regex::new(SCRIPTURE_REFERENCE_REGULAR_EXPRESSION).expect("invalid scripture regex");
    for mat in scripture_re.find_iter(&clean_text) {
        references.extend(normalize_reference(mat.as_str(), bible));
    }

    if let Some(groups) = book_groups {
        references.extend(_get_book_group_references(&clean_text, groups));
    }

    references
}

pub fn normalize_reference(reference: &str, bible: Option<&crate::bible::Bible>) -> Vec<NormalizedReference> {
    let mut references: Vec<NormalizedReference> = Vec::new();
    let mut books: Vec<Book> = Vec::new();
    let mut cleaned_references: Vec<String> = Vec::new();
    let mut reference_without_books = reference.to_string();
    let mut book_found = true;

    // iterate over books, finding book name matches at start or continuing segments
    while book_found {
        book_found = false;

        for book in Book::iter() {
            let book_re = Regex::new(book.regular_expression()).expect("invalid book regex");
            if let Some(cap) = book_re.find(&reference_without_books) {
                let start = cap.start();
                let end = cap.end();

                if start != 0 && books.is_empty() {
                    continue;
                }

                book_found = true;

                if !books.is_empty() {
                    cleaned_references.push(reference_without_books[..start].to_string());
                }

                reference_without_books = reference_without_books[end..].to_string();
                books.push(book);
            }
        }
    }

    cleaned_references.push(reference_without_books);

    // Require at least one book found
    if books.is_empty() {
        return references;
    }

    // First book
    let first_book_references = _process_sub_references(&books[0], cleaned_references[0].trim(), bible);

    if books.len() == 1 {
        return first_book_references;
    }

    // Second book
    let second_book_references = _process_sub_references(&books[1], cleaned_references[1].trim(), bible);

    if first_book_references.len() > 1 {
        references.extend(first_book_references[..first_book_references.len()-1].iter().cloned());
    }

    let last_first_reference = first_book_references.last().expect("expected at least one reference").clone();
    let first_second_reference = second_book_references.first().expect("expected at least one reference").clone();

    references.push(NormalizedReference {
        book: last_first_reference.book.clone(),
        start_chapter: last_first_reference.start_chapter,
        start_verse: last_first_reference.start_verse,
        end_chapter: first_second_reference.end_chapter,
        end_verse: first_second_reference.end_verse,
        end_book: first_second_reference.end_book.clone(),
    });

    if second_book_references.len() > 1 {
        references.extend(second_book_references.into_iter().skip(1));
    }

    references
}

fn _process_sub_references(book: &Book, reference: &str, bible: Option<&crate::bible::Bible>) -> Vec<NormalizedReference> {
    let mut references: Vec<NormalizedReference> = Vec::new();
    let mut start_chapter: Option<i32> = None;

    for sub in reference.split(COMMA) {
        let sub = sub.trim();
        if (sub.is_empty() || sub == DASH || sub == PERIOD) && references.is_empty() {
            references.push(NormalizedReference {
                book: book.clone(),
                start_chapter: None,
                start_verse: None,
                end_chapter: None,
                end_verse: None,
                end_book: book.clone(),
            });
            continue;
        }

        let to_process = if sub.ends_with(DASH) { &sub[..sub.len()-1] } else { sub };
        let (sc, sv, ec, ev) = _process_sub_reference(to_process, book, start_chapter);

        let new_reference = NormalizedReference {
            book: book.clone(),
            start_chapter: sc,
            start_verse: sv,
            end_chapter: ec,
            end_verse: ev,
            end_book: book.clone(),
        };

        if is_valid_reference(&new_reference, bible) {
            references.push(new_reference);
        }

        start_chapter = ec;
    }

    references
}

fn _process_sub_reference(sub_reference: &str, book: &Book, start_chapter: Option<i32>) -> (Option<i32>, Option<i32>, Option<i32>, Option<i32>) {
    let mut start_verse: Option<i32> = None;
    let mut end_chapter: Option<i32> = None;
    let mut end_verse: Option<i32> = None;
    let mut no_verses = false;

    let clean_sub = sub_reference.replace(PERIOD, COLON);
    let chapter_and_verse_range: Vec<&str> = clean_sub.split(DASH).collect();
    let min_chapter_and_verse: Vec<&str> = chapter_and_verse_range[0].trim().split(COLON).collect();

    let mut sc = start_chapter;

    if min_chapter_and_verse.len() == 1 {
        if sc.is_some() {
            start_verse = Some(min_chapter_and_verse[0].trim().parse().ok().expect("invalid number"));
        } else if is_single_chapter_book(book) {
            sc = Some(1);
            start_verse = Some(min_chapter_and_verse[0].trim().parse().ok().expect("invalid number"));
        } else {
            sc = Some(min_chapter_and_verse[0].trim().parse().ok().expect("invalid number"));
            no_verses = true;
        }
    } else if min_chapter_and_verse.len() == 2 {
        sc = Some(min_chapter_and_verse[0].trim().parse().ok().expect("invalid number"));
        start_verse = Some(min_chapter_and_verse[1].trim().parse().ok().expect("invalid number"));
    }

    if chapter_and_verse_range.len() > 1 {
        let max_chapter_and_verse: Vec<&str> = chapter_and_verse_range[1].split(COLON).collect();

        if max_chapter_and_verse.len() == 1 {
            if no_verses {
                end_chapter = Some(max_chapter_and_verse[0].trim().parse().ok().expect("invalid number"));
            } else {
                end_chapter = sc;
                end_verse = Some(max_chapter_and_verse[0].trim().parse().ok().expect("invalid number"));
            }
        } else if max_chapter_and_verse.len() == 2 {
            end_chapter = Some(max_chapter_and_verse[0].trim().parse().ok().expect("invalid number"));
            end_verse = Some(max_chapter_and_verse[1].trim().parse().ok().expect("invalid number"));
        }
    }

    if end_chapter.is_none() {
        end_chapter = sc;
    }
    if end_verse.is_none() {
        end_verse = start_verse;
    }

    (sc, start_verse, end_chapter, end_verse)
}

fn _get_book_group_references(text: &str, book_groups: &HashMap<&str, Vec<Book>>) -> Vec<NormalizedReference> {
    let mut references: Vec<NormalizedReference> = Vec::new();

    let joined = book_groups.keys().cloned().collect::<Vec<&str>>().join("|");
    let book_group_regex = Regex::new(&joined).expect("invalid book group regex");

    for mat in book_group_regex.find_iter(text) {
        references.extend(_process_book_group_match(mat.as_str(), book_groups));
    }

    references
}

fn _process_book_group_match(text: &str, book_groups: &HashMap<&str, Vec<Book>>) -> Vec<NormalizedReference> {
    let mut references: Vec<NormalizedReference> = Vec::new();

    let mut books: &Vec<Book> = &Vec::new();
    for (re, group_books) in book_groups {
        let re = Regex::new(re).expect("invalid book group regex");
        if re.is_match(text) {
            books = group_books;
            break;
        }
    }

    if books.is_empty() {
        return references;
    }

    let mut start_book = books[0].clone();
    let mut previous_book = start_book.clone();

    for book in books.iter().skip(1) {
        if book.value() == previous_book.value() + 1 {
            previous_book = book.clone();
            continue;
        }

        references.push(_build_book_group_reference(start_book.clone(), previous_book.clone()));
        start_book = book.clone();
        previous_book = book.clone();
    }

    references.push(_build_book_group_reference(start_book, previous_book));

    references
}

fn _build_book_group_reference(start_book: Book, end_book: Book) -> NormalizedReference {
    let max_chapter = get_number_of_chapters(&end_book);
    let max_verse = get_number_of_verses(&end_book, max_chapter);
    NormalizedReference {
        book: start_book,
        start_chapter: Some(1),
        start_verse: Some(1),
        end_chapter: Some(max_chapter),
        end_verse: Some(max_verse),
        end_book,
    }
}