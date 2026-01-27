// Rust port of the provided Python `verses.py` logic.
// This file provides utilities for verse id composition/decomposition
// and book/chapter/verse counts. It uses numeric book identifiers (u8).
//
// Note: integrate with your project's `Book` enum and `Bible` trait as needed.
// This module is self-contained and uses `u8` for book numbers.

use once_cell::sync::Lazy;
use std::collections::HashMap;
use std::fmt;
use crate::bible::Bible;
use crate::books::BookItem;

pub const BOOK_PLACE: usize = 1_000_000;
pub const CHAPTER_PLACE: usize = 1_000;

/// Error returned when an invalid chapter is requested.
#[derive(Debug, Clone)]
pub struct InvalidChapterError {
    pub message: String,
}

impl fmt::Display for InvalidChapterError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(&self.message)
    }
}

impl std::error::Error for InvalidChapterError {}

/// Error returned when an invalid verse or verse id is requested.
#[derive(Debug, Clone)]
pub struct InvalidVerseError {
    pub message: String,
}

impl InvalidVerseError {
    pub fn for_verse_id(verse_id: usize) -> Self {
        Self {
            message: format!("{} is not a valid verse id", verse_id),
        }
    }

    pub fn for_book_chapter_verse(book: &BookItem, chapter: usize, verse: usize, max: usize) -> Self {
        Self {
            message: format!(
                "{} {}:{} is not a valid Bible verse. Valid verses for that book and chapter are 1-{}",
                book.name, chapter, verse, max
            ),
        }
    }
}

impl fmt::Display for InvalidVerseError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(&self.message)
    }
}

impl std::error::Error for InvalidVerseError {}

