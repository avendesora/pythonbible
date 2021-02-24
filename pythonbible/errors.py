from typing import Any, Optional


class InvalidBookError(Exception):
    """Raised when the book id is not valid."""


class InvalidChapterError(Exception):
    """Raised when the chapter number is not a valid chapter number for the given book of the Bible."""


class InvalidVerseError(Exception):
    """Raised when the verse id or book, chapter, and verse number being processed is not a valid Bible verse."""

    def __init__(self, message: Optional[str] = None, **kwargs) -> None:
        """

        :param message: optional message string
        :param kwargs: optional keyword arguments (verse_id, book, chapter, verse) for more specific messaging
        """
        self.message: Optional[str] = message
        self.verse_id: Optional[Any] = kwargs.get("verse_id")
        self.book: Optional[Any] = kwargs.get("book")
        self.chapter: Optional[Any] = kwargs.get("chapter")
        self.verse: Optional[Any] = kwargs.get("verse")

        if not self.message:
            if self.book and self.chapter and self.verse:
                self.message = f"{self.book.title} {self.chapter}:{self.verse} is not a valid verse."
            elif self.verse_id:
                self.message = f"{self.verse_id} is not a valid verse."

        super(InvalidVerseError, self).__init__(self.message)


class InvalidBibleParserError(Exception):
    """Raised when the Bible parser is not valid."""


class MissingVerseFileError(Exception):
    """Raised when the verse file for a given version is not found."""


class MissingBookFileError(Exception):
    """Raised when the book file for a given version is not found."""
