import re
from typing import List, Optional, Match, AnyStr

from .books import Book
from .normalized_reference import NormalizedReference
from .regular_expressions import (
    BOOK_REGULAR_EXPRESSIONS,
    SCRIPTURE_REFERENCE_REGULAR_EXPRESSION,
)
from .roman_numeral_util import convert_all_roman_numerals_to_integers
from .validator import is_valid_reference
from .verses import get_max_number_of_verses, get_number_of_chapters


def get_references(text: str) -> List[NormalizedReference]:
    """
    Searches the text for scripture references and returns any that are found in a list of normalized tuple references.

    :param text: a string that may contain zero or more scripture references
    :return: a list of tuples. each tuple is in the format (book, start_chapter, start_verse, end_chapter, end_verse)
    """
    references: List[NormalizedReference] = []

    # First replace all roman numerals in the text with integers.
    clean_text: str = convert_all_roman_numerals_to_integers(text)

    for match in re.finditer(SCRIPTURE_REFERENCE_REGULAR_EXPRESSION, clean_text):
        references.extend(normalize_reference(match[0]))

    return references


def normalize_reference(reference: str) -> List[NormalizedReference]:
    """
    Converts a scripture reference string into a list of normalized tuple references.

    :param reference: a string that is a scripture reference
    :return: a list of tuples. each tuple is in the format (book, start_chapter, start_verse, end_chapter, end_verse)
    """
    references: List[NormalizedReference] = []
    books: list[Book] = []
    cleaned_references: list[str] = []
    reference_without_books: str = reference
    start: int
    end: int
    book_found: bool = True

    while book_found:
        book_found = False

        for book, regular_expression in BOOK_REGULAR_EXPRESSIONS.items():
            match: Optional[Match[AnyStr]] = re.search(
                regular_expression, reference_without_books, re.IGNORECASE
            )

            if match:
                start, end = match.regs[0]

                if start != 0 and len(books) == 0:
                    continue

                book_found = True

                if len(books) > 0:
                    cleaned_references.append(reference_without_books[:start])

                reference_without_books = reference_without_books[end:]
                books.append(book)
                continue

    cleaned_references.append(reference_without_books)

    # First Book
    first_book_references = _process_sub_references(
        books[0], cleaned_references[0].strip()
    )

    if len(books) == 1:
        return first_book_references

    # Second Book
    second_book_references = _process_sub_references(
        books[1], cleaned_references[1].strip()
    )

    if len(first_book_references) > 1:
        references.extend(first_book_references[:-1])

    # Combine last first reference with first second reference
    last_first_reference = first_book_references[-1]
    first_second_reference = second_book_references[0]

    references.append(
        NormalizedReference(
            last_first_reference.book,
            last_first_reference.start_chapter,
            last_first_reference.start_verse,
            first_second_reference.end_chapter,
            first_second_reference.end_verse,
            first_second_reference.book,
        )
    )

    if len(second_book_references) > 1:
        references.extend(second_book_references[1:])

    return references


def _process_sub_references(book: Book, reference: str) -> List[NormalizedReference]:
    references: List[NormalizedReference] = []
    start_chapter: Optional[int] = None

    for sub_reference in reference.split(","):
        if (len(sub_reference) == 0 or sub_reference == "-") and len(references) == 0:
            max_chapter: int = get_number_of_chapters(book)
            max_verse: int = get_max_number_of_verses(book, max_chapter)
            references.append(NormalizedReference(book, 1, 1, max_chapter, max_verse))
            continue

        if sub_reference.endswith("-"):
            sub_reference = sub_reference[:-1]

        start_chapter, start_verse, end_chapter, end_verse = _process_sub_reference(
            sub_reference, book, start_chapter
        )

        new_reference = NormalizedReference(
            book, start_chapter, start_verse, end_chapter, end_verse
        )

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
    min_chapter_and_verse = chapter_and_verse_range[0].strip()
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
