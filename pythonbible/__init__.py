"""
pythonbible includes features for parsing texts for scripture references,
converting references into integer verse ids for efficient use/storage,
converting verse ids back into normalized references, and formatting
references as human-readable strings.
"""

__version__ = "0.6.1"

from .bible.osis.parser import OSISParser
from .book_groups import BOOK_GROUPS, BookGroup
from .books import Book
from .converter import (
    convert_reference_to_verse_ids,
    convert_references_to_verse_ids,
    convert_verse_ids_to_references,
)
from .counters.book_counter import count_books
from .counters.chapter_counter import count_chapters
from .counters.verse_counter import count_verses
from .errors import (
    InvalidBibleParserError,
    InvalidBookError,
    InvalidChapterError,
    InvalidVerseError,
    MissingBookFileError,
    MissingVerseFileError,
)
from .formatter import (
    format_scripture_references,
    format_scripture_text,
    format_single_reference,
    get_book_titles,
    get_parser,
    get_verse_text,
)
from .normalized_reference import NormalizedReference
from .parser import get_references, normalize_reference
from .validator import (
    is_valid_book,
    is_valid_chapter,
    is_valid_reference,
    is_valid_verse,
    is_valid_verse_id,
)
from .verses import (
    get_book_chapter_verse,
    get_book_number,
    get_chapter_number,
    get_max_number_of_verses,
    get_number_of_chapters,
    get_verse_id,
    get_verse_number,
)
from .versions import Version
