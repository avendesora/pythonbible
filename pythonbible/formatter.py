import json
import os
from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Callable, Dict, List, Optional, Type

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
    get_max_number_of_verses,
    get_number_of_chapters,
    is_single_chapter_book,
)
from pythonbible.versions import DEFAULT_VERSION, Version


@dataclass
class BookTitles:
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

    sorted_references: List[NormalizedReference] = references

    # Only sort if there is more than one reference as it can take a long time if there
    # are a lot of verses covered by the references.
    if len(references) > 1:
        verse_ids: List[int] = convert_references_to_verse_ids(references)
        verse_ids.sort()
        sorted_references = convert_verse_ids_to_references(verse_ids)

    formatted_reference: str = ""

    previous_reference: Optional[NormalizedReference] = None

    for reference in sorted_references:
        previous_book: Optional[Book] = _get_previous_book(previous_reference)

        if previous_book != reference.book:
            if previous_reference:
                formatted_reference += ";"

            formatted_reference += format_single_reference(reference, **kwargs)
            previous_reference = reference
            continue

        if _is_reference_with_a_new_chapter(previous_reference, reference):
            formatted_reference += ","
            formatted_reference += format_single_reference(
                reference, include_books=False, **kwargs
            )
            continue

        # Reference with same book and chapter as previous reference
        formatted_reference += ","
        formatted_reference += format_single_reference(
            reference, include_books=False, include_chapters=False, **kwargs
        )
        previous_reference = reference

    return formatted_reference


def _get_previous_book(reference: Optional[NormalizedReference]) -> Optional[Book]:
    if reference is None:
        return None

    return reference.book if reference.end_book is None else reference.end_book


def _is_reference_with_a_new_chapter(
    previous_reference: Optional[NormalizedReference],
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
    **kwargs,
) -> str:
    start_book: str = _get_start_book(reference, include_books, **kwargs)
    start_chapter: str = _get_start_chapter(reference, include_chapters, **kwargs)
    start_verse: str = _get_start_verse(reference, **kwargs)
    end_book: str = _get_end_book(reference, include_books, **kwargs)
    end_chapter: str = _get_end_chapter(reference, include_chapters, **kwargs)
    end_verse: str = _get_end_verse(reference, **kwargs)

    start_separator: str = " " if start_book and (start_chapter or start_verse) else ""
    end_separator: str = " " if end_book and (end_chapter or end_verse) else ""
    range_separator: str = (
        " - " if end_book else "-" if end_chapter or end_verse else ""
    )

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
        ]
    )


def _get_start_book(
    reference: NormalizedReference, include_books: bool = True, **kwargs
) -> str:
    return _get_book_title(reference.book, include_books, **kwargs)


def _get_end_book(
    reference: NormalizedReference, include_books: bool = True, **kwargs
) -> str:
    if reference.end_book and reference.end_book != reference.book:
        return _get_book_title(reference.end_book, include_books, **kwargs)

    return ""


def _get_book_title(book: Book, include_books: bool = True, **kwargs) -> str:
    if not include_books:
        return ""

    version: Version = kwargs.get("version", DEFAULT_VERSION)
    full_title: bool = kwargs.get("full_title", False)
    book_titles: Optional[BookTitles] = get_book_titles(book, version)

    return (
        (book_titles.long_title if full_title else book_titles.short_title)
        if book_titles
        else ""
    )


def _get_start_chapter(
    reference: NormalizedReference, include_chapters: bool = True, **kwargs
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


def _get_start_verse(reference: NormalizedReference, **kwargs) -> str:
    force_include_chapters: bool = kwargs.get("always_include_chapter_numbers", False)

    if (
        _does_reference_include_all_verses_in_start_book(reference)
        and not force_include_chapters
    ):
        return ""

    return f"{reference.start_verse}"


def _get_end_chapter(
    reference: NormalizedReference, include_chapters: bool = True, **kwargs
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


def _get_end_verse(reference: NormalizedReference, **kwargs) -> str:
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


def _does_reference_include_all_verses_in_start_book(reference: NormalizedReference):
    if reference.start_chapter != 1:
        return False

    if reference.start_verse != 1:
        return False

    if reference.end_book and reference.end_book != reference.book:
        return True

    max_chapters = get_number_of_chapters(reference.book)

    if reference.end_chapter != max_chapters:
        return False

    return reference.end_verse == get_max_number_of_verses(reference.book, max_chapters)


def _does_reference_include_all_verses_in_end_book(reference: NormalizedReference):
    max_chapters = get_number_of_chapters(reference.end_book)

    if reference.end_chapter != max_chapters:
        return False

    return reference.end_verse == get_max_number_of_verses(
        reference.end_book, max_chapters
    )


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


@lru_cache()
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


@lru_cache()
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


@lru_cache()
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


@lru_cache()
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
