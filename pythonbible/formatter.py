from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import TYPE_CHECKING
from typing import Any

from pythonbible.bible.bibles import get_bible
from pythonbible.bible.titles import LONG_TITLES
from pythonbible.bible.titles import SHORT_TITLES
from pythonbible.converter import convert_references_to_verse_ids
from pythonbible.converter import convert_verse_ids_to_references
from pythonbible.errors import MissingBookFileError
from pythonbible.verses import get_book_chapter_verse
from pythonbible.verses import get_number_of_chapters
from pythonbible.verses import get_number_of_verses
from pythonbible.verses import is_single_chapter_book
from pythonbible.versions import DEFAULT_VERSION
from pythonbible.versions import Version

if TYPE_CHECKING:
    from pythonbible.books import Book
    from pythonbible.normalized_reference import NormalizedReference


@dataclass
class BookTitles:
    long_title: str
    short_title: str


# TODO - handle Psalms vs Psalm appropriately
# TODO - handle single chapter books appropriately (e.g. Obadiah 1-4 rather than
#        Obadiah 1:1-4)
def format_scripture_references(
    references: list[NormalizedReference] | None,
    **kwargs: Any,
) -> str:
    """Return a human-readable string of the given normalized scripture references.

    :param references: A list of normalized scripture references
    :type references: list[NormalizedReference]
    :return: A human-readable string of the given normalized scripture references
    :rtype: str
    """
    if references is None:
        return ""

    sorted_references: list[NormalizedReference] = references

    # Only sort if there is more than one reference as it can take a long time if there
    # are a lot of verses covered by the references.
    if len(references) > 1:
        verse_ids: list[int] = convert_references_to_verse_ids(references)
        verse_ids.sort()
        sorted_references = convert_verse_ids_to_references(verse_ids)

    formatted_reference: str = ""

    previous_reference: NormalizedReference | None = None

    for reference in sorted_references:
        previous_book: Book | None = _get_previous_book(previous_reference)

        if previous_book != reference.book:
            if previous_reference:
                formatted_reference += ";"

            formatted_reference += format_single_reference(reference, **kwargs)
            previous_reference = reference
            continue

        if _is_reference_with_a_new_chapter(previous_reference, reference):
            formatted_reference += ","
            formatted_reference += format_single_reference(
                reference,
                include_books=False,
                **kwargs,
            )
            continue

        # Reference with same book and chapter as previous reference
        formatted_reference += ","
        formatted_reference += format_single_reference(
            reference,
            include_books=False,
            include_chapters=False,
            **kwargs,
        )
        previous_reference = reference

    return formatted_reference


def _get_previous_book(reference: NormalizedReference | None) -> Book | None:
    if reference is None:
        return None

    return reference.book if reference.end_book is None else reference.end_book


def _is_reference_with_a_new_chapter(
    previous_reference: NormalizedReference | None,
    current_reference: NormalizedReference,
) -> bool:
    if (
        previous_reference
        and previous_reference.end_chapter != current_reference.start_chapter
    ):
        return True

    return current_reference.end_chapter > current_reference.start_chapter


def format_single_reference(
    reference: NormalizedReference,
    include_books: bool = True,
    include_chapters: bool = True,
    **kwargs: Any,
) -> str:
    """Return a human-readable string of the given normalized scripture reference.

    :param reference: A normalized scripture reference
    :type reference: NormalizedReference
    :param include_books: If True includes the book title(s) in the returned reference
                          string, defaults to True
    :type include_books: bool
    :param include_chapters: If True includes the chapter number(s) in the returned
                             reference string, defaults to True
    :type include_chapters: bool
    :return: A human-readable string of the given normalized scripture reference
    :rtype: str
    """
    start_book: str = _get_start_book(reference, include_books, **kwargs)
    start_chapter: str = _get_start_chapter(reference, include_chapters, **kwargs)
    start_verse: str = _get_start_verse(reference, **kwargs)
    end_book: str = _get_end_book(reference, include_books, **kwargs)
    end_chapter: str = _get_end_chapter(reference, include_chapters, **kwargs)
    end_verse: str = _get_end_verse(reference, **kwargs)

    start_separator: str = " " if start_book and (start_chapter or start_verse) else ""
    end_separator: str = " " if end_book and (end_chapter or end_verse) else ""
    range_separator: str = ""

    if end_book:
        range_separator = " - "
    elif end_chapter or end_verse:
        range_separator = "-"

    return "".join(
        [
            start_book,
            start_separator,
            start_chapter,
            start_verse,
            range_separator,
            end_book,
            end_separator,
            end_chapter,
            end_verse,
        ],
    )


