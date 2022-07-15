from __future__ import annotations

import json
import os
from dataclasses import dataclass
from functools import lru_cache
from types import MappingProxyType
from typing import Any, Callable, Type

from pythonbible.bible.bible_parser import BibleParser
from pythonbible.bible.osis.parser import OSISParser
from pythonbible.books import Book
from pythonbible.converter import (
    convert_references_to_verse_ids,
    convert_verse_ids_to_references,
)
from pythonbible.errors import (
    InvalidVerseError,
    MissingBookFileError,
    MissingVerseFileError,
)
from pythonbible.normalized_reference import NormalizedReference
from pythonbible.verses import (
    VERSE_IDS,
    get_book_chapter_verse,
    get_number_of_chapters,
    get_number_of_verses,
    is_single_chapter_book,
)
from pythonbible.versions import DEFAULT_VERSION, Version


@dataclass
class BookTitles:
    long_title: str
    short_title: str


VERSION_MAP: dict[Version, Type[BibleParser]] = MappingProxyType(
    {
        Version.AMERICAN_STANDARD: OSISParser,
        Version.KING_JAMES: OSISParser,
    },
)


def get_parser(**kwargs: Any) -> BibleParser:
    version: Version = kwargs.get("version", DEFAULT_VERSION)
    version_map: dict[Version, Type[BibleParser]] = kwargs.get(
        "version_map",
        VERSION_MAP,
    )
    return version_map.get(version, OSISParser)(version)


DEFAULT_PARSER: BibleParser = get_parser()

CURRENT_FOLDER: str = os.path.dirname(os.path.realpath(__file__))
DATA_FOLDER: str = os.path.join(CURRENT_FOLDER, "bible", "data")
verse_texts: dict[Version, dict[int, str]] = {}
book_titles: dict[Version, dict[Book, BookTitles]] = {}


# TODO - handle Psalms vs Psalm appropriately
# TODO - handle single chapter books appropriately (e.g. Obadiah 1-4 rather than
#        Obadiah 1:1-4)
def format_scripture_references(
    references: list[NormalizedReference] | None,
    **kwargs: Any,
) -> str:
    """
    Return a human-readable string of the given normalized scripture references.

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
    """
    Return a human-readable string of the given normalized scripture reference.

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
    version_book_titles: BookTitles | None = get_book_titles(book, version)

    if not version_book_titles:
        return ""

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


# TODO - rewrite this to not need a parser
def format_scripture_text(verse_ids: list[int], **kwargs: Any) -> str:
    """
    Return the formatted scripture text for the given list of verse IDs.

    :param verse_ids: A list of integer verse ids
    :type verse_ids: list[int]
    :return: The formatted scripture text for the verse ids
    :rtype: str
    """
    one_verse_per_paragraph: bool = kwargs.get("one_verse_per_paragraph", False)
    full_title: bool = kwargs.get("full_title", False)
    format_type: str = kwargs.get("format_type", "html")
    include_verse_numbers: bool = kwargs.get("include_verse_numbers", True)
    parser: BibleParser = kwargs.get("parser", DEFAULT_PARSER)

    if one_verse_per_paragraph or len(verse_ids) == 1:
        return _format_scripture_text_verse_by_verse(
            verse_ids,
            parser.version,
            full_title,
            format_type,
            include_verse_numbers,
        )

    return _format_scripture_text_with_parser(
        verse_ids,
        parser,
        full_title,
        format_type,
        include_verse_numbers,
    )


def _format_scripture_text_verse_by_verse(
    verse_ids: list[int],
    version: Version,
    full_title: bool,
    format_type: str,
    include_verse_numbers: bool,
) -> str:
    verse_ids.sort()
    text: str = ""
    current_book: Book | None = None
    current_chapter: int | None = None

    for verse_id in verse_ids:
        book, chapter_number, verse_number = get_book_chapter_verse(verse_id)

        if book != current_book:
            current_book = book
            current_chapter = chapter_number
            version_book_titles: BookTitles | None = get_book_titles(book, version)

            if version_book_titles:
                title: str = (
                    version_book_titles.long_title
                    if full_title
                    else version_book_titles.short_title
                )
                text += _format_title(title, format_type, not text)

            text += _format_chapter(chapter_number, format_type)

        elif chapter_number != current_chapter:
            current_chapter = chapter_number
            text += _format_chapter(chapter_number, format_type)

        verse_text: str | None = get_verse_text(verse_id, version)

        if include_verse_numbers:
            verse_text = f"{verse_number}. {verse_text}"

        text += _format_paragraph(verse_text, format_type)

    return text


