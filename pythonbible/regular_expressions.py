from __future__ import annotations

import re
from types import MappingProxyType
from typing import Pattern

from pythonbible.books import Book


def build_book_regular_expression(
    book: str,
    prefix: str = None,
    suffix: str = None,
) -> str:
    return _add_suffix(_add_prefix(book, prefix), suffix)


def _add_prefix(regex: str, prefix: str = None) -> str:
    return regex if prefix is None else rf"(?:{prefix})(?:\s)?{regex}"


def _add_suffix(regex: str, suffix: str = None) -> str:
    return regex if suffix is None else rf"{regex}(?:\s*{suffix})?"


SAMUEL_REGULAR_EXPRESSION = "(Samuel" r"|Sam\.*" r"|Sa\.*" r"|Sm\.*)"
KINGS_REGULAR_EXPRESSION = "(Kings" r"|Kgs\.*" r"|Kin\.*" r"|Ki\.*)"
CHRONICLES_REGULAR_EXPRESSION = (
    "(Chronicles" r"|Chron\.*" r"|Chro\.*" r"|Chr\.*" r"|Ch\.*)"
)
JOHN_REGULAR_EXPRESSION = "(John" r"|Joh\.*" r"|Jhn\.*" r"|Jo\.*" r"|Jn\.*)"
CORINTHIANS_REGULAR_EXPRESSION = r"Co\.*(?:r\.*(?:inthians)?)?"
THESSALONIANS_REGULAR_EXPRESSION = r"Th\.*(?:(s|(es(?:s)?))\.*(?:alonians)?)?"
TIMOTHY_REGULAR_EXPRESSION = r"Ti\.*(?:m\.*(?:othy)?)?"
PETER_REGULAR_EXPRESSION = r"(Pe\.*(?:t\.*(?:er)?)?|Pt\.*)"

MACCABEES_REGULAR_EXPRESSION = "(Maccabees" r"|Macc\.*" r"|Mac\.*" r"|Ma\.*" r"|M\.*)"

FIRST = "1" r"|I\s+" r"|1st\s+" r"|First\s+"
SECOND = "2" "|II" r"|2nd\s+" r"|Second\s+"
THIRD = "3" "|III" r"|3rd\s+" r"|Third\s+"

FIRST_BOOK = rf"{FIRST}|(First\s+Book\s+of(?:\s+the)?)"
SECOND_BOOK = rf"{SECOND}|(Second\s+Book\s+of(?:\s+the)?)"

EPISTLE_OF_PAUL_TO = r"Epistle\s+of\s+Paul\s+(?:the\s+Apostle\s+)?to(?:\s+the)?"
GENERAL_EPISTLE_OF = r"(?:General\s+)?Epistle\s+(?:General\s+)?of"

FIRST_PAUL_EPISTLE = rf"{FIRST}|(First\s+{EPISTLE_OF_PAUL_TO})"
SECOND_PAUL_EPISTLE = rf"{SECOND}|(Second\s+{EPISTLE_OF_PAUL_TO})"

FIRST_GENERAL_EPISTLE = rf"{FIRST}|(First\s+{GENERAL_EPISTLE_OF})"
SECOND_GENERAL_EPISTLE = rf"{SECOND}|(Second\s+{GENERAL_EPISTLE_OF})"
THIRD_GENERAL_EPISTLE = rf"{THIRD}|(Third\s+{GENERAL_EPISTLE_OF})"

