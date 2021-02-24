import json
import os
from functools import lru_cache
from typing import Any, Callable, Dict, List, NamedTuple, Optional, Type

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
from pythonbible.verses import VERSE_IDS, get_book_chapter_verse
from pythonbible.versions import DEFAULT_VERSION, Version


class BookTitles(NamedTuple):
    long_title: str
    short_title: str


VERSION_MAP: Dict[Version, Type[BibleParser]] = {
    Version.AMERICAN_STANDARD: OSISParser,
    Version.KING_JAMES: OSISParser,
}


def get_parser(**kwargs) -> BibleParser:
    version: Version = kwargs.get("version", DEFAULT_VERSION)
    version_map: Dict[Version, Type[BibleParser]] = kwargs.get(
        "version_map", VERSION_MAP
    )
    return version_map.get(version, OSISParser)(version)


DEFAULT_PARSER: BibleParser = get_parser()

CURRENT_FOLDER: str = os.path.dirname(os.path.realpath(__file__))
DATA_FOLDER: str = os.path.join(os.path.join(CURRENT_FOLDER, "bible"), "data")
VERSE_TEXTS: Dict[Version, Dict[int, str]] = {}
BOOK_TITLES: Dict[Version, Dict[Book, BookTitles]] = {}


# TODO - handle Psalms vs Psalm appropriately
# TODO - handle single chapter books appropriately (e.g. Obadiah 1-4 rather than Obadiah 1:1-4)
def format_scripture_references(
    references: Optional[List[NormalizedReference]], **kwargs
) -> str:
    """

    :param references: a list of normalized scripture references
    :return: a string version of the references formatted to be human-readable
    """
    if references is None:
        return ""

    verse_ids: List[int] = convert_references_to_verse_ids(references)
    verse_ids.sort()
    sorted_references: List[NormalizedReference] = convert_verse_ids_to_references(
        verse_ids
    )

    formatted_reference: str = ""

    previous_reference: Optional[NormalizedReference] = None

    for reference in sorted_references:
        # First reference
        if previous_reference is None:
            formatted_reference += format_single_reference(
                reference.book,
                reference.start_chapter,
                reference.start_verse,
                reference.end_chapter,
                reference.end_verse,
                **kwargs,
            )
            previous_reference = reference
            continue

        previous_book: Optional[Book] = previous_reference.book

        # Reference with a new book
        if previous_book != reference.book:
            formatted_reference += ";"
            formatted_reference += format_single_reference(
                reference.book,
                reference.start_chapter,
                reference.start_verse,
                reference.end_chapter,
                reference.end_verse,
                **kwargs,
            )
            previous_reference = reference
            continue

        previous_end_chapter: Optional[int] = previous_reference.end_chapter

        # Reference with a new chapter
        if previous_end_chapter != reference.start_chapter or (
            reference.end_chapter
            and reference.start_chapter
            and reference.end_chapter > reference.start_chapter
        ):
            formatted_reference += ","
            formatted_reference += format_single_reference(
                None,
                reference.start_chapter,
                reference.start_verse,
                reference.end_chapter,
                reference.end_verse,
                **kwargs,
            )
            continue

        # Reference with same book and chapter as previous reference
        formatted_reference += ","
        formatted_reference += format_single_reference(
            None, None, reference.start_verse, None, reference.end_verse, **kwargs
        )
        previous_reference = reference

    return formatted_reference


def format_single_reference(
    book: Optional[Book],
    start_chapter: Optional[int],
    start_verse,
    end_chapter: Optional[int],
    end_verse,
    **kwargs,
) -> str:
    formatted_reference: str = ""

    if book:
        version: Version = kwargs.get("version", DEFAULT_VERSION)
        book_titles: Optional[BookTitles] = get_book_titles(book, version)
        full_title: bool = kwargs.get("full_title", False)

        if book_titles:
            title: str = (
                book_titles.long_title if full_title else book_titles.short_title
            )
            formatted_reference += f"{title} "

    if start_chapter:
        formatted_reference += f"{start_chapter}:{start_verse}"
    else:
        formatted_reference += f"{start_verse}"

    if end_chapter and start_chapter and end_chapter > start_chapter:
        formatted_reference += f"-{end_chapter}:{end_verse}"
    elif end_verse > start_verse:
        formatted_reference += f"-{end_verse}"

    return formatted_reference


def format_scripture_text(verse_ids: List[int], **kwargs) -> str:
    one_verse_per_paragraph: bool = kwargs.get("one_verse_per_paragraph", False)
    full_title: bool = kwargs.get("full_title", False)
    format_type: str = kwargs.get("format_type", "html")
    include_verse_numbers: bool = kwargs.get("include_verse_numbers", True)
    parser: BibleParser = kwargs.get("parser", DEFAULT_PARSER)

    if one_verse_per_paragraph or len(verse_ids) == 1:
        return format_scripture_text_verse_by_verse(
            verse_ids, parser.version, full_title, format_type, include_verse_numbers
        )

    return format_scripture_text_with_parser(
        verse_ids, parser, full_title, format_type, include_verse_numbers
    )


