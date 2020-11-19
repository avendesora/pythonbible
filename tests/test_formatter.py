import time

import pytest

import pythonbible as bible


def test_format_scripture_references(
    normalized_references_complex, formatted_reference
):
    # Given a list of normalized references
    # When we format them into a reference string
    reference = bible.format_scripture_references(normalized_references_complex)

    # Then the reference string is correctly formatted.
    assert reference == formatted_reference


def test_format_scripture_references_null():
    # Given a null references object
    # When we attempt to format it into a reference string
    formatted_reference = bible.format_scripture_references(None)

    # Then the result is null
    assert formatted_reference is None


def test_format_scripture_references_sorting(
    normalized_references_complex, formatted_reference
):
    # Given a list of normalized references that are not in proper order
    normalized_references_complex.reverse()

    # When we format them into a reference string
    reference = bible.format_scripture_references(normalized_references_complex)

    # Then the reference string is correctly formatted.
    assert reference == formatted_reference


def test_format_scripture_reference_single_verse(verse_id):
    # Given a single verse id
    book, chapter, verse = bible.get_book_chapter_verse(verse_id)

    # When we format the reference for it for different versions
    short_kjv_reference = bible.format_single_reference(
        book, chapter, verse, chapter, verse, version=bible.Version.KING_JAMES
    )
    short_asv_reference = bible.format_single_reference(
        book, chapter, verse, chapter, verse, version=bible.Version.AMERICAN_STANDARD
    )
    long_kjv_reference = bible.format_single_reference(
        book,
        chapter,
        verse,
        chapter,
        verse,
        version=bible.Version.KING_JAMES,
        full_title=True,
    )
    long_asv_reference = bible.format_single_reference(
        book,
        chapter,
        verse,
        chapter,
        verse,
        version=bible.Version.AMERICAN_STANDARD,
        full_title=True,
    )

    # Then the short references should match, but the long ones should be different.
    assert short_kjv_reference == short_asv_reference
    assert long_kjv_reference != long_asv_reference


def test_format_scripture_text(verse_ids, html_scripture_text):
    # Given a list of verse ids
    # When we get the scripture text for those verse ids
    scripture_text = bible.format_scripture_text(verse_ids)

    # Then the scripture text is formatted correctly.
    assert scripture_text == html_scripture_text


def test_format_scripture_text_non_html(verse_ids, non_html_scripture_text):
    # Given a list of verse ids
    # When we get the non html scripture text for those verse ids
    scripture_text = bible.format_scripture_text(verse_ids, format_type="text")

    # Then the scripture text is formatted correctly.
    assert scripture_text == non_html_scripture_text


def test_format_scripture_text_one_verse_per_paragraph(
    verse_ids_multiple_chapters, html_scripture_text_one_verse_per_paragraph
):
    # Given a list of verse ids
    # When we get the scripture text for those verse ids
    scripture_text = bible.format_scripture_text(
        verse_ids_multiple_chapters, one_verse_per_paragraph=True
    )

    # Then the scripture text is formatted correctly.
    assert scripture_text == html_scripture_text_one_verse_per_paragraph


def test_get_verse_text(verse_id, verse_text_no_verse_number):
    # Given a valid verse id
    # When using that verse to get the verse text
    verse_text = bible.get_verse_text(verse_id, version=bible.Version.KING_JAMES)

    # Then the verse text is the appropriate verse text.
    assert verse_text == verse_text_no_verse_number


def test_get_verse_text_invalid(invalid_verse_id):
    # Given an invalid verse id
    # When attempting to get the verse text for that verse id
    # Then an error is raised.
    with pytest.raises(bible.InvalidVerseError):
        bible.get_verse_text(invalid_verse_id)


def test_get_verse_text_no_version_file(verse_id):
    # Given a valid verse id and a version that doesn't have a file
    version = bible.Version.MESSAGE

    # When using that verse id and version to the get the verse text
    # Then a MissingVerseFileError is raised.
    with pytest.raises(bible.MissingVerseFileError):
        bible.get_verse_text(verse_id, version=version)


def test_verse_text_caching():
    # Given a lengthy reference
    references = bible.get_references("Jeremiah")
    verse_ids = bible.convert_references_to_verse_ids(references)

    # When getting the scripture text multiple times
    first_start_time = time.time()
    first_verses = [bible.get_verse_text(verse_id) for verse_id in verse_ids]
    second_start_time = time.time()
    second_verses = [bible.get_verse_text(verse_id) for verse_id in verse_ids]
    end_time = time.time()

    first_time = second_start_time - first_start_time
    second_time = end_time - second_start_time

    # Then the results are cached, so we get the same results much faster the second time
    assert first_time * 0.1 > second_time
    assert first_verses == second_verses


def test_get_book_titles(book, long_book_title, short_book_title):
    # Given a book
    # When we get the book titles for that book
    book_titles = bible.get_book_titles(book, version=bible.Version.KING_JAMES)

    # Then the long and short book titles match what is expected.
    assert book_titles.long_title == long_book_title
    assert book_titles.short_title == short_book_title


def test_get_book_titles_no_version_file(book):
    # Given a valid book and a version that doesn't have a file
    version = bible.Version.MESSAGE

    # When using that book and version to the get the book titles
    # Then a MissingBookFileError is raised.
    with pytest.raises(bible.MissingBookFileError):
        bible.get_book_titles(book, version)
