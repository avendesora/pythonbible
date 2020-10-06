import re

from bible.books import VERSE_IDS
from bible.errors import InvalidVerseError
from bible.regular_expressions import BOOK_REGULAR_EXPRESSIONS
from bible.regular_expressions import SCRIPTURE_REFERENCE_REGULAR_EXPRESSION


def get_references(text):
    """
    Searches the text for scripture references and returns any that are found in a list of normalized tuple references.
    :param text: a string that may contain zero or more scripture references
    :return: a list of tuples. each tuple is in the format (book, start_chapter, start_verse, end_chapter, end_verse)
    """
    references = []

    for match in re.finditer(SCRIPTURE_REFERENCE_REGULAR_EXPRESSION, text):
        references.extend(normalize_reference(match[0]))

    return references


def normalize_reference(reference):
    """
    Converts a scripture reference string into a list of normalized tuple references.
    :param reference: a string that is a scripture reference
    :return: a list of tuples. each tuple is in the format (book, start_chapter, start_verse, end_chapter, end_verse)
    """
    references = []
    book = None

    for book, regular_expression in BOOK_REGULAR_EXPRESSIONS.items():
        match = re.match(regular_expression, reference, re.IGNORECASE)

        if match:
            reference_without_book = reference.replace(match[0], "")
            break

    start_chapter = None
    start_verse = None
    end_chapter = None
    end_verse = None
    no_verses = False

    for sub_reference in reference_without_book.split(","):
        chapter_and_verse_range = sub_reference.split("-")

        min_chapter_and_verse = chapter_and_verse_range[0]

        min_chapter_and_verse = min_chapter_and_verse.split(":")

        if len(min_chapter_and_verse) == 1:
            if start_chapter:
                start_verse = int(min_chapter_and_verse[0].strip())
                end_verse = start_verse
            else:
                start_chapter = int(min_chapter_and_verse[0].strip())
                start_verse = 1
                no_verses = True
        elif len(min_chapter_and_verse) == 2:
            start_chapter = int(min_chapter_and_verse[0].strip())
            end_chapter = start_chapter
            start_verse = int(min_chapter_and_verse[1].strip())
            end_verse = start_verse

        if len(chapter_and_verse_range) > 1:
            max_chapter_and_verse = chapter_and_verse_range[1]
            max_chapter_and_verse = max_chapter_and_verse.split(":")

            if len(max_chapter_and_verse) == 1:
                if no_verses:
                    end_chapter = int(max_chapter_and_verse[0].strip())
                    end_verse = (
                        999  # TODO - get actual max verse for book and end chapter
                    )
                else:
                    end_verse = int(max_chapter_and_verse[0].strip())
            elif len(max_chapter_and_verse) == 2:
                end_chapter = int(max_chapter_and_verse[0].strip())
                end_verse = int(max_chapter_and_verse[1].strip())

        references.append((book, start_chapter, start_verse, end_chapter, end_verse))

    # TODO - make sure references are valid
    return references


def convert_references_to_verse_ids(references):
    """

    :param references:
    :return:
    """
    verse_ids = []

    for reference in references:
        verse_ids.extend(convert_reference_to_verse_ids(reference))

    return verse_ids


def convert_reference_to_verse_ids(reference):
    """

    :param reference:
    :return:
    """
    start_verse_id = get_verse_id(reference[0], reference[1], reference[2])
    end_verse_id = get_verse_id(reference[0], reference[3], reference[4])
    return VERSE_IDS[VERSE_IDS.index(start_verse_id):VERSE_IDS.index(end_verse_id) + 1]


def get_verse_id(book_of_the_bible, chapter_number, verse_number):
    """

    :param book_of_the_bible:
    :param chapter_number:
    :param verse_number:
    :return:
    """
    verse_id = int(book_of_the_bible) * 1000000 + chapter_number * 1000 + verse_number

    if verse_id not in VERSE_IDS:
        raise InvalidVerseError(
            f"{book_of_the_bible.name()} {chapter_number}:{verse_number} is not a valid Bible verse."
        )

    return verse_id