# noinspection SpellCheckingInspection
BOOK_REGULAR_EXPRESSIONS: dict[Book, str] = MappingProxyType(
    {
        Book.GENESIS: r"Gen\.*(?:esis)?",
        Book.EXODUS: r"Exo\.*(?:d\.*)?(?:us)?",
        Book.LEVITICUS: r"Lev\.*(?:iticus)?",
        Book.NUMBERS: r"Num\.*(?:bers)?",
        Book.DEUTERONOMY: r"Deu\.*(?:t\.*)?(?:eronomy)?",
        Book.JOSHUA: "(Joshua" r"|Josh\.*" r"|Jos\.*" r"|Jsh\.*)",
        Book.JUDGES: "(Judges" r"|Judg\.*" r"|Jdgs\.*" r"|Jdg\.*)",
        Book.RUTH: "(Ruth" r"|Rut\.*" r"|Rth\.*)",
        Book.SAMUEL_1: build_book_regular_expression(
            SAMUEL_REGULAR_EXPRESSION,
            prefix=FIRST_BOOK,
            suffix=r"Otherwise\s+Called\s+The\s+First\s+Book\s+of\s+the\s+Kings",
        ),
        Book.SAMUEL_2: build_book_regular_expression(
            SAMUEL_REGULAR_EXPRESSION,
            prefix=SECOND_BOOK,
            suffix=r"Otherwise\s+Called\s+The\s+Second\s+Book\s+of\s+the\s+Kings",
        ),
        Book.KINGS_1: build_book_regular_expression(
            KINGS_REGULAR_EXPRESSION,
            prefix=FIRST_BOOK,
            suffix=r"\,\s+Commonly\s+Called\s+the\s+Third\s+Book\s+of\s+the\s+Kings",
        ),
        Book.KINGS_2: build_book_regular_expression(
            KINGS_REGULAR_EXPRESSION,
            prefix=SECOND_BOOK,
            suffix=r"\,\s+Commonly\s+Called\s+the\s+Fourth\s+Book\s+of\s+the\s+Kings",
        ),
        Book.CHRONICLES_1: build_book_regular_expression(
            CHRONICLES_REGULAR_EXPRESSION,
            prefix=FIRST_BOOK,
        ),
        Book.CHRONICLES_2: build_book_regular_expression(
            CHRONICLES_REGULAR_EXPRESSION,
            prefix=SECOND_BOOK,
        ),
        Book.EZRA: r"Ezr\.*(?:a)?",
        Book.NEHEMIAH: r"Neh\.*(?:emiah)?",
        Book.ESTHER: r"Est\.*(?:h\.*)?(?:er)?",
        Book.JOB: "Job",
        Book.PSALMS: "(Psalms"
        "|Psalm"
        r"|Pslm\.*"
        r"|Psa\.*"
        r"|Psm\.*"
        r"|Pss\.*"
        r"|Ps\.*)",
        Book.PROVERBS: "(Proverbs" r"|Prov\.*" r"|Pro\.*" r"|Prv\.*)",
        Book.ECCLESIASTES: r"(Ecclesiastes(?:\s+or\,\s+the\s+Preacher)?"
        r"|Eccles\.*(?!iasticus?)"
        r"|Eccle\.*(?!siasticus?)"
        r"|Eccl\.*(?!esiasticus?)(?!us?)"
        r"|Ecc\.*(?!lesiasticus?)(?!lus?)"
        r"|Ec\.*(?!clesiasticus?)(?!clus?)"
        r"|Qoh\.*)",
        Book.SONG_OF_SONGS: r"(Song(?: of (Solomon|Songs|Sol\.*))?)"
        "|Canticles"
        "|(Canticle(?: of Canticles)?)"
        "|SOS"
        "|Cant",
        Book.ISAIAH: r"Isa\.*(?:iah)?",
        Book.JEREMIAH: r"Jer\.*(?:emiah)?",
        Book.LAMENTATIONS: build_book_regular_expression(
            r"Lam\.*(?:entations)?",
            suffix=r"of\s+Jeremiah",
        ),
        Book.EZEKIEL: "(Ezekiel" r"|Ezek\.*" r"|Eze\.*" r"|Ezk\.*)",
        Book.DANIEL: r"Dan\.*(?:iel)?",
        Book.HOSEA: r"Hos\.*(?:ea)?",
        Book.JOEL: r"Joe\.*(?:l)?",
        Book.AMOS: r"Amo\.*(?:s)?",
        Book.OBADIAH: r"Oba\.*(?:d\.*(?:iah)?)?",
        Book.JONAH: "Jonah" r"|Jon\.*" r"|Jnh\.*",
        Book.MICAH: r"Mic\.*(?:ah)?",
        Book.NAHUM: r"Nah\.*(?:um)?",
        Book.HABAKKUK: r"Hab\.*(?:akkuk)?",
        Book.ZEPHANIAH: r"Zep\.*(?:h\.*(?:aniah)?)?",
        Book.HAGGAI: r"Hag\.*(?:gai)?",
        Book.ZECHARIAH: r"Zec\.*(?:h\.*(?:ariah)?)?",
        Book.MALACHI: r"Mal\.*(?:achi)?",
        Book.MATTHEW: r"Mat\.*(?:t\.*(?:hew)?)?",
        Book.MARK: "Mark" r"|Mar\.*" r"|Mrk\.*",
        Book.LUKE: r"Luk\.*(?:e)?",
        Book.JOHN: rf"(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I)){JOHN_REGULAR_EXPRESSION}",
        Book.ACTS: build_book_regular_expression(
            r"Act\.*(?:s)?",
            suffix="of the Apostles",
        ),
        Book.ROMANS: r"Rom\.*(?:ans)?",
        Book.CORINTHIANS_1: build_book_regular_expression(
            CORINTHIANS_REGULAR_EXPRESSION,
            prefix=FIRST_PAUL_EPISTLE,
        ),
        Book.CORINTHIANS_2: build_book_regular_expression(
            CORINTHIANS_REGULAR_EXPRESSION,
            prefix=SECOND_PAUL_EPISTLE,
        ),
        Book.GALATIANS: r"Gal\.*(?:atians)?",
        Book.EPHESIANS: r"Eph\.*(?:es\.*(?:ians)?)?",
        Book.PHILIPPIANS: r"Ph(?:(p\.*)|(?:il\.*(?!e\.*(?:m\.*(?:on)?)?)(?:ippians)?))",
        Book.COLOSSIANS: r"Col\.*(?:ossians)?",
        Book.THESSALONIANS_1: build_book_regular_expression(
            THESSALONIANS_REGULAR_EXPRESSION,
            prefix=FIRST_PAUL_EPISTLE,
        ),
        Book.THESSALONIANS_2: build_book_regular_expression(
            THESSALONIANS_REGULAR_EXPRESSION,
            prefix=SECOND_PAUL_EPISTLE,
        ),
        Book.TIMOTHY_1: build_book_regular_expression(
            TIMOTHY_REGULAR_EXPRESSION,
            prefix=FIRST_PAUL_EPISTLE,
        ),
        Book.TIMOTHY_2: build_book_regular_expression(
            TIMOTHY_REGULAR_EXPRESSION,
            prefix=SECOND_PAUL_EPISTLE,
        ),
        Book.TITUS: r"Tit\.*(?:us)?",
        # assume 'Phi' is Philemon if Philippians failed
        Book.PHILEMON: "(Philemon|"
        r"Philem\.*|"
        r"Phile\.*|"
        r"Phlm\.*|"
        r"Phi\.*|"
        r"Phm\.*)",
        Book.HEBREWS: r"Heb\.*(?:rews)?",
        Book.JAMES: r"Ja(?:me)?s\.*",
        Book.PETER_1: build_book_regular_expression(
            PETER_REGULAR_EXPRESSION,
            prefix=FIRST_GENERAL_EPISTLE,
        ),
        Book.PETER_2: build_book_regular_expression(
            PETER_REGULAR_EXPRESSION,
            prefix=SECOND_GENERAL_EPISTLE,
        ),
        Book.JOHN_1: build_book_regular_expression(
            JOHN_REGULAR_EXPRESSION,
            prefix=FIRST_GENERAL_EPISTLE,
        ),
        Book.JOHN_2: build_book_regular_expression(
            JOHN_REGULAR_EXPRESSION,
            prefix=SECOND_GENERAL_EPISTLE,
        ),
        Book.JOHN_3: build_book_regular_expression(
            JOHN_REGULAR_EXPRESSION,
            prefix=THIRD_GENERAL_EPISTLE,
        ),
        Book.JUDE: r"Jud\.*(:?e)?",
        Book.REVELATION: build_book_regular_expression(
            r"Rev\.*(?:elation)?",
            suffix="of ((Jesus Christ)|John|(St. John the Divine))",
        ),
        Book.ESDRAS_1: build_book_regular_expression(
            "(Esdras" r"|Esdr\.*" r"|Esd\.*" r"|Es\.*)",
            FIRST,
        ),
        Book.TOBIT: "(Tobit" r"|Tob\.*" r"|Tb\.*)",
        Book.WISDOM_OF_SOLOMON: "(Wisdom of Solomon"
        "|Wisdom"
        r"|Wisd\.* of Sol\.*"
        r"|Wis\.*"
        r"|Ws\.*)",
        Book.ECCLESIASTICUS: "(Sirach" r"|Sir\.*" "|Ecclesiasticus" r"|Ecclus\.*)",
        Book.MACCABEES_1: build_book_regular_expression(
            MACCABEES_REGULAR_EXPRESSION,
            FIRST,
        ),
        Book.MACCABEES_2: build_book_regular_expression(
            MACCABEES_REGULAR_EXPRESSION,
            SECOND,
        ),
    },
)

