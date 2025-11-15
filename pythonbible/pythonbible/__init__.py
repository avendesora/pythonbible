"""The pythonbible library.

pythonbible includes features for parsing texts for scripture references,
converting references into integer verse ids for efficient use/storage,
converting verse ids back into normalized references, and formatting
references as human-readable strings.
"""

from __future__ import annotations

__version__ = "0.15.0"

from .bible import add_bible
from .bible import get_bible
from .bible.bible import Bible
from .bible.errors import VersionMissingVerseError
from .book_groups import BOOK_GROUPS
from .book_groups import BookGroup
from .books import Book
from .converter import convert_reference_to_verse_ids
from .converter import convert_references_to_verse_ids
from .converter import convert_verse_ids_to_references
from .counters.book_counter import count_books
from .counters.chapter_counter import count_chapters
from .counters.verse_counter import count_verses
from .errors import InvalidBibleParserError
from .errors import InvalidBookError
from .errors import InvalidChapterError
from .errors import InvalidVerseError
from .errors import MissingBookFileError
from .errors import MissingVerseFileError
from .formatter import format_scripture_references
from .formatter import format_scripture_text
from .formatter import format_single_reference
from .formatter import get_verse_text
from .normalized_reference import NormalizedReference
from .parser import get_references
from .parser import normalize_reference
from .validator import is_valid_book
from .validator import is_valid_chapter
from .validator import is_valid_reference
from .validator import is_valid_verse
from .validator import is_valid_verse_id
from .verses import get_book_chapter_verse
from .verses import get_book_number
from .verses import get_chapter_number
from .verses import get_number_of_chapters
from .verses import get_number_of_verses
from .verses import get_verse_id
from .verses import get_verse_number
from .versions import Version

__all__ = [
    "BOOK_GROUPS",
    "Bible",
    "Book",
    "BookGroup",
    "InvalidBibleParserError",
    "InvalidBookError",
    "InvalidChapterError",
    "InvalidVerseError",
    "MissingBookFileError",
    "MissingVerseFileError",
    "NormalizedReference",
    "Version",
    "VersionMissingVerseError",
    "__version__",
    "add_bible",
    "convert_reference_to_verse_ids",
    "convert_references_to_verse_ids",
    "convert_verse_ids_to_references",
    "count_books",
    "count_chapters",
    "count_verses",
    "format_scripture_references",
    "format_scripture_text",
    "format_single_reference",
    "get_bible",
    "get_book_chapter_verse",
    "get_book_number",
    "get_chapter_number",
    "get_number_of_chapters",
    "get_number_of_verses",
    "get_references",
    "get_verse_id",
    "get_verse_number",
    "get_verse_text",
    "is_valid_book",
    "is_valid_chapter",
    "is_valid_reference",
    "is_valid_verse",
    "is_valid_verse_id",
    "normalize_reference",
]
# Reference the imported names so ruff/auto-fixes do not remove them as "unused".
_ = (
    add_bible,
    get_bible,
    Bible,
    VersionMissingVerseError,
    BOOK_GROUPS,
    BookGroup,
    Book,
    convert_reference_to_verse_ids,
    convert_references_to_verse_ids,
    convert_verse_ids_to_references,
    count_books,
    count_chapters,
    count_verses,
    InvalidBibleParserError,
    InvalidBookError,
    InvalidChapterError,
    InvalidVerseError,
    MissingBookFileError,
    MissingVerseFileError,
    format_scripture_references,
    format_scripture_text,
    format_single_reference,
    get_verse_text,
    NormalizedReference,
    get_references,
    normalize_reference,
    is_valid_book,
    is_valid_chapter,
    is_valid_reference,
    is_valid_verse,
    is_valid_verse_id,
    get_book_chapter_verse,
    get_book_number,
    get_chapter_number,
    get_number_of_chapters,
    get_number_of_verses,
    get_verse_id,
    get_verse_number,
    Version,
    __version__,
)
