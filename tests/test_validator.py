import pythonbible as bible


def test_is_valid_verse_id(verse_id: int) -> None:
    # Given a valid verse id
    # When we test to see if it is valid
    # Then the result is True
    assert bible.is_valid_verse_id(verse_id)


def test_is_valid_verse_id_null() -> None:
    # Given a null verse id
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_verse_id(None)


def test_is_valid_verse_id_string(verse_id: int) -> None:
    # Given a string verse id
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_verse_id(str(verse_id))


def test_is_valid_verse_id_invalid(invalid_verse_id: int) -> None:
    # Given an invalid verse id
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_verse_id(invalid_verse_id)


def test_is_valid_reference(reference: bible.NormalizedReference) -> None:
    # Given a valid normalized reference tuple
    # When we test to see if it is valid
    # Then the result is True
    assert bible.is_valid_reference(reference)


def test_is_valid_reference_null() -> None:
    # Given a null reference
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference(None)


def test_is_valid_reference_string(reference_string: str) -> None:
    # Given a string reference
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference(reference_string)


def test_is_valid_reference_wrong_size(
    book: bible.Book, chapter: int, verse: int
) -> None:
    # Given a reference that is a tuple of the wrong size
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference((book, chapter, verse))


def test_is_valid_reference_invalid_book(chapter: int, verse: int) -> None:
    # Given a normalized reference tuple with an invalid book
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference(
        bible.NormalizedReference("invalid book", chapter, verse, chapter, verse)
    )


def test_is_valid_reference_invalid_chapter(
    book: bible.Book, invalid_chapter: int, verse: int
) -> None:
    # Given a normalized reference tuple with an invalid chapter
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference(
        bible.NormalizedReference(book, invalid_chapter, verse, invalid_chapter, verse)
    )


def test_is_valid_reference_invalid_start_verse(
    book: bible.Book, chapter: int, verse: int, invalid_verse: int
) -> None:
    # Given a normalized reference tuple with an invalid start verse
    reference: bible.NormalizedReference = bible.NormalizedReference(
        book, chapter, invalid_verse, chapter, verse
    )
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference(reference)


def test_is_valid_reference_invalid_end_verse(
    book: bible.Book, chapter: int, verse: int, invalid_verse: int
) -> None:
    # Given a normalized reference tuple with an invalid end verse
    reference: bible.NormalizedReference = bible.NormalizedReference(
        book, chapter, verse, chapter, invalid_verse
    )
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference(reference)


def test_is_valid_reference_smaller_end_verse(
    book: bible.Book, chapter: int, verse: int
) -> None:
    # Given a reference where the end verse comes before the start verse
    reference: bible.NormalizedReference = bible.NormalizedReference(
        book.title, chapter, verse + 1, chapter, verse
    )

    # When we test to see if it is valid
    # Then the result is false
    assert not bible.is_valid_reference(reference)


def test_is_valid_book(book: bible.Book) -> None:
    # Given a valid book object
    # When we test to see if it is valid
    # Then the result is True
    assert bible.is_valid_book(book)


def test_is_valid_book_null() -> None:
    # Given a null book object
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_book(None)


def test_is_valid_book_string(book: bible.Book) -> None:
    # Given a string book object
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_book(book.title)


def test_is_valid_chapter(book: bible.Book, chapter: int) -> None:
    # Given a valid book and chapter
    # When we test to see if the chapter is valid
    # Then the result is True
    assert bible.is_valid_chapter(book, chapter)


def test_is_valid_chapter_null(book: bible.Book) -> None:
    # Given a valid book and a null chapter
    # When we test to see if the chapter is valid
    # Then the result is False
    assert not bible.is_valid_chapter(book, None)


def test_is_valid_chapter_string(book: bible.Book, chapter: int) -> None:
    # Given a valid book and a string chapter
    # When we test to see if the chapter is valid
    # Then the result is False
    assert not bible.is_valid_chapter(book, str(chapter))


def test_is_valid_chapter_invalid(book: bible.Book, invalid_chapter: int) -> None:
    # Given a valid book and an invalid chapter
    # When we test to see if the chapter is valid
    # Then the result is False
    assert not bible.is_valid_chapter(book, invalid_chapter)


def test_is_valid_verse(book: bible.Book, chapter: int, verse: int) -> None:
    # Given a valid book, chapter, and verse
    # When we test to see if the verse is valid
    # Then the result is True
    assert bible.is_valid_verse(book, chapter, verse)


def test_is_valid_verse_null(book: bible.Book, chapter: int) -> None:
    # Given a valid book, chapter, and a null verse
    # When we test to see if the verse is valid
    # Then the result is False
    assert not bible.is_valid_verse(book, chapter, None)


def test_is_valid_verse_string(book: bible.Book, chapter: int, verse: int) -> None:
    # Given a valid book, chapter, and a string verse
    # When we test to see if the verse is valid
    # Then the result is False
    assert not bible.is_valid_verse(book, chapter, str(verse))


def test_is_valid_verse_invalid(
    book: bible.Book, chapter: int, invalid_verse: int
) -> None:
    # Given a valid book, chapter, and an invalid verse
    # When we test to see if the verse is valid
    # Then the result is False
    assert not bible.is_valid_verse(book, chapter, invalid_verse)
