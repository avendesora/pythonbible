from __future__ import annotations

from functools import singledispatch

from pythonbible.normalized_reference import NormalizedReference
from pythonbible.parser import get_references


@singledispatch
def count_books(references: list[NormalizedReference]) -> int:
    """Return the count of books of the Bible included in the given list of references.

    :param references: A list of normalized references
    :type references: list[NormalizedReference]
    :return: The count of books of the Bible included in the given list of references
    :rtype: int
    """
    return _get_number_of_books_in_references(references)


@count_books.register
def _count_books_single(reference: NormalizedReference) -> int:
    return _get_number_of_books_in_reference(reference)


@count_books.register
def _count_books_string(reference: str) -> int:
    return _get_number_of_books_in_references(get_references(reference))


def _get_number_of_books_in_references(references: list[NormalizedReference]) -> int:
    return sum(_get_number_of_books_in_reference(reference) for reference in references)


def _get_number_of_books_in_reference(reference: NormalizedReference) -> int:
    return (
        reference.end_book.value - reference.book.value + 1 if reference.end_book else 1
    )
