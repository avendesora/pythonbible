from __future__ import annotations

from functools import lru_cache
from importlib import import_module
from pathlib import Path
from typing import TYPE_CHECKING

from pythonbible.errors import MissingVerseFileError

if TYPE_CHECKING:
    from pythonbible.bible.bible import Bible
    from pythonbible.books import Book
    from pythonbible.versions import Version


CURRENT_FOLDER = Path(__file__).parent

BIBLES: dict[Version, dict[str, Bible]] = {}
SHORT_TITLES: dict[Version, dict[Book, str]] = {}
LONG_TITLES: dict[Version, dict[Book, str]] = {}


@lru_cache
def get_bible(version: Version, bible_type: str) -> Bible:
    """Return the Bible for the given version and format.

    :param version: The version of the Bible
    :type version: Version
    :param bible_type: The type of the Bible
    :type bible_type: str
    :return: The Bible for the given version and type
    :rtype: Bible
    """
    version_bibles = BIBLES.get(version, {})

    if not version_bibles:
        _init_version(version)
        version_bibles = BIBLES.get(version, {})

    if version_bible := version_bibles.get(bible_type):
        return version_bible

    raise MissingVerseFileError


def add_bible(version: Version, bible_type: str, version_bible: Bible) -> None:
    """Add the Bible to the dictionary of Bibles.

    This should allow a user to BYOB (bring your own Bible) to the library, which can
    be useful if a user has licensed a copyrighted Bible (which is not included in the
    pythonbible library) for use within their application.

    :param version: The version of the Bible
    :type version: Version
    :param bible_type: The type of the Bible
    :type bible_type: str
    :param version_bible: The Bible to add
    :type version_bible: Bible
    """
    if version not in BIBLES:
        BIBLES[version] = {}

    BIBLES[version][bible_type] = version_bible


@lru_cache
def get_short_title(version: Version, book: Book) -> str:
    """Return the short title for the given book and version.

    :param version: The version of the Bible
    :type version: Version
    :param book: The book of the Bible
    :type book: Book
    :return: The short title for the given book and version
    :rtype: str
    """
    version_short_titles = SHORT_TITLES.get(version, {})

    if not version_short_titles:
        try:
            _init_version(version)
            version_short_titles = SHORT_TITLES.get(version, {})
        except MissingVerseFileError:
            return book.title

    return version_short_titles.get(book, book.title)


@lru_cache
def get_long_title(version: Version, book: Book) -> str:
    """Return the long title for the given book and version.

    :param version: The version of the Bible
    :type version: Version
    :param book: The book of the Bible
    :type book: Book
    :return: The long title for the given book and version
    :rtype: str
    """
    version_long_titles = LONG_TITLES.get(version, {})

    if not version_long_titles:
        try:
            _init_version(version)
            version_long_titles = LONG_TITLES.get(version, {})
        except MissingVerseFileError:
            return book.title

    return version_long_titles.get(book, book.title)


def _do_version_files_exist(version: Version) -> bool:
    version_folder = CURRENT_FOLDER / "versions" / version.value.lower()
    return version_folder.exists()


def _init_version(version: Version) -> None:
    # Lazy-loading of Bible files to conserve memory
    if not _do_version_files_exist(version):
        raise MissingVerseFileError

    version_module = import_module(
        f".{version.value.lower()}",
        "pythonbible.bible.versions",
    )
    BIBLES[version] = version_module.BIBLES[version]
    SHORT_TITLES[version] = version_module.SHORT_TITLES
    LONG_TITLES[version] = version_module.LONG_TITLES
