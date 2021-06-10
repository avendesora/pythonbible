from functools import singledispatch
from typing import List

from pythonbible.books import Book
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.parser import get_references
from pythonbible.verses import get_number_of_chapters


@singledispatch
def count_chapters(references: List[NormalizedReference]) -> int:
    return _get_number_of_chapters_in_references(references)


@count_chapters.register
def _count_chapters_single(reference: NormalizedReference) -> int:
    return _get_number_of_chapters_in_reference(reference)


@count_chapters.register
def _count_chapters_string(reference: str) -> int:
    return _get_number_of_chapters_in_references(get_references(reference))


def _get_number_of_chapters_in_references(references: List[NormalizedReference]) -> int:
    return sum(
        _get_number_of_chapters_in_reference(reference) for reference in references
    )


def _get_number_of_chapters_in_reference(reference: NormalizedReference) -> int:
    if not reference.end_book or reference.book == reference.end_book:
        return reference.end_chapter - reference.start_chapter + 1

    # Start book chapters
    number_of_chapters: int = (
        get_number_of_chapters(reference.book) - reference.start_chapter + 1
    )

    # Middle book(s) chapters
    for book_id in range(reference.book.value + 1, reference.end_book.value):
        number_of_chapters += get_number_of_chapters(Book(book_id))

    # End book chapters
    number_of_chapters += reference.end_chapter

    return number_of_chapters
