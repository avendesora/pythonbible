from __future__ import annotations

import re

import pytest

import pythonbible as bible


def test_invalid_verse_error_with_message() -> None:
    # Given a message
    message: str = "invalid verse"

    # When an InvalidVerseError is raised with that message
    with pytest.raises(bible.InvalidVerseError, match=re.escape(message)):
        raise bible.InvalidVerseError(message)


def test_invalid_verse_error_with_verse_id(invalid_verse_id: int) -> None:
    # Given an invalid verse id
    expected_message: str = f"{invalid_verse_id} is not a valid verse."

    # When an InvalidVerseError is raised with that verse_id
    with pytest.raises(bible.InvalidVerseError, match=re.escape(expected_message)):
        raise bible.InvalidVerseError(verse_id=invalid_verse_id)


def test_invalid_verse_error_with_book_chapter_and_verse(
    book: bible.Book,
    chapter: int,
    invalid_verse: int,
) -> None:
    # Given a book, chapter, and invalid verse
    expected_message: str = (
        f"{book.title} {chapter}:{invalid_verse} is not a valid verse."
    )

    # When an InvalidVerseError is raised
    with pytest.raises(bible.InvalidVerseError, match=re.escape(expected_message)):
        raise bible.InvalidVerseError(book=book, chapter=chapter, verse=invalid_verse)


def test_invalid_verse_error_with_book_and_verse_id(
    book: bible.Book,
    invalid_verse_id: int,
) -> None:
    # Given a book and an invalid verse id
    expected_message: str = f"{invalid_verse_id} is not a valid verse."

    # When an InvalidVerseError is raised
    with pytest.raises(bible.InvalidVerseError, match=re.escape(expected_message)):
        raise bible.InvalidVerseError(book=book, verse_id=invalid_verse_id)


def test_invalid_verse_error_with_book_chapter_and_verse_id(
    book: bible.Book,
    chapter: int,
    invalid_verse_id: int,
) -> None:
    # Given a book, chapter, and an invalid verse id
    expected_message: str = f"{invalid_verse_id} is not a valid verse."

    # When an InvalidVerseError is raised
    with pytest.raises(bible.InvalidVerseError, match=re.escape(expected_message)):
        raise bible.InvalidVerseError(
            book=book,
            chapter=chapter,
            verse_id=invalid_verse_id,
        )


def test_invalid_verse_error_with_book_verse_and_verse_id(
    book: bible.Book,
    verse: int,
    invalid_verse_id: int,
) -> None:
    # Given a book, verse, and an invalid verse id
    expected_message: str = f"{invalid_verse_id} is not a valid verse."

    # When an InvalidVerseError is raised
    with pytest.raises(bible.InvalidVerseError, match=re.escape(expected_message)):
        raise bible.InvalidVerseError(book=book, verse=verse, verse_id=invalid_verse_id)


def test_invalid_verse_error_with_chapter_and_verse_id(
    chapter: int,
    invalid_verse_id: int,
) -> None:
    # Given a chapter and an invalid verse id
    expected_message: str = f"{invalid_verse_id} is not a valid verse."

    # When an InvalidVerseError is raised
    with pytest.raises(bible.InvalidVerseError, match=re.escape(expected_message)):
        raise bible.InvalidVerseError(chapter=chapter, verse_id=invalid_verse_id)


def test_invalid_verse_error_with_chapter_verse_and_verse_id(
    chapter: int,
    verse: int,
    invalid_verse_id: int,
) -> None:
    # Given a chapter, verse, and an invalid verse id
    expected_message: str = f"{invalid_verse_id} is not a valid verse."

    # When an InvalidVerseError is raised
    with pytest.raises(bible.InvalidVerseError, match=re.escape(expected_message)):
        raise bible.InvalidVerseError(
            chapter=chapter,
            verse=verse,
            verse_id=invalid_verse_id,
        )


def test_invalid_verse_error_with_verse_and_verse_id(
    verse: int,
    invalid_verse_id: int,
) -> None:
    # Given a verse and an invalid verse id
    expected_message: str = f"{invalid_verse_id} is not a valid verse."

    # When an InvalidVerseError is raised
    with pytest.raises(bible.InvalidVerseError, match=re.escape(expected_message)):
        raise bible.InvalidVerseError(verse=verse, verse_id=invalid_verse_id)
