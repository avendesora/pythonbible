use crate::books::BookItem;
use crate::normalized_reference::NormalizedReference;
use crate::verses::{
    get_number_of_chapters, get_number_of_verses, get_verse_id,
    VERSE_IDS,
};
use crate::bible::Bible;

/// Check to see if the given verse_id corresponds to a valid verse in the Bible.
pub fn is_valid_verse_id(verse_id: i32, bible: Option<&Bible>) -> bool {
    if let Some(b) = bible {
        return b.is_valid_verse_id(verse_id);
    }
    if verse_id <= 0 {
        return false;
    }

    VERSE_IDS.contains(&(verse_id as usize))
}

/// Check to see if the given NormalizedReference is a valid scripture reference.
///
/// (i.e. all of the verses in the reference are valid verses)
pub fn is_valid_reference(
    reference: &NormalizedReference,
    bible: Option<&Bible>,
) -> bool {
    // start defaults
    // start defaults
    let start_book = &reference.book;
    let start_chapter = reference.start_chapter.map(|c| c as i32).unwrap_or(1);
    let start_verse = reference.start_verse.map(|v| v as i32).unwrap_or(1);

    if !is_valid_verse(start_book, start_chapter, start_verse, bible) {
        return false;
    }

    let end_book = reference.end_book.as_ref().unwrap_or(start_book);
    let end_chapter = match reference.end_chapter.map(|c| c as i32) {
        Some(c) => c,
        None => match get_number_of_chapters(end_book, bible) {
            Ok(n) => n as i32,
            Err(_) => return false,
        },
    };
    let end_verse = match reference.end_verse.map(|v| v as i32) {
        Some(v) => v,
        None => match get_number_of_verses(end_book, end_chapter as usize, bible) {
                Ok(n) => n as i32,
            Err(_) => return false,
        },
    };

    if !is_valid_verse(end_book, end_chapter, end_verse, bible) {
        return false;
    }

    let start_verse_id = match get_verse_id(start_book, start_chapter as usize, start_verse as usize, bible) {
        Ok(id) => id,
        Err(_) => return false,
    };
    let end_verse_id = match get_verse_id(end_book, end_chapter as usize, end_verse as usize, bible) {
        Ok(id) => id,
        Err(_) => return false,
    };
    start_verse_id <= end_verse_id
}

/// Check to see if the given book is a valid book of the Bible.
pub fn is_valid_book(book: &BookItem, bible: Option<&Bible>) -> bool {
    if let Some(b) = bible {
        match get_verse_id(book, 1, 1, Some(b)) {
            Ok(id) => return b.is_valid_verse_id(id as i32),
            Err(_) => return false,
        }
    }

    // In Rust the type system guarantees `book` is a Book, so it's valid when no `Bible` is provided.
    true
}

/// Check to see if the given chapter is valid for `book`.
pub fn is_valid_chapter(book: &BookItem, chapter: i32, bible: Option<&Bible>) -> bool {
    if !is_valid_book(book, bible) {
        return false;
    }

    if chapter <= 0 {
        return false;
    }

    if bible.is_none() {
        match get_number_of_chapters(book, bible) {
            Ok(n) => return (1..=(n as i32)).contains(&chapter),
            Err(_) => return false,
        }
    }

    // When a `Bible` is provided, consult its max_verses map.
    if let Some(b) = bible {
        match get_number_of_chapters(book, Some(b)) {
            Ok(n) => return (1..=(n as i32)).contains(&chapter),
            Err(_) => return false,
        }
    }

    false
}

/// Check to see if the given book, chapter, and verse are valid.
pub fn is_valid_verse(book: &BookItem, chapter: i32, verse: i32, bible: Option<&Bible>) -> bool {
    if !is_valid_chapter(book, chapter, bible) {
        return false;
    }

    if verse <= 0 {
        return false;
    }

    let max_verse = match get_number_of_verses(book, chapter as usize, bible) {
        Ok(n) => n as i32,
        Err(_) => return false,
    };
    (1..=max_verse).contains(&verse)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::verses::VERSE_IDS;
    // use crate::versions::Version;

    #[test]
    fn test_is_valid_verse_id_valid() {
        let id = *VERSE_IDS.first().expect("no verse ids") as i32;
        assert!(is_valid_verse_id(id, None));
    }

    #[test]
    fn test_is_valid_verse_id_negative() {
        assert!(!is_valid_verse_id(-1, None));
    }

    #[test]
    fn test_is_valid_verse_id_too_large() {
        let max = *VERSE_IDS.iter().max().unwrap_or(&0);
        let id = (max + 1) as i32;
        assert!(!is_valid_verse_id(id, None));
    }

    // #[test]
    // fn test_is_valid_verse_id_with_bible() {
    //     let bible = get_bible(Version::AMERICAN_STANDARD, "plain_text");
    //     let id = *VERSE_IDS.first().expect("no verse ids") as i32;
    //     assert!(is_valid_verse_id(id, Some(&bible)));
    // }
}