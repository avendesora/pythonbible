from __future__ import annotations

from enum import Enum
from typing import Any
from typing import Type


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


SAMUEL_REGULAR_EXPRESSION = r"(Samuel|Sam\.*|Sa\.*|Sm\.*)"
KINGS_REGULAR_EXPRESSION = r"(Kings|Kgs\.*|Kin\.*|Ki\.*)"
CHRONICLES_REGULAR_EXPRESSION = r"(Chronicles|Chron\.*|Chro\.*|Chr\.*|Ch\.*)"
JOHN_REGULAR_EXPRESSION = r"(John|Joh\.*|Jhn\.*|Jo\.*(?!shua|b|nah|el)|Jn\.*)"
CORINTHIANS_REGULAR_EXPRESSION = r"Co\.*(?:r\.*(?:inthians)?)?"
THESSALONIANS_REGULAR_EXPRESSION = r"Th\.*(?:(s|(es(?:s)?))\.*(?:alonians)?)?"
TIMOTHY_REGULAR_EXPRESSION = r"Ti\.*(?:m\.*(?:othy)?)?"
PETER_REGULAR_EXPRESSION = r"(Pe\.*(?:t\.*(?:er)?)?|Pt\.*)"

MACCABEES_REGULAR_EXPRESSION = r"(Maccabees|Macc\.*|Mac\.*|Ma\.*|M\.*)"

FIRST = r"1|I\s+|1st\s+|First\s+"
SECOND = r"2|II|2nd\s+|Second\s+"
THIRD = r"3|III|3rd\s+|Third\s+"

FIRST_BOOK = rf"{FIRST}|(First\s+Book\s+of(?:\s+the)?)"
SECOND_BOOK = rf"{SECOND}|(Second\s+Book\s+of(?:\s+the)?)"

EPISTLE_OF_PAUL_TO = r"Epistle\s+of\s+Paul\s+(?:the\s+Apostle\s+)?to(?:\s+the)?"
GENERAL_EPISTLE_OF = r"(?:General\s+)?Epistle\s+(?:General\s+)?of"

FIRST_PAUL_EPISTLE = rf"{FIRST}|(First\s+{EPISTLE_OF_PAUL_TO})"
SECOND_PAUL_EPISTLE = rf"{SECOND}|(Second\s+{EPISTLE_OF_PAUL_TO})"

FIRST_GENERAL_EPISTLE = rf"{FIRST}|(First\s+{GENERAL_EPISTLE_OF})"
SECOND_GENERAL_EPISTLE = rf"{SECOND}|(Second\s+{GENERAL_EPISTLE_OF})"
THIRD_GENERAL_EPISTLE = rf"{THIRD}|(Third\s+{GENERAL_EPISTLE_OF})"


