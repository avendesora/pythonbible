import pythonbible as bible


def test_invalid_verse_error_with_message() -> None:
    # Given a message
    message: str = "invalid verse"

    try:
        # When an InvalidVerseError is raised with that message
        raise bible.InvalidVerseError(message)
    except bible.InvalidVerseError as e:
        # Then the resulting error message is as expected.
        assert e.message == message


def test_invalid_verse_error_with_verse_id(invalid_verse_id: int) -> None:
    # Given an invalid verse id

    try:
        # When an InvalidVerseError is raised with that message
        raise bible.InvalidVerseError(verse_id=invalid_verse_id)
    except bible.InvalidVerseError as e:
        # Then the resulting error message is as expected.
        expected_message: str = f"{invalid_verse_id} is not a valid verse."
        assert e.message == expected_message


def test_invalid_verse_error_with_book_chapter_and_verse(
    book: bible.Book, chapter: int, invalid_verse: int
) -> None:
    # Given a book, chapter, and invalid verse

    try:
        # When an InvalidVerseError is raised
        raise bible.InvalidVerseError(book=book, chapter=chapter, verse=invalid_verse)
    except bible.InvalidVerseError as e:
        # Then the resulting error message is as expected.
        expected_message: str = (
            f"{book.title} {chapter}:{invalid_verse} is not a valid verse."
        )
        assert e.message == expected_message


def test_invalid_verse_error_with_book_and_verse_id(
    book: bible.Book, invalid_verse_id: int
) -> None:
    # Given a book and an invalid verse id

    try:
        # When an InvalidVerseError is raised
        raise bible.InvalidVerseError(book=book, verse_id=invalid_verse_id)
    except bible.InvalidVerseError as e:
        # Then the resulting error message is as expected.
        expected_message: str = f"{invalid_verse_id} is not a valid verse."
        assert e.message == expected_message


def test_invalid_verse_error_with_book_chapter_and_verse_id(
    book: bible.Book, chapter: int, invalid_verse_id: int
) -> None:
    # Given a book, chapter, and an invalid verse id

    try:
        # When an InvalidVerseError is raised
        raise bible.InvalidVerseError(
            book=book, chapter=chapter, verse_id=invalid_verse_id
        )
    except bible.InvalidVerseError as e:
        # Then the resulting error message is as expected.
        expected_message: str = f"{invalid_verse_id} is not a valid verse."
        assert e.message == expected_message


def test_invalid_verse_error_with_book_verse_and_verse_id(
    book: bible.Book, verse: int, invalid_verse_id: int
):
    # Given a book, verse, and an invalid verse id

    try:
        # When an InvalidVerseError is raised
        raise bible.InvalidVerseError(book=book, verse=verse, verse_id=invalid_verse_id)
    except bible.InvalidVerseError as e:
        # Then the resulting error message is as expected.
        expected_message: str = f"{invalid_verse_id} is not a valid verse."
        assert e.message == expected_message


def test_invalid_verse_error_with_chapter_and_verse_id(
    chapter: int, invalid_verse_id: int
) -> None:
    # Given a chapter and an invalid verse id

    try:
        # When an InvalidVerseError is raised
        raise bible.InvalidVerseError(chapter=chapter, verse_id=invalid_verse_id)
    except bible.InvalidVerseError as e:
        # Then the resulting error message is as expected.
        expected_message: str = f"{invalid_verse_id} is not a valid verse."
        assert e.message == expected_message


def test_invalid_verse_error_with_chapter_verse_and_verse_id(
    chapter: int, verse: int, invalid_verse_id: int
) -> None:
    # Given a chapter, verse, and an invalid verse id

    try:
        # When an InvalidVerseError is raised
        raise bible.InvalidVerseError(
            chapter=chapter, verse=verse, verse_id=invalid_verse_id
        )
    except bible.InvalidVerseError as e:
        # Then the resulting error message is as expected.
        expected_message: str = f"{invalid_verse_id} is not a valid verse."
        assert e.message == expected_message


def test_invalid_verse_error_with_verse_and_verse_id(
    verse: int, invalid_verse_id: int
) -> None:
    # Given a verse and an invalid verse id

    try:
        # When an InvalidVerseError is raised
        raise bible.InvalidVerseError(verse=verse, verse_id=invalid_verse_id)
    except bible.InvalidVerseError as e:
        # Then the resulting error message is as expected.
        expected_message: str = f"{invalid_verse_id} is not a valid verse."
        assert e.message == expected_message
