"""
pythonbible includes features for parsing texts for scripture references,
converting references into integer verse ids for efficient use/storage,
converting verse ids back into normalized references, and formatting
references as human-readable strings.
"""

__version__ = "0.1.0"

from .bible.osis.parser import OSISParser
from .books import Book
from .converter import (
    convert_reference_to_verse_ids,
    convert_references_to_verse_ids,
    convert_verse_ids_to_references,
)
from .errors import InvalidChapterError, InvalidVerseError
from .formatter import (
    format_scripture_references,
    format_scripture_text,
    format_single_reference,
    get_parser,
)
from .parser import (
    get_references,
    normalize_reference,
)
from .validator import (
    is_valid_book,
    is_valid_chapter,
    is_valid_reference,
    is_valid_verse,
    is_valid_verse_id,
)
from .verses import (
    get_book,
    get_book_chapter_verse,
    get_chapter,
    get_max_number_of_verses,
    get_verse,
    get_verse_id,
)
from .versions import Version