pub(crate) static MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER: Lazy<HashMap<u8, &'static [usize]>> =
    Lazy::new(|| {
        let mut m: HashMap<u8, &'static [usize]> = HashMap::new();
        m.insert(
            1, // Genesis
            &[
                31, 25, 24, 26, 32, 22, 24, 22, 29, 32, 32, 20, 18, 24, 21, 16, 27, 33, 38, 18, 34,
                24, 20, 67, 34, 35, 46, 22, 35, 43, 55, 32, 20, 31, 29, 43, 36, 30, 23, 23, 57, 38,
                34, 34, 28, 34, 31, 22, 33, 26,
    ],
        );
        m.insert(
            2, // Exodus
            &[
                22, 25, 22, 31, 23, 30, 25, 32, 35, 29, 10, 51, 22, 31, 27, 36, 16, 27, 25, 26, 36,
                31, 33, 18, 40, 37, 21, 43, 46, 38, 18, 35, 23, 35, 35, 38, 29, 31, 43, 38,
    ],
        );
        m.insert(
            3, // Leviticus
            &[
                17, 16, 17, 35, 19, 30, 38, 36, 24, 20, 47, 8, 59, 57, 33, 34, 16, 30, 37, 27, 24,
                33, 44, 23, 55, 46, 34,
    ],
        );
        m.insert(
            4, // Numbers
            &[
                54, 34, 51, 49, 31, 27, 89, 26, 23, 36, 35, 16, 33, 45, 41, 50, 13, 32, 22, 29, 35,
                41, 30, 25, 18, 65, 23, 31, 40, 16, 54, 42, 56, 29, 34, 13,
    ],
        );
        m.insert(
            5, // Deuteronomy
            &[
                46, 37, 29, 49, 33, 25, 26, 20, 29, 22, 32, 32, 18, 29, 23, 22, 20, 22, 21, 20, 23,
                30, 25, 22, 19, 19, 26, 68, 29, 20, 30, 52, 29, 12,
    ],
        );
        m.insert(
            6, // Joshua
            &[
                18, 24, 17, 24, 15, 27, 26, 35, 27, 43, 23, 24, 33, 15, 63, 10, 18, 28, 51, 9, 45,
                34, 16, 33,
    ],
        );
        m.insert(
            7, // Judges
            &[
                36, 23, 31, 24, 31, 40, 25, 35, 57, 18, 40, 15, 25, 20, 20, 31, 13, 31, 30, 48, 25,
    ],
        );
        m.insert(8, &[22, 23, 18, 22]); // Ruth
        m.insert(
            9, // 1 Samuel
            &[
                28, 36, 21, 22, 12, 21, 17, 22, 27, 27, 15, 25, 23, 52, 35, 23, 58, 30, 24, 42, 15,
                23, 29, 22, 44, 25, 12, 25, 11, 31, 13,
    ],
        );
        m.insert(
            10, // 2 Samuel
            &[
                27, 32, 39, 12, 25, 23, 29, 18, 13, 19, 27, 31, 39, 33, 37, 23, 29, 33, 43, 26, 22,
                51, 39, 25,
    ],
        );
        m.insert(
            11, // 1 Kings
            &[
                53, 46, 28, 34, 18, 38, 51, 66, 28, 29, 43, 33, 34, 31, 34, 34, 24, 46, 21, 43, 29,
        53,
    ],
        );
        m.insert(
            12, // 2 Kings
            &[
                18, 25, 27, 44, 27, 33, 20, 29, 37, 36, 21, 21, 25, 29, 38, 20, 41, 37, 37, 21, 26,
                20, 37, 20, 30,
    ],
        );
        m.insert(
            13, // 1 Chronicles
            &[
                54, 55, 24, 43, 26, 81, 40, 40, 44, 14, 47, 40, 14, 17, 29, 43, 27, 17, 19, 8, 30,
                19, 32, 31, 31, 32, 34, 21, 30,
    ],
        );
        m.insert(
            14, // 2 Chronicles
            &[
                17, 18, 17, 22, 14, 42, 22, 18, 31, 19, 23, 16, 22, 15, 19, 14, 19, 34, 11, 37, 20,
                12, 21, 27, 28, 23, 9, 27, 36, 27, 21, 33, 25, 33, 27, 23,
    ],
        );
        m.insert(15, &[11, 70, 13, 24, 17, 22, 28, 36, 15, 44]); // Ezra
        m.insert(
            16, // Nehemiah
            &[11, 20, 32, 23, 19, 19, 73, 18, 38, 39, 36, 47, 31],
        );
        m.insert(17, &[22, 23, 15, 17, 14, 14, 10, 17, 32, 3]); // Esther
        m.insert(
            18, // Job
            &[
                22, 13, 26, 21, 27, 30, 21, 22, 35, 22, 20, 25, 28, 22, 35, 22, 16, 21, 29, 29, 34,
                30, 17, 25, 6, 14, 23, 28, 25, 31, 40, 22, 33, 37, 16, 33, 24, 41, 30, 24, 34, 17,
    ],
        );
        m.insert(
            19, // Psalms
            &[
                6, 12, 8, 8, 12, 10, 17, 9, 20, 18, 7, 8, 6, 7, 5, 11, 15, 50, 14, 9, 13, 31, 6, 10,
                22, 12, 14, 9, 11, 12, 24, 11, 22, 22, 28, 12, 40, 22, 13, 17, 13, 11, 5, 26, 17,
                11, 9, 14, 20, 23, 19, 9, 6, 7, 23, 13, 11, 11, 17, 12, 8, 12, 11, 10, 13, 20, 7,
                35, 36, 5, 24, 20, 28, 23, 10, 12, 20, 72, 13, 19, 16, 8, 18, 12, 13, 17, 7, 18, 52,
                17, 16, 15, 5, 23, 11, 13, 12, 9, 9, 5, 8, 28, 22, 35, 45, 48, 43, 13, 31, 7, 10, 10,
                9, 8, 18, 19, 2, 29, 176, 7, 8, 9, 4, 8, 5, 6, 5, 6, 8, 8, 3, 18, 3, 3, 21, 26, 9, 8,
                24, 13, 10, 7, 12, 15, 21, 10, 20, 14, 9, 6,
    ],
        );
        m.insert(
            20, // Proverbs
            &[
                33, 22, 35, 27, 23, 35, 27, 36, 18, 32, 31, 28, 25, 35, 33, 33, 28, 24, 29, 30, 31,
                29, 35, 34, 28, 28, 27, 28, 27, 33, 31,
    ],
        );
        m.insert(
            21, // Ecclesiastes
            &[18, 26, 22, 16, 20, 12, 29, 17, 18, 20, 10, 14],
        );
        m.insert(22, &[17, 17, 11, 16, 16, 13, 13, 14]); // Song of Songs
        m.insert(
            23, // Isaiah
            &[
                31, 22, 26, 6, 30, 13, 25, 22, 21, 34, 16, 6, 22, 32, 9, 14, 14, 7, 25, 6, 17, 25,
                18, 23, 12, 21, 13, 29, 24, 33, 9, 20, 24, 17, 10, 22, 38, 22, 8, 31, 29, 25, 28,
                28, 25, 13, 15, 22, 26, 11, 23, 15, 12, 17, 13, 12, 21, 14, 21, 22, 11, 12, 19, 12,
                25, 24,
    ],
        );
        m.insert(
            24, // Jeremiah
            &[
                19, 37, 25, 31, 31, 30, 34, 22, 26, 25, 23, 17, 27, 22, 21, 21, 27, 23, 15, 18, 14,
                30, 40, 10, 38, 24, 22, 17, 32, 24, 40, 44, 26, 22, 19, 32, 21, 28, 18, 16, 18, 22,
                13, 30, 5, 28, 7, 47, 39, 46, 64, 34,
    ],
        );
        m.insert(25, &[22, 22, 66, 22, 22]); // Lamentations
        m.insert(
            26, // Ezekiel
            &[
                28, 10, 27, 17, 17, 14, 27, 18, 11, 22, 25, 28, 23, 23, 8, 63, 24, 32, 14, 49, 32,
                31, 49, 27, 17, 21, 36, 26, 21, 26, 18, 32, 33, 31, 15, 38, 28, 23, 29, 49, 26, 20,
                27, 31, 25, 24, 23, 35,
    ],
        );
        m.insert(
            27, // Daniel
            &[21, 49, 30, 37, 31, 28, 28, 27, 27, 21, 45, 13],
        );
        m.insert(
            28, // Hosea
            &[11, 23, 5, 19, 15, 11, 16, 14, 17, 15, 12, 14, 16, 9],
        );
        m.insert(29, &[20, 32, 21]); // Joel
        m.insert(
            30, // Amos
            &[15, 16, 15, 13, 27, 14, 17, 14, 15],
        );
        m.insert(31, &[21]); // Obadiah
        m.insert(32, &[17, 10, 10, 11]); // Jonah
        m.insert(33, &[16, 13, 12, 13, 15, 16, 20]); // Micah
        m.insert(34, &[15, 13, 19]); // Nahum
        m.insert(35, &[17, 20, 19]); // Habakkuk
        m.insert(36, &[18, 15, 20]); // Zephaniah
        m.insert(37, &[15, 23]); // Haggai
        m.insert(
            38, // Zechariah
            &[21, 13, 10, 14, 11, 15, 14, 23, 17, 12, 17, 14, 9, 21],
        );
        m.insert(39, &[14, 17, 18, 6]); // Malachi
        m.insert(
            40, // Matthew
            &[
                25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36, 39, 28, 27, 35, 30, 34,
                46, 46, 39, 51, 46, 75, 66, 20,
    ],
        );
        m.insert(
            41, // Mark
            &[
                45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72, 47, 20,
    ],
        );
        m.insert(
            42, // Luke
            &[
                80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35, 32, 31, 37, 43, 48, 47,
                38, 71, 56, 53,
    ],
        );
        m.insert(
            43, // John
            &[
                51, 25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31, 27, 33, 26, 40, 42, 31,
        25,
    ],
        );
        m.insert(
            44, // Acts
            &[
                26, 47, 26, 37, 42, 15, 60, 40, 43, 48, 30, 25, 52, 28, 41, 40, 34, 28, 41, 38,
                40, 30, 35, 27, 27, 32, 44, 31,
    ],
        );
        m.insert(
            45, // Romans
            &[32, 29, 31, 25, 21, 23, 25, 39, 33, 21, 36, 21, 14, 23, 33, 27],
        );
        m.insert(
            46, // 1 Corinthians
            &[
                31, 16, 23, 21, 13, 20, 40, 13, 27, 33, 34, 31, 13, 40, 58, 24,
    ],
        );
        m.insert(
            47, // 2 Corinthians
            &[24, 17, 18, 18, 21, 18, 16, 24, 15, 18, 33, 21, 14],
        );
        m.insert(48, &[24, 21, 29, 31, 26, 18]); // Galatians
        m.insert(49, &[23, 22, 21, 32, 33, 24]); // Ephesians
        m.insert(50, &[30, 30, 21, 23]); // Philippians
        m.insert(51, &[29, 23, 25, 18]); // Colossians
        m.insert(52, &[10, 20, 13, 18, 28]); // 1 Thessalonians
        m.insert(53, &[12, 17, 18]); // 2 Thessalonians
        m.insert(54, &[20, 15, 16, 16, 25, 21]); // 1 Timothy
        m.insert(55, &[18, 26, 17, 22]); // 2 Timothy
        m.insert(56, &[16, 15, 15]); // Titus
        m.insert(57, &[25]); // Philemon
        m.insert(
            58, // Hebrews
            &[14, 18, 19, 16, 14, 20, 28, 13, 28, 39, 40, 29, 25],
        );
        m.insert(59, &[27, 26, 18, 17, 20]); // James
        m.insert(60, &[25, 25, 22, 19, 14]); // 1 Peter
        m.insert(61, &[21, 22, 18]); // 2 Peter
        m.insert(62, &[10, 29, 24, 21, 21]); // 1 John
        m.insert(63, &[13]); // 2 John
        m.insert(64, &[14]); // 3 John
        m.insert(65, &[25]); // Jude
        m.insert(
            66, // Revelation
            &[
                20, 29, 22, 11, 14, 17, 17, 13, 21, 11, 19, 17, 18, 20, 8, 21, 18, 24, 21, 15,
                27, 21,
    ],
        );
        m.insert(
            67, // Esdras 1 (apocrypha)
            &[
                58, 31, 24, 63, 73, 34, 30, 97, 56, 21, 27, 27, 19, 31, 19, 29, 20, 25, 20,
    ],
        );
        m.insert(
            68, // Tobit
            &[22, 14, 17, 21, 22, 18, 16, 21, 6, 13, 18, 22, 18, 15],
        );
        m.insert(
            69, // Wisdom of Solomon
            &[
                77, 38, 37, 20, 72, 27, 32, 36, 19, 23, 27, 27, 20, 31, 19, 29, 20, 25, 20,
    ],
        );
        m.insert(
            70, // Ecclesiasticus (Sirach)
            &[
                40, 23, 34, 36, 18, 38, 40, 21, 25, 34, 36, 19, 32, 27, 22, 31, 33, 33, 28, 33,
                31, 33, 38, 47, 36, 30, 33, 30, 35, 27, 42, 28, 33, 31, 26, 28, 34, 39, 41, 32, 28,
                25, 37, 27, 31, 23, 31, 28, 19, 31, 38,
    ],
        );
        m.insert(
            71, // Maccabees 1
            &[67, 70, 60, 61, 68, 63, 50, 32, 73, 89, 74, 54, 54, 49, 41, 24],
        );
        m.insert(
            72, // Maccabees 2
            &[67, 70, 60, 61, 68, 63, 50, 36, 73, 89, 74, 54, 54, 49, 41, 24],
        );
        m
    });

