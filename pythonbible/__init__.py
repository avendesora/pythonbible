"""The pythonbible library.

pythonbible includes features for parsing texts for scripture references,
converting references into integer verse ids for efficient use/storage,
converting verse ids back into normalized references, and formatting
references as human-readable strings.
"""

from __future__ import annotations

__version__ = "0.12.0"

from .bible.bible import Bible
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
from .errors import VersionMissingVerseError
from .formatter import format_scripture_references
from .formatter import format_scripture_text
from .formatter import format_single_reference
from .formatter import get_book_titles
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
