from typing import List

import pytest

import pythonbible as bible
from pythonbible.converter import is_new_chapter_next_verse


def test_convert_reference_to_verse_ids(reference: bible.NormalizedReference) -> None:
    # Given a valid normalized scripture reference
    # When the reference is converted into a list of verse id integers
    verse_ids: List[int] = bible.convert_reference_to_verse_ids(reference)

    # Then the resulting list of verse id integers is accurate
    assert len(verse_ids) == 60
    assert verse_ids[0] == 1001001
    assert verse_ids[59] == 1003004


def test_convert_reference_to_verse_ids_null() -> None:
    # Given a null reference
    # When we attempt to convert it into a list of verse ids
    verse_ids: List[int] = bible.convert_reference_to_verse_ids(None)

    # Then the result is an empty list
    assert len(verse_ids) == 0


def test_convert_reference_to_verse_ids_invalid(
    invalid_reference: bible.NormalizedReference,
) -> None:
    # Given an invalid reference
    # When we attempt to convert it into a list of verse ids
    with pytest.raises(bible.InvalidChapterError):
        bible.convert_reference_to_verse_ids(invalid_reference)


def test_convert_references_to_verse_ids(
    references: List[bible.NormalizedReference], verse_ids: List[int]
) -> None:
    # Given a list of valid normalized scripture references
    # When the references are converted into a list of verse id integers
    actual_verse_ids: List[int] = bible.convert_references_to_verse_ids(references)

    # Then the resulting list of verse id integers is accurate
    assert actual_verse_ids == verse_ids


def test_convert_references_to_verse_ids_null() -> None:
    # Given a null references object
    # When we attempt to convert it into a list of verse ids
    actual_verse_ids: List[int] = bible.convert_references_to_verse_ids(None)

    # Then the result is an empty list
    assert len(actual_verse_ids) == 0


def test_convert_references_to_verse_ids_complex(
    normalized_references_complex: List[bible.NormalizedReference],
    verse_ids_complex: List[int],
) -> None:
    # Given a list of complex references
    # When converted into verse ids
    actual_verse_ids: List[int] = bible.convert_references_to_verse_ids(
        normalized_references_complex
    )

    # Then the list of verse ids is correct
    assert actual_verse_ids == verse_ids_complex


def test_convert_verse_ids_to_references(
    verse_ids: List[int], references: List[bible.NormalizedReference]
) -> None:
    # Given a list of integer verse ids
    # When we convert them into a list of normalized reference tuples
    actual_references: List[
        bible.NormalizedReference
    ] = bible.convert_verse_ids_to_references(verse_ids)

    # Then the resulting list of references is accurate
    assert actual_references == references


def test_convert_verse_ids_to_references_null() -> None:
    # Given a null verse_ids object
    # When we attempt to convert them into a list of references
    actual_references: List[
        bible.NormalizedReference
    ] = bible.convert_verse_ids_to_references(None)

    # Then the list of references is empty
    assert len(actual_references) == 0


def test_convert_verse_ids_to_references_invalid(invalid_verse_id: int) -> None:
    # Given a list of verse ids with an invalid verse id
    # When we attempt to convert them into a list of references
    # Then an error is raised
    with pytest.raises(bible.InvalidVerseError, match="1100100 is not a valid verse."):
        bible.convert_verse_ids_to_references([invalid_verse_id])


def test_convert_verse_ids_to_references_invalid2(
    verse_id: int, invalid_verse_id: int
) -> None:
    # Given a list of verse ids with an invalid verse id
    # When we attempt to convert them into a list of references
    # Then an error is raised
    with pytest.raises(bible.InvalidVerseError, match="1100100 is not a valid verse."):
        bible.convert_verse_ids_to_references([verse_id, invalid_verse_id])


def test_convert_verse_ids_to_references_complex(
    normalized_references_complex: List[bible.NormalizedReference],
    verse_ids_complex: List[int],
) -> None:
    # Given a list of "complex" verse ids
    # When we convert them into a list of references
    actual_references: List[
        bible.NormalizedReference
    ] = bible.convert_verse_ids_to_references(verse_ids_complex)

    # Then the list of references is correct
    assert actual_references == normalized_references_complex


def test_is_new_chapter_next_verse(book: bible.Book) -> None:
    # Given a book, start chapter, start verse, next chapter, next verse such that
    # the chapters are consecutive and the first verse is the last verse of the
    # first chapter and the second verse is the first verse of the next chapter
    chapter_1: int = 1
    chapter_2: int = 2
    verse_1: int = bible.get_max_number_of_verses(book, chapter_1)
    verse_2: int = 1

    # When we check to see if there are no gaps between the first chapter and verse
    # and the second chapter and verse
    # Then the result is True
    assert is_new_chapter_next_verse(book, chapter_1, verse_1, chapter_2, verse_2)


def test_is_new_chapter_next_verse_false(book: bible.Book) -> None:
    # Given a book, chapters and verses with a gap
    chapter_1: int = 1
    chapter_2: int = 2
    verse_1: int = bible.get_max_number_of_verses(book, chapter_1) - 1
    verse_2: int = 1

    # When we check to see if there are no gaps between the first chapter and verse
    # and the second chapter and verse
    # Then the result is False
    assert not is_new_chapter_next_verse(book, chapter_1, verse_1, chapter_2, verse_2)


def test_whole_book() -> None:
    """Test for https://github.com/avendesora/pythonbible/issues/7!"""
    # Given a reference that is just a book title
    reference_string: str = "Genesis"

    # When we convert that to normalized references
    references: List[bible.NormalizedReference] = bible.get_references(reference_string)

    # Then it should return the normalized reference for the entire book.
    assert len(references) == 1
    assert references[0] == bible.NormalizedReference(bible.Book.GENESIS, 1, 1, 50, 26)
