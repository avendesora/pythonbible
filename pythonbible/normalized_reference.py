from dataclasses import dataclass

from pythonbible.books import Book


@dataclass
class NormalizedReference:
    book: Book
    start_chapter: int
    start_verse: int
    end_chapter: int
    end_verse: int
