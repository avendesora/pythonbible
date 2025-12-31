from __future__ import annotations

from typing import TYPE_CHECKING

from pythonbible.books import Book

if TYPE_CHECKING:
    from pythonbible.versions import Version


class VersionMissingBookError(Exception):
    """Raised when the book for a given version is missing from the version."""

    def __init__(
        self: VersionMissingBookError,
        version: Version,
        book: Book,
    ) -> None:
        """Initialize VersionMissingBookError.

        :param version: version string
        :param book: Book enum
        """
        msg = f"{version.title} is missing book {book.title}."
        super().__init__(msg)


class VersionMissingChapterError(Exception):
    """Raised when the chapter for a given version is missing from the version."""

    def __init__(
        self: VersionMissingChapterError,
        version: Version,
        book: Book,
        chapter: int,
    ) -> None:
        """Initialize VersionMissingChapterError.

        :param version: version string
        :param book: Book enum
        :param chapter: chapter number
        """
        msg = f"{version.title} is missing chapter {chapter} of book {book.title}."
        super().__init__(msg)


class VersionMissingVerseError(Exception):
    """Raised when the verse for a given version is missing from the version."""

    def __init__(
        self: VersionMissingVerseError,
        version: Version,
        verse_id: int,
    ) -> None:
        """Initialize VersionMissingVerseError.

        :param version: version string
        :param verse_id: verse id
        """
        try:
            book = Book(verse_id // 1_000_000).title  # type: ignore[call-arg]
        except ValueError:
            book = "Unknown Book"

        chapter = (verse_id // 1_000) % 1_000
        verse = (verse_id // 1_000) % 1_000
        msg = f"{version.title} is missing verse {verse_id} ({book} {chapter}:{verse})."
        super().__init__(msg)
