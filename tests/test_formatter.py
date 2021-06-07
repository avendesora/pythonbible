import time
from typing import List, Optional

import pytest

import pythonbible as bible
from pythonbible.formatter import BookTitles


def test_format_scripture_references(
    normalized_references_complex: List[bible.NormalizedReference],
    formatted_reference: str,
) -> None:
    # Given a list of normalized references
    # When we format them into a reference string
    reference: str = bible.format_scripture_references(normalized_references_complex)

    # Then the reference string is correctly formatted.
    assert reference == formatted_reference


def test_format_scripture_references_null() -> None:
    # Given a null references object
    # When we attempt to format it into a reference string
    formatted_reference: str = bible.format_scripture_references(None)

    # Then the result is null
    assert formatted_reference == ""


def test_format_scripture_references_sorting(
    normalized_references_complex: List[bible.NormalizedReference],
    formatted_reference: str,
) -> None:
    # Given a list of normalized references that are not in proper order
    normalized_references_complex.reverse()

    # When we format them into a reference string
    reference: str = bible.format_scripture_references(normalized_references_complex)

    # Then the reference string is correctly formatted.
    assert reference == formatted_reference


def test_format_scripture_reference_single_verse(verse_id: int) -> None:
    # Given a single verse id
    book: bible.Book
    chapter: int
    verse: int
    book, chapter, verse = bible.get_book_chapter_verse(verse_id)

    # When we format the reference for it for different versions
    short_kjv_reference: str = bible.format_single_reference(
        bible.NormalizedReference(book, chapter, verse, chapter, verse),
        version=bible.Version.KING_JAMES,
    )
    short_asv_reference: str = bible.format_single_reference(
        bible.NormalizedReference(book, chapter, verse, chapter, verse),
        version=bible.Version.KING_JAMES,
    )
    long_kjv_reference: str = bible.format_single_reference(
        bible.NormalizedReference(book, chapter, verse, chapter, verse),
        version=bible.Version.KING_JAMES,
        full_title=True,
    )
    long_asv_reference: str = bible.format_single_reference(
        bible.NormalizedReference(book, chapter, verse, chapter, verse),
        version=bible.Version.AMERICAN_STANDARD,
        full_title=True,
    )

    # Then the short references should match, but the long ones should be different.
    assert short_kjv_reference == short_asv_reference
    assert long_kjv_reference != long_asv_reference


def test_format_scripture_text(verse_ids: List[int], html_scripture_text: str) -> None:
    # Given a list of verse ids
    # When we get the scripture text for those verse ids
    scripture_text: str = bible.format_scripture_text(verse_ids)

    # Then the scripture text is formatted correctly.
    assert scripture_text == html_scripture_text


def test_format_scripture_text_non_html(
    verse_ids: List[int], non_html_scripture_text: str
) -> None:
    # Given a list of verse ids
    # When we get the non html scripture text for those verse ids
    scripture_text: str = bible.format_scripture_text(verse_ids, format_type="text")

    # Then the scripture text is formatted correctly.
    assert scripture_text == non_html_scripture_text


def test_format_scripture_text_one_verse_per_paragraph(
    verse_ids_multiple_chapters: List[int],
    html_scripture_text_one_verse_per_paragraph: str,
) -> None:
    # Given a list of verse ids
    # When we get the scripture text for those verse ids
    scripture_text: str = bible.format_scripture_text(
        verse_ids_multiple_chapters, one_verse_per_paragraph=True
    )

    # Then the scripture text is formatted correctly.
    assert scripture_text == html_scripture_text_one_verse_per_paragraph


def test_get_verse_text(verse_id: int, verse_text_no_verse_number: str) -> None:
    # Given a valid verse id
    # When using that verse to get the verse text
    verse_text: Optional[str] = bible.get_verse_text(
        verse_id, version=bible.Version.KING_JAMES
    )

    # Then the verse text is the appropriate verse text.
    assert verse_text == verse_text_no_verse_number


def test_get_verse_text_invalid(invalid_verse_id: int) -> None:
    # Given an invalid verse id
    # When attempting to get the verse text for that verse id
    # Then an error is raised.
    with pytest.raises(bible.InvalidVerseError, match="1100100 is not a valid verse."):
        bible.get_verse_text(invalid_verse_id)


def test_get_verse_text_no_version_file(verse_id: int) -> None:
    # Given a valid verse id and a version that doesn't have a file
    version: bible.Version = bible.Version.MESSAGE

    # When using that verse id and version to the get the verse text
    # Then a MissingVerseFileError is raised.
    with pytest.raises(bible.MissingVerseFileError):
        bible.get_verse_text(verse_id, version=version)