/// Generate all valid verse ids as a vector (book_number * BOOK_PLACE + chapter * CHAPTER_PLACE + verse)
fn generate_verse_ids() -> Vec<usize> {
    let mut ids = Vec::new();
    for (&book, chapters) in MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER.iter() {
        for (chapter_idx, &max_verse) in chapters.iter().enumerate() {
            let chapter = chapter_idx + 1;
            for verse in 1..=max_verse {
                let id = (book as usize) * BOOK_PLACE + chapter * CHAPTER_PLACE + verse;
                ids.push(id);
            }
        }
    }
    ids
}

pub static VERSE_IDS: Lazy<Vec<usize>> = Lazy::new(|| generate_verse_ids());

/// Return the number of chapters for a given book number.
pub fn get_number_of_chapters(book: &BookItem, bible: Option<&Bible>) -> Result<usize, crate::bible::BibleError> {
    if let Some(b) = bible {
        return b.get_number_of_chapters(&book);
    }
    Ok(MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER
        .get(&book.number)
        .map(|s| s.len())
        .unwrap_or(0))
}

/// Check if a book is a single chapter book.
pub fn is_single_chapter_book(book: &BookItem, bible: Option<&Bible>) -> Result<bool, crate::bible::BibleError> {
    Ok(get_number_of_chapters(book, bible)? == 1)
}

