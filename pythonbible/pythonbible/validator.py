from __future__ import annotations

from typing import TYPE_CHECKING

from pythonbible.books import Book
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.verses import MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER
from pythonbible.verses import VERSE_IDS
from pythonbible.verses import get_number_of_chapters
from pythonbible.verses import get_number_of_verses
from pythonbible.verses import get_verse_id

if TYPE_CHECKING:
    from pythonbible.bible.bible import Bible


def is_valid_verse_id(verse_id: int, bible: Bible | None = None) -> bool:
    """Check to see if the given verse_id corresponds to a valid verse in the Bible.

    :param verse_id: a verse id
    :type verse_id: int
    :param bible: an optional Bible object to check for verse existence
    :type bible: Bible | None
    :return: True if the verse_id is in the list of valid verse ids; otherwise, False
    :rtype: bool
    """
    if bible is not None:
        return bible.is_valid_verse_id(verse_id)

    return verse_id in VERSE_IDS


def is_valid_reference(
    reference: NormalizedReference,
    bible: Bible | None = None,
) -> bool:
    """Check to see if the given NormalizedReference is a valid scripture reference.

    (i.e. all of the verses in the reference are valid verses)

    :param reference: a normalized reference
    :type reference: NormalizedReference
    :param bible: an optional Bible object to check for verse existence
    :type bible: Bible | None
    :return: True if the reference is valid; otherwise, False
    :rtype: bool
    """
    if reference is None or not isinstance(reference, NormalizedReference):
        return False

    start_book: Book = reference.book
    start_chapter: int = reference.start_chapter or 1
    start_verse: int = reference.start_verse or 1

    if not is_valid_verse(
        start_book,
        start_chapter,
        start_verse,
        bible,
    ):
        return False

    end_book: Book = reference.end_book or start_book
    end_chapter: int = reference.end_chapter or get_number_of_chapters(end_book, bible)
    end_verse: int = reference.end_verse or get_number_of_verses(
        end_book, end_chapter, bible
    )

    if not is_valid_verse(end_book, end_chapter, end_verse, bible):
        return False

    start_verse_id: int = get_verse_id(
        start_book,
        start_chapter,
        start_verse,
        bible,
    )
    end_verse_id: int = get_verse_id(
        end_book,
        end_chapter,
        end_verse,
        bible,
    )

    return start_verse_id <= end_verse_id


def is_valid_book(book: Book, bible: Bible | None = None) -> bool:
    """Check to see if the given book is a valid book of the Bible.

    :param book: a book of the Bible
    :type book: Book
    :param bible: an optional Bible object to check for book existence
    :type bible: Bible | None
    :return: True if the given book is valid; otherwise, False
    :rtype: bool
    """
    if book is None:
        return False

    if bible is None:
        return isinstance(book, Book)

    verse_id = get_verse_id(book, 1, 1)
    return bible.is_valid_verse_id(verse_id)


def is_valid_chapter(book: Book, chapter: int, bible: Bible | None = None) -> bool:
    """Check to see if the given Book is a valid book of the Bible.

    If so, checks to see if the given chapter number is a valid chapter number for the
    given book.

    :param book: a book of the Bible
    :type book: Book
    :param chapter: a chapter number for the given book of the Bible
    :type chapter: int
    :param bible: an optional Bible object to check for chapter existence
    :type bible: Bible | None
    :return: True if the given book and chapter are valid; otherwise, False
    :rtype: bool
    """
    if not is_valid_book(book, bible):
        return False

    if chapter is None or not isinstance(chapter, int):
        return False

    if bible is None:
        chapter_list: list[int] | None = MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER.get(book)
        return chapter_list is not None and 1 <= chapter <= len(chapter_list)

    chapter_dict: dict[int, int] | None = bible.max_verses.get(book)

    return chapter_dict is not None and chapter in chapter_dict


def is_valid_verse(
    book: Book,
    chapter: int,
    verse: int,
    bible: Bible | None = None,
) -> bool:
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
    :param bible: an optional Bible object to check for verse existence
    :type bible: Bible | None
    :return: True if the given book, chapter, and verse are valid; otherwise, False
    :rtype: bool
    """
    if not is_valid_chapter(book, chapter, bible):
        return False

    if verse is None or not isinstance(verse, int):
        return False

    max_verse: int = get_number_of_verses(book, chapter, bible)

    return 1 <= verse <= max_verse
