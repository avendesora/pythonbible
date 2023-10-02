from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pythonbible.books import Book


class InvalidBookError(Exception):
    """Raised when the book id is not valid."""


class InvalidChapterError(Exception):
    """Raised when the chapter number is not valid for the given book of the Bible."""


class InvalidVerseError(Exception):
    """Raised when the verse id is not a valid Bible verse.

    Or raised when the book, chapter, and verse number being processed is not a valid
    Bible verse.
    """

    def __init__(
        self: InvalidVerseError,
        message: str | None = None,
        verse_id: int | None = None,
        book: Book | None = None,
        chapter: int | None = None,
        verse: int | None = None,
    ) -> None:
        """Initialize InvalidVerseError.

        :param message: optional message string
        :param verse_id: optional verse id
        :param book: optional Book
        :param chapter: optional chapter number
        :param verse: optional verse number
        """
        self.message: str | None = message

        if not self.message:
            if book and chapter and verse:
                self.message = f"{book.title} {chapter}:{verse} is not a valid verse."
            elif verse_id:
                self.message = f"{verse_id} is not a valid verse."

        super().__init__(self.message)


class InvalidBibleParserError(Exception):
    """Raised when the Bible parser is not valid."""


class MissingVerseFileError(Exception):
    """Raised when the verse file for a given version is not found."""


class MissingBookFileError(Exception):
    """Raised when the book file for a given version is not found."""


class VersionMissingVerseError(Exception):
    """Raised when the verse for a given version is missing from the version."""

    def __init__(
        self: VersionMissingVerseError,
        version: str,
        verse_id: int,
    ) -> None:
        """Initialize VersionMissingVerseError.

        :param version: version string
        :param verse_id: verse id
        """
        super().__init__(f"{version} is missing verse {verse_id}.")