/// Return the number of verses for given book number and chapter (1-based).
/// Returns Err(InvalidChapterError) if chapter is invalid.
pub fn get_number_of_verses(
    book: &BookItem,
    chapter: usize,
    bible: Option<&Bible>,
) -> Result<usize, Box<dyn std::error::Error + Send + Sync>> {
    if let Some(b) = bible {
        return b
            .get_number_of_verses(book, chapter as i32)
            .map(|n| n as usize)
            .map_err(|e| Box::new(e) as Box<dyn std::error::Error + Send + Sync>);
    }
    match MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER.get(&book.number) {
        Some(chapters) => chapters
            .get(chapter - 1)
            .copied()
            .ok_or_else(|| {
                Box::new(InvalidChapterError {
                message: format!(
                    "{} is not a valid chapter number for the book {}. Valid chapter numbers are 1-{}.",
                    chapter,
                    book.number,
                    chapters.len()
                ),
                }) as Box<dyn std::error::Error + Send + Sync>
            }),
        None => Err(Box::new(InvalidChapterError {
            message: format!("Unknown book number: {}", book.number),
        })),
    }
}

/// Compose a verse id from book number, chapter, verse.
/// Returns Err(InvalidVerseError) if the verse is out of range.
pub fn get_verse_id(
    book: &BookItem,
    chapter: usize,
    verse: usize,
    bible: Option<&Bible>,
) -> Result<usize, InvalidVerseError> {
    let max = get_number_of_verses(&book, chapter, bible)
        .map_err(|e| InvalidVerseError {
            message: e.to_string(),
        })?;

    if !(1..=max).contains(&verse) {
        return Err(InvalidVerseError::for_book_chapter_verse(book, chapter, verse, max));
    }

    Ok((book.number as usize) * BOOK_PLACE + chapter * CHAPTER_PLACE + verse)
}

