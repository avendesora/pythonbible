"""Tests for advanced usage examples in the documentation.

These are intended to ensure that the code snippets provided in the documentation
remain accurate and functional as the library evolves.

If any of these tests fail, it indicates that the corresponding documentation
examples need to be updated to reflect the current state of the library.
"""

from __future__ import annotations

import pytest

import pythonbible as bible


@pytest.mark.parametrize(
    ("reference_text", "expected_reference"),
    [
        (
            "Obadiah 1",
            [
                bible.NormalizedReference(
                    book=bible.Book.OBADIAH,
                    start_chapter=1,
                    start_verse=1,
                    end_chapter=1,
                    end_verse=1,
                    end_book=bible.Book.OBADIAH,
                ),
            ],
        ),
        (
            "Genesis 1",
            [
                bible.NormalizedReference(
                    book=bible.Book.GENESIS,
                    start_chapter=1,
                    start_verse=None,
                    end_chapter=1,
                    end_verse=None,
                    end_book=bible.Book.GENESIS,
                ),
            ],
        ),
        (
            "Philemon 3-6",
            [
                bible.NormalizedReference(
                    book=bible.Book.PHILEMON,
                    start_chapter=1,
                    start_verse=3,
                    end_chapter=1,
                    end_verse=6,
                    end_book=bible.Book.PHILEMON,
                ),
            ],
        ),
        (
            "Genesis 3-6",
            [
                bible.NormalizedReference(
                    book=bible.Book.GENESIS,
                    start_chapter=3,
                    start_verse=None,
                    end_chapter=6,
                    end_verse=None,
                    end_book=bible.Book.GENESIS,
                ),
            ],
        ),
        (
            "Genesis - Deuteronomy",
            [
                bible.NormalizedReference(
                    book=bible.Book.GENESIS,
                    start_chapter=None,
                    start_verse=None,
                    end_chapter=None,
                    end_verse=None,
                    end_book=bible.Book.DEUTERONOMY,
                ),
            ],
        ),
        (
            "Genesis;Exodus;Leviticus;Numbers;Deuteronomy",
            [
                bible.NormalizedReference(
                    book=bible.Book.GENESIS,
                    start_chapter=None,
                    start_verse=None,
                    end_chapter=None,
                    end_verse=None,
                    end_book=bible.Book.GENESIS,
                ),
                bible.NormalizedReference(
                    book=bible.Book.EXODUS,
                    start_chapter=None,
                    start_verse=None,
                    end_chapter=None,
                    end_verse=None,
                    end_book=bible.Book.EXODUS,
                ),
                bible.NormalizedReference(
                    book=bible.Book.LEVITICUS,
                    start_chapter=None,
                    start_verse=None,
                    end_chapter=None,
                    end_verse=None,
                    end_book=bible.Book.LEVITICUS,
                ),
                bible.NormalizedReference(
                    book=bible.Book.NUMBERS,
                    start_chapter=None,
                    start_verse=None,
                    end_chapter=None,
                    end_verse=None,
                    end_book=bible.Book.NUMBERS,
                ),
                bible.NormalizedReference(
                    book=bible.Book.DEUTERONOMY,
                    start_chapter=None,
                    start_verse=None,
                    end_chapter=None,
                    end_verse=None,
                    end_book=bible.Book.DEUTERONOMY,
                ),
            ],
        ),
    ],
)
def test_finding_references(
    reference_text: str,
    expected_reference: bible.NormalizedReference,
) -> None:
    assert bible.get_references(reference_text) == expected_reference


@pytest.mark.parametrize(
    ("input_reference", "output_reference", "always_include_chapter_numbers"),
    [
        ("Jude 2-8", "Jude 2-8", False),
        ("Jude 2-8", "Jude 1:2-8", True),
        ("Genesis - Deuteronomy", "Genesis - Deuteronomy", False),
        ("Genesis - Deuteronomy", "Genesis 1:1 - Deuteronomy 34:12", True),
    ],
)
def test_formatting_references_for_print_display(
    input_reference: str,
    output_reference: str,
    always_include_chapter_numbers: bool,
) -> None:
    references = bible.get_references(input_reference)
    assert (
        bible.format_scripture_references(
            references,
            always_include_chapter_numbers=always_include_chapter_numbers,
        )
        == output_reference
    )


def test_finding_references_by_book_groups_no_groups() -> None:
    assert bible.get_references("What are all of the books of the Old Testament?") == []


def test_finding_references_by_book_groups_default_groups() -> None:
    references = bible.get_references(
        "What are all of the books of the Old Testament?",
        book_groups=bible.BOOK_GROUPS,
    )

    assert references == [
        bible.NormalizedReference(
            book=bible.Book.GENESIS,
            start_chapter=1,
            start_verse=1,
            end_chapter=4,
            end_verse=6,
            end_book=bible.Book.MALACHI,
        ),
    ]

    assert bible.format_scripture_references(references) == "Genesis - Malachi"
    assert (
        bible.format_scripture_references(
            references,
            always_include_chapter_numbers=True,
        )
        == "Genesis 1:1 - Malachi 4:6"
    )


def test_finding_references_by_book_groups_subset_groups() -> None:
    ot_regex = bible.BookGroup.OLD_TESTAMENT.regular_expression
    nt_regex = bible.BookGroup.NEW_TESTAMENT.regular_expression
    ot_books = bible.BookGroup.OLD_TESTAMENT.books
    nt_books = bible.BookGroup.NEW_TESTAMENT.books
    book_groups_subset = {
        ot_regex: ot_books,
        nt_regex: nt_books,
    }
    references = bible.get_references(
        "I want to find the Old Testament books, not the Gospels.",
        book_groups=book_groups_subset,
    )
    assert references == [
        bible.NormalizedReference(
            book=bible.Book.GENESIS,
            start_chapter=1,
            start_verse=1,
            end_chapter=4,
            end_verse=6,
            end_book=bible.Book.MALACHI,
        ),
    ]


def test_finding_references_by_book_groups_custom_group() -> None:
    custom_book_groups: dict[str, tuple[bible.Book, ...]] = {
        "my favorite books": (
            bible.Book.PSALMS,
            bible.Book.PROVERBS,
            bible.Book.JOHN,
            bible.Book.PHILIPPIANS,
            bible.Book.JAMES,
        ),
    }
    references = bible.get_references(
        "What are my favorite books of the Bible?",
        book_groups=custom_book_groups,
    )

    assert references == [
        bible.NormalizedReference(
            book=bible.Book.PSALMS,
            start_chapter=1,
            start_verse=1,
            end_chapter=31,
            end_verse=31,
            end_book=bible.Book.PROVERBS,
        ),
        bible.NormalizedReference(
            book=bible.Book.JOHN,
            start_chapter=1,
            start_verse=1,
            end_chapter=21,
            end_verse=25,
            end_book=bible.Book.JOHN,
        ),
        bible.NormalizedReference(
            book=bible.Book.PHILIPPIANS,
            start_chapter=1,
            start_verse=1,
            end_chapter=4,
            end_verse=23,
            end_book=bible.Book.PHILIPPIANS,
        ),
        bible.NormalizedReference(
            book=bible.Book.JAMES,
            start_chapter=1,
            start_verse=1,
            end_chapter=5,
            end_verse=20,
            end_book=bible.Book.JAMES,
        ),
    ]

    assert (
        bible.format_scripture_references(references)
        == "Psalms - Proverbs;John;Philippians;James"
    )
