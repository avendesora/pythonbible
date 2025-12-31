from __future__ import annotations

import pytest

import pythonbible as bible


@pytest.mark.parametrize(
    ("input_text", "expected_references"),
    [
        (
            "Genesis",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    None,
                    None,
                    None,
                    None,
                    bible.Book.GENESIS,
                ),
            ],
        ),
        (
            "Genesis 1",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    1,
                    None,
                    1,
                    None,
                    bible.Book.GENESIS,
                ),
            ],
        ),
        (
            "Genesis 1:1",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    1,
                    1,
                    1,
                    1,
                    bible.Book.GENESIS,
                ),
            ],
        ),
        (
            "Genesis 1:1-2",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    1,
                    1,
                    1,
                    2,
                    bible.Book.GENESIS,
                ),
            ],
        ),
        (
            "Genesis 1-2",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    1,
                    None,
                    2,
                    None,
                    bible.Book.GENESIS,
                ),
            ],
        ),
        (
            "Genesis 1:1-2:3",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    1,
                    1,
                    2,
                    3,
                    bible.Book.GENESIS,
                ),
            ],
        ),
        (
            "Genesis - Exodus",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    None,
                    None,
                    None,
                    None,
                    bible.Book.EXODUS,
                ),
            ],
        ),
        (
            "Genesis 1 - Exodus",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    1,
                    None,
                    None,
                    None,
                    bible.Book.EXODUS,
                ),
            ],
        ),
        (
            "Genesis - Exodus 2",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    None,
                    None,
                    2,
                    None,
                    bible.Book.EXODUS,
                ),
            ],
        ),
        (
            "Genesis 1 - Exodus 2",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    1,
                    None,
                    2,
                    None,
                    bible.Book.EXODUS,
                ),
            ],
        ),
        (
            "Genesis 1:1 - Exodus 2",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    1,
                    1,
                    2,
                    None,
                    bible.Book.EXODUS,
                ),
            ],
        ),
        (
            "Genesis 1 - Exodus 2:3",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    1,
                    None,
                    2,
                    3,
                    bible.Book.EXODUS,
                ),
            ],
        ),
        (
            "Genesis 1:1 - Exodus 2:3",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    1,
                    1,
                    2,
                    3,
                    bible.Book.EXODUS,
                ),
            ],
        ),
        (
            "Genesis 1:1-2:3, Exodus 3:4-5:6",
            [
                bible.NormalizedReference(
                    bible.Book.GENESIS,
                    1,
                    1,
                    2,
                    3,
                    bible.Book.GENESIS,
                ),
                bible.NormalizedReference(
                    bible.Book.EXODUS,
                    3,
                    4,
                    5,
                    6,
                    bible.Book.EXODUS,
                ),
            ],
        ),
    ],
)
def test_parser_normalized_reference_nulls(
    input_text: str,
    expected_references: list[bible.NormalizedReference],
) -> None:
    # Given a reference string that does not include verse numbers
    # When we parse the references from that text
    # Then the normalized reference does not include verse numbers
    assert bible.get_references(input_text) == expected_references
