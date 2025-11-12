from __future__ import annotations

from functools import lru_cache
from typing import TYPE_CHECKING
from typing import Any

from pythonbible.bible import get_bible
from pythonbible.converter import convert_references_to_verse_ids
from pythonbible.converter import convert_verse_ids_to_references
from pythonbible.errors import MissingBookFileError
from pythonbible.errors import MissingVerseFileError
from pythonbible.verses import get_book_chapter_verse
from pythonbible.verses import get_number_of_chapters
from pythonbible.verses import get_number_of_verses
from pythonbible.verses import is_single_chapter_book
from pythonbible.versions import DEFAULT_VERSION
from pythonbible.versions import Version

if TYPE_CHECKING:
    from pythonbible.bible.bible import Bible
    from pythonbible.books import Book
    from pythonbible.normalized_reference import NormalizedReference


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

    return (current_reference.end_chapter or 0) > (current_reference.start_chapter or 1)


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
    version: Version = kwargs.get("version", DEFAULT_VERSION)
    full_title: bool = kwargs.get("full_title", False)

    start_book: str = _get_start_book(reference, version, full_title, include_books)
    start_chapter: str = _get_start_chapter(reference, include_chapters, **kwargs)
    start_verse: str = _get_start_verse(reference, **kwargs)
    end_book: str = _get_end_book(reference, version, full_title, include_books)
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
    version: Version,
    full_title: bool,
    include_books: bool = True,
) -> str:
    return _get_book_title(reference.book, version, full_title, include_books)


def _get_end_book(
    reference: NormalizedReference,
    version: Version,
    full_title: bool,
    include_books: bool = True,
) -> str:
    if reference.end_book and reference.end_book != reference.book:
        return _get_book_title(reference.end_book, version, full_title, include_books)

    return ""


def _get_book_title(
    book: Book,
    version: Version,
    full_title: bool,
    include_books: bool = True,
) -> str:
    if not include_books:
        return ""

    try:
        bible: Bible = get_bible(version, "plain_text")
        return (
            bible.long_titles.get(book, book.title)
            if full_title
            else bible.short_titles.get(book, book.title)
        )
    except MissingVerseFileError:
        return book.title


def _is_single_chapter_book(book: Book, **kwargs: Any) -> bool:
    version: Version | None = kwargs.get("version")

    if not version:
        return is_single_chapter_book(book)

    try:
        bible: Bible = get_bible(version, "plain_text")
        chapters = bible.max_verses.get(book)
        return len(chapters) == 1 if chapters else is_single_chapter_book(book)
    except MissingBookFileError:
        return is_single_chapter_book(book)


def _get_number_of_chapters(book: Book, **kwargs: Any) -> int:
    version: Version | None = kwargs.get("version")

    if not version:
        return get_number_of_chapters(book)

    try:
        bible: Bible = get_bible(version, "plain_text")
        chapters = bible.max_verses.get(book)
        return len(chapters) if chapters else get_number_of_chapters(book)
    except MissingBookFileError:
        return get_number_of_chapters(book)


def _get_number_of_verses(book: Book, chapter: int, **kwargs: Any) -> int:
    version: Version | None = kwargs.get("version")

    if not version:
        return get_number_of_verses(book, chapter)

    try:
        bible: Bible = get_bible(version, "plain_text")
        chapters = bible.max_verses.get(book)

        if not chapters:
            return get_number_of_verses(book, chapter)

        verses = chapters.get(chapter) if chapters else None
        return verses or get_number_of_verses(book, chapter)
    except MissingBookFileError:
        return get_number_of_verses(book, chapter)


def _get_start_chapter(
    reference: NormalizedReference,
    include_chapters: bool = True,
    **kwargs: Any,
) -> str:
    if not include_chapters:
        return ""

    force_include_chapters: bool = kwargs.get("always_include_chapter_numbers", False)

    if (
        _does_reference_include_all_verses_in_start_book(reference, **kwargs)
        and not force_include_chapters
    ):
        return ""

    if _is_single_chapter_book(reference.book, **kwargs) and not force_include_chapters:
        return ""

    return f"{reference.start_chapter or 1}:"


