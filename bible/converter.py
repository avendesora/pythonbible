from bible.errors import InvalidVerseError
from bible.validator import is_valid_verse_id
from bible.verses import (
    VERSE_IDS,
    get_book_chapter_verse,
    get_max_number_of_verses,
    get_verse_id,
)


def convert_references_to_verse_ids(references):
    """

    :param references: a list of normalized reference tuples
    :return: the list of verse ids associated with each of the references in the reference list
    """
    if references is None:
        return None

    verse_ids = []

    for reference in references:
        verse_ids.extend(convert_reference_to_verse_ids(reference))

    return verse_ids


def convert_reference_to_verse_ids(reference):
    """

    :param reference: a normalized reference tuple
    :return: the list of verse ids associated with the reference
    """
    if reference is None:
        return None

    start_verse_id = get_verse_id(reference[0], reference[1], reference[2])
    end_verse_id = get_verse_id(reference[0], reference[3], reference[4])
    return VERSE_IDS[
        VERSE_IDS.index(start_verse_id) : VERSE_IDS.index(end_verse_id) + 1
    ]


def convert_verse_ids_to_references(verse_ids):
    """

    :param verse_ids:
    :return: a list of normalized reference tuples
    """
    if verse_ids is None:
        return None

    verse_ids.sort()

    references = []
    current_book = None
    current_start_chapter = None
    current_start_verse = None
    current_end_chapter = None
    current_end_verse = None

    for verse_id in verse_ids:
        if not is_valid_verse_id(verse_id):
            raise InvalidVerseError(verse_id)

        book, chapter, verse = get_book_chapter_verse(verse_id)

        if current_book is None:
            current_book = book
            current_start_chapter = chapter
            current_start_verse = verse
            current_end_chapter = chapter
            current_end_verse = verse
            continue

        # A new book should always mean a new reference.
        if book != current_book:
            references.append(
                (
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
                    (
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
        if verse != current_end_verse + 1:
            references.append(
                (
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
            (
                current_book,
                current_start_chapter,
                current_start_verse,
                current_end_chapter,
                current_end_verse,
            )
        )

    return references


def is_new_chapter_next_verse(book, end_chapter, end_verse, chapter, verse):
    max_verse = get_max_number_of_verses(book, end_chapter)

    if end_verse != max_verse:
        return False

    return chapter == (end_chapter + 1) and verse == 1
