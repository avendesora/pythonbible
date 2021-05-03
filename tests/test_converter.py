from typing import List

import pytest

import pythonbible as bible
from pythonbible.verses import VERSE_IDS


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


def test_whole_book() -> None:
    """Test for https://github.com/avendesora/pythonbible/issues/7!"""
    # Given a reference that is just a book title
    reference_string: str = "Genesis"

    # When we convert that to normalized references
    references: List[bible.NormalizedReference] = bible.get_references(reference_string)

    # Then it should return the normalized reference for the entire book.
    assert len(references) == 1
    assert references[0] == bible.NormalizedReference(bible.Book.GENESIS, 1, 1, 50, 26)


def test_cross_book() -> None:
    # Given a reference that spans multiple books
    reference_string: str = "Paul's epistles"

    # When we convert that to normalized references
    references: List[bible.NormalizedReference] = bible.get_references(
        reference_string, book_groups=bible.BOOK_GROUPS
    )

    # and then convert that to verse ids
    verse_ids: List[int] = bible.convert_references_to_verse_ids(references)

    # Then it return the verse ids for the verses in all of the books in the reference.
    first_verse: int = VERSE_IDS.index(45001001)
    last_verse: int = VERSE_IDS.index(57001025)
    assert verse_ids == VERSE_IDS[first_verse : last_verse + 1]


def test_cross_book_reverse() -> None:
    # Given a list of verse ids that spans multiple books
    first_verse: int = VERSE_IDS.index(45001001)
    last_verse: int = VERSE_IDS.index(57001025)
    verse_ids: List[int] = VERSE_IDS[first_verse : last_verse + 1]

    # When we convert that to normalized references
    references: List[bible.NormalizedReference] = bible.convert_verse_ids_to_references(
        verse_ids
    )

    # Then the result is a single normalized reference that spans multiple books
    # rather than one for each book.
    assert references == [
        bible.NormalizedReference(bible.Book.ROMANS, 1, 1, 1, 25, bible.Book.PHILEMON),
    ]
