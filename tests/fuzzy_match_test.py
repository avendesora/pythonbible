"""Tests for discussion: https://github.com/avendesora/pythonbible/discussions/120."""

from __future__ import annotations

import pytest

import pythonbible as bible


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_1() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = (
        "Second Timothy chapter two verses three and four says endure hardship"
    )
    expected = [bible.NormalizedReference(bible.Book.TIMOTHY_2, 2, 3, 2, 4, None)]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_2() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = "If you read Ephesians four 17 through 32 all the ammunition"
    expected = [bible.NormalizedReference(bible.Book.EPHESIANS, 4, 17, 4, 32, None)]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_3() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = (
        "remember that powerful message of Paul in first Corinthians nine"
    )
    expected = [bible.NormalizedReference(bible.Book.CORINTHIANS_1, 9, 1, 9, 27, None)]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_4() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = (
        "in Jesus's first sermonic presentation on planet earth in Matthew five "
        "through seven"
    )

    expected = [bible.NormalizedReference(bible.Book.MATTHEW, 5, 1, 7, 29, None)]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_5() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = "Jesus said over in Matthew chapter six, verse number 12"
    expected = [bible.NormalizedReference(bible.Book.MATTHEW, 6, 12, 6, 12, None)]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_6() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = "Genesis four, 25."
    expected = [bible.NormalizedReference(bible.Book.GENESIS, 4, 25, 4, 25, None)]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_7() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = "and forth between Haggai two and Ezra three."
    expected = [
        bible.NormalizedReference(bible.Book.HAGGAI, 2, 1, 2, 23, None),
        bible.NormalizedReference(bible.Book.EZRA, 3, 1, 3, 13, None),
    ]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_8() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = "and go and report to John one-fifteen and thirty."
    expected = [
        bible.NormalizedReference(bible.Book.JOHN, 1, 15, 1, 15, None),
        bible.NormalizedReference(bible.Book.JOHN, 1, 30, 1, 30, None),
    ]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_9() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = (
        "I want to focus on here is Colossians chapter three, 22 through "
        "verses through chapter four, verse one."
    )
    expected = [bible.NormalizedReference(bible.Book.COLOSSIANS, 3, 22, 4, 1, None)]

    assert bible.get_references(fuzzy_match_input) == expected


def test_fuzzy_match_10() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = "In 1 Corinthians 9.22, you see Paul saying"
    expected = [bible.NormalizedReference(bible.Book.CORINTHIANS_1, 9, 22, 9, 22, None)]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_11() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = "says in Mark 16 10 that the disciples were"
    expected = [bible.NormalizedReference(bible.Book.MARK, 16, 10, 16, 10, None)]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_12() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = (
        "through that fire, 1 Kings 18.24-38, 1 Chronicles 21.26, 2 Chronicles 7.1-3."
    )
    expected = [
        bible.NormalizedReference(bible.Book.KINGS_1, 18, 24, 18, 38, None),
        bible.NormalizedReference(bible.Book.CHRONICLES_1, 21, 26, 21, 26, None),
        bible.NormalizedReference(bible.Book.CHRONICLES_2, 7, 1, 7, 3, None),
    ]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_13() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = (
        "open their Bibles to first Corinthians 14, 34, 35 and say, look"
    )
    expected = [
        bible.NormalizedReference(bible.Book.CORINTHIANS_1, 14, 34, 14, 35, None),
    ]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_14() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = "Genesis 1, 26, 2, 7, and 21, 22."
    expected = [
        bible.NormalizedReference(bible.Book.GENESIS, 1, 26, 1, 26, None),
        bible.NormalizedReference(bible.Book.GENESIS, 2, 7, 2, 7, None),
        bible.NormalizedReference(bible.Book.GENESIS, 21, 22, 21, 22, None),
    ]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_15() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = (
        "look in Revelations 21, 1 through 7, you can start reading all about"
    )
    expected = [bible.NormalizedReference(bible.Book.REVELATION, 21, 1, 21, 7, None)]

    assert bible.get_references(fuzzy_match_input) == expected


def test_fuzzy_match_16() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = "Psalms 103.12 says"
    expected = [bible.NormalizedReference(bible.Book.PSALMS, 103, 12, 103, 12, None)]

    assert bible.get_references(fuzzy_match_input) == expected


@pytest.mark.xfail(reason="fuzzy matching isn't fully supported yet")
def test_fuzzy_match_17() -> None:
    """Test fuzzy matching of references."""
    fuzzy_match_input = "for one another Galatians 6 1 & 2 clearly gives us"
    expected = [bible.NormalizedReference(bible.Book.GALATIANS, 6, 1, 6, 2, None)]

    assert bible.get_references(fuzzy_match_input) == expected
