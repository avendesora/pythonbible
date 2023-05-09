from __future__ import annotations

from functools import singledispatch

from pythonbible.books import Book
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.parser import get_references
from pythonbible.verses import get_number_of_chapters
from pythonbible.verses import get_number_of_verses


@singledispatch
def count_verses(references: list[NormalizedReference]) -> int:
    """Return the count of verses included in the given list of references.

    :param references: A list of normalized references
    :type references: list[NormalizedReference]
    :return: The count of verses included in the given list of references
    :rtype: int
    """
    return _get_number_verses_in_references(references)


@count_verses.register
def _count_verses_single(reference: NormalizedReference) -> int:
    return _get_number_of_verses_in_reference(reference)


@count_verses.register
def _count_verses_string(reference: str) -> int:
    return _get_number_verses_in_references(get_references(reference))


def _get_number_verses_in_references(references: list[NormalizedReference]) -> int:
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
            start_verse: int | None = (
                reference.start_verse
                if book == start_book and chapter == reference.start_chapter
                else None
            )
            end_verse: int | None = (
                reference.end_verse
                if book == end_book and chapter == reference.end_chapter
                else None
            )

            number_of_verses += _get_number_of_verses_in_chapter(
                book,
                chapter,
                start_verse,
                end_verse,
            )

    return number_of_verses


def _get_number_of_verses_in_chapter(
    book: Book,
    chapter: int,
    start_verse: int | None,
    end_verse: int | None,
) -> int:
    return (end_verse or get_number_of_verses(book, chapter)) - (start_verse or 1) + 1
