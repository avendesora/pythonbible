from functools import singledispatch
from typing import List, Optional

from pythonbible.books import Book
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.parser import get_references
from pythonbible.verses import get_max_number_of_verses, get_number_of_chapters


@singledispatch
def count_verses(references: List[NormalizedReference]) -> int:
    return _get_number_verses_in_references(references)


@count_verses.register
def _count_verses_single(reference: NormalizedReference) -> int:
    return _get_number_of_verses_in_reference(reference)


@count_verses.register
def _count_verses_string(reference: str) -> int:
    return _get_number_verses_in_references(get_references(reference))


def _get_number_verses_in_references(references: List[NormalizedReference]) -> int:
    return sum(
        _get_number_of_verses_in_reference(reference) for reference in references
    )


def _get_number_of_verses_in_reference(reference: NormalizedReference) -> int:
    number_of_verses: int = 0
    start_book = reference.book
    end_book = reference.end_book or start_book

    for book_id in range(start_book.value, end_book.value + 1):
        book: Book = Book(book_id)
        start_chapter: int = reference.start_chapter if book == start_book else 1
        end_chapter: int = (
            reference.end_chapter if book == end_book else get_number_of_chapters(book)
        )

        for chapter in range(start_chapter, end_chapter + 1):
            start_verse: Optional[int] = (
                reference.start_verse
                if book == start_book and chapter == reference.start_chapter
                else None
            )
            end_verse: Optional[int] = (
                reference.end_verse
                if book == end_book and chapter == reference.end_chapter
                else None
            )

            number_of_verses += _get_number_of_verses_in_chapter(
                book, chapter, start_verse, end_verse
            )

    return number_of_verses


def _get_number_of_verses_in_chapter(
    book: Book, chapter: int, start_verse: Optional[int], end_verse: Optional[int]
) -> int:
    return (
        (end_verse or get_max_number_of_verses(book, chapter)) - (start_verse or 1) + 1
    )
