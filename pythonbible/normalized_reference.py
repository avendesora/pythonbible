from dataclasses import dataclass
from typing import Optional

from pythonbible.books import Book


@dataclass
class NormalizedReference:
    book: Book
    start_chapter: int
    start_verse: int
    end_chapter: int
    end_verse: int
    end_book: Optional[Book] = None
