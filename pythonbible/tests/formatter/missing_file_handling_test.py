from __future__ import annotations

from typing import NoReturn

import pythonbible as bible
import pythonbible.bible as bible_module
from pythonbible import formatter


def test_get_book_title_missing_verse_file() -> None:
    # Arrange: get a book object
    refs = bible.get_references("Genesis 1:1")
    reference = refs[0]
    book = reference.book

    # Act: use a version with no files to trigger MissingVerseFileError from get_bible
    title = formatter._get_book_title(
        book, bible.Version.MESSAGE, full_title=False, include_books=True
    )

    # Assert: the fallback should be the raw book title
    assert title == book.title


def test_is_single_chapter_book_handles_missing_book_file() -> None:
    # Arrange: pick a book known to be single-chapter (Obadiah)
    refs = bible.get_references("Obadiah 1:2-4")
    book = refs[0].book

    # Create a BrokenBible whose max_verses property raises MissingBookFileError
    class BrokenBible:
        @property
        def max_verses(self) -> NoReturn:
            raise bible.MissingBookFileError

    # Register the broken bible for a specific version and bible_type
    version = bible.Version.KING_JAMES
    bible_module.add_bible(version, "plain_text", BrokenBible())  # type: ignore[arg-type]

    try:
        # Act: call the helper that catches MissingBookFileError
        result = formatter._is_single_chapter_book(book, version=version)

        # Assert: it should fall back to the verses module is_single_chapter_book
        assert result == bible.verses.is_single_chapter_book(book)

    finally:
        # Cleanup the injected bible so other tests are not affected
        bible_module.BIBLES.pop(version, None)


def test_get_number_of_chapters_fallback_on_missing_book_file() -> None:
    # Arrange: pick a known book
    refs = bible.get_references("Genesis")
    book = refs[0].book

    # Create a BrokenBible whose max_verses property raises MissingBookFileError
    class BrokenBible:
        @property
        def max_verses(self) -> NoReturn:
            raise bible.MissingBookFileError

    version = bible.Version.KING_JAMES
    bible_module.add_bible(version, "plain_text", BrokenBible())  # type: ignore[arg-type]

    try:
        # Act
        chapters = formatter._get_number_of_chapters(book, version=version)

        # Assert: fallback value matches the verses module implementation
        assert chapters == bible.get_number_of_chapters(book)

    finally:
        bible_module.BIBLES.pop(version, None)


def test_get_number_of_verses_fallback_on_missing_book_file() -> None:
    # Arrange: pick a known book and chapter
    refs = bible.get_references("Genesis 1:1")
    book = refs[0].book
    chapter = refs[0].start_chapter or 1

    # Create a BrokenBible whose max_verses property raises MissingBookFileError
    class BrokenBible:
        @property
        def max_verses(self) -> NoReturn:
            raise bible.MissingBookFileError

    version = bible.Version.KING_JAMES
    bible_module.add_bible(version, "plain_text", BrokenBible())  # type: ignore[arg-type]

    try:
        # Act
        verses = formatter._get_number_of_verses(book, chapter, version=version)

        # Assert: fallback value matches the verses module implementation
        assert verses == bible.get_number_of_verses(book, chapter)

    finally:
        bible_module.BIBLES.pop(version, None)


def test_get_number_of_verses_with_no_chapters_entry() -> None:
    # Arrange: pick a known book and chapter
    refs = bible.get_references("Genesis 1:1")
    book = refs[0].book
    chapter = refs[0].start_chapter or 1

    # Create a Bible-like object with an empty max_verses dict (so .get(book)
    # returns None)
    class EmptyChaptersBible:
        def __init__(self) -> None:
            self.max_verses: dict[bible.Book, dict[int, int]] = {}

    version = bible.Version.KING_JAMES
    bible_module.add_bible(version, "plain_text", EmptyChaptersBible())  # type: ignore[arg-type]

    try:
        # Act
        verses = formatter._get_number_of_verses(book, chapter, version=version)

        # Assert: fallback value matches the verses module implementation because
        # chapters was falsy
        assert verses == bible.get_number_of_verses(book, chapter)

    finally:
        bible_module.BIBLES.pop(version, None)