BOOK_REGEX: str = "|".join(
    rf"\b{regular_expression_value}\b\.?"
    for regular_expression_value in BOOK_REGULAR_EXPRESSIONS.values()
)

CHAPTER_REGEX: str = r"(\d{1,3})"
CHAPTER_VERSE_SEPARATOR: str = "([:.])"
VERSE_REGEX: str = r"(\d{1,3})"
CHAPTER_AND_VERSE_REGEX: str = (
    rf"({CHAPTER_REGEX}(\s*{CHAPTER_VERSE_SEPARATOR}\s*{VERSE_REGEX})?)"
)
RANGE_REGEX: str = (
    rf"({CHAPTER_AND_VERSE_REGEX}(\s*-\s*({CHAPTER_REGEX}\s*"
    rf"{CHAPTER_VERSE_SEPARATOR}\s*)?{VERSE_REGEX})?)"
)
ADDITIONAL_REFERENCE_REGEX: str = rf"(\s*,\s*({RANGE_REGEX}|{VERSE_REGEX}))"
FULL_CHAPTER_AND_VERSE_REGEX: str = f"({RANGE_REGEX}({ADDITIONAL_REFERENCE_REGEX})*)"

FULL_BOOK_REGEX = rf"({BOOK_REGEX})\s*({FULL_CHAPTER_AND_VERSE_REGEX})?"
CROSS_BOOK_REGEX = rf"({FULL_BOOK_REGEX}(\s*-\s*({FULL_BOOK_REGEX}))?)"

SCRIPTURE_REFERENCE_REGULAR_EXPRESSION: Pattern[str] = re.compile(
    CROSS_BOOK_REGEX,
    re.IGNORECASE | re.UNICODE,
)
