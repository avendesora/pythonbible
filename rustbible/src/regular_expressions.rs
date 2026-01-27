use once_cell::sync::Lazy;
use fancy_regex::Regex;
use crate::books::BOOKS;

/// Compiles the scripture reference regex on first use and exposes it as a static.
pub static SCRIPTURE_REFERENCE_REGULAR_EXPRESSION: Lazy<Regex> = Lazy::new(|| {
    // Basic token fragments (mirrors the Python constants).
    let digit = r"(\d{1,3})";
    let space = r"\s*";

    // Compose separators using `space`.
    let colon = format!(r"{}([:.]){}", space, space); // captures ':' or '.'
    let dash = format!(r"{}-{}", space, space);
    let comma = format!(r"{} , {}", space, space).replace(" , ", ","); // keep consistent spacing pattern
    // The above replace ensures the comma string is like f"{SPACE},{SPACE}"

    // Build BOOK by joining each book's regular_expression
    let book_parts: Vec<String> = BOOKS.iter().map(|b| b.regular_expression.clone()).collect();
    let book = format!(r"\b({})\b\.*", book_parts.join("|"));

    // Chapter / Verse tokens
    let chapter = digit;
    let verse = digit;

    // CHAPTER_AND_VERSE: (CHAPTER (COLON VERSE)?)
    let chapter_and_verse = format!(r"({}(?:{}{})?)", chapter, colon, verse);

    // RANGE
    // f"{DASH}(({BOOK}{SPACE}(?:{CHAPTER_AND_VERSE})?)|{CHAPTER_AND_VERSE}|{VERSE})"
    let range = format!(
        r"{}(({}{}(?:{})?)|{}|{})",
        dash, book, space, chapter_and_verse, chapter_and_verse, verse
    );

    // ADDITIONAL_REFERENCE: f"({COMMA}({CHAPTER_AND_VERSE}(?:{RANGE})?|{VERSE}))"
    let additional_reference = format!(r"({}({}(?:{})?|{}))", comma, chapter_and_verse, range, verse);

    // FULL_CHAPTER_AND_VERSE: f"({CHAPTER_AND_VERSE}(?:{RANGE})?({ADDITIONAL_REFERENCE})*)"
    let full_chapter_and_verse = format!(r"({}(?:{})?({})*)", chapter_and_verse, range, additional_reference);

    // FULL_BOOK: f"({BOOK}){SPACE}(?:{FULL_CHAPTER_AND_VERSE})?"
    let full_book = format!(r"({}){}(?:{})?", book, space, full_chapter_and_verse);

    // CROSS_BOOK: f"({FULL_BOOK}(?:{DASH}({FULL_BOOK}))?)"
    let cross_book = format!(r"({}(?:{}({}))?)", full_book, dash, full_book);

    // Compile case-insensitive (Python used IGNORECASE | UNICODE). Rust `(?i)` sets case-insensitive.
    let pattern = format!(r"(?i){}", cross_book);

    Regex::new(&pattern).expect("failed to compile scripture reference regex")
});

/// Convenience accessor returning a reference to the compiled regex.
pub fn scripture_reference_regex() -> &'static Regex {
    &*SCRIPTURE_REFERENCE_REGULAR_EXPRESSION
}

#[cfg(test)]
mod tests {
    use fancy_regex::Regex;
    use crate::Book;
    use crate::books::BOOKS;
    use crate::regular_expressions::scripture_reference_regex;

    fn build_common_fragments() -> (String, String, String, String, String, String) {
        // mirrors the construction inside the library
        let digit = r"(\d{1,3})".to_string();
        let space = r"\s*".to_string();
        let colon = format!(r"{}([:.]){}", space, space); // captures ':' or '.'
        let dash = format!(r"{}-{}", space, space);
        let comma = format!(r"{} , {}", space, space).replace(" , ", ","); // keep consistent spacing pattern
        // Build BOOK by joining each book's regular_expression
        let book_parts: Vec<String> = BOOKS.iter().map(|b| b.regular_expression.clone()).collect();
        let book = format!(r"\b({})\b\.*", book_parts.join("|"));

        (digit, space, colon, dash, comma, book)
    }

    #[test]
    fn test_chapter_regular_expression() {
        let (digit, _, _, _, _, _) = build_common_fragments();
        let re = Regex::new(&digit).expect("compile digit");
        let text = "The chapter number is 132.";
        let m = re.find(text).expect("find failed").expect("should match chapter");
        assert_eq!(m.as_str(), "132");
    }

    #[test]
    fn test_verse_regular_expression() {
        let (digit, _, _, _, _, _) = build_common_fragments();
        let re = Regex::new(&digit).expect("compile digit");
        let text = "The verse number is 25.";
        let m = re.find(text).expect("find failed").expect("should match verse");
        assert_eq!(m.as_str(), "25");
    }

