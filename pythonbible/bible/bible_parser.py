"""Contains the BibleParser generic parser class."""
from __future__ import annotations

from abc import abstractmethod
from collections import OrderedDict
from typing import Any

from pythonbible.books import Book
from pythonbible.versions import Version


class BibleParser:
    """
    Parse files containing scripture text.

    BibleParser is a generic parser to provide common functionality for specific
    parsers (e.g. OSIS, USFM, USFX, etc.) for parsing scripture text.
    """

    def __init__(self: BibleParser, version: Version) -> None:
        """
        Initialize the Bible parser with the version.

        :param version:
        """
        self.version: Version = version

    @abstractmethod
    def get_book_title(self: BibleParser, book: Book) -> str:
        """
        Given a book, return the full title for that book from the XML file.

        :param book:
        :return: the full title string
        """

    @abstractmethod
    def get_short_book_title(self: BibleParser, book: Book) -> str:
        """
        Given a book, return the short title for that book from the XML file.

        :param book:
        :return: the short title string
        """

    @abstractmethod
    def get_scripture_passage_text(
        self: BibleParser,
        verse_ids: list[int],
        **kwargs: Any,
    ) -> dict[Book, dict[int, list[str]]]:
        """
        Get the scripture passage for the given verse ids.

        Given a list of verse ids, return the structured scripture text passage
        organized by book, chapter, and paragraph.

        If the include_verse_number keyword argument is True, include the verse
        numbers in the scripture passage; otherwise, do not include them.

        :param verse_ids:
        :param kwargs
        :return: an OrderedDict(Book, OrderedDict(int, list(string)))
        """

    @abstractmethod
    def verse_text(self: BibleParser, verse_id: int, **kwargs: Any) -> str:
        """
        Get the scripture text for the given verse id.

        Given a verse id, return the string scripture text passage for that verse.

        If the include_verse_number keyword argument is True, include the verse
        numbers in the scripture passage; otherwise, do not include them.

        :param verse_id:
        :param kwargs:
        :return:
        """


def sort_paragraphs(
    paragraphs: dict[Book, dict[int, list[str]]],
) -> dict[Book, dict[int, list[str]]]:
    """
    Sort paragraphs of scripture text.

    Given a structured collection of paragraphs organized by book, chapter, and
    list of paragraphs, return that collection in an ordered dictionary with the
    books and chapters sorted appropriately. (Assume the list of paragraphs is
    already sorted appropriately.)

    :param paragraphs:
    :return: an OrderedDict(Book, OrderedDict(int, list(string)))
    """
    ordered_paragraphs: dict[Book, dict[int, list[str]]] = OrderedDict()

    book_keys: list[Book] = list(paragraphs.keys())
    book_keys.sort()

    for book in book_keys:
        chapters: dict[int, list[str]] = paragraphs.get(book, OrderedDict())
        ordered_chapters: dict[int, list[str]] = OrderedDict()

        chapter_keys: list[int] = list(chapters.keys())
        chapter_keys.sort()

        for chapter in chapter_keys:
            ordered_chapters[chapter] = chapters.get(chapter, [])

        ordered_paragraphs[book] = ordered_chapters

    return ordered_paragraphs
