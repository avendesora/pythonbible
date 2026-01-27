use std::fmt;
use crate::books::BookItem;

/// Represents a single normalized scripture reference.
///
/// Fields correspond to the original Python dataclass; `book` and `end_book` use
/// `&'static Book` references because the canonical `BOOKS` collection is static.
#[derive(Debug, Clone)]
pub struct NormalizedReference {
    pub book: &'static BookItem,
    pub start_chapter: Option<u32>,
    pub start_verse: Option<u32>,
    pub end_chapter: Option<u32>,
    pub end_verse: Option<u32>,
    pub end_book: Option<&'static BookItem>,
}

impl PartialEq for NormalizedReference {
    fn eq(&self, other: &Self) -> bool {
        std::ptr::eq(self.book, other.book)
            && self.start_chapter == other.start_chapter
            && self.start_verse == other.start_verse
            && self.end_chapter == other.end_chapter
            && self.end_verse == other.end_verse
            && match (self.end_book, other.end_book) {
                (Some(a), Some(b)) => std::ptr::eq(a, b),
                (None, None) => true,
                _ => false,
            }
    }
}

impl Eq for NormalizedReference {}

impl NormalizedReference {
    /// Create a new normalized reference with explicit fields.
    pub fn new(
        book: &'static BookItem,
        start_chapter: Option<u32>,
        start_verse: Option<u32>,
        end_chapter: Option<u32>,
        end_verse: Option<u32>,
        end_book: Option<&'static BookItem>,
    ) -> Self {
        Self {
            book,
            start_chapter,
            start_verse,
            end_chapter,
            end_verse,
            end_book,
        }
    }

    /// Convenience constructor for a single verse (or chapter if `verse` is `None`).
    pub fn single(book: &'static BookItem, chapter: u32, verse: Option<u32>) -> Self {
        Self {
            book,
            start_chapter: Some(chapter),
            start_verse: verse,
            end_chapter: None,
            end_verse: None,
            end_book: None,
        }
    }

    /// Returns true when the reference does not span books.
    pub fn is_single_book(&self) -> bool {
        self.end_book.is_none()
    }

    /// Returns true when the reference refers to a single verse (start and end the same).
    pub fn is_single_verse(&self) -> bool {
        self.start_chapter.is_some()
            && self.start_verse.is_some()
            && self.end_chapter.is_none()
            && self.end_verse.is_none()
            && self.end_book.is_none()
    }
}

impl fmt::Display for NormalizedReference {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        // Base: Book and optional start chapter/verse
        write!(f, "{}", self.book.name)?;
        if let Some(sc) = self.start_chapter {
            write!(f, " {}", sc)?;
            if let Some(sv) = self.start_verse {
                write!(f, ":{}", sv)?;
            }
        }

        // End part when present
        if self.end_book.is_some() || self.end_chapter.is_some() || self.end_verse.is_some() {
            write!(f, " - ")?;
            if let Some(eb) = self.end_book {
                write!(f, "{}", eb.name)?;
            }
            if let Some(ec) = self.end_chapter {
                write!(f, " {}", ec)?;
                if let Some(ev) = self.end_verse {
                    write!(f, ":{}", ev)?;
                }
            } else if self.end_book.is_some() && self.end_chapter.is_none() && self.end_verse.is_none() {
                // If only end_book provided, nothing more to add.
            }
        }

        Ok(())
    }
}
