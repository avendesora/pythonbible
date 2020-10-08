import pytest

import bible


def test_get_verse_id(book, chapter, verse, verse_id):
    # Given a book of the Bible, a chapter number, and a verse number

    # When the get_verse_id() function is called
    actual_verse_id = bible.verses.get_verse_id(book, chapter, verse)

    # Then the verse id is the appropriate integer value
    assert verse_id == actual_verse_id


def test_get_verse_id_invalid_chapter(book, invalid_chapter, verse):
    # Given a book of the Bible, a chapter number, and a verse number that is not valid

    # When the get_verse_id() function is called, Then an exception is raised.
    with pytest.raises(bible.InvalidChapterError):
        bible.verses.get_verse_id(book, invalid_chapter, verse)


def test_get_verse_id_invalid_verse(book, chapter, invalid_verse):
    # Given a book of the Bible, a chapter number, and a verse number that is not valid

    # When the get_verse_id() function is called, Then an exception is raised.
    with pytest.raises(bible.InvalidVerseError):
        bible.verses.get_verse_id(book, chapter, invalid_verse)


def test_get_max_verse_number(book, chapter):
    # Given a book of the Bible and a chapter number
    # When we get the maximum verse number for that book and chapter
    max_verse_number = bible.get_max_number_of_verses(book, chapter)

    # Then the maximum verse number is the expected value
    assert max_verse_number == 31


def test_get_max_verse_number_invalid_chapter(book, invalid_chapter):
    # Given a book of the Bible and an invalid chapter number
    # When we attempt to get the maximum verse number for that book and chapter
    # Then an exception is raise.
    with pytest.raises(bible.InvalidChapterError):
        bible.get_max_number_of_verses(book, invalid_chapter)
