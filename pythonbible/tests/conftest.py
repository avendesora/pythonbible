from __future__ import annotations

import pytest

import pythonbible as bible


@pytest.fixture
def verse_id() -> int:
    return 1001001


@pytest.fixture
def invalid_verse_id() -> int:
    return 1100100


@pytest.fixture
def book() -> bible.Book:
    return bible.Book.GENESIS


@pytest.fixture
def chapter() -> int:
    return 1


@pytest.fixture
def verse() -> int:
    return 1


@pytest.fixture
def invalid_chapter() -> int:
    return 100


@pytest.fixture
def invalid_verse() -> int:
    return 100


@pytest.fixture
def normalized_references_complex() -> list[bible.NormalizedReference]:
    return [
        bible.NormalizedReference(bible.Book.PSALMS, 130, 4, 130, 4, bible.Book.PSALMS),
        bible.NormalizedReference(bible.Book.PSALMS, 130, 8, 130, 8, bible.Book.PSALMS),
        bible.NormalizedReference(
            bible.Book.JEREMIAH,
            29,
            32,
            30,
            10,
            bible.Book.JEREMIAH,
        ),
        bible.NormalizedReference(
            bible.Book.JEREMIAH,
            31,
            12,
            31,
            12,
            bible.Book.JEREMIAH,
        ),
        bible.NormalizedReference(bible.Book.MATTHEW, 1, 18, 2, 18, bible.Book.MATTHEW),
        bible.NormalizedReference(bible.Book.LUKE, 3, 5, 3, 7, bible.Book.LUKE),
    ]


@pytest.fixture
def reference() -> bible.NormalizedReference:
    return bible.NormalizedReference(bible.Book.GENESIS, 1, 1, 3, 4)


@pytest.fixture
def invalid_reference() -> bible.NormalizedReference:
    return bible.NormalizedReference(bible.Book.GENESIS, 1, 1, 100, 100)


@pytest.fixture
def reference_string() -> str:
    return "Genesis 1:1-3:4"


@pytest.fixture
def references() -> list[bible.NormalizedReference]:
    return [
        bible.NormalizedReference(
            bible.Book.MATTHEW,
            18,
            12,
            18,
            14,
            bible.Book.MATTHEW,
        ),
        bible.NormalizedReference(bible.Book.LUKE, 15, 3, 15, 7, bible.Book.LUKE),
    ]


@pytest.fixture
def verse_ids() -> list[int]:
    return [
        40018012,
        40018013,
        40018014,
        42015003,
        42015004,
        42015005,
        42015006,
        42015007,
    ]


@pytest.fixture
def verse_ids_complex() -> list[int]:
    return [
        19130004,
        19130008,
        24029032,
        24030001,
        24030002,
        24030003,
        24030004,
        24030005,
        24030006,
        24030007,
        24030008,
        24030009,
        24030010,
        24031012,
        40001018,
        40001019,
        40001020,
        40001021,
        40001022,
        40001023,
        40001024,
        40001025,
        40002001,
        40002002,
        40002003,
        40002004,
        40002005,
        40002006,
        40002007,
        40002008,
        40002009,
        40002010,
        40002011,
        40002012,
        40002013,
        40002014,
        40002015,
        40002016,
        40002017,
        40002018,
        42003005,
        42003006,
        42003007,
    ]
