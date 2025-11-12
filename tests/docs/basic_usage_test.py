"""Tests for basic usage examples in the documentation.

These are intended to ensure that the code snippets provided in the documentation
remain accurate and functional as the library evolves.

If any of these tests fail, it indicates that the corresponding documentation
examples need to be updated to reflect the current state of the library.
"""

from __future__ import annotations

import pythonbible as bible


def test_finding_scripture_references_in_text() -> None:
    results = bible.get_references(
        "The parable of the lost sheep is told in Matthew 18:12-14 and Luke 15:3-7."
    )
    assert results == [
        bible.NormalizedReference(
            book=bible.Book.MATTHEW,
            start_chapter=18,
            start_verse=12,
            end_chapter=18,
            end_verse=14,
            end_book=bible.Book.MATTHEW,
        ),
        bible.NormalizedReference(
            book=bible.Book.LUKE,
            start_chapter=15,
            start_verse=3,
            end_chapter=15,
            end_verse=7,
            end_book=bible.Book.LUKE,
        ),
    ]


def test_converting_references_to_verse_ids_single() -> None:
    references = [
        bible.NormalizedReference(
            book=bible.Book.GENESIS,
            start_chapter=1,
            start_verse=1,
            end_chapter=1,
            end_verse=4,
        ),
    ]
    verse_ids = bible.convert_references_to_verse_ids(references)
    assert verse_ids == [1001001, 1001002, 1001003, 1001004]


def test_converting_references_to_verse_ids_multiple() -> None:
    references = [
        bible.NormalizedReference(
            book=bible.Book.MATTHEW,
            start_chapter=18,
            start_verse=12,
            end_chapter=18,
            end_verse=14,
        ),
        bible.NormalizedReference(
            book=bible.Book.LUKE,
            start_chapter=15,
            start_verse=3,
            end_chapter=15,
            end_verse=7,
        ),
    ]
    verse_ids = bible.convert_references_to_verse_ids(references)
    assert verse_ids == [
        40018012,
        40018013,
        40018014,
        42015003,
        42015004,
        42015005,
        42015006,
        42015007,
    ]


def test_converting_verse_ids_to_references() -> None:
    verse_ids = [
        40018012,
        40018013,
        40018014,
        42015003,
        42015004,
        42015005,
        42015006,
        42015007,
    ]
    references = bible.convert_verse_ids_to_references(verse_ids)
    assert references == [
        bible.NormalizedReference(
            book=bible.Book.MATTHEW,
            start_chapter=18,
            start_verse=12,
            end_chapter=18,
            end_verse=14,
            end_book=bible.Book.MATTHEW,
        ),
        bible.NormalizedReference(
            book=bible.Book.LUKE,
            start_chapter=15,
            start_verse=3,
            end_chapter=15,
            end_verse=7,
            end_book=bible.Book.LUKE,
        ),
    ]


def test_formatting_scripture_references() -> None:
    references = bible.get_references(
        "My favorite verses are Philippians 4:8, Isaiah 55:13, and Philippians 4:4-7."
    )
    formatted_references = bible.format_scripture_references(references)
    assert formatted_references == "Isaiah 55:13;Philippians 4:4-8"


def test_formatting_scripture_text() -> None:
    formatted_text = bible.get_verse_text(1001001)
    assert formatted_text == "In the beginning God created the heavens and the earth."