/// Decompose a verse id into (book_number, chapter, verse).
/// Returns Err(InvalidVerseError) if verse id does not correspond to a known verse.
pub fn get_book_chapter_verse(verse_id: usize) -> Result<(u8, usize, usize), InvalidVerseError> {
    let verse_ids = generate_verse_ids();
    if !verse_ids.contains(&verse_id) {
        return Err(InvalidVerseError::for_verse_id(verse_id));
    }
    let book_number = get_book_number(verse_id);
    let chapter = get_chapter_number(verse_id);
    let verse = get_verse_number(verse_id);
    Ok((book_number, chapter, verse))
}

/// Return the book number component of a verse id.
pub fn get_book_number(verse_id: usize) -> u8 {
    (verse_id / BOOK_PLACE) as u8
}

/// Return the chapter number component of a verse id.
pub fn get_chapter_number(verse_id: usize) -> usize {
    (verse_id % BOOK_PLACE) / CHAPTER_PLACE
}

/// Return the verse number component of a verse id.
pub fn get_verse_number(verse_id: usize) -> usize {
    verse_id % CHAPTER_PLACE
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::books::Book;

    #[test]
    fn test_get_verse_id_valid() {
        let book = Book::Genesis.item();
        let book_number = book.number;
        let chapter = 1;
        let verse = 1;
        let expected = (book_number as usize) * BOOK_PLACE + chapter * CHAPTER_PLACE + verse;
        let id = get_verse_id(book, chapter, verse, None).unwrap();
        assert_eq!(id, expected);
    }

    #[test]
    fn test_get_verse_id_invalid_chapter() {
        let genesis = Book::Genesis.item();
        let err = get_verse_id(genesis, 999, 1, None).unwrap_err();
        let msg = err.message;
        assert!(msg.contains("not a valid chapter number") || msg.contains("Unknown book number"));
    }

    #[test]
    fn test_get_verse_id_invalid_verse() {
        let genesis = Book::Genesis.item();
        let err = get_verse_id(genesis, 1, 100, None).unwrap_err();
        assert!(err.message.contains("is not a valid Bible verse"));
        assert!(err.message.contains("1-31"));
    }

    #[test]
    fn test_get_max_verse_number() {
        let genesis = Book::Genesis.item();
        let max = get_number_of_verses(genesis, 1, None).unwrap();
        assert_eq!(max, 31);
    }

    #[test]
    fn test_get_max_verse_number_invalid_chapter() {
        let genesis = Book::Genesis.item();
        let err = get_number_of_verses(genesis, 999, None).unwrap_err();
        let msg = err.to_string();
        assert!(msg.contains("not a valid chapter number") || msg.contains("Unknown book number"));
    }

    #[test]
    fn test_get_book_chapter_verse() {
        let book = Book::Genesis.item();
        let chapter = 1;
        let verse = 1;
        let verse_id = (book.number as usize) * BOOK_PLACE + chapter * CHAPTER_PLACE + verse;
        let (b, c, v) = get_book_chapter_verse(verse_id).unwrap();
        assert_eq!(b, book.number);
        assert_eq!(c, chapter);
        assert_eq!(v, verse);
    }

    #[test]
    fn test_get_book_chapter_verse_invalid() {
        let err = get_book_chapter_verse(1_100_100).unwrap_err();
        assert!(err.to_string().contains("is not a valid verse id"));
    }

    #[test]
    fn test_get_book_chapter_verse_components() {
        let book: u8 = 1;
        let chapter = 1;
        let verse = 1;
        let verse_id = (book as usize) * BOOK_PLACE + chapter * CHAPTER_PLACE + verse;
        assert_eq!(get_book_number(verse_id), book);
        assert_eq!(get_chapter_number(verse_id), chapter);
        assert_eq!(get_verse_number(verse_id), verse);
    }

    #[test]
    fn test_number_of_chapters_with_bible() {
        let genesis = Book::Genesis.item();
        assert_eq!(get_number_of_chapters(genesis, None).unwrap(), 50);
    }

    #[test]
    fn test_is_single_chapter_book_with_bible() {
        // Jude is typically a single-chapter book; use book number 65 as in this module.
        let jude = Book::Jude.item();
        assert!(is_single_chapter_book(jude, None).unwrap());
    }

    #[test]
    fn test_get_number_of_verses_with_bible() {
        let genesis = Book::Genesis.item();
        let n = get_number_of_verses(genesis, 1, None).unwrap();
        assert_eq!(n, 31);
    }

    #[test]
    fn test_get_verse_id_with_bible() {
        let genesis = Book::Genesis.item();
        let id = get_verse_id(genesis, 1, 1, None).unwrap();
        assert_eq!(id, (1usize) * BOOK_PLACE + 1 * CHAPTER_PLACE + 1);
    }
}