def _get_start_book(
    reference: NormalizedReference,
    include_books: bool = True,
    **kwargs: Any,
) -> str:
    return _get_book_title(reference.book, include_books, **kwargs)


def _get_end_book(
    reference: NormalizedReference,
    include_books: bool = True,
    **kwargs: Any,
) -> str:
    if reference.end_book and reference.end_book != reference.book:
        return _get_book_title(reference.end_book, include_books, **kwargs)

    return ""


def _get_book_title(book: Book, include_books: bool = True, **kwargs: Any) -> str:
    if not include_books:
        return ""

    version: Version = kwargs.get("version", DEFAULT_VERSION)
    full_title: bool = kwargs.get("full_title", False)
    version_book_titles: BookTitles = get_book_titles(book, version)

    return (
        version_book_titles.long_title
        if full_title
        else version_book_titles.short_title
    )


def _get_start_chapter(
    reference: NormalizedReference,
    include_chapters: bool = True,
    **kwargs: Any,
) -> str:
    if not include_chapters:
        return ""

    force_include_chapters: bool = kwargs.get("always_include_chapter_numbers", False)

    if (
        _does_reference_include_all_verses_in_start_book(reference)
        and not force_include_chapters
    ):
        return ""

    if is_single_chapter_book(reference.book) and not force_include_chapters:
        return ""

    return f"{reference.start_chapter}:"


def _get_start_verse(reference: NormalizedReference, **kwargs: Any) -> str:
    force_include_chapters: bool = kwargs.get("always_include_chapter_numbers", False)

    if (
        _does_reference_include_all_verses_in_start_book(reference)
        and not force_include_chapters
    ):
        return ""

    return f"{reference.start_verse}"


def _get_end_chapter(
    reference: NormalizedReference,
    include_chapters: bool = True,
    **kwargs: Any,
) -> str:
    if not include_chapters:
        return ""

    force_include_chapters: bool = kwargs.get("always_include_chapter_numbers", False)

    if reference.end_book and reference.book != reference.end_book:
        if (
            _does_reference_include_all_verses_in_end_book(reference)
            and not force_include_chapters
        ):
            return ""

        if is_single_chapter_book(reference.end_book) and not force_include_chapters:
            return ""

        return f"{reference.end_chapter}:"

    if (
        _does_reference_include_all_verses_in_start_book(reference)
        and not force_include_chapters
    ):
        return ""

    if is_single_chapter_book(reference.book) and not force_include_chapters:
        return ""

    if reference.start_chapter == reference.end_chapter:
        return ""

    return f"{reference.end_chapter}:"


def _get_end_verse(reference: NormalizedReference, **kwargs: Any) -> str:
    force_include_chapters: bool = kwargs.get("always_include_chapter_numbers", False)

    if reference.end_book and reference.book != reference.end_book:
        if (
            _does_reference_include_all_verses_in_end_book(reference)
            and not force_include_chapters
        ):
            return ""

        return f"{reference.end_verse}"

    if (
        _does_reference_include_all_verses_in_start_book(reference)
        and not force_include_chapters
    ):
        return ""

    return (
        f"{reference.end_verse}"
        if reference.start_verse != reference.end_verse
        or reference.start_chapter != reference.end_chapter
        else ""
    )


def _does_reference_include_all_verses_in_start_book(
    reference: NormalizedReference,
) -> bool:
    if reference.start_chapter != 1:
        return False

    if reference.start_verse != 1:
        return False

    if reference.end_book and reference.end_book != reference.book:
        return True

    max_chapters = get_number_of_chapters(reference.book)

    if reference.end_chapter != max_chapters:
        return False

    return reference.end_verse == get_number_of_verses(reference.book, max_chapters)


def _does_reference_include_all_verses_in_end_book(
    reference: NormalizedReference,
) -> bool:
    max_chapters = get_number_of_chapters(reference.end_book)

    if reference.end_chapter != max_chapters:
        return False

    return reference.end_verse == get_number_of_verses(reference.end_book, max_chapters)


