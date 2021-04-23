from typing import List

from pythonbible.books import Book
from pythonbible.errors import InvalidVerseError
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.validator import is_valid_verse_id
from pythonbible.verses import VERSE_IDS, get_book_chapter_verse, get_verse_id


def convert_references_to_verse_ids(references: List[NormalizedReference]) -> List[int]:
    """

    :param references: a list of normalized references
    :return: the list of verse ids associated with each of the references in the reference list
    """
    verse_ids: List[int] = []

    if references is not None:
        for reference in references:
            verse_ids.extend(convert_reference_to_verse_ids(reference))

    return verse_ids


def convert_reference_to_verse_ids(reference: NormalizedReference) -> List[int]:
    """

    :param reference: a normalized reference
    :return: the list of verse ids associated with the reference
    """
    if reference is None:
        return []

    end_book = reference.book if reference.end_book is None else reference.end_book

    start_verse_id: int = get_verse_id(
        reference.book, reference.start_chapter, reference.start_verse
    )
    end_verse_id: int = get_verse_id(
        end_book, reference.end_chapter, reference.end_verse
    )
    return VERSE_IDS[
        VERSE_IDS.index(start_verse_id) : VERSE_IDS.index(end_verse_id) + 1
    ]


def convert_verse_ids_to_references(verse_ids: List[int]) -> List[NormalizedReference]:
    """

    :param verse_ids:
    :return: a list of normalized references
    """
    references: List[NormalizedReference] = []

    if verse_ids is None or not verse_ids:
        return references

    verse_ids.sort()

    # Initialize with the first verse id in the list
    first_verse = verse_ids[0]

    if not is_valid_verse_id(first_verse):
        raise InvalidVerseError(verse_id=first_verse)

    previous_verse_id: int = verse_ids[0]

    book: Book
    chapter: int
    verse: int
    book, chapter, verse = get_book_chapter_verse(previous_verse_id)

    start_book: Book = book
    previous_book: Book = book
    start_chapter: int = chapter
    start_verse: int = verse
    previous_chapter: int = chapter
    previous_verse: int = verse

    # Loop through the remaining verse ids in the list
    for verse_id in verse_ids[1:]:
        if not is_valid_verse_id(verse_id):
            raise InvalidVerseError(verse_id=verse_id)

        book, chapter, verse = get_book_chapter_verse(verse_id)

        # If it's just the next verse in the range, updated the previous fields and continue.
        if VERSE_IDS.index(verse_id) - VERSE_IDS.index(previous_verse_id) == 1:
            previous_book = book
            previous_chapter = chapter
            previous_verse = verse
            previous_verse_id = verse_id
            continue

        # At the beginning of a new range, so create the reference and reset all of the fields.
        references.append(
            NormalizedReference(
                start_book,
                start_chapter,
                start_verse,
                previous_chapter,
                previous_verse,
                previous_book if start_book != previous_book else None,
            )
        )

        start_book = book
        previous_book = book
        start_chapter = chapter
        start_verse = verse
        previous_chapter = chapter
        previous_verse = verse
        previous_verse_id = verse_id

    # The last range reference doesn't get created within the loop, so create it now.
    references.append(
        NormalizedReference(
            start_book,
            start_chapter,
            start_verse,
            previous_chapter,
            previous_verse,
            previous_book if start_book != previous_book else None,
        )
    )

    return references