def format_scripture_text_verse_by_verse(
    verse_ids: List[int],
    version: Version,
    full_title: bool,
    format_type: str,
    include_verse_numbers: bool,
) -> str:
    verse_ids.sort()
    text: str = ""
    current_book: Optional[Book] = None
    current_chapter: Optional[int] = None

    for verse_id in verse_ids:
        book, chapter_number, verse_number = get_book_chapter_verse(verse_id)

        if book != current_book:
            current_book = book
            current_chapter = chapter_number
            book_titles: Optional[BookTitles] = get_book_titles(book, version)

            if book_titles:
                title: str = (
                    book_titles.long_title if full_title else book_titles.short_title
                )
                text += _format_title(title, format_type, len(text) == 0)

            text += _format_chapter(chapter_number, format_type)

        elif chapter_number != current_chapter:
            current_chapter = chapter_number
            text += _format_chapter(chapter_number, format_type)

        verse_text: Optional[str] = get_verse_text(verse_id, version)

        if include_verse_numbers:
            verse_text = f"{verse_number}. {verse_text}"

        text += _format_paragraph(verse_text, format_type)

    return text


def format_scripture_text_with_parser(
    verse_ids: List[int],
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
        verse_ids, include_verse_number=include_verse_numbers
    )

    for book, chapters in paragraphs.items():
        title: str = title_function(book)
        text += _format_title(title, format_type, len(text) == 0)

        for chapter, paragraphs in chapters.items():
            text += _format_chapter(chapter, format_type)

            for paragraph in paragraphs:
                text += _format_paragraph(paragraph, format_type)

    return text


def _format_title(title: str, format_type: str, is_first_book: bool) -> str:
    if format_type == "html":
        return f"<h1>{title}</h1>\n"

    if not is_first_book:
        return f"\n\n{title}\n\n"

    return f"{title}\n\n"


def _format_chapter(chapter: int, format_type: str) -> str:
    if format_type == "html":
        return f"<h2>Chapter {chapter}</h2>\n"

    return f"Chapter {chapter}\n\n"


def _format_paragraph(paragraph: Optional[str], format_type: str) -> str:
    if format_type == "html":
        return f"<p>{paragraph}</p>\n"

    return f"   {paragraph}\n"


@lru_cache(maxsize=None)
def get_verse_text(verse_id: int, version: Version = DEFAULT_VERSION) -> Optional[str]:
    """
    Given a verse id and, optionally, a Bible version, return the text for that verse.

    :param verse_id:
    :param version:
    :return: the verse text
    """
    if verse_id not in VERSE_IDS:
        raise InvalidVerseError(verse_id=verse_id)

    try:
        version_verse_texts: Dict[int, str] = _get_version_verse_texts(version)
    except FileNotFoundError as e:
        raise MissingVerseFileError(e)

    return version_verse_texts.get(verse_id)


@lru_cache(maxsize=None)
def _get_version_verse_texts(version: Version) -> Dict[int, str]:
    verse_texts: Optional[Dict[int, str]] = VERSE_TEXTS.get(version)

    if verse_texts is None:
        json_filename: str = os.path.join(
            os.path.join(DATA_FOLDER, version.value.lower()), "verses.json"
        )
        verse_texts = {}

        with open(json_filename, "r") as json_file:
            for verse_id, verse_text in json.load(json_file).items():
                verse_texts[int(verse_id)] = verse_text

        VERSE_TEXTS[version] = verse_texts

    return verse_texts


@lru_cache(maxsize=None)
def get_book_titles(
    book: Book, version: Version = DEFAULT_VERSION
) -> Optional[BookTitles]:
    """
    Given a book of the Bible and optionally a version return the book title.

    :param book:
    :param version:
    :return: the book title
    """
    try:
        version_book_tiles: Dict[Book, BookTitles] = _get_version_book_titles(version)
    except FileNotFoundError as e:
        raise MissingBookFileError(e)

    return version_book_tiles.get(book)


@lru_cache(maxsize=None)
def _get_version_book_titles(version: Version) -> Dict[Book, BookTitles]:
    book_titles: Optional[Dict[Book, BookTitles]] = BOOK_TITLES.get(version)

    if book_titles is None:
        json_filename: str = os.path.join(
            os.path.join(DATA_FOLDER, version.value.lower()), "books.json"
        )
        book_titles = {}

        with open(json_filename, "r") as json_file:
            for book_id, titles in json.load(json_file).items():
                book: Book = Book(int(book_id))
                book_titles[book] = BookTitles(titles[0], titles[1])

        BOOK_TITLES[version] = book_titles

    return book_titles
