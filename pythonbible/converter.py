from typing import List, Optional

from pythonbible.books import Book
from pythonbible.errors import InvalidVerseError
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.validator import is_valid_verse_id
from pythonbible.verses import (
    VERSE_IDS,
    get_book_chapter_verse,
    get_max_number_of_verses,
    get_verse_id,
)


def convert_references_to_verse_ids(references: List[NormalizedReference]) -> List[int]:
    """

    :param references: a list of normalized reference tuples
    :return: the list of verse ids associated with each of the references in the reference list
    """
    verse_ids: List[int] = []

    if references is not None:
        for reference in references:
            verse_ids.extend(convert_reference_to_verse_ids(reference))

    return verse_ids


def convert_reference_to_verse_ids(reference: NormalizedReference) -> List[int]:
    """

    :param reference: a normalized reference tuple
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
    :return: a list of normalized reference tuples
    """
    references: List[NormalizedReference] = []

    if verse_ids is None or len(verse_ids) == 0:
        return references

    verse_ids.sort()

    # Initialize with the first verse id in the list
    first_verse = verse_ids[0]

    if not is_valid_verse_id(first_verse):
        raise InvalidVerseError(verse_id=first_verse)

    book: Book
    chapter: int
    verse: int
    book, chapter, verse = get_book_chapter_verse(verse_ids[0])
    current_book: Book = book
    current_start_chapter: int = chapter
    current_start_verse: int = verse
    current_end_chapter: int = chapter
    current_end_verse: int = verse

    # Loop through the remaining verse ids in the list
    for verse_id in verse_ids[1:]:
        if not is_valid_verse_id(verse_id):
            raise InvalidVerseError(verse_id=verse_id)

        book, chapter, verse = get_book_chapter_verse(verse_id)

        # A new book should always mean a new reference.
        if book != current_book:
            references.append(
                NormalizedReference(
                    current_book,
                    current_start_chapter,
                    current_start_verse,
                    current_end_chapter,
                    current_end_verse,
                )
            )

            current_book = book
            current_start_chapter = chapter
            current_start_verse = verse
            current_end_chapter = chapter
            current_end_verse = verse
            continue

        # A new chapter should mean a new reference unless the previous verse was
        # the last verse of the previous chapter and the current verse is the first
        # verse of the next chapter.
        if chapter != current_end_chapter:
            is_next_verse = is_new_chapter_next_verse(
                current_book, current_end_chapter, current_end_verse, chapter, verse
            )

            if not is_next_verse:
                references.append(
                    NormalizedReference(
                        current_book,
                        current_start_chapter,
                        current_start_verse,
                        current_end_chapter,
                        current_end_verse,
                    )
                )

                current_start_chapter = chapter
                current_start_verse = verse

            current_end_chapter = chapter
            current_end_verse = verse
            continue

        # At this point, the book and chapter should be the same as the previous
        # verse id, so if the verse is not the next verse after the previous
        # verse, then that should mean a new reference.
        if verse != (current_end_verse if current_end_verse else 0) + 1:
            references.append(
                NormalizedReference(
                    current_book,
                    current_start_chapter,
                    current_start_verse,
                    current_end_chapter,
                    current_end_verse,
                )
            )

            current_start_chapter = chapter
            current_start_verse = verse
            current_end_chapter = chapter
            current_end_verse = verse
            continue

        # At this point, this is the next verse in the range, so just update the
        # current end chapter and verse
        current_end_chapter = chapter
        current_end_verse = verse

    # The last reference doesn't get created during the loop, so create it now
    # (assuming that at least one verse id was valid).
    if current_book:
        references.append(
            NormalizedReference(
                current_book,
                current_start_chapter,
                current_start_verse,
                current_end_chapter,
                current_end_verse,
            )
        )

    return references


def is_new_chapter_next_verse(
    book: Book,
    end_chapter: Optional[int],
    end_verse: Optional[int],
    chapter: int,
    verse: int,
) -> bool:
    max_verse: int = get_max_number_of_verses(book, end_chapter)

    if end_verse != max_verse:
        return False

    return chapter == ((end_chapter if end_chapter else 0) + 1) and verse == 1