def test_verse_text_caching() -> None:
    # Given a lengthy reference
    references: List[bible.NormalizedReference] = bible.get_references("Jeremiah 29")
    verse_ids: List[int] = bible.convert_references_to_verse_ids(references)

    # When getting the scripture text multiple times
    first_start_time: float = time.time()
    first_verses: List[Optional[str]] = [
        bible.get_verse_text(verse_id) for verse_id in verse_ids
    ]
    second_start_time: float = time.time()
    second_verses: List[Optional[str]] = [
        bible.get_verse_text(verse_id) for verse_id in verse_ids
    ]
    end_time: float = time.time()

    first_time: float = second_start_time - first_start_time
    second_time: float = end_time - second_start_time

    # Then the results are cached, so we get the same results much faster the second time
    assert first_time * 0.1 > second_time
    assert first_verses == second_verses


def test_get_book_titles(
    book: bible.Book, long_book_title: str, short_book_title: str
) -> None:
    # Given a book
    # When we get the book titles for that book
    book_titles: Optional[BookTitles] = bible.get_book_titles(
        book, version=bible.Version.KING_JAMES
    )

    # Then the long and short book titles match what is expected.
    assert book_titles is not None
    assert book_titles.long_title == long_book_title
    assert book_titles.short_title == short_book_title


def test_get_book_titles_no_version_file(book: bible.Book) -> None:
    # Given a valid book and a version that doesn't have a file
    version: bible.Version = bible.Version.MESSAGE

    # When using that book and version to the get the book titles
    # Then a MissingBookFileError is raised.
    with pytest.raises(bible.MissingBookFileError):
        bible.get_book_titles(book, version)


def test_format_scripture_references_multiple_book_range() -> None:
    # Given a reference that spans multiple books
    references: List[bible.NormalizedReference] = bible.get_references(
        "Old Testament", book_groups=bible.BOOK_GROUPS
    )

    # When formatting that reference into a reference string
    reference_string: str = bible.format_scripture_references(references)

    # Then the resulting reference string should be a range that spans multiple books.
    assert reference_string == "Genesis - Malachi"


def test_single_chapter_books() -> None:
    # Given a reference for a book that has only one chapter
    references: List[bible.NormalizedReference] = bible.get_references("Obadiah 1:2-4")

    # When formatting that reference into a reference string
    reference_string: str = bible.format_scripture_references(references)

    # Then the resulting reference includes the book title and verse numbers but not chapter numbers.
    assert reference_string == "Obadiah 2-4"


def test_single_chapter_book_in_multiple_book_reference() -> None:
    # Given a reference that includes a book with only one chapter but spans multiple books
    references: List[bible.NormalizedReference] = bible.get_references(
        "Amos 1:3 - Obadiah 1:12"
    )

    # When formatting that reference into a reference string
    reference_string: str = bible.format_scripture_references(references)

    # Then the resulting reference has chapter numbers for the book with multiple
    # chapters and no chapter numbers for the single chapter book.
    assert reference_string == "Amos 1:3 - Obadiah 12"


def test_single_chapter_books_force_chapter_numbers() -> None:
    # Given a reference for a book that has only one chapter
    references: List[bible.NormalizedReference] = bible.get_references("Obadiah")

    # When formatting that reference into a reference string and including the keyword
    # argument to force include chapter numbers
    reference_string: str = bible.format_scripture_references(
        references, always_include_chapter_numbers=True
    )

    # Then the resulting reference includes the book title and verse numbers but not chapter numbers.
    assert reference_string == "Obadiah 1:1-21"


def test_cross_book_range_not_whole_books_or_chapters() -> None:
    # Given a reference that is a range that spans multiple books but not entire books/chapters
    original_reference_string = "Genesis 50:3 - Exodus 1:10"
    references: List[bible.NormalizedReference] = bible.get_references(
        original_reference_string
    )

    # When formatting that reference into a reference string
    reference_string: str = bible.format_scripture_references(references)

    # Then the resulting reference string includes chapter and verse numbers
    assert reference_string == original_reference_string


def test_multi_chapter_book_reference_contains_whole_book() -> None:
    # Given a reference that contains all the verses of a single book that has multiple chapters
    references: List[bible.NormalizedReference] = bible.get_references(
        "Genesis 1:1-50:26"
    )

    # When formatting that reference into a reference string
    reference_string: str = bible.format_scripture_references(references)

    # Then the resulting reference string does not include chapter and verse numbers
    assert reference_string == "Genesis"
