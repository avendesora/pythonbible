import re

from bible import regular_expressions


def test_chapter_regular_expression():
    # given a string with a chapter number
    chapter_string = "The chapter number is 132."

    # when evaluating that string against the chapter regular expression
    match = re.search(regular_expressions.CHAPTER_REGEX, chapter_string)

    # then the match is found
    assert match.group(0) == "132"


def test_verse_regular_expression():
    # given a string with a verse number
    verse_string = "The verse number is 25."

    # when evaluating that string against the verse regular expression
    match = re.search(regular_expressions.VERSE_REGEX, verse_string)

    # then the match is found
    assert match.group(0) == "25"


def test_chapter_and_verse_regular_expression():
    chapter_and_verse_references = [
        "1:2",
        "3",
        "142 : 5",
        "43:    324",
    ]

    for reference in chapter_and_verse_references:
        # given a string with a chapter and verse reference
        chapter_and_verse_string = f"The chapter and verse reference is {reference}."

        # when evaluating that string against the chapter and verse regular expression
        match = re.search(
            regular_expressions.CHAPTER_AND_VERSE_REGEX, chapter_and_verse_string
        )

        # then the match is found
        assert match.group(0) == reference


def test_chapter_range_regular_expression():
    chapter_range_references = [
        "1:2-3",
        "3-4",
        "142 : 5 - 53 : 23",
        "43:    324 - 325",
    ]

    for reference in chapter_range_references:
        # given a string with a chapter range reference
        chapter_range_string = f"The chapter range reference is {reference}."

        # when evaluating that string against the chapter range regular expression
        match = re.search(regular_expressions.RANGE_REGEX, chapter_range_string)

        # then the match is found
        assert match.group(0) == reference


def test_additional_reference_regular_expression():
    additional_references = [
        "1:2,4",
        "3-4,6",
        "123 : 5 - 13, 16 - 18",
        "32:43-45,54,33:12",
    ]

    for reference in additional_references:
        # given a string with an additional reference
        additional_reference_string = f"The additional reference is {reference}."

        # when evaluating that string against the additional reference regular expression
        match = re.search(
            regular_expressions.FULL_CHAPTER_AND_VERSE_REGEX,
            additional_reference_string,
        )

        # then the match is found
        assert match.group(0) == reference


def test_multiple_additional_references():
    # given a string with multiple additional references
    full_string = "You should read Matthew 1:18 - 2:18, Luke 3: 5-7, Psalm 130:4,8 and Jeremiah 29:32-30:10,11"

    # when evaluating that string against the full regular expression
    match = re.findall(regular_expressions.FULL_CHAPTER_AND_VERSE_REGEX, full_string)

    # then the matches are found
    assert len(match) == 4
    assert match[0][0] == "1:18 - 2:18"
    assert match[1][0] == "3: 5-7"
    assert match[2][0] == "130:4,8"
    assert match[3][0] == "29:32-30:10,11"


def test_multiple_full_references():
    # given a string with multiple full scripture references
    full_string = "You should read Matthew 1:18 - 2:18, Luke 3: 5-7, Psalm 130:4,8 and Jeremiah 29:32-30:10,11"

    # when evaluating that string against the full regular expression
    match = re.findall(
        regular_expressions.SCRIPTURE_REFERENCE_REGULAR_EXPRESSION, full_string
    )

    # then the matches are found
    assert len(match) == 4
    assert match[0][0] == "Matthew"
    assert match[0][1] == "1:18 - 2:18"
    assert match[1][0] == "Luke"
    assert match[1][1] == "3: 5-7"
    assert match[2][0] == "Psalm"
    assert match[2][1] == "130:4,8"
    assert match[3][0] == "Jeremiah"
    assert match[3][1] == "29:32-30:10,11"
