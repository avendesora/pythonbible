from __future__ import annotations

import pytest

import pythonbible as bible


@pytest.mark.parametrize(
    ("reference_string", "expected_references_by_version"),
    [
        (
            "Genesis",
            {
                bible.Version.AMERICAN_STANDARD: ("Genesis", "Genesis 1:1-50:26"),
                bible.Version.KING_JAMES: ("Genesis", "Genesis 1:1-50:26"),
            },
        ),
        (
            "Psalm 119",
            {
                bible.Version.AMERICAN_STANDARD: (
                    "Psalms 119:1-176",
                    "Psalms 119:1-176",
                ),
                bible.Version.DOUAY_RHEIMS: ("Psalms 119:1", "Psalms 119:1"),
                bible.Version.KING_JAMES: ("Psalms 119:1-176", "Psalms 119:1-176"),
            },
        ),
    ],
)
def test_format_scripture_references(
    reference_string: str,
    expected_references_by_version: dict[bible.Version, tuple[str, str]],
) -> None:
    # Given a reference string and a dictionary of expected references by version,
    # When the scripture references are formatted,
    for version, expected_references in expected_references_by_version.items():
        # Then the actual references should match the expected references by version.
        actual_reference = bible.format_scripture_references(
            bible.get_references(reference_string),
            version=version,
        )
        actual_reference_with_chapters = bible.format_scripture_references(
            bible.get_references(reference_string),
            version=version,
            always_include_chapter_numbers=True,
        )

        # Then the actual references should match the expected references by version.
        assert actual_reference == expected_references[0]
        assert actual_reference_with_chapters == expected_references[1]
