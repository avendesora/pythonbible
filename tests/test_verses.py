import pytest

import pythonbible as bible


def test_get_verse_id(
    book: bible.Book, chapter: int, verse: int, verse_id: int
) -> None:
    # Given a book of the Bible, a chapter number, and a verse number

    # When the get_verse_id() function is called
    actual_verse_id: int = bible.verses.get_verse_id(book, chapter, verse)

    # Then the verse id is the appropriate integer value
    assert verse_id == actual_verse_id


def test_get_verse_id_invalid_chapter(
    book: bible.Book, invalid_chapter: int, verse: int
) -> None:
    # Given a book of the Bible, a chapter number, and a verse number that is not valid

    # When the get_verse_id() function is called, Then an exception is raised.
    with pytest.raises(bible.InvalidChapterError):
        bible.verses.get_verse_id(book, invalid_chapter, verse)


def test_get_verse_id_invalid_verse(
    book: bible.Book, chapter: int, invalid_verse: int
) -> None:
    # Given a book of the Bible, a chapter number, and a verse number that is not valid

    # When the get_verse_id() function is called, Then an exception is raised.
    with pytest.raises(
        bible.InvalidVerseError,
        match="Genesis 1:100 is not a valid Bible verse. Valid verses for that book and chapter are 1-31",
    ):
        bible.verses.get_verse_id(book, chapter, invalid_verse)


def test_get_max_verse_number(book: bible.Book, chapter: int) -> None:
    # Given a book of the Bible and a chapter number
    # When we get the maximum verse number for that book and chapter
    max_verse_number: int = bible.get_max_number_of_verses(book, chapter)

    # Then the maximum verse number is the expected value
    assert max_verse_number == 31


def test_get_max_verse_number_invalid_chapter(
    book: bible.Book, invalid_chapter: int
) -> None:
    # Given a book of the Bible and an invalid chapter number
    # When we attempt to get the maximum verse number for that book and chapter
    # Then an exception is raise.
    with pytest.raises(bible.InvalidChapterError):
        bible.get_max_number_of_verses(book, invalid_chapter)


def test_get_book_chapter_verse(
    verse_id: int, book: bible.Book, chapter: int, verse: int
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
    with pytest.raises(bible.InvalidVerseError, match="1100100 is not a valid verse."):
        bible.get_book_chapter_verse(invalid_verse_id)


def test_get_book(verse_id: int, book: bible.Book) -> None:
    # Given a valid verse id
    # When using that verse id to get the book
    book_number: int = bible.get_book_number(verse_id)

    # Then the resulting book matches the expected book
    assert bible.Book(book_number) == book


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
