import pytest

import pythonbible as bible
from pythonbible.formatter import DEFAULT_PARSER


def test_get_scripture_passage_text(verse_ids_complex, kjv_passage):
    # Given a list of verse ids
    # When we get the scripture passage for those verses
    passage = DEFAULT_PARSER.get_scripture_passage_text(verse_ids_complex)

    # Then the scripture passage is correct.
    assert passage == kjv_passage


def test_get_scripture_passage_text_no_numbers(
    verse_ids_complex, kjv_passage_no_verse_numbers
):
    # Given a list of verse ids
    # When we get the scripture passage for those verses
    passage = DEFAULT_PARSER.get_scripture_passage_text(
        verse_ids_complex, include_verse_number=False
    )

    # Then the scripture passage is correct.
    assert passage == kjv_passage_no_verse_numbers


def test_get_asv_scripture_passage_text(verse_ids_complex, asv_passage):
    # Given a list of verse ids
    # When we get the ASV scripture passage for those verses
    parser = bible.OSISParser(bible.Version.AMERICAN_STANDARD)
    passage = parser.get_scripture_passage_text(verse_ids_complex)

    # Then the scripture passage is correct.
    assert passage == asv_passage


def test_get_scripture_passage_ellipsis():
    passage = DEFAULT_PARSER.get_scripture_passage_text(
        [
            1001003,
            1001005,
        ]
    )
    assert "..." in passage.get(bible.Book.GENESIS).get(1)[0]


def test_get_book_title():
    book_title = DEFAULT_PARSER.get_book_title(bible.Book.GENESIS)
    assert book_title == "The First Book of Moses, called Genesis"


def test_get_short_book_title():
    book_title = DEFAULT_PARSER.get_short_book_title(bible.Book.GENESIS)
    assert book_title == "Genesis"


def test_get_scripture_passage_null():
    assert DEFAULT_PARSER.get_scripture_passage_text(None) is None


def test_get_verse_text(verse_id, verse_text):
    # Given a verse id
    # When we get the scripture text for that verse id
    actual_text = DEFAULT_PARSER.get_verse_text(verse_id)

    # Then it is what we expect it to be.
    assert actual_text == verse_text


def test_get_verse_text_null():
    # Given a null verse id
    # When we attempt to get the scripture text for that verse id
    # Then it raise an InvalidVerseError
    with pytest.raises(bible.InvalidVerseError):
        DEFAULT_PARSER.get_verse_text(None)


def test_get_verse_text_invalid_verse(invalid_verse_id):
    # Given an invalid verse id
    # When we attempt to get the scripture text for that verse id
    # Then it raise an InvalidVerseError
    with pytest.raises(bible.InvalidVerseError):
        DEFAULT_PARSER.get_verse_text(invalid_verse_id)


def test_get_scripture_passage_one_verse_per_paragraph():
    """Test for https://github.com/avendesora/python-bible/issues/5."""
    # Given "Genesis 1" as a reference / verse ids
    references = bible.get_references("Genesis 1")
    verse_ids = bible.convert_references_to_verse_ids(references)

    # When we get the scripture passage with one verse per paragraph
    passage = DEFAULT_PARSER.get_scripture_passage_text(
        verse_ids, one_verse_per_paragraph=True
    )

    # Then it does not raise an exception
    assert passage is not None
