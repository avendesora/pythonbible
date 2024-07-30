from __future__ import annotations

from typing import TYPE_CHECKING

from pythonbible.errors import InvalidVerseError
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.validator import is_valid_verse_id
from pythonbible.verses import VERSE_IDS
from pythonbible.verses import get_book_chapter_verse
from pythonbible.verses import get_number_of_chapters
from pythonbible.verses import get_number_of_verses
from pythonbible.verses import get_verse_id

if TYPE_CHECKING:
    from pythonbible.books import Book


def convert_references_to_verse_ids(references: list[NormalizedReference]) -> list[int]:
    """Convert a list of NormalizedReference objects into a list of verse id integers.

    :param references: A list of normalized references
    :type references: list[NormalizedReference]
    :return: The list of verse ids associated with the references
    :rtype: list[int]
    """
    verse_ids: list[int] = []

    if references is not None:
        for reference in references:
            verse_ids.extend(convert_reference_to_verse_ids(reference))

    return verse_ids


def convert_reference_to_verse_ids(reference: NormalizedReference) -> tuple[int, ...]:
    """Convert the given NormalizedReference object into a tuple of verse id integers.

    :param reference: A normalized reference
    :type reference: NormalizedReference
    :return: The tuple of verse ids associated with the reference
    :rtype: tuple[int, ...]
    """
    # TODO - require version since chapter and verse counts can differ by version
    if reference is None:
        return ()

    start_book: Book = reference.book
    start_chapter: int = reference.start_chapter or 1
    start_verse: int = reference.start_verse or 1

    end_book: Book = reference.end_book or start_book
    end_chapter: int = reference.end_chapter or get_number_of_chapters(end_book)
    end_verse: int = reference.end_verse or get_number_of_verses(end_book, end_chapter)

    start_verse_id: int = get_verse_id(
        start_book,
        start_chapter,
        start_verse,
    )
    end_verse_id: int = get_verse_id(
        end_book,
        end_chapter,
        end_verse,
    )
    return VERSE_IDS[
        VERSE_IDS.index(start_verse_id) : VERSE_IDS.index(end_verse_id) + 1
    ]


def convert_verse_ids_to_references(verse_ids: list[int]) -> list[NormalizedReference]:
    """Convert a list of verse ids into a list of NormalizedReferences.

    :param verse_ids: A list of verse ids
    :type verse_ids: list[int]
    :return: The list of normalized references associated with the verse ids
    :rtype: list[NormalizedReference]
    :raises InvalidVerseError: if one or more of the verse_ids does not correspond to
                               a valid verse
    """
    references: list[NormalizedReference] = []

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

        # If it's just the next verse in the range, updated the previous fields and
        # continue.
        if VERSE_IDS.index(verse_id) - VERSE_IDS.index(previous_verse_id) == 1:
            previous_book = book
            previous_chapter = chapter
            previous_verse = verse
            previous_verse_id = verse_id
            continue

        # At the beginning of a new range, so create the reference and reset all of the
        # fields.
        references.append(
            NormalizedReference(
                start_book,
                start_chapter,
                start_verse,
                previous_chapter,
                previous_verse,
                previous_book,
            ),
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
            previous_book,
        ),
    )

    return references
