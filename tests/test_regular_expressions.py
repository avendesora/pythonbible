try:
    import regex as re
except ModuleNotFoundError:
    import re

from typing import List, Match, Optional

import pythonbible as bible
from pythonbible import regular_expressions


def test_chapter_regular_expression() -> None:
    # given a string with a chapter number
    chapter_string: str = "The chapter number is 132."

    # when evaluating that string against the chapter regular expression
    match: Optional[Match[str]] = re.search(
        regular_expressions.CHAPTER_REGEX, chapter_string
    )

    # then the match is found
    assert match and match.group(0) == "132"


def test_verse_regular_expression() -> None:
    # given a string with a verse number
    verse_string: str = "The verse number is 25."

    # when evaluating that string against the verse regular expression
    match: Optional[Match[str]] = re.search(
        regular_expressions.VERSE_REGEX, verse_string
    )

    # then the match is found
    assert match and match.group(0) == "25"


def test_chapter_and_verse_regular_expression() -> None:
    chapter_and_verse_references: List[str] = [
        "1:2",
        "3",
        "142 : 5",
        "43:    324",
    ]

    for reference in chapter_and_verse_references:
        # given a string with a chapter and verse reference
        chapter_and_verse_string: str = (
            f"The chapter and verse reference is {reference}."
        )

        # when evaluating that string against the chapter and verse regular expression
        match: Optional[Match[str]] = re.search(
            regular_expressions.CHAPTER_AND_VERSE_REGEX, chapter_and_verse_string
        )

        # then the match is found
        assert match and match.group(0) == reference


def test_chapter_range_regular_expression() -> None:
    chapter_range_references: List[str] = [
        "1:2-3",
        "3-4",
        "142 : 5 - 53 : 23",
        "43:    324 - 325",
    ]

    for reference in chapter_range_references:
        # given a string with a chapter range reference
        chapter_range_string: str = f"The chapter range reference is {reference}."

        # when evaluating that string against the chapter range regular expression
        match: Optional[Match[str]] = re.search(
            regular_expressions.RANGE_REGEX, chapter_range_string
        )

        # then the match is found
        assert match and match.group(0) == reference


def test_additional_reference_regular_expression() -> None:
    additional_references: List[str] = [
        "1:2,4",
        "3-4,6",
        "123 : 5 - 13, 16 - 18",
        "32:43-45,54,33:12",
    ]

    for reference in additional_references:
        # given a string with an additional reference
        additional_reference_string: str = f"The additional reference is {reference}."

        # when evaluating that string against the additional reference regular expression
        match: Optional[Match[str]] = re.search(
            regular_expressions.FULL_CHAPTER_AND_VERSE_REGEX,
            additional_reference_string,
        )

        # then the match is found
        assert match and match.group(0) == reference


def test_multiple_additional_references() -> None:
    # given a string with multiple additional references
    full_string: str = "You should read Matthew 1:18 - 2:18, Luke 3: 5-7, Psalm 130:4,8 and Jeremiah 29:32-30:10,11"

    # when evaluating that string against the full regular expression
    match: List[Match[str]] = re.findall(
        regular_expressions.FULL_CHAPTER_AND_VERSE_REGEX, full_string
    )

    # then the matches are found
    assert len(match) == 4
    assert match[0][0] == "1:18 - 2:18"
    assert match[1][0] == "3: 5-7"
    assert match[2][0] == "130:4,8"
    assert match[3][0] == "29:32-30:10,11"


def test_multiple_full_references() -> None:
    # given a string with multiple full scripture references
    full_string: str = "You should read Matthew 1:18 - 2:18, Luke 3: 5-7, Psalm 130:4,8 and Jeremiah 29:32-30:10,11"

    # when evaluating that string against the full regular expression
    match: List[Match[str]] = re.findall(
        regular_expressions.SCRIPTURE_REFERENCE_REGULAR_EXPRESSION, full_string
    )

    # then the matches are found
    assert len(match) == 4
    assert match[0][0] == "Matthew 1:18 - 2:18"
    assert match[1][0] == "Luke 3: 5-7"
    assert match[2][0] == "Psalm 130:4,8"
    assert match[3][0] == "Jeremiah 29:32-30:10,11"


def test_multiple_full_references_lower_case() -> None:
    # given a lower case string with multiple full scripture references
    full_string: str = "You should read Matthew 1:18 - 2:18, Luke 3: 5-7, Psalm 130:4,8 and Jeremiah 29:32-30:10,12".lower()

    # when evaluating that string against the full regular expression
    match: List[Match[str]] = re.findall(
        regular_expressions.SCRIPTURE_REFERENCE_REGULAR_EXPRESSION, full_string
    )

    # then the matches are found
    assert len(match) == 4
    assert match[0][0] == "Matthew 1:18 - 2:18".lower()
    assert match[1][0] == "Luke 3: 5-7".lower()
    assert match[2][0] == "Psalm 130:4,8".lower()
    assert match[3][0] == "Jeremiah 29:32-30:10,12".lower()


def test_reference_with_no_verses() -> None:
    # given a string with a reference with no verse numbers
    test_string: str = "The ten commandments can be found in Exodus 20."

    # when evaluating that string against the full regular expression
    match: List[Match[str]] = re.findall(
        regular_expressions.SCRIPTURE_REFERENCE_REGULAR_EXPRESSION, test_string
    )

    # then the matches are found
    assert len(match) == 1
    assert match[0][0] == "Exodus 20"


def test_philemon_not_philippians() -> None:
    # given a string with a Philemon reference
    text: str = "Philemon 1:9"

    # when evaluating the string to see if it matches the Philippians regular expression
    matches: List[Match[str]] = re.findall(
        regular_expressions.BOOK_REGULAR_EXPRESSIONS.get(bible.Book.PHILIPPIANS, ""),
        text,
    )

    # then the matches are not found
    assert len(matches) == 0

    # when evaluating the string to see if it matches the Philemon regular expression
    matches = re.findall(
        regular_expressions.BOOK_REGULAR_EXPRESSIONS.get(bible.Book.PHILEMON, ""), text
    )

    # then the match is found
    assert len(matches) == 1


def test_cross_book_regex() -> None:
    # given a reference that ranges over multiple books
    text: str = "The books of the law are Genesis - Deuteronomy"

    matches: List[Match[str]] = re.findall(regular_expressions.CROSS_BOOK_REGEX, text)

    assert len(matches) == 1
    assert matches[0][0] == "Genesis - Deuteronomy"
