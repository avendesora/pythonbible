from bible.books import Book
from bible.verses import (
    MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER,
    VERSE_IDS,
    get_max_number_of_verses,
    get_verse_id,
)


def is_valid_verse_id(verse_id):
    return verse_id in VERSE_IDS


def is_valid_reference(reference):
    if reference is None or not isinstance(reference, tuple):
        return False

    if len(reference) != 5:
        return False

    book = reference[0]
    start_chapter = reference[1]
    start_verse = reference[2]
    end_chapter = reference[3]
    end_verse = reference[4]

    if not is_valid_verse(book, start_chapter, start_verse):
        return False

    if not is_valid_verse(book, end_chapter, end_verse):
        return False

    start_verse_id = get_verse_id(book, start_chapter, start_verse)
    end_verse_id = get_verse_id(book, end_chapter, end_verse)

    return start_verse_id <= end_verse_id


def is_valid_book(book):
    return book and isinstance(book, Book)


def is_valid_chapter(book, chapter):
    if not is_valid_book(book):
        return False

    if chapter is None or not isinstance(chapter, int):
        return False

    chapter_list = MAX_VERSE_NUMBER_BY_BOOK_AND_CHAPTER.get(book)
    return 1 <= chapter <= len(chapter_list)


def is_valid_verse(book, chapter, verse):
    if not is_valid_chapter(book, chapter):
        return False

    if verse is None or not isinstance(verse, int):
        return False

    max_verse = get_max_number_of_verses(book, chapter)
    return 1 <= verse <= max_verse
