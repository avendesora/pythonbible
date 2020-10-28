import re
from collections import namedtuple

from pythonbible.regular_expressions import BOOK_REGULAR_EXPRESSIONS
from pythonbible.regular_expressions import SCRIPTURE_REFERENCE_REGULAR_EXPRESSION
from pythonbible.roman_numeral_util import convert_all_roman_numerals_to_integers
from pythonbible.validator import is_valid_reference
from pythonbible.verses import get_max_number_of_verses, get_number_of_chapters

NormalizedReference = namedtuple("NormalizedReference", "book start_chapter start_verse end_chapter end_verse")


def get_references(text):
    """
    Searches the text for scripture references and returns any that are found in a list of normalized tuple references.

    :param text: a string that may contain zero or more scripture references
    :return: a list of tuples. each tuple is in the format (book, start_chapter, start_verse, end_chapter, end_verse)
    """
    references = []

    # First replace all roman numerals in the text with integers.
    clean_text = convert_all_roman_numerals_to_integers(text)

    for match in re.finditer(SCRIPTURE_REFERENCE_REGULAR_EXPRESSION, clean_text):
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

    if len(reference_without_book.strip()) == 0:
        max_chapter = get_number_of_chapters(book)
        max_verse = get_max_number_of_verses(book, max_chapter)
        references.append(NormalizedReference(book, 1, 1, max_chapter, max_verse))
    else:
        for sub_reference in reference_without_book.split(","):
            start_chapter, start_verse, end_chapter, end_verse = _process_sub_reference(
                sub_reference, book, start_chapter
            )

            new_reference = NormalizedReference(book, start_chapter, start_verse, end_chapter, end_verse)

            if is_valid_reference(new_reference):
                references.append(new_reference)
            else:
                # TODO - ignore? raise error?
                pass

            start_chapter = end_chapter

    return references


def _process_sub_reference(sub_reference, book, start_chapter):
    start_verse = None
    end_chapter = None
    end_verse = None
    no_verses = False

    clean_sub_reference = sub_reference.replace(".", ":")
    chapter_and_verse_range = clean_sub_reference.split("-")
    min_chapter_and_verse = chapter_and_verse_range[0]
    min_chapter_and_verse = min_chapter_and_verse.split(":")

    if len(min_chapter_and_verse) == 1:
        if start_chapter:
            start_verse = int(min_chapter_and_verse[0].strip())
            end_chapter = start_chapter
            end_verse = start_verse
        else:
            start_chapter = int(min_chapter_and_verse[0].strip())
            start_verse = 1
            end_chapter = start_chapter
            end_verse = get_max_number_of_verses(book, end_chapter)
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
                end_verse = get_max_number_of_verses(book, end_chapter)
            else:
                end_verse = int(max_chapter_and_verse[0].strip())
        elif len(max_chapter_and_verse) == 2:
            end_chapter = int(max_chapter_and_verse[0].strip())
            end_verse = int(max_chapter_and_verse[1].strip())

    return start_chapter, start_verse, end_chapter, end_verse
