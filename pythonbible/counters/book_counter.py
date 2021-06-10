from functools import singledispatch
from typing import List

from pythonbible.normalized_reference import NormalizedReference
from pythonbible.parser import get_references


@singledispatch
def count_books(references: List[NormalizedReference]) -> int:
    """Return the count of books of the Bible included in the given reference(s)."""
    return _get_number_of_books_in_references(references)


@count_books.register
def _count_books_single(reference: NormalizedReference) -> int:
    return _get_number_of_books_in_reference(reference)


@count_books.register
def _count_books_string(reference: str) -> int:
    return _get_number_of_books_in_references(get_references(reference))


def _get_number_of_books_in_references(references: List[NormalizedReference]) -> int:
    return sum(_get_number_of_books_in_reference(reference) for reference in references)


def _get_number_of_books_in_reference(reference: NormalizedReference) -> int:
    return (
        reference.end_book.value - reference.book.value + 1 if reference.end_book else 1
    )
