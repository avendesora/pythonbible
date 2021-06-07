from typing import List, Optional

from pythonbible.books import Book
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.verses import get_max_number_of_verses, get_number_of_chapters


def count_books(references: List[NormalizedReference]) -> int:
    return sum(_get_number_of_books_in_reference(reference) for reference in references)


def _get_number_of_books_in_reference(reference: NormalizedReference) -> int:
    return (
        reference.end_book.value - reference.book.value + 1 if reference.end_book else 1
    )


def count_chapters(references: List[NormalizedReference]) -> int:
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


def count_verses(references: List[NormalizedReference]) -> int:
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
