import pythonbible as bible


def test_is_valid_verse_id(verse_id):
    # Given a valid verse id
    # When we test to see if it is valid
    # Then the result is True
    assert bible.is_valid_verse_id(verse_id)


def test_is_valid_verse_id_null():
    # Given a null verse id
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_verse_id(None)


def test_is_valid_verse_id_string(verse_id):
    # Given a string verse id
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_verse_id(str(verse_id))


def test_is_valid_verse_id_invalid(invalid_verse_id):
    # Given an invalid verse id
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_verse_id(invalid_verse_id)


def test_is_valid_reference(reference):
    # Given a valid normalized reference tuple
    # When we test to see if it is valid
    # Then the result is True
    assert bible.is_valid_reference(reference)


def test_is_valid_reference_null():
    # Given a null reference
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference(None)


def test_is_valid_reference_string(reference_string):
    # Given a string reference
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference(reference_string)


def test_is_valid_reference_wrong_size(book, chapter, verse):
    # Given a reference that is a tuple of the wrong size
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference((book, chapter, verse))


def test_is_valid_reference_invalid_book(book, chapter, verse):
    # Given a normalized reference tuple with an invalid book
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference((book.title, chapter, verse, chapter, verse))


def test_is_valid_reference_invalid_chapter(book, invalid_chapter, verse):
    # Given a normalized reference tuple with an invalid chapter
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference(
        (book.title, invalid_chapter, verse, invalid_chapter, verse)
    )


def test_is_valid_reference_invalid_start_verse(book, chapter, verse, invalid_verse):
    # Given a normalized reference tuple with an invalid start verse
    reference = (book, chapter, invalid_verse, chapter, verse)
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference(reference)


def test_is_valid_reference_invalid_end_verse(book, chapter, verse, invalid_verse):
    # Given a normalized reference tuple with an invalid end verse
    reference = (book, chapter, verse, chapter, invalid_verse)
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_reference(reference)


def test_is_valid_reference_smaller_end_verse(book, chapter, verse):
    # Given a reference where the end verse comes before the start verse
    reference = (book.title, chapter, verse + 1, chapter, verse)

    # When we test to see if it is valid
    # Then the result is false
    assert not bible.is_valid_reference(reference)


def test_is_valid_book(book):
    # Given a valid book object
    # When we test to see if it is valid
    # Then the result is True
    assert bible.is_valid_book(book)


def test_is_valid_book_null():
    # Given a null book object
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_book(None)


def test_is_valid_book_string(book):
    # Given a string book object
    # When we test to see if it is valid
    # Then the result is False
    assert not bible.is_valid_book(book.title)


def test_is_valid_chapter(book, chapter):
    # Given a valid book and chapter
    # When we test to see if the chapter is valid
    # Then the result is True
    assert bible.is_valid_chapter(book, chapter)


def test_is_valid_chapter_null(book):
    # Given a valid book and a null chapter
    # When we test to see if the chapter is valid
    # Then the result is False
    assert not bible.is_valid_chapter(book, None)


def test_is_valid_chapter_string(book, chapter):
    # Given a valid book and a string chapter
    # When we test to see if the chapter is valid
    # Then the result is False
    assert not bible.is_valid_chapter(book, str(chapter))


def test_is_valid_chapter_invalid(book, invalid_chapter):
    # Given a valid book and an invalid chapter
    # When we test to see if the chapter is valid
    # Then the result is False
    assert not bible.is_valid_chapter(book, invalid_chapter)


def test_is_valid_verse(book, chapter, verse):
    # Given a valid book, chapter, and verse
    # When we test to see if the verse is valid
    # Then the result is True
    assert bible.is_valid_verse(book, chapter, verse)


def test_is_valid_verse_null(book, chapter):
    # Given a valid book, chapter, and a null verse
    # When we test to see if the verse is valid
    # Then the result is False
    assert not bible.is_valid_verse(book, chapter, None)


def test_is_valid_verse_string(book, chapter, verse):
    # Given a valid book, chapter, and a string verse
    # When we test to see if the verse is valid
    # Then the result is False
    assert not bible.is_valid_verse(book, chapter, str(verse))


def test_is_valid_verse_invalid(book, chapter, invalid_verse):
    # Given a valid book, chapter, and an invalid verse
    # When we test to see if the verse is valid
    # Then the result is False
    assert not bible.is_valid_verse(book, chapter, invalid_verse)
