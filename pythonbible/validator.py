from __future__ import annotations

from pythonbible.books import Book
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.verses import MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER
from pythonbible.verses import VERSE_IDS
from pythonbible.verses import get_number_of_verses
from pythonbible.verses import get_verse_id


def is_valid_verse_id(verse_id: int) -> bool:
    """Check to see if the given verse_id corresponds to a valid verse in the Bible.

    :param verse_id: a verse id
    :type verse_id: int
    :return: True if the verse_id is in the list of valid verse ids; otherwise, False
    :rtype: bool
    """
    return verse_id in VERSE_IDS


def is_valid_reference(reference: NormalizedReference) -> bool:
    """Check to see if the given NormalizedReference is a valid scripture reference.

    (i.e. all of the verses in the reference are valid verses)

    :param reference: a normalized reference
    :type reference: NormalizedReference
    :return: True if the reference is valid; otherwise, False
    :rtype: bool
    """
    if reference is None or not isinstance(reference, NormalizedReference):
        return False

    if not is_valid_verse(
        reference.book,
        reference.start_chapter,
        reference.start_verse,
    ):
        return False

    if not is_valid_verse(reference.book, reference.end_chapter, reference.end_verse):
        return False

    start_verse_id: int = get_verse_id(
        reference.book,
        reference.start_chapter,
        reference.start_verse,
    )
    end_verse_id: int = get_verse_id(
        reference.book,
        reference.end_chapter,
        reference.end_verse,
    )

    return start_verse_id <= end_verse_id


def is_valid_book(book: Book) -> bool:
    """Check to see if the given book is a valid book of the Bible.

    :param book: a book of the Bible
    :type book: Book
    :return: True if the given book is valid; otherwise, False
    :rtype: bool
    """
    return book is not None and isinstance(book, Book)


def is_valid_chapter(book: Book, chapter: int) -> bool:
    """Check to see if the given Book is a valid book of the Bible.

    If so, checks to see if the given chapter number is a valid chapter number for the
    given book.

    :param book: a book of the Bible
    :type book: Book
    :param chapter: a chapter number for the given book of the Bible
    :type chapter: int
    :return: True if the given book and chapter are valid; otherwise, False
    :rtype: bool
    """
    if not is_valid_book(book):
        return False

    if chapter is None or not isinstance(chapter, int):
        return False

    chapter_list: list[int] | None = MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER.get(book)

    return chapter_list is not None and 1 <= chapter <= len(chapter_list)


def is_valid_verse(book: Book, chapter: int, verse: int) -> bool:
    """Check to see if the given Book is a valid book of the Bible.

    Then checks to see if the given chapter number is a valid chapter number for the
    given book, then checks to see if the given verse number is a valid verse number
    for the given book and chapter.

    :param book: a book of the Bible
    :type book: Book
    :param chapter: a chapter number for the given book of the Bible
    :type chapter: int
    :param verse: a verse number for the given book and chapter
    :type verse: int
    :return: True if the given book, chapter, and verse are valid; otherwise, False
    :rtype: bool
    """
    if not is_valid_chapter(book, chapter):
        return False

    if verse is None or not isinstance(verse, int):
        return False

    max_verse: int = get_number_of_verses(book, chapter)

    return 1 <= verse <= max_verse
