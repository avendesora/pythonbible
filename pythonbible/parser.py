from __future__ import annotations

import re
from typing import Match
from typing import Pattern

from pythonbible.books import Book
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.regular_expressions import SCRIPTURE_REFERENCE_REGULAR_EXPRESSION
from pythonbible.roman_numeral_util import convert_all_roman_numerals_to_integers
from pythonbible.validator import is_valid_reference
from pythonbible.verses import get_number_of_chapters
from pythonbible.verses import get_number_of_verses
from pythonbible.verses import is_single_chapter_book

COLON = ":"
COMMA = ","
DASH = "-"
HTML_MDASH = "&mdash;"
HTML_NDASH = "&ndash;"
PERIOD = "."


def get_references(
    text: str,
    book_groups: dict[str, tuple[Book, ...]] | None = None,
) -> list[NormalizedReference]:
    """Search the text for scripture references.

    Return any scripture references that are found in a list of normalized references.

    :param text: String that may contain zero or more scripture references
    :type text: str
    :param book_groups: Optional dictionary of BookGroup (e.g. Old Testament) to its
                        related regular expression
    :type book_groups: dict[str, tuple[Book, ...]] or None
    :return: The list of found scripture references
    :rtype: list[NormalizedReference]
    """
    references: list[NormalizedReference] = []

    # First replace all roman numerals in the text with integers.
    clean_text: str = convert_all_roman_numerals_to_integers(text)
    clean_text = clean_text.replace(HTML_NDASH, DASH).replace(HTML_MDASH, DASH)

    for reference_match in re.finditer(
        SCRIPTURE_REFERENCE_REGULAR_EXPRESSION,
        clean_text,
    ):
        references.extend(normalize_reference(reference_match[0]))

    if book_groups:
        references.extend(_get_book_group_references(clean_text, book_groups))

    return references


def normalize_reference(reference: str) -> list[NormalizedReference]:
    """Convert a scripture reference string into a list of normalized tuple references.

    :param reference: a string that is a scripture reference
    :return: a list of tuples. each tuple is in the format (book, start_chapter,
             start_verse, end_chapter, end_verse)
    """
    references: list[NormalizedReference] = []
    books: list[Book] = []
    cleaned_references: list[str] = []
    reference_without_books: str = reference
    start: int
    end: int
    book_found: bool = True

    while book_found:
        book_found = False

        for book in Book:
            if reference_match := re.search(
                book.regular_expression,
                reference_without_books,
                re.IGNORECASE,
            ):
                start, end = reference_match.regs[0]

                if start != 0 and not books:
                    continue

                book_found = True

                if books:
                    cleaned_references.append(reference_without_books[:start])

                reference_without_books = reference_without_books[end:]
                books.append(book)

    cleaned_references.append(reference_without_books)

    # First Book
    first_book_references = _process_sub_references(
        books[0],
        cleaned_references[0].strip(),
    )

    if len(books) == 1:
        return first_book_references

    # Second Book
    second_book_references = _process_sub_references(
        books[1],
        cleaned_references[1].strip(),
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
        ),
    )

    if len(second_book_references) > 1:
        references.extend(second_book_references[1:])

    return references


def _process_sub_references(book: Book, reference: str) -> list[NormalizedReference]:
    references: list[NormalizedReference] = []
    start_chapter: int = 0

    for sub_reference in reference.split(COMMA):
        if (not sub_reference or sub_reference in {DASH, PERIOD}) and not references:
            max_chapter: int = get_number_of_chapters(book)
            max_verse: int = get_number_of_verses(book, max_chapter)
            references.append(NormalizedReference(book, 1, 1, max_chapter, max_verse))
            continue

        start_chapter, start_verse, end_chapter, end_verse = _process_sub_reference(
            sub_reference[:-1] if sub_reference.endswith(DASH) else sub_reference,
            book,
            start_chapter,
        )

        new_reference = NormalizedReference(
            book,
            start_chapter,
            start_verse,
            end_chapter,
            end_verse,
        )

        if is_valid_reference(new_reference):
            references.append(new_reference)

        start_chapter = end_chapter

    return references


def _process_sub_reference(
    sub_reference: str,
    book: Book,
    start_chapter: int,
) -> tuple[int, int, int, int]:
    start_verse: int = 0
    end_chapter: int = start_chapter
    end_verse: int = start_verse
    no_verses: bool = False

    clean_sub_reference: str = sub_reference.replace(PERIOD, COLON)
    chapter_and_verse_range: list[str] = clean_sub_reference.split(DASH)
    min_chapter_and_verse: list[str] = chapter_and_verse_range[0].strip().split(COLON)

    if len(min_chapter_and_verse) == 1:
        if start_chapter > 0:
            start_verse = int(min_chapter_and_verse[0].strip())
            end_chapter = start_chapter
            end_verse = start_verse
        elif is_single_chapter_book(book):
            start_chapter = 1
            start_verse = int(min_chapter_and_verse[0].strip())
            end_chapter = 1
            end_verse = start_verse
        else:
            start_chapter = int(min_chapter_and_verse[0].strip())
            start_verse = 1
            end_chapter = start_chapter
            end_verse = get_number_of_verses(book, end_chapter)
            no_verses = True
    elif len(min_chapter_and_verse) == 2:
        start_chapter = int(min_chapter_and_verse[0].strip())
        end_chapter = start_chapter
        start_verse = int(min_chapter_and_verse[1].strip())
        end_verse = start_verse

    if len(chapter_and_verse_range) > 1:
        max_chapter_and_verse = chapter_and_verse_range[1].split(COLON)

        if len(max_chapter_and_verse) == 1:
            if no_verses:
                end_chapter = int(max_chapter_and_verse[0].strip())
                end_verse = get_number_of_verses(book, end_chapter)
            else:
                end_verse = int(max_chapter_and_verse[0].strip())
        elif len(max_chapter_and_verse) == 2:
            end_chapter = int(max_chapter_and_verse[0].strip())
            end_verse = int(max_chapter_and_verse[1].strip())

    return start_chapter, start_verse, end_chapter, end_verse


def _get_book_group_references(
    text: str,
    book_groups: dict[str, tuple[Book, ...]],
) -> list[NormalizedReference]:
    references: list[NormalizedReference] = []
    book_group_regex: Pattern[str] = re.compile(
        "|".join(book_groups.keys()),
        re.IGNORECASE | re.UNICODE,
    )

    for match in re.finditer(book_group_regex, text):
        references.extend(_process_book_group_match(match[0], book_groups))

    return references


def _process_book_group_match(
    text: str,
    book_groups: dict[str, tuple[Book, ...]],
) -> list[NormalizedReference]:
    references: list[NormalizedReference] = []
    regular_expression: str
    books: tuple[Book, ...]

    for regular_expression, book_group_books in book_groups.items():
        reference_match: Match[str] | None = re.match(
            regular_expression,
            text,
            re.IGNORECASE,
        )

        if reference_match:
            books = book_group_books
            break

    start_book: Book = books[0]
    previous_book: Book = start_book

    for book in books[1:]:
        if book.value == previous_book.value + 1:
            previous_book = book
            continue

        references.append(_build_book_group_reference(start_book, previous_book))
        start_book = book
        previous_book = book

    references.append(_build_book_group_reference(start_book, previous_book))

    return references


def _build_book_group_reference(
    start_book: Book,
    end_book: Book,
) -> NormalizedReference:
    max_chapter: int = get_number_of_chapters(end_book)
    max_verse: int = get_number_of_verses(end_book, max_chapter)
    return NormalizedReference(start_book, 1, 1, max_chapter, max_verse, end_book)
