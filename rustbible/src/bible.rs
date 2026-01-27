use std::collections::HashMap;
use std::fmt::Debug;

use crate::versions::Version;
use crate::books::BookItem;

/// Errors analogous to the Python `VersionMissing*Error` exceptions.
#[derive(Debug)]
pub enum BibleError {
    VersionMissingBook { version: Version, book: BookItem },
    VersionMissingChapter { version: Version, book: BookItem, chapter: i32 },
    VersionMissingVerse { version: Version, verse_id: i32 },
}

impl std::fmt::Display for BibleError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            BibleError::VersionMissingBook { version, book } => {
                write!(f, "version {:?} missing book {:?}", version, book)
            }
            BibleError::VersionMissingChapter { version, book, chapter } => {
                write!(f, "version {:?} missing chapter {} in book {:?}", version, chapter, book)
            }
            BibleError::VersionMissingVerse { version, verse_id } => {
                write!(f, "version {:?} missing verse id {}", version, verse_id)
            }
        }
    }
}

impl std::error::Error for BibleError {}

/// The Bible struct containing scripture content and indices.
///
/// Uses concrete `Version` and `Book` types from the crate.
#[derive(Clone, Debug)]
pub struct Bible {
    pub version: Version,
    pub scripture_content: String,
    pub verse_start_indices: HashMap<i32, usize>,
    pub verse_end_indices: HashMap<i32, usize>,
    pub max_verses: HashMap<u8, HashMap<i32, i32>>,
    pub short_titles: HashMap<u8, String>,
    pub long_titles: HashMap<u8, String>,
    pub is_html: bool,
}

impl Bible {
    pub fn new(
        version: Version,
        scripture_content: String,
        verse_start_indices: HashMap<i32, usize>,
        verse_end_indices: HashMap<i32, usize>,
        max_verses: HashMap<u8, HashMap<i32, i32>>,
        short_titles: HashMap<u8, String>,
        long_titles: HashMap<u8, String>,
        is_html: bool,
    ) -> Self {
        Self {
            version,
            scripture_content,
            verse_start_indices,
            verse_end_indices,
            max_verses,
            short_titles,
            long_titles,
            is_html,
        }
    }

    /// Get scripture for a single verse id or a range.
    pub fn get_scripture(
        &self,
        start_verse_id: i32,
        end_verse_id: Option<i32>,
    ) -> Result<String, BibleError> {
        if !self.is_valid_verse_id(start_verse_id) {
            return Err(BibleError::VersionMissingVerse {
                version: self.version.clone(),
                verse_id: start_verse_id,
            });
        }

        if let Some(ev) = end_verse_id {
            if !self.is_valid_verse_id(ev) {
                return Err(BibleError::VersionMissingVerse {
                    version: self.version.clone(),
                    verse_id: ev,
                });
            }
        }

        let end_id = end_verse_id.unwrap_or(start_verse_id);
        let (start_index, end_index) = self.get_start_and_end_indices(start_verse_id, end_id)?;

        // Ensure indices are in-range for slicing
        let content_len = self.scripture_content.len();
        let s = start_index.min(content_len);
        let e = end_index.min(content_len).max(s);

        let slice = &self.scripture_content[s..e];
        Ok(clean(slice, self.is_html))
    }

    fn get_start_and_end_indices(
        &self,
        start_verse_id: i32,
        end_verse_id: i32,
    ) -> Result<(usize, usize), BibleError> {
        let start_index = self.verse_start_indices.get(&start_verse_id);
        let end_index = self.verse_end_indices.get(&end_verse_id);

        match (start_index, end_index) {
            (Some(&s), Some(&e)) => Ok((s, e)),
            (None, _) => Err(BibleError::VersionMissingVerse {
                version: self.version.clone(),
                verse_id: start_verse_id,
            }),
            (_, None) => Err(BibleError::VersionMissingVerse {
                version: self.version.clone(),
                verse_id: end_verse_id,
            }),
        }
    }

    /// Check if a verse id exists.
    pub fn is_valid_verse_id(&self, verse_id: i32) -> bool {
        self.verse_start_indices.contains_key(&verse_id)
    }

    /// Get number of chapters for a book.
    pub fn get_number_of_chapters(&self, book: &BookItem) -> Result<usize, BibleError> {
        if let Some(chapters) = self.max_verses.get(&book.number) {
            Ok(chapters.len())
        } else {
            Err(BibleError::VersionMissingBook {
                version: self.version.clone(),
                book: (*book).clone(),
            })
        }
    }

    /// Get number of verses for a book and chapter.
    pub fn get_number_of_verses(&self, book: &BookItem, chapter: i32) -> Result<i32, BibleError> {
        if let Some(chapters) = self.max_verses.get(&book.number) {
            if !chapters.contains_key(&chapter) {
                return Err(BibleError::VersionMissingChapter {
                    version: self.version.clone(),
                    book: (*book).clone(),
                    chapter,
                });
            }
            Ok(*chapters.get(&chapter).unwrap_or(&-1))
        } else {
            Err(BibleError::VersionMissingBook {
                version: self.version.clone(),
                book: (*book).clone(),
            })
        }
    }

    /// Return all verse ids available.
    pub fn get_verse_ids(&self) -> Vec<i32> {
        self.verse_start_indices.keys().copied().collect()
    }
}

/// Trim and optionally clean HTML-like wrappers.
pub fn clean(scripture_content: &str, is_html: bool) -> String {
    let cleaned = scripture_content.trim();
    if is_html {
        clean_html(cleaned)
    } else {
        cleaned.to_string()
    }
}

/// Clean minimal HTML paragraph wrappers similar to the Python logic.
pub fn clean_html(scripture_content: &str) -> String {
    if scripture_content.is_empty()
        || scripture_content == "</p><p>"
        || scripture_content == "<p></p>"
    {
        return String::new();
    }

    let mut s = scripture_content.to_string();

    if s.ends_with("<p>") {
        let len = s.len();
        // remove last 3 chars
        s.truncate(len.saturating_sub(3));
    }

    if !s.starts_with("<p>") {
        s = format!("<p>{}", s);
    }

    if !s.ends_with("</p>") {
        s = format!("{}{}", s, "</p>");
    }

    if s == "<p></p>" {
        String::new()
    } else {
        s
    }
}
