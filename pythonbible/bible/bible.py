"""Contains the Bible class."""

from __future__ import annotations

from functools import lru_cache
from typing import TYPE_CHECKING

from pythonbible.bible.errors import VersionMissingVerseError
from pythonbible.errors import InvalidVerseError
from pythonbible.validator import is_valid_verse_id
from pythonbible.verses import get_book_chapter_verse

if TYPE_CHECKING:
    from pythonbible.books import Book
    from pythonbible.versions import Version


class Bible:
    """The Bible class.

    The Bible class contains the scripture content for a version and format along with
    the functionality necessary to get the scripture content for a verse or range of
    verses.
    """

    version: Version
    scripture_content: str
    verse_start_indices: dict[int, int]
    verse_end_indices: dict[int, int]
    is_html: bool

    _max_verses: dict[Book, dict[int, int]]

    def __init__(
        self: Bible,
        version: Version,
        scripture_content: str,
        verse_start_indices: dict[int, int],
        verse_end_indices: dict[int, int],
        is_html: bool = False,
    ) -> None:
        """Initialize a Bible object.

        :param version: The version of the Bible.
        :param scripture_content: The scripture content for the Bible.
        :param verse_start_indices: The start indices for each verse.
        :param verse_end_indices: The end indices for each verse.
        """
        self.version = version
        self.scripture_content = scripture_content
        self.verse_start_indices = verse_start_indices
        self.verse_end_indices = verse_end_indices
        self.is_html = is_html
        self._max_verses = {}

    @property
    def max_verse_number_by_book_and_chapter(self: Bible) -> dict[Book, dict[int, int]]:
        """Get the maximum verse number by book and chapter."""
        if not self._max_verses:
            for verse_id in self.verse_start_indices:
                book, chapter, verse = get_book_chapter_verse(verse_id)
                chapters: dict[int, int] = self._max_verses.get(
                    book,
                    {},
                )
                verses = chapters.get(chapter, 0)

                if verse > verses:
                    chapters[chapter] = verse
                    self._max_verses[book] = chapters

        return self._max_verses

    def get_scripture(
        self: Bible,
        start_verse_id: int,
        end_verse_id: int | None = None,
    ) -> str:
        if not is_valid_verse_id(start_verse_id):
            msg = f"start verse id ({start_verse_id}) is not a valid verse id."
            raise InvalidVerseError(msg)

        if end_verse_id and not is_valid_verse_id(end_verse_id):
            msg = f"end verse id ({end_verse_id}) is not a valid verse id."
            raise InvalidVerseError(msg)

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
        start_index = self.verse_start_indices.get(start_verse_id)

        if start_index is None:
            raise VersionMissingVerseError(self.version.value, start_verse_id)

        end_index = self.verse_end_indices.get(end_verse_id)

        if end_index is None:
            raise VersionMissingVerseError(self.version.value, end_verse_id)

        return start_index, end_index


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
