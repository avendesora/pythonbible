from __future__ import annotations

from functools import singledispatch

from pythonbible.bible.bible import Bible
from pythonbible.books import Book
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.parser import get_references
from pythonbible.verses import get_number_of_chapters


@singledispatch
def count_chapters(
    references: list[NormalizedReference],
    bible: Bible | None = None,
) -> int:
    """Return the count of chapters in the given list of references.

    :param references: A list of normalized references
    :type references: list[NormalizedReference]
    :param bible: An optional Bible object to validate against
    :type bible: Bible | None
    :return: The count of chapters of books of the Bible included in the given list of
             references
    :rtype: int
    :raises VersionMissingBookError: If a book in the reference is not present in the
                                     given Bible version
    """
    return _get_number_of_chapters_in_references(references, bible)


@count_chapters.register
def _count_chapters_single(  # type: ignore[misc]
    reference: NormalizedReference,
    bible: Bible | None = None,
) -> int:
    return _get_number_of_chapters_in_reference(reference, bible)


@count_chapters.register
def _count_chapters_string(  # type: ignore[misc]
    reference: str,
    bible: Bible | None = None,
) -> int:
    return _get_number_of_chapters_in_references(get_references(reference), bible)


def _get_number_of_chapters_in_references(
    references: list[NormalizedReference],
    bible: Bible | None = None,
) -> int:
    return sum(
        _get_number_of_chapters_in_reference(reference, bible)
        for reference in references
    )


def _get_number_of_chapters_in_reference(
    reference: NormalizedReference,
    bible: Bible | None = None,
) -> int:
    start_chapter = reference.start_chapter or 1

    if not reference.end_book or reference.book == reference.end_book:
        end_chapter = reference.end_chapter or get_number_of_chapters(
            reference.book,
            bible,
        )
        return end_chapter - start_chapter + 1

    # Start book chapters
    number_of_chapters: int = (
        get_number_of_chapters(reference.book, bible) - start_chapter + 1
    )

    # Middle book(s) chapters
    number_of_chapters += sum(
        get_number_of_chapters(Book(book_id), bible)  # type: ignore[call-arg,misc]
        for book_id in range(
            reference.book.value + 1,
            reference.end_book.value,
        )
    )

    # End book chapters
    end_chapter = reference.end_chapter or get_number_of_chapters(
        reference.end_book,
        bible,
    )
    number_of_chapters += end_chapter

    return number_of_chapters