    #[test]
    fn test_chapter_and_verse_regular_expression() {
        let (digit, _space, colon, _dash, _comma, _book) = build_common_fragments();
        let chapter_and_verse = format!(r"({}(?:{}{})?)", digit, colon, digit);
        let re = Regex::new(&chapter_and_verse).expect("compile chap_and_verse");

        let references = ["1:2", "3", "142 : 5", "43:    324"];
        for &reference in references.iter() {
            let text = format!("The chapter and verse reference is {}.", reference);
                let m = re.find(&text).expect("find failed").expect("should match chapter_and_verse");
            assert_eq!(m.as_str(), reference);
        }
    }

    #[test]
    fn test_range_regular_expression() {
        let (digit, space, colon, dash, _comma, book) = build_common_fragments();
        let chapter_and_verse = format!(r"({}(?:{}{})?)", digit, colon, digit);
        // RANGE: f"{DASH}(({BOOK}{SPACE}(?:{CHAPTER_AND_VERSE})?)|{CHAPTER_AND_VERSE}|{VERSE})"
        let range = format!(
            r"{}(({}{}(?:{})?)|{}|{})",
            dash, book, space, chapter_and_verse, chapter_and_verse, digit
        );
        let re = Regex::new(&range).expect("compile range");

        let cases = vec![
            ("1:2-3", "-3"),
            ("3-4", "-4"),
            ("142 : 5 - 53 : 23", " - 53 : 23"),
            ("43:    324 - 325", " - 325"),
            ("Genesis - Deuteronomy", " - Deuteronomy"),
            ("Genesis 1 - Exodus 2", " - Exodus 2"),
            ("Genesis 1:1 - Exodus 2:2", " - Exodus 2:2"),
        ];

        for (reference, expected) in cases {
            let text = format!("The chapter range reference is {}", reference);
            let m = re.find(&text).expect("find failed").expect("should match range");
            assert_eq!(m.as_str(), expected);
        }
    }

    #[test]
    fn test_additional_reference_regular_expression() {
        let (digit, _space, colon, dash, comma, _book) = build_common_fragments();
        let chapter_and_verse = format!(r"({}(?:{}{})?)", digit, colon, digit);
        // Build a range-like piece for use in additional_reference tests (using empty book placeholder)
        let range_lib = format!(r"{}(({}(?:{})?)|{}|{})", dash, "", chapter_and_verse, chapter_and_verse, digit);
        // ADDITIONAL_REFERENCE: f"({COMMA}({CHAPTER_AND_VERSE}(?:{RANGE})?|{VERSE}))"
        let additional_reference = format!(r"({}({}(?:{})?|{}))", comma, chapter_and_verse, range_lib, digit);
        let full_chapter_and_verse = format!(r"({}(?:{})?({})*)", chapter_and_verse, range_lib, additional_reference);
        let re = Regex::new(&full_chapter_and_verse).expect("compile full_chapter_and_verse");

        let references = [
            "1:2,4",
            "3-4,6",
            "123 : 5 - 13, 16 - 18",
            "32:43-45,54,33:12",
        ];

        for &reference in references.iter() {
            let text = format!("The additional reference is {}.", reference);
            let m = re.find(&text).expect("find failed").expect("should match full chapter and verse");
            assert_eq!(m.as_str(), reference);
        }
    }

    #[test]
    fn test_multiple_additional_references() {
        // Use the compiled scripture_reference_regex to extract the inner chapter/verse tails
        let text = "You should read Matthew 1:18 - 2:18, Luke 3: 5-7, Psalm 130:4,8 and Jeremiah 29:32-30:10,11";
        let scripture_re = scripture_reference_regex();
        let mut found: Vec<String> = Vec::new();
        for mat_res in scripture_re.find_iter(text) {
            let mat = mat_res.expect("find_iter item failed");
            let s = mat.as_str().to_string();
            if let Some(pos) = s.find(' ') {
                let tail = s[pos+1..].trim().to_string();
                found.push(tail);
            }
        }
        assert_eq!(found.len(), 4);
        assert_eq!(found[0], "1:18 - 2:18");
        assert_eq!(found[1], "3: 5-7");
        assert_eq!(found[2], "130:4,8");
        assert_eq!(found[3], "29:32-30:10,11");
    }

    #[test]
    fn test_multiple_full_references() {
        let text = "You should read Matthew 1:18 - 2:18, Luke 3: 5-7, Psalm 130:4,8 and Jeremiah 29:32-30:10,11";
        let scripture_re = scripture_reference_regex();
        let matches: Vec<String> = scripture_re
            .find_iter(text)
            .filter_map(|r| r.ok().map(|m| m.as_str().to_string()))
            .collect();
        assert_eq!(matches.len(), 4);
        assert_eq!(matches[0], "Matthew 1:18 - 2:18");
        assert_eq!(matches[1], "Luke 3: 5-7");
        assert_eq!(matches[2], "Psalm 130:4,8");
        assert_eq!(matches[3], "Jeremiah 29:32-30:10,11");
    }

