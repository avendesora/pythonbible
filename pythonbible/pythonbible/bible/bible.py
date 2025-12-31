"""Contains the Bible class."""

from __future__ import annotations

from functools import lru_cache
from typing import TYPE_CHECKING

from pythonbible.bible.errors import VersionMissingBookError
from pythonbible.bible.errors import VersionMissingChapterError
from pythonbible.bible.errors import VersionMissingVerseError

if TYPE_CHECKING:
    from pythonbible.books import Book
    from pythonbible.versions import Version


class Bible:
    """The Bible class.

    The Bible class contains the scripture content for a version and format along with
    the functionality necessary to get the scripture content for a verse or range of
    verses.

    :param version: The version of the Bible.
    :type version: Version
    :param scripture_content: The scripture content for the Bible.
    :type scripture_content: str
    :param verse_start_indices: The start indices for each verse.
    :type verse_start_indices: dict[int, int]
    :param verse_end_indices: The end indices for each verse.
    :type verse_end_indices: dict[int, int]
    :param max_verses: The maximum verses for each book and chapter.
    :type max_verses: dict[Book, dict[int, int]]
    :param short_titles: The short titles for each book.
    :type short_titles: dict[Book, str]
    :param long_titles: The long titles for each book.
    :type long_titles: dict[Book, str]
    :param is_html: Whether the scripture content is HTML.
    :type is_html: bool
    """

    version: Version
    scripture_content: str
    verse_start_indices: dict[int, int]
    verse_end_indices: dict[int, int]
    max_verses: dict[Book, dict[int, int]]
    short_titles: dict[Book, str]
    long_titles: dict[Book, str]
    is_html: bool

    def __init__(
        self: Bible,
        version: Version,
        scripture_content: str,
        verse_start_indices: dict[int, int],
        verse_end_indices: dict[int, int],
        max_verses: dict[Book, dict[int, int]],
        short_titles: dict[Book, str],
        long_titles: dict[Book, str],
        is_html: bool = False,
    ) -> None:
        """Initialize a Bible object.

        :param version: The version of the Bible.
        :type version: Version
        :param scripture_content: The scripture content for the Bible.
        :type scripture_content: str
        :param verse_start_indices: The start indices for each verse.
        :type verse_start_indices: dict[int, int]
        :param verse_end_indices: The end indices for each verse.
        :type verse_end_indices: dict[int, int]
        :param max_verses: The maximum verses for each book and chapter.
        :type max_verses: dict[Book, dict[int, int]]
        :param short_titles: The short titles for each book.
        :param short_titles: The short titles for each book.
        :param long_titles: The long titles for each book.
        :type long_titles: dict[Book, str]
        :param is_html: Whether the scripture content is HTML.
        :type is_html: bool
        """
        self.version = version
        self.scripture_content = scripture_content
        self.verse_start_indices = verse_start_indices
        self.verse_end_indices = verse_end_indices
        self.max_verses = max_verses
        self.short_titles = short_titles
        self.long_titles = long_titles
        self.is_html = is_html

    def get_scripture(
        self: Bible,
        start_verse_id: int,
        end_verse_id: int | None = None,
    ) -> str:
        """Get the scripture content for the given verse ID or range of verse IDs.

        :param start_verse_id: The starting verse ID.
        :type start_verse_id: int
        :param end_verse_id: The ending verse ID.
        :type end_verse_id: int | None
        :return: The scripture content for the given verse ID or range of verse IDs.
        :rtype: str
        :raises VersionMissingVerseError: if a verse ID is not valid for the version
        """
        if not self.is_valid_verse_id(start_verse_id):
            raise VersionMissingVerseError(self.version, start_verse_id)

        if end_verse_id and not self.is_valid_verse_id(end_verse_id):
            raise VersionMissingVerseError(self.version, end_verse_id)

        end_verse_id = end_verse_id or start_verse_id
        start_index, end_index = self._get_start_and_end_indices(
            start_verse_id,
            end_verse_id,
        )

        return _clean(self.scripture_content[start_index:end_index], self.is_html)

    def _get_start_and_end_indices(
        self: Bible,
        start_verse_id: int,
        end_verse_id: int,
    ) -> tuple[int, int]:
        start_index = self.verse_start_indices.get(start_verse_id, -1)
        end_index = self.verse_end_indices.get(end_verse_id, -1)
        return start_index, end_index

    def is_valid_verse_id(self, verse_id: int) -> bool:
        """Check if the given verse ID is valid in this Bible version.

        :param verse_id: a verse id
        :type verse_id: int
        :return: True if the verse_id is valid; otherwise, False.
        :rtype: bool
        """
        return verse_id in self.verse_start_indices

    def get_number_of_chapters(self, book: Book) -> int:
        """Get the number of chapters in the given book.

        :param book: a book of the Bible
        :type book: Book
        :return: the number of chapters in the given book
        :rtype: int
        :raises VersionMissingBookError: if the book is not valid for the version
        """
        if chapters := self.max_verses.get(book):
            return len(chapters)

        raise VersionMissingBookError(self.version, book)

    def get_number_of_verses(self, book: Book, chapter: int) -> int:
        """Get the number of verses in the given book and chapter.

        :param book: a book of the Bible
        :type book: Book
        :param chapter: a chapter number
        :type chapter: int
        :return: the number of verses in the given book and chapter
        :rtype: int
        :raises VersionMissingBookError: if the book is not valid for the version
        :raises VersionMissingChapterError: if the chapter is not valid for the book
        """
        chapters = self.max_verses.get(book)

        if not chapters:
            raise VersionMissingBookError(self.version, book)

        if chapter not in chapters:
            raise VersionMissingChapterError(self.version, book, chapter)

        return chapters.get(chapter, -1)

    def get_verse_ids(self) -> tuple[int, ...]:
        """Get all verse IDs in this Bible version.

        :return: A tuple of all verse IDs
        :rtype: tuple[int, ...]
        """
        return tuple(self.verse_start_indices.keys())


@lru_cache()
def _clean(scripture_content: str, is_html: bool) -> str:
    cleaned_content: str = scripture_content.strip()
    return clean_html(cleaned_content) if is_html else cleaned_content


@lru_cache()
def clean_html(scripture_content: str) -> str:
    if not scripture_content or scripture_content in {"</p><p>", "<p></p>"}:
        return ""

    cleaned_content: str = scripture_content

    if cleaned_content.endswith("<p>"):
        cleaned_content = cleaned_content[:-3]

    if not cleaned_content.startswith("<p>"):
        cleaned_content = f"<p>{cleaned_content}"

    if not cleaned_content.endswith("</p>"):
        cleaned_content = f"{cleaned_content}</p>"

    return "" if cleaned_content == "<p></p>" else cleaned_content