def format_scripture_text(verse_ids: list[int], **kwargs: Any) -> str:
    """Return the formatted scripture text for the given list of verse IDs.

    :param verse_ids: A list of integer verse ids
    :type verse_ids: list[int]
    :return: The formatted scripture text for the verse ids
    :rtype: str
    """
    one_verse_per_paragraph: bool = kwargs.get("one_verse_per_paragraph", False)
    full_title: bool = kwargs.get("full_title", False)
    format_type: str = kwargs.get("format_type", "html")
    include_verse_numbers: bool = kwargs.get("include_verse_numbers", True)
    version: Version = kwargs.get("version", DEFAULT_VERSION)

    is_html: bool = format_type == "html"

    bible_type = "html" if is_html else "plain_text"

    if not include_verse_numbers:
        bible_type += "_readers"

    bible = get_bible(version, bible_type)

    verse_ids.sort()
    text: str = ""
    current_book: Book | None = None
    current_chapter: int | None = None
    current_start_verse: int | None = None
    current_end_verse: int | None = None

    for verse_id in verse_ids:
        book, chapter_number, verse_number = get_book_chapter_verse(verse_id)

        if (
            one_verse_per_paragraph
            or current_end_verse is None
            or verse_id - current_end_verse > 1
        ):
            if current_start_verse and current_end_verse:
                verse_text = bible.get_scripture(current_start_verse, current_end_verse)
                text += _format_paragraph(verse_text)

            current_start_verse = verse_id

        current_end_verse = verse_id

        if book != current_book:
            current_book = book
            current_chapter = chapter_number
            version_book_titles: BookTitles = get_book_titles(book, version)
            title: str = (
                version_book_titles.long_title
                if full_title
                else version_book_titles.short_title
            )
            text += _format_title(title, is_html, not text)
            text += _format_chapter(chapter_number, is_html)
        elif chapter_number != current_chapter:
            current_chapter = chapter_number
            text += _format_chapter(chapter_number, is_html)

    if current_start_verse and current_end_verse:
        verse_text = bible.get_scripture(current_start_verse, current_end_verse)
        text += _format_paragraph(verse_text)

    return text


def _format_title(title: str, is_html: bool, is_first_book: bool) -> str:
    if is_html:
        return f"<h1>{title}</h1>\n"

    return f"{title}\n\n" if is_first_book else f"\n\n{title}\n\n"


def _format_chapter(chapter: int, is_html: bool) -> str:
    return f"<h2>Chapter {chapter}</h2>\n" if is_html else f"Chapter {chapter}\n\n"


def _format_paragraph(paragraph: str) -> str:
    return f"{paragraph}\n"


@lru_cache()
def get_verse_text(verse_id: int, version: Version = DEFAULT_VERSION) -> str:
    """Return the scripture text of the given verse id and version of the Bible.

    :param verse_id: a verse id
    :type verse_id: int
    :param version: a version of the Bible, defaults to American Standard
    :type version: Version
    :return: The scripture text of the given verse id and version
    :rtype: str
    :raises InvalidVerseError: if the given verse id does not correspond to a valid
                               verse
    :raises MissingVerseFileError: if the verse file for the given verse_id and version
                                   does not exist
    """
    bible = get_bible(version, "plain_text_readers")
    return bible.get_scripture(verse_id, verse_id)


@lru_cache()
def get_book_titles(book: Book, version: Version = DEFAULT_VERSION) -> BookTitles:
    """Return the book titles for the given Book and optional Version.

    :param book: a book of the Bible
    :type book: Book
    :param version: a version of the Bible, defaults to American Standard
    :type version: Version
    :return: the long and short titles of the given book and version
    :rtype: BookTitles
    :raises MissingBookFileError: if the book file for the given book and version does
                                  not exist
    """
    short_titles, long_titles = _get_version_book_titles(version)
    short_title = short_titles.get(book, book.title)
    long_title = long_titles.get(book, book.title)

    return BookTitles(long_title, short_title)


@lru_cache()
def _get_version_book_titles(
    version: Version,
) -> tuple[dict[Book, str], dict[Book, str]]:
    try:
        return SHORT_TITLES[version], LONG_TITLES[version]
    except KeyError as key_error:
        raise MissingBookFileError(key_error) from key_error