def _format_scripture_text_with_parser(
    verse_ids: list[int],
    parser: BibleParser,
    full_title: bool,
    format_type: str,
    include_verse_numbers: bool,
) -> str:
    title_function: Callable[[Any], Any] = (
        parser.get_book_title if full_title else parser.get_short_book_title
    )
    text: str = ""

    paragraphs: Any = parser.get_scripture_passage_text(
        verse_ids,
        include_verse_number=include_verse_numbers,
    )

    for book, chapters in paragraphs.items():
        title: str = title_function(book)
        text += _format_title(title, format_type, not text)

        for chapter, chapter_paragraphs in chapters.items():
            text += _format_chapter(chapter, format_type)
            text += "".join(
                _format_paragraph(paragraph, format_type)
                for paragraph in chapter_paragraphs
            )

    return text


def _format_title(title: str, format_type: str, is_first_book: bool) -> str:
    if format_type == "html":
        return f"<h1>{title}</h1>\n"

    return f"{title}\n\n" if is_first_book else f"\n\n{title}\n\n"


def _format_chapter(chapter: int, format_type: str) -> str:
    if format_type == "html":
        return f"<h2>Chapter {chapter}</h2>\n"

    return f"Chapter {chapter}\n\n"


def _format_paragraph(paragraph: str | None, format_type: str) -> str:
    if format_type == "html":
        return f"<p>{paragraph}</p>\n"

    return f"   {paragraph}\n"


@lru_cache()
def get_verse_text(verse_id: int, version: Version = DEFAULT_VERSION) -> str | None:
    """
    Return the scripture text of the given verse id and version of the Bible.

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
    if verse_id not in VERSE_IDS:
        raise InvalidVerseError(verse_id=verse_id)

    try:
        version_verse_texts: dict[int, str] = _get_version_verse_texts(version)
    except FileNotFoundError as file_not_found_error:
        raise MissingVerseFileError(file_not_found_error)

    return version_verse_texts.get(verse_id)


@lru_cache()
def _get_version_verse_texts(version: Version) -> dict[int, str]:
    version_verse_texts: dict[int, str] | None = verse_texts.get(version)

    if version_verse_texts is None:
        json_filename: str = os.path.join(
            DATA_FOLDER,
            version.value.lower(),
            "verses.json",
        )
        version_verse_texts = {}

        with open(json_filename, "r", encoding="utf-8") as json_file:
            for verse_id, verse_text in json.load(json_file).items():
                version_verse_texts[int(verse_id)] = verse_text

        verse_texts[version] = version_verse_texts

    return version_verse_texts


@lru_cache()
def get_book_titles(
    book: Book,
    version: Version = DEFAULT_VERSION,
) -> BookTitles | None:
    """
    Return the book titles for the given Book and optional Version.

    :param book: a book of the Bible
    :type book: Book
    :param version: a version of the Bible, defaults to American Standard
    :type version: Version
    :return: the long and short titles of the given book and version
    :rtype: BookTitles | None
    :raises MissingBookFileError: if the book file for the given book and version does
                                  not exist
    """
    try:
        version_book_titles: dict[Book, BookTitles] = _get_version_book_titles(version)
    except FileNotFoundError as file_not_found_error:
        raise MissingBookFileError(file_not_found_error)

    return version_book_titles.get(book)


@lru_cache()
def _get_version_book_titles(version: Version) -> dict[Book, BookTitles]:
    version_book_titles: dict[Book, BookTitles] | None = book_titles.get(version)

    if version_book_titles is None:
        json_filename: str = os.path.join(
            DATA_FOLDER,
            version.value.lower(),
            "books.json",
        )
        version_book_titles = {}

        with open(json_filename, "r", encoding="utf-8") as json_file:
            for book_id, titles in json.load(json_file).items():
                book: Book = Book(int(book_id))
                version_book_titles[book] = BookTitles(titles[0], titles[1])

        book_titles[version] = version_book_titles

    return version_book_titles
