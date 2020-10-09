import pythonbible as bible


def test_invalid_verse_error_with_message():
    # Given a message
    message = "invalid verse"

    try:
        # When an InvalidVerseError is raised with that message
        raise bible.InvalidVerseError(message)
    except bible.InvalidVerseError as e:
        # Then the resulting error message is as expected.
        assert e.message == message


def test_invalid_verse_error_with_verse_id(invalid_verse_id):
    # Given an invalid verse id

    try:
        # When an InvalidVerseError is raised with that message
        raise bible.InvalidVerseError(verse_id=invalid_verse_id)
    except bible.InvalidVerseError as e:
        # Then the resulting error message is as expected.
        expected_message = f"{invalid_verse_id} is not a valid verse."
        assert e.message == expected_message


def test_invalid_verse_error_with_book_chapter_and_verse(book, chapter, invalid_verse):
    # Given a book, chapter, and invalid verse

    try:
        # When an InvalidVerseError is raised with that message
        raise bible.InvalidVerseError(book=book, chapter=chapter, verse=invalid_verse)
    except bible.InvalidVerseError as e:
        # Then the resulting error message is as expected.
        expected_message = (
            f"{book.name()} {chapter}:{invalid_verse} is not a valid verse."
        )
        assert e.message == expected_message
