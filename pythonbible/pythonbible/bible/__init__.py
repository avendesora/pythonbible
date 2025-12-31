from __future__ import annotations

from importlib import import_module
from pathlib import Path
from typing import TYPE_CHECKING

from pythonbible.errors import MissingBiblePackageError
from pythonbible.versions import Version

if TYPE_CHECKING:
    from pythonbible.bible.bible import Bible


CURRENT_FOLDER = Path(__file__).parent

BIBLES: dict[Version, dict[str, Bible]] = {}

BIBLE_PACKAGE_NAMES: dict[Version, str] = {
    Version.AMERICAN_KING_JAMES: "pythonbible_akjv",
    Version.AMERICAN_STANDARD: "pythonbible_asv",
    Version.BIBLE_IN_BASIC_ENGLISH: "pythonbible_bbe",
    Version.WORLWIDE_ENGLISH: "pythonbible_bwe",
    Version.DARBY: "pythonbible_dar",
    Version.DIAGLOT_NT: "pythonbible_diaglot",
    Version.DOUAY_RHEIMS: "pythonbible_dr",
    Version.ETHERIDGE: "pythonbible_etheridge",
    Version.GENEVA: "pythonbible_gb",
    Version.KING_JAMES: "pythonbible_kjv",
    Version.LEESER: "pythonbible_leeser",
    Version.LIVING_ORACLES_NT: "pythonbible_lont",
    Version.KING_JAMES_MODERN_1963: "pythonbible_mkjv1963",
    Version.MONTGOMERY_NT: "pythonbible_mont",
    Version.NEW_HEART: "pythonbible_nheb",
    Version.OPEN_ENGLISH: "pythonbible_oeb",
    Version.ROTHERHAM: "pythonbible_roth",
    Version.REVISED_WEBSTER: "pythonbible_rwebster",
    Version.REVISED_YOUNGS: "pythonbible_rylt",
    Version.TYNDALE: "pythonbible_tyndale",
    Version.KING_JAMES_UPDATED: "pythonbible_ukjv",
    Version.WEBSTER: "pythonbible_wbs",
    Version.WORLD_ENGLISH: "pythonbible_web",
    Version.WESLEY_NT: "pythonbible_wesley",
    Version.WEYMOUTH_NT: "pythonbible_wmth",
    Version.WYCLIFFE: "pythonbible_wyc",
    Version.YOUNGS: "pythonbible_ylt",
}


def get_bible(version: Version, bible_type: str) -> Bible:
    """Return the Bible for the given version and format.

    :param version: The version of the Bible
    :type version: Version
    :param bible_type: The type of the Bible
    :type bible_type: str
    :return: The Bible for the given version and type
    :rtype: Bible
    :raises MissingBiblePackageError: If no package is found for the given version
    """
    version_bibles = BIBLES.get(version, {})
    error_message = f"No package found for {version.value} ({version.title})."

    if not version_bibles:
        if package_name := BIBLE_PACKAGE_NAMES.get(version):
            module_name = f"{package_name}.{bible_type.lower()}_bible"
        else:
            raise MissingBiblePackageError(error_message)

        try:
            version_module = import_module(module_name)
        except ModuleNotFoundError as e:
            raise MissingBiblePackageError(error_message) from e

        return version_module.bible

    if version_bible := version_bibles.get(bible_type):
        return version_bible

    raise MissingBiblePackageError(error_message)


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
