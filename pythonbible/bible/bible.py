"""Contains the Bible class."""
from __future__ import annotations

from functools import lru_cache

from pythonbible.errors import InvalidVerseError
from pythonbible.validator import is_valid_verse_id
from pythonbible.versions import Version


class Bible:
    """
    The Bible class.

    The Bible class contains the scripture content for a version and format along with
    the functionality necessary to get the scripture content for a verse or range of
    verses.
    """

    def __init__(
        self: Bible,
        version: Version,
        scripture_content: str,
        verse_start_indices: dict[int, int],
        verse_end_indices: dict[int, int],
        is_html: bool = False,
    ) -> None:
        self.version: Version = version
        self.scripture_content: str = scripture_content
        self.verse_start_indices: dict[int, int] = verse_start_indices
        self.verse_end_indices: dict[int, int] = verse_end_indices
        self.is_html: bool = is_html

    @lru_cache()
    def get_scripture(
        self: Bible,
        start_verse_id: int,
        end_verse_id: int | None = None,
    ) -> str:
        if not is_valid_verse_id(start_verse_id):
            raise InvalidVerseError(
                f"start verse id ({start_verse_id}) is not a valid verse id.",
            )

        if end_verse_id and not is_valid_verse_id(end_verse_id):
            raise InvalidVerseError(
                f"end verse id ({end_verse_id}) is not a valid verse id.",
            )

        end_verse_id = end_verse_id or start_verse_id
        start_index = self.verse_start_indices.get(start_verse_id)
        end_index = self.verse_end_indices.get(end_verse_id)

        return _clean(self.scripture_content[start_index:end_index], self.is_html)


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