    #[test]
    fn test_multiple_full_references_case_insensitive() {
        let text = "You should read Matthew 1:18 - 2:18, Luke 3: 5-7, Psalm 130:4,8 and Jeremiah 29:32-30:10,12".to_lowercase();
        let scripture_re = scripture_reference_regex();
    let matches: Vec<String> = scripture_re
        .find_iter(&text)
        .filter_map(|r| r.ok().map(|m| m.as_str().to_string()))
        .collect();
        assert_eq!(matches.len(), 4);
        assert_eq!(matches[0], "Matthew 1:18 - 2:18".to_lowercase());
        assert_eq!(matches[1], "Luke 3: 5-7".to_lowercase());
        assert_eq!(matches[2], "Psalm 130:4,8".to_lowercase());
        assert_eq!(matches[3], "Jeremiah 29:32-30:10,12".to_lowercase());
    }

    #[test]
    fn test_reference_with_no_verses() {
        let text = "The ten commandments can be found in Exodus 20.";
        let scripture_re = scripture_reference_regex();
        let matches: Vec<String> = scripture_re
            .find_iter(text)
            .filter_map(|r| r.ok().map(|m| m.as_str().to_string()))
            .collect();
        assert_eq!(matches.len(), 1);
        assert_eq!(matches[0], "Exodus 20");
    }

    #[test]
    fn test_philemon_not_philippians() {
        // given a string with a Philemon reference
        let text = "Philemon 1:9";

        // when evaluating the string to see if it matches the Philippians regular expression
        let philippians = Book::Philippians.item();
        let philippians_re = Regex::new(&format!(r"(?i){}", philippians.regular_expression)).expect("compile philippians");

        // then the matches are not found
        assert!(philippians_re.find(text).ok().flatten().is_none());

        // when evaluating the string to see if it matches the Philemon regular expression
        let philemon = Book::Philemon.item();
        let philemon_re = Regex::new(&format!(r"(?i){}", philemon.regular_expression)).expect("compile philemon");

        // then the match is found
        let matches: Vec<_> = philemon_re.find_iter(text).collect();
        assert_eq!(matches.len(), 1);
    }

    #[test]
    fn test_cross_book_regex() {
        let text = "The books of the law are Genesis - Deuteronomy";
        // Rebuild CROSS_BOOK pattern shape similar to library
        let (digit, space, colon, dash, _comma, book) = build_common_fragments();
        let chapter_and_verse = format!(r"({}(?:{}{})?)", digit, colon, digit);
        let range = format!(
            r"{}(({}{}(?:{})?)|{}|{})",
            dash, book, space, chapter_and_verse, chapter_and_verse, digit
        );
        let additional_reference = format!(r"({}({}(?:{})?|{}))", ",", chapter_and_verse, range, digit);
        let full_chapter_and_verse = format!(r"({}(?:{})?({})*)", chapter_and_verse, range, additional_reference);
        let full_book = format!(r"({}){}(?:{})?", book, space, full_chapter_and_verse);
        let cross_book = format!(r"({}(?:{}({}))?)", full_book, dash, full_book);
        let cross_re = Regex::new(&format!(r"(?i){}", cross_book)).expect("compile cross_book");

        let matches: Vec<_> = cross_re
            .find_iter(text)
            .filter_map(|r| r.ok().map(|m| m.as_str().to_string()))
            .collect();
        assert_eq!(matches.len(), 1);
        assert_eq!(matches[0], "Genesis - Deuteronomy");
    }

    #[test]
    fn test_jo() {
        // "Jo" should match John but not Joshua/Job/Jonah
        let john = Book::John.item();
        let john_re = Regex::new(&format!(r"(?i){}", john.regular_expression)).expect("compile john");

        let text = "Jo 1:1";
        let matches: Vec<_> = john_re.find_iter(text).collect();
        assert_eq!(matches.len(), 1);

        let negatives = ["Joshua", "Job", "Jonah"];
        for s in negatives.iter() {
            let t = format!("{} 1:1", s);
            let m = john_re.find(&t);
            assert!(m.ok().flatten().is_none(), "unexpected john match for '{}'", t);
        }
    }

    #[test]
    fn test_jud() {
        // "Jud" should match Jude but not Judges
        let jude = Book::Jude.item();
        let jude_re = Regex::new(&format!(r"(?i){}", jude.regular_expression)).expect("compile jude");

        let text = "Jud 1:1";
        let matches: Vec<_> = jude_re.find_iter(text).collect();
        assert_eq!(matches.len(), 1);

        let text2 = "Judges 1:1";
        let m = jude_re.find(text2);
        assert!(m.ok().flatten().is_none());
    }
}
