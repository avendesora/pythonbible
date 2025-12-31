from __future__ import annotations

import pytest

import pythonbible as bible


def test_get_verse_id(
    book: bible.Book,
    chapter: int,
    verse: int,
    verse_id: int,
) -> None:
    # Given a book of the Bible, a chapter number, and a verse number

    # When the get_verse_id() function is called
    actual_verse_id: int = bible.verses.get_verse_id(book, chapter, verse)

    # Then the verse id is the appropriate integer value
    assert verse_id == actual_verse_id


def test_get_verse_id_invalid_chapter(
    book: bible.Book,
    invalid_chapter: int,
    verse: int,
) -> None:
    # Given a book of the Bible, a chapter number, and a verse number that is not valid

    # When the get_verse_id() function is called, Then an exception is raised.
    with pytest.raises(bible.InvalidChapterError):
        bible.verses.get_verse_id(book, invalid_chapter, verse)


def test_get_verse_id_invalid_verse(
    book: bible.Book,
    chapter: int,
    invalid_verse: int,
) -> None:
    # Given a book of the Bible, a chapter number, and a verse number that is not valid

    # When the get_verse_id() function is called, Then an exception is raised.
    with pytest.raises(
        bible.InvalidVerseError,
        match=r"Genesis 1:100 is not a valid Bible verse. Valid verses for that book "
        "and chapter are 1-31",
    ):
        bible.verses.get_verse_id(book, chapter, invalid_verse)


def test_get_max_verse_number(book: bible.Book, chapter: int) -> None:
    # Given a book of the Bible and a chapter number
    # When we get the maximum verse number for that book and chapter
    max_verse_number: int = bible.get_number_of_verses(book, chapter)

    # Then the maximum verse number is the expected value
    assert max_verse_number == 31


def test_get_max_verse_number_invalid_chapter(
    book: bible.Book,
    invalid_chapter: int,
) -> None:
    # Given a book of the Bible and an invalid chapter number
    # When we attempt to get the maximum verse number for that book and chapter
    # Then an exception is raise.
    with pytest.raises(bible.InvalidChapterError):
        bible.get_number_of_verses(book, invalid_chapter)


def test_get_book_chapter_verse(
    verse_id: int,
    book: bible.Book,
    chapter: int,
    verse: int,
) -> None:
    # Given a valid verse id
    # When using that verse id to get the book, chapter, and verse
    actual_book: bible.Book
    actual_chapter: int
    actual_verse: int
    actual_book, actual_chapter, actual_verse = bible.get_book_chapter_verse(verse_id)

    # Then the results match the expected book, chapter, and verse
    assert actual_book == book
    assert actual_chapter == chapter
    assert actual_verse == verse


def test_get_book_chapter_verse_invalid(invalid_verse_id: int) -> None:
    # Given an invalid verse id
    # When attempting to get the book, chapter, and verse
    # Then an error is raised.
    with pytest.raises(bible.InvalidVerseError, match=r"1100100 is not a valid verse."):
        bible.get_book_chapter_verse(invalid_verse_id)


def test_get_book(verse_id: int, book: bible.Book) -> None:
    # Given a valid verse id
    # When using that verse id to get the book
    book_number: int = bible.get_book_number(verse_id)

    # Then the resulting book matches the expected book
    assert bible.Book(book_number) == book  # type: ignore[call-arg]


def test_get_chapter(verse_id: int) -> None:
    # Given a valid verse id
    # When using that verse id to get the chapter
    chapter_number: int = bible.get_chapter_number(verse_id)

    # Then the resulting chapter number matches the expected chapter number (1)
    assert chapter_number == 1


def test_get_verse(verse_id: int) -> None:
    # Given a valid verse id
    # When using that verse id to get the verse
    verse_number: int = bible.get_verse_number(verse_id)

    # Then the resulting verse number matching the expected verse number (1)
    assert verse_number == 1


def test_get_number_of_chapters_with_bible(book: bible.Book) -> None:
    # Given a book of the Bible and a Bible instance
    version_bible: bible.Bible = bible.get_bible(
        bible.Version.AMERICAN_STANDARD,
        "plain_text",
    )

    # When getting the number of chapters for the book
    number_of_chapters: int = bible.get_number_of_chapters(book, version_bible)

    # Then the number of chapters is the expected value
    assert number_of_chapters == 50


def test_is_single_chapter_book_with_bible() -> None:
    # Given a single-chapter book of the Bible and a Bible instance
    book = bible.Book.JUDE
    version_bible: bible.Bible = bible.get_bible(
        bible.Version.AMERICAN_STANDARD,
        "plain_text",
    )

    # When checking to see if the book is a single-chapter book
    is_single_chapter: bool = bible.verses.is_single_chapter_book(
        book,
        version_bible,
    )

    # Then the result is True
    assert is_single_chapter


def test_get_number_of_verses_with_bible(book: bible.Book) -> None:
    # Given a book of the Bible, a chapter number, and a Bible instance
    chapter = 1
    version_bible: bible.Bible = bible.get_bible(
        bible.Version.AMERICAN_STANDARD,
        "plain_text",
    )

    # When getting the number of verses for the book and chapter
    number_of_verses: int = bible.get_number_of_verses(
        book,
        chapter,
        version_bible,
    )

    # Then the number of verses is the expected value
    assert number_of_verses == 31


def test_get_verse_id_with_bible(
    book: bible.Book,
    chapter: int,
    verse: int,
) -> None:
    # Given a book of the Bible, a chapter number, a verse number, and a Bible instance
    version_bible: bible.Bible = bible.get_bible(
        bible.Version.AMERICAN_STANDARD,
        "plain_text",
    )

    # When getting the verse id for the book, chapter, and verse
    verse_id: int = bible.get_verse_id(
        book,
        chapter,
        verse,
        version_bible,
    )

    # Then the verse id is the expected value
    assert verse_id == 1001001
