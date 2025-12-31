from __future__ import annotations

from functools import singledispatch

from pythonbible.bible.bible import Bible
from pythonbible.bible.errors import VersionMissingBookError
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.parser import get_references


@singledispatch
def count_books(
    references: list[NormalizedReference],
    bible: Bible | None = None,
) -> int:
    """Return the count of books of the Bible included in the given list of references.

    :param references: A list of normalized references
    :type references: list[NormalizedReference]
    :param bible: An optional Bible object to validate against
    :type bible: Bible | None
    :return: The count of books of the Bible included in the given list of references
    :rtype: int
    :raises VersionMissingBookError: If a book in the reference is not present in the
                                     given Bible version
    """
    return _get_number_of_books_in_references(references, bible)


@count_books.register
def _count_books_single(  # type: ignore[misc]
    reference: NormalizedReference,
    bible: Bible | None = None,
) -> int:
    return _get_number_of_books_in_reference(reference, bible)


@count_books.register
def _count_books_string(  # type: ignore[misc]
    reference: str,
    bible: Bible | None = None,
) -> int:
    return _get_number_of_books_in_references(get_references(reference), bible)


def _get_number_of_books_in_references(
    references: list[NormalizedReference],
    bible: Bible | None = None,
) -> int:
    return sum(
        _get_number_of_books_in_reference(reference, bible) for reference in references
    )


def _get_number_of_books_in_reference(
    reference: NormalizedReference,
    bible: Bible | None = None,
) -> int:
    if bible is not None:
        # Ensure all books in the reference are valid for the given Bible
        if reference.book not in bible.max_verses:
            raise VersionMissingBookError(bible.version, reference.book)

        if reference.end_book and reference.end_book not in bible.max_verses:
            raise VersionMissingBookError(bible.version, reference.end_book)

    return (
        reference.end_book.value - reference.book.value + 1 if reference.end_book else 1
    )
