from __future__ import annotations

from pythonbible.verses import get_book_chapter_verse


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
        book, chapter, verse = get_book_chapter_verse(verse_id)
        msg = f"{version} is missing verse {verse_id} ({book} {chapter}:{verse})."
        super().__init__(msg)