class Book(Enum):
    """Book is an Enum that contains all the books of the Bible.

    :param title: the common English name of the book
    :type title: str
    :param regular_expression: the regular expression for the book
    :type regular_expression: str
    """

    def __new__(
        cls: Type[Book],
        *args: dict[str, Any],
        **kwargs: dict[str, Any],
    ) -> Book:
        obj: Book = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self: Book, _: int, title: str, regular_expression: str) -> None:
        """Set the title and regular_expression properties."""
        self._title_ = title
        self._regular_expression_ = regular_expression

    GENESIS = 1, "Genesis", r"Gen\.*(?:esis)?"
    EXODUS = 2, "Exodus", r"Exo\.*(?:d\.*)?(?:us)?"
    LEVITICUS = 3, "Leviticus", r"Lev\.*(?:iticus)?"
    NUMBERS = 4, "Numbers", r"Num\.*(?:bers)?"
    DEUTERONOMY = 5, "Deuteronomy", r"Deu\.*(?:t\.*)?(?:eronomy)?"
    JOSHUA = 6, "Joshua", r"(Joshua|Josh\.*|Jos\.*|Jsh\.*)"
    JUDGES = 7, "Judges", r"(Judges|Judg\.*|Jdgs\.*|Jdg\.*)"
    RUTH = 8, "Ruth", r"(Ruth|Rut\.*|Rth\.*)"
    SAMUEL_1 = (
        9,
        "1 Samuel",
        build_book_regular_expression(
            SAMUEL_REGULAR_EXPRESSION,
            prefix=FIRST_BOOK,
            suffix=r"Otherwise\s+Called\s+The\s+First\s+Book\s+of\s+the\s+Kings",
        ),
    )
    SAMUEL_2 = (
        10,
        "2 Samuel",
        build_book_regular_expression(
            SAMUEL_REGULAR_EXPRESSION,
            prefix=SECOND_BOOK,
            suffix=r"Otherwise\s+Called\s+The\s+Second\s+Book\s+of\s+the\s+Kings",
        ),
    )
    KINGS_1 = (
        11,
        "1 Kings",
        build_book_regular_expression(
            KINGS_REGULAR_EXPRESSION,
            prefix=FIRST_BOOK,
            suffix=r"\,\s+Commonly\s+Called\s+the\s+Third\s+Book\s+of\s+the\s+Kings",
        ),
    )
    KINGS_2 = (
        12,
        "2 Kings",
        build_book_regular_expression(
            KINGS_REGULAR_EXPRESSION,
            prefix=SECOND_BOOK,
            suffix=r"\,\s+Commonly\s+Called\s+the\s+Fourth\s+Book\s+of\s+the\s+Kings",
        ),
    )
    CHRONICLES_1 = (
        13,
        "1 Chronicles",
        build_book_regular_expression(
            CHRONICLES_REGULAR_EXPRESSION,
            prefix=FIRST_BOOK,
        ),
    )
    CHRONICLES_2 = (
        14,
        "2 Chronicles",
        build_book_regular_expression(
            CHRONICLES_REGULAR_EXPRESSION,
            prefix=SECOND_BOOK,
        ),
    )
    EZRA = 15, "Ezra", r"Ezr\.*(?:a)?"
    NEHEMIAH = 16, "Nehemiah", r"Neh\.*(?:emiah)?"
    ESTHER = 17, "Esther", r"Est\.*(?:h\.*)?(?:er)?"
    JOB = 18, "Job", "Job"
    PSALMS = 19, "Psalms", r"(Psalms|Psalm|Pslm\.*|Psa\.*|Psm\.*|Pss\.*|Ps\.*)"
    PROVERBS = 20, "Proverbs", r"(Proverbs|Prov\.*|Pro\.*|Prv\.*)"
    ECCLESIASTES = (
        21,
        "Ecclesiastes",
        r"(Ecclesiastes(?:\s+or\,\s+the\s+Preacher)?"
        r"|Eccles\.*(?!iasticus?)"
        r"|Eccle\.*(?!siasticus?)"
        r"|Eccl\.*(?!esiasticus?)(?!us?)"
        r"|Ecc\.*(?!lesiasticus?)(?!lus?)"
        r"|(?<!Z)Ec\.*(?!clesiasticus?)(?!clus?)|Qoh\.*)",
    )
    SONG_OF_SONGS = (
        22,
        "Song of Songs",
        r"(Song(?: of (Solomon|Songs|Sol\.*))?)"
        r"|Canticles|(Canticle(?: of Canticles)?)|SOS|Cant",
    )
    ISAIAH = 23, "Isaiah", r"Isa\.*(?:iah)?"
    JEREMIAH = 24, "Jeremiah", r"Jer\.*(?:emiah)?"
    LAMENTATIONS = (
        25,
        "Lamentations",
        build_book_regular_expression(
            r"Lam\.*(?:entations)?",
            suffix=r"of\s+Jeremiah",
        ),
    )
    EZEKIEL = 26, "Ezekiel", r"(Ezekiel|Ezek\.*|Eze\.*|Ezk\.*)"
    DANIEL = 27, "Daniel", r"Dan\.*(?:iel)?"
    HOSEA = 28, "Hosea", r"Hos\.*(?:ea)?"
    JOEL = 29, "Joel", r"Joe\.*(?:l)?"
    AMOS = 30, "Amos", r"Amo\.*(?:s)?"
    OBADIAH = 31, "Obadiah", r"Oba\.*(?:d\.*(?:iah)?)?"
    JONAH = 32, "Jonah", r"Jonah|Jon\.*|Jnh\.*"
    MICAH = 33, "Micah", r"Mic\.*(?:ah)?"
    NAHUM = 34, "Nahum", r"(?<!Jo)Nah\.*(?:um)?"
    HABAKKUK = 35, "Habakkuk", r"Hab\.*(?:akkuk)?"
    ZEPHANIAH = 36, "Zephaniah", r"Zep\.*(?:h\.*(?:aniah)?)?"
    HAGGAI = 37, "Haggai", r"Hag\.*(?:gai)?"
    ZECHARIAH = 38, "Zechariah", r"Zec\.*(?:h\.*(?:ariah)?)?"
    MALACHI = 39, "Malachi", r"Mal\.*(?:achi)?"
    MATTHEW = 40, "Matthew", r"Mat\.*(?:t\.*(?:hew)?)?"
    MARK = 41, "Mark", r"Mark|Mar\.*|Mrk\.*"
    LUKE = 42, "Luke", r"Luk\.*(?:e)?"
    JOHN = 43, "John", rf"(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I)){JOHN_REGULAR_EXPRESSION}"
    ACTS = (
        44,
        "Acts",
        build_book_regular_expression(
            r"Act\.*(?:s)?",
            suffix="of the Apostles",
        ),
    )
    ROMANS = 45, "Romans", r"Rom\.*(?:ans)?"
    CORINTHIANS_1 = (
        46,
        "1 Corinthians",
        build_book_regular_expression(
            CORINTHIANS_REGULAR_EXPRESSION,
            prefix=FIRST_PAUL_EPISTLE,
        ),
    )
    CORINTHIANS_2 = (
        47,
        "2 Corinthians",
        build_book_regular_expression(
            CORINTHIANS_REGULAR_EXPRESSION,
            prefix=SECOND_PAUL_EPISTLE,
        ),
    )
    GALATIANS = 48, "Galatians", r"Gal\.*(?:atians)?"
    EPHESIANS = 49, "Ephesians", r"(?<!Z)Eph\.*(?:es\.*(?:ians)?)?"
    PHILIPPIANS = (
        50,
        "Philippians",
        r"Ph(?:(p\.*)|(?:il\.*(?!e\.*(?:m\.*(?:on)?)?)(?:ippians)?))",
    )
    COLOSSIANS = 51, "Colossians", r"Col\.*(?:ossians)?"
    THESSALONIANS_1 = (
        52,
        "1 Thessalonians",
        build_book_regular_expression(
            THESSALONIANS_REGULAR_EXPRESSION,
            prefix=FIRST_PAUL_EPISTLE,
        ),
    )
    THESSALONIANS_2 = (
        53,
        "2 Thessalonians",
        build_book_regular_expression(
            THESSALONIANS_REGULAR_EXPRESSION,
            prefix=SECOND_PAUL_EPISTLE,
        ),
    )
    TIMOTHY_1 = (
        54,
        "1 Timothy",
        build_book_regular_expression(
            TIMOTHY_REGULAR_EXPRESSION,
            prefix=FIRST_PAUL_EPISTLE,
        ),
    )
    TIMOTHY_2 = (
        55,
        "2 Timothy",
        build_book_regular_expression(
            TIMOTHY_REGULAR_EXPRESSION,
            prefix=SECOND_PAUL_EPISTLE,
        ),
    )
    TITUS = 56, "Titus", r"Tit\.*(?:us)?"
    PHILEMON = (
        57,
        "Philemon",
        r"(Philemon|Philem\.*|Phile\.*|Phlm\.*|Phi\.*(?!l)|Phm\.*)",
    )
    HEBREWS = 58, "Hebrews", r"Heb\.*(?:rews)?"
    JAMES = 59, "James", r"Ja(?:me)?s\.*"
    PETER_1 = (
        60,
        "1 Peter",
        build_book_regular_expression(
            PETER_REGULAR_EXPRESSION,
            prefix=FIRST_GENERAL_EPISTLE,
        ),
    )
    PETER_2 = (
        61,
        "2 Peter",
        build_book_regular_expression(
            PETER_REGULAR_EXPRESSION,
            prefix=SECOND_GENERAL_EPISTLE,
        ),
    )
    JOHN_1 = (
        62,
        "1 John",
        build_book_regular_expression(
            JOHN_REGULAR_EXPRESSION,
            prefix=FIRST_GENERAL_EPISTLE,
        ),
    )
    JOHN_2 = (
        63,
        "2 John",
        build_book_regular_expression(
            JOHN_REGULAR_EXPRESSION,
            prefix=SECOND_GENERAL_EPISTLE,
        ),
    )
    JOHN_3 = (
        64,
        "3 John",
        build_book_regular_expression(
            JOHN_REGULAR_EXPRESSION,
            prefix=THIRD_GENERAL_EPISTLE,
        ),
    )
    JUDE = 65, "Jude", r"Jud\.*(:?e)?(?!ges)"
    REVELATION = (
        66,
        "Revelation",
        build_book_regular_expression(
            r"Rev\.*(?:elation)?",
            suffix="of ((Jesus Christ)|John|(St. John the Divine))",
        ),
    )
    ESDRAS_1 = (
        67,
        "1 Esdras",
        build_book_regular_expression(
            r"(Esdras|Esdr\.*|Esd\.*|Es\.*)",
            FIRST,
        ),
    )
    TOBIT = 68, "Tobit", r"(Tobit|Tob\.*|Tb\.*)"
    WISDOM_OF_SOLOMON = (
        69,
        "Wisdom of Solomon",
        r"(Wisdom of Solomon|Wisdom|Wisd\.* of Sol\.*|Wis\.*|(?<!Hebre)Ws\.*)",
    )
    ECCLESIASTICUS = (
        70,
        "Ecclesiasticus",
        r"(Sirach|Sir\.*|Ecclesiasticus|Ecclus\.*)",
    )
    MACCABEES_1 = (
        71,
        "1 Maccabees",
        build_book_regular_expression(
            MACCABEES_REGULAR_EXPRESSION,
            FIRST,
        ),
    )
    MACCABEES_2 = (
        72,
        "2 Maccabees",
        build_book_regular_expression(
            MACCABEES_REGULAR_EXPRESSION,
            SECOND,
        ),
    )

    @property
    def title(self: Book) -> str:
        return self._title_

    @property
    def regular_expression(self: Book) -> str:
        return self._regular_expression_
