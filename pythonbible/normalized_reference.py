from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pythonbible.books import Book


@dataclass
class NormalizedReference:
    """NormalizedReference is a dataclass that represents a single scripture reference.

    The scripture reference contains one or more consecutive verses.

    :param book: the first book of the Bible in the reference
    :type book: Book
    :param start_chapter: the number of the first chapter in the reference
    :type start_chapter: int
    :param start_verse: the number of the first verse in the reference
    :type start_verse: int
    :param end_chapter: the number of the last chapter in the reference
    :type end_chapter: int
    :param end_verse: the number of the last verse in the reference
    :type end_verse: int
    :param end_book: the last book of the Bible in the reference if the reference
                     contains more than one book, defaults to None
    :type end_book: Book
    """

    book: Book
    start_chapter: int
    start_verse: int
    end_chapter: int
    end_verse: int
    end_book: Book | None = None