def _get_start_verse(reference: NormalizedReference, **kwargs: Any) -> str:
    force_include_chapters: bool = kwargs.get("always_include_chapter_numbers", False)

    if (
        _does_reference_include_all_verses_in_start_book(reference, **kwargs)
        and not force_include_chapters
    ):
        return ""

    return f"{reference.start_verse or 1}"


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
            _does_reference_include_all_verses_in_end_book(reference, **kwargs)
            and not force_include_chapters
        ):
            return ""

        if (
            _is_single_chapter_book(reference.end_book, **kwargs)
            and not force_include_chapters
        ):
            return ""

        end_chapter = reference.end_chapter or _get_number_of_chapters(
            reference.end_book,
            **kwargs,
        )
        return f"{end_chapter}:"

    if (
        _does_reference_include_all_verses_in_start_book(reference, **kwargs)
        and not force_include_chapters
    ):
        return ""

    if _is_single_chapter_book(reference.book, **kwargs):
        return ""

    if (
        reference.start_chapter
        and reference.end_chapter
        and reference.start_chapter == reference.end_chapter
    ):
        return ""

    end_chapter = reference.end_chapter or _get_number_of_chapters(
        reference.book,
        **kwargs,
    )
    return f"{end_chapter}:"


def _get_end_verse(reference: NormalizedReference, **kwargs: Any) -> str:
    force_include_chapters: bool = kwargs.get("always_include_chapter_numbers", False)

    if reference.end_book and reference.book != reference.end_book:
        if (
            _does_reference_include_all_verses_in_end_book(reference, **kwargs)
            and not force_include_chapters
        ):
            return ""

        end_chapter = reference.end_chapter or _get_number_of_chapters(
            reference.end_book,
            **kwargs,
        )
        end_verse = reference.end_verse or _get_number_of_verses(
            reference.end_book,
            end_chapter,
            **kwargs,
        )
        return f"{end_verse}"

    if (
        _does_reference_include_all_verses_in_start_book(reference, **kwargs)
        and not force_include_chapters
    ):
        return ""

    start_chapter = reference.start_chapter or 1
    start_verse = reference.start_verse or 1
    end_chapter = reference.end_chapter or _get_number_of_chapters(
        reference.book,
        **kwargs,
    )
    end_verse = reference.end_verse or _get_number_of_verses(
        reference.book,
        end_chapter,
        **kwargs,
    )

    return (
        f"{end_verse}"
        if start_verse != end_verse or start_chapter != end_chapter
        else ""
    )


def _does_reference_include_all_verses_in_start_book(
    reference: NormalizedReference,
    **kwargs: Any,
) -> bool:
    if reference.start_chapter is None and reference.end_chapter is None:
        return True

    if reference.start_chapter != 1:
        return False

    if reference.start_verse != 1:
        return False

    if reference.end_book and reference.end_book != reference.book:
        return True

    max_chapters = _get_number_of_chapters(reference.book, **kwargs)

    if reference.end_chapter != max_chapters:
        return False

    return reference.end_verse == _get_number_of_verses(
        reference.book,
        max_chapters,
        **kwargs,
    )


def _does_reference_include_all_verses_in_end_book(
    reference: NormalizedReference,
    **kwargs: Any,
) -> bool:
    if reference.start_chapter is None and reference.end_chapter is None:
        return True

    end_book: Book = reference.end_book or reference.book
    max_chapters = _get_number_of_chapters(end_book, **kwargs)

    if reference.end_chapter != max_chapters:
        return False

    return reference.end_verse == _get_number_of_verses(
        end_book,
        max_chapters,
        **kwargs,
    )


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
        book, chapter_number, _ = get_book_chapter_verse(verse_id)

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
            title: str = (
                bible.long_titles.get(book, book.title)
                if full_title
                else bible.short_titles.get(book, book.title)
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
