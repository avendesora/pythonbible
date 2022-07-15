from __future__ import annotations

from typing import Any


class InvalidBookError(Exception):
    """Raise when the book id is not valid."""


class InvalidChapterError(Exception):
    """Raise when the chapter number is not valid for the given book of the Bible."""


class InvalidVerseError(Exception):
    """
    Raise when the verse id is not a valid Bible verse.

    Or raise when the book, chapter, and verse number being processed is not a valid
    Bible verse.
    """

    def __init__(
        self: InvalidVerseError,
        message: str | None = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize InvalidVerseError.

        :param message: optional message string
        :param kwargs: optional keyword arguments (verse_id, book, chapter, verse) for
                       more specific messaging
        """
        self.message: str | None = message
        self.verse_id: Any | None = kwargs.get("verse_id")
        self.book: Any | None = kwargs.get("book")
        self.chapter: Any | None = kwargs.get("chapter")
        self.verse: Any | None = kwargs.get("verse")

        if not self.message:
            if self.book and self.chapter and self.verse:
                self.message = (
                    f"{self.book.title} {self.chapter}:{self.verse} "
                    f"is not a valid verse."
                )
            elif self.verse_id:
                self.message = f"{self.verse_id} is not a valid verse."

        super().__init__(self.message)


class InvalidBibleParserError(Exception):
    """Raised when the Bible parser is not valid."""


class MissingVerseFileError(Exception):
    """Raised when the verse file for a given version is not found."""


class MissingBookFileError(Exception):
    """Raised when the book file for a given version is not found."""
