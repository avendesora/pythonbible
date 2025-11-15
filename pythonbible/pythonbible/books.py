from __future__ import annotations

from enum import Enum
from typing import Any
from typing import Type


def _build_book_regular_expression(
    book: str,
    prefix: str | None = None,
    suffix: str | None = None,
) -> str:
    return _add_suffix(_add_prefix(book, prefix), suffix)


def _add_prefix(regex: str, prefix: str | None = None) -> str:
    return regex if prefix is None else rf"(?:{prefix})(?:\s)?{regex}"


def _add_suffix(regex: str, suffix: str | None = None) -> str:
    return regex if suffix is None else rf"{regex}(?:\s*{suffix})?"


_SAMUEL_REGULAR_EXPRESSION = r"(Samuel|Sam\.*|Sa\.*|Sm\.*)"
_KINGS_REGULAR_EXPRESSION = r"(Kings|Kgs\.*|Kin\.*|Ki\.*)"
_CHRONICLES_REGULAR_EXPRESSION = r"(Chronicles|Chron\.*|Chro\.*|Chr\.*|Ch\.*)"
_JOHN_REGULAR_EXPRESSION = r"(John|Joh\.*|Jhn\.*|Jo\.*(?!shua|b|nah|el)|Jn\.*)"
_CORINTHIANS_REGULAR_EXPRESSION = r"Co\.*(?:r\.*(?:inthians)?)?"
_THESSALONIANS_REGULAR_EXPRESSION = r"Th\.*(?:(s|(es(?:s)?))\.*(?:alonians)?)?"
_TIMOTHY_REGULAR_EXPRESSION = r"Ti\.*(?:m\.*(?:othy)?)?"
_PETER_REGULAR_EXPRESSION = r"(Pe\.*(?:t\.*(?:er)?)?|Pt\.*)"

_MACCABEES_REGULAR_EXPRESSION = r"(Maccabees|Macc\.*|Mac\.*|Ma\.*|M\.*)"

_FIRST = r"1|I\s+|1st\s+|First\s+"
_SECOND = r"2|II|2nd\s+|Second\s+"
_THIRD = r"3|III|3rd\s+|Third\s+"

_FIRST_BOOK = rf"{_FIRST}|(First\s+Book\s+of(?:\s+the)?)"
_SECOND_BOOK = rf"{_SECOND}|(Second\s+Book\s+of(?:\s+the)?)"

_EPISTLE_OF_PAUL_TO = r"Epistle\s+of\s+Paul\s+(?:the\s+Apostle\s+)?to(?:\s+the)?"
_GENERAL_EPISTLE_OF = r"(?:General\s+)?Epistle\s+(?:General\s+)?of"

_FIRST_PAUL_EPISTLE = rf"{_FIRST}|(First\s+{_EPISTLE_OF_PAUL_TO})"
_SECOND_PAUL_EPISTLE = rf"{_SECOND}|(Second\s+{_EPISTLE_OF_PAUL_TO})"

_FIRST_GENERAL_EPISTLE = rf"{_FIRST}|(First\s+{_GENERAL_EPISTLE_OF})"
_SECOND_GENERAL_EPISTLE = rf"{_SECOND}|(Second\s+{_GENERAL_EPISTLE_OF})"
_THIRD_GENERAL_EPISTLE = rf"{_THIRD}|(Third\s+{_GENERAL_EPISTLE_OF})"


class Book(Enum):
    """Book is an Enum that contains all the books of the Bible.

    :param name: the unique text identifier of the book
    :type name: str
    :param value: the unique numerical identifier of the book
    :type value: int
    :param title: the common English name of the book
    :type title: str
    :param regular_expression: the regular expression for the book
    :type regular_expression: str
    :param abbreviations: the allowed title abbreviations for the book
    :type abbreviations: tuple[str, ...]
    """

    def __new__(
        cls: Type[Book],
        *args: dict[str, Any],
        **kwargs: dict[str, Any],
    ) -> Book:
        obj: Book = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(
        self: Book,
        _: int,
        title: str,
        regular_expression: str,
        abbreviations: tuple[str, ...],
    ) -> None:
        """Set the title and regular_expression properties."""
        self._title_ = title
        self._regular_expression_ = regular_expression
        self._abbreviations_ = abbreviations

    @property
    def title(self: Book) -> str:
        return self._title_

    @property
    def regular_expression(self: Book) -> str:
        return self._regular_expression_

    @property
    def abbreviations(self: Book) -> tuple[str, ...]:
        return self._abbreviations_

    GENESIS = 1, "Genesis", r"Gen\.*(?:esis)?", ("Gen",)
    EXODUS = 2, "Exodus", r"Exo\.*(?:d\.*)?(?:us)?", ("Exo", "Exod")
    LEVITICUS = 3, "Leviticus", r"Lev\.*(?:iticus)?", ("Lev",)
    NUMBERS = 4, "Numbers", r"Num\.*(?:bers)?", ("Num",)
    DEUTERONOMY = 5, "Deuteronomy", r"Deu\.*(?:t\.*)?(?:eronomy)?", ("Deu", "Deut")
    JOSHUA = 6, "Joshua", r"(Joshua|Josh\.*|Jos\.*|Jsh\.*)", ("Jos", "Jsh", "Josh")
    JUDGES = 7, "Judges", r"(Judges|Judg\.*|Jdgs\.*|Jdg\.*)", ("Jdg", "Jdgs", "Judg")
    RUTH = 8, "Ruth", r"(Ruth|Rut\.*|Rth\.*)", ("Rth", "Rut")
    SAMUEL_1 = (
        9,
        "1 Samuel",
        _build_book_regular_expression(
            _SAMUEL_REGULAR_EXPRESSION,
            prefix=_FIRST_BOOK,
            suffix=r"Otherwise\s+Called\s+The\s+First\s+Book\s+of\s+the\s+Kings",
        ),
        ("Sa", "Sam", "Sm"),
    )
    SAMUEL_2 = (
        10,
        "2 Samuel",
        _build_book_regular_expression(
            _SAMUEL_REGULAR_EXPRESSION,
            prefix=_SECOND_BOOK,
            suffix=r"Otherwise\s+Called\s+The\s+Second\s+Book\s+of\s+the\s+Kings",
        ),
        ("Sa", "Sam", "Sm"),
    )
    KINGS_1 = (
        11,
        "1 Kings",
        _build_book_regular_expression(
            _KINGS_REGULAR_EXPRESSION,
            prefix=_FIRST_BOOK,
            suffix=r"\,\s+Commonly\s+Called\s+the\s+Third\s+Book\s+of\s+the\s+Kings",
        ),
        ("Kgs", "Ki", "Kin"),
    )
    KINGS_2 = (
        12,
        "2 Kings",
        _build_book_regular_expression(
            _KINGS_REGULAR_EXPRESSION,
            prefix=_SECOND_BOOK,
            suffix=r"\,\s+Commonly\s+Called\s+the\s+Fourth\s+Book\s+of\s+the\s+Kings",
        ),
        ("Kgs", "Ki", "Kin"),
    )
    CHRONICLES_1 = (
        13,
        "1 Chronicles",
        _build_book_regular_expression(
            _CHRONICLES_REGULAR_EXPRESSION,
            prefix=_FIRST_BOOK,
        ),
        ("Ch", "Chr", "Chro", "Chron"),
    )
    CHRONICLES_2 = (
        14,
        "2 Chronicles",
        _build_book_regular_expression(
            _CHRONICLES_REGULAR_EXPRESSION,
            prefix=_SECOND_BOOK,
        ),
        ("Ch", "Chr", "Chro", "Chron"),
    )
    EZRA = 15, "Ezra", r"Ezr\.*(?:a)?", ("Ezr",)
    NEHEMIAH = 16, "Nehemiah", r"Neh\.*(?:emiah)?", ("Neh",)
    ESTHER = 17, "Esther", r"Est\.*(?:h\.*)?(?:er)?", ("Est", "Esth")
    JOB = 18, "Job", "Job", ()
    PSALMS = (
        19,
        "Psalms",
        r"(Psalms|Psalm|Pslm\.*|Psa\.*|Psm\.*|Pss\.*|Ps\.*)",
        ("Ps", "Psa", "Pslm", "Psm", "Pss"),
    )
    PROVERBS = (
        20,
        "Proverbs",
        r"(Proverbs|Prov\.*|Pro\.*|Prv\.*)",
        ("Pro", "Prov", "Prv"),
    )
    ECCLESIASTES = (
        21,
        "Ecclesiastes",
        r"(Ecclesiastes(?:\s+or\,\s+the\s+Preacher)?"
        r"|Eccles\.*(?!iasticus?)"
        r"|Eccle\.*(?!siasticus?)"
        r"|Eccl\.*(?!esiasticus?)(?!us?)"
        r"|Ecc\.*(?!lesiasticus?)(?!lus?)"
        r"|(?<!Z)Ec\.*(?!clesiasticus?)(?!clus?)|Qoh\.*)",
        ("Ec", "Ecc", "Eccl", "Eccle", "Eccles", "Qoh"),
    )
    SONG_OF_SONGS = (
        22,
        "Song of Songs",
        r"(Song(?: of (Solomon|Songs|Sol\.*))?)"
        "|Canticles|(Canticle(?: of Canticles)?)|SOS|Cant",
        ("Cant", "Canticle", "Canticles", "Song", "Song of Sol", "SOS"),
    )
    ISAIAH = 23, "Isaiah", r"Isa\.*(?:iah)?", ("Isa",)
    JEREMIAH = 24, "Jeremiah", r"Jer\.*(?:emiah)?", ("Jer",)
    LAMENTATIONS = (
        25,
        "Lamentations",
        _build_book_regular_expression(
            r"Lam\.*(?:entations)?",
            suffix=r"of\s+Jeremiah",
        ),
        ("Lam",),
    )
    EZEKIEL = 26, "Ezekiel", r"(Ezekiel|Ezek\.*|Eze\.*|Ezk\.*)", ("Eze", "Ezek", "Ezk")
    DANIEL = 27, "Daniel", r"Dan\.*(?:iel)?", ("Dan",)
    HOSEA = 28, "Hosea", r"Hos\.*(?:ea)?", ("Hos",)
    JOEL = 29, "Joel", r"Joe\.*(?:l)?", ("Joe",)
    AMOS = 30, "Amos", r"Amo\.*(?:s)?", ("Amo",)
    OBADIAH = 31, "Obadiah", r"Oba\.*(?:d\.*(?:iah)?)?", ("Oba", "Obad")
    JONAH = 32, "Jonah", r"Jonah|Jon\.*|Jnh\.*", ("Jnh", "Jon")
    MICAH = 33, "Micah", r"Mic\.*(?:ah)?", ("Mic",)
    NAHUM = 34, "Nahum", r"(?<!Jo)Nah\.*(?:um)?", ("Nah",)
    HABAKKUK = 35, "Habakkuk", r"Hab\.*(?:akkuk)?", ("Hab",)
    ZEPHANIAH = 36, "Zephaniah", r"Zep\.*(?:h\.*(?:aniah)?)?", ("Zep", "Zeph")
    HAGGAI = 37, "Haggai", r"Hag\.*(?:gai)?", ("Hag",)
    ZECHARIAH = 38, "Zechariah", r"Zec\.*(?:h\.*(?:ariah)?)?", ("Zec", "Zech")
    MALACHI = 39, "Malachi", r"Mal\.*(?:achi)?", ("Mal",)
    MATTHEW = 40, "Matthew", r"Mat\.*(?:t\.*(?:hew)?)?", ("Mat", "Matt")
    MARK = 41, "Mark", r"Mark|Mar\.*|Mrk\.*", ("Mar", "Mrk")
    LUKE = 42, "Luke", r"Luk\.*(?:e)?", ("Luk",)
    JOHN = (
        43,
        "John",
        rf"(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I)){_JOHN_REGULAR_EXPRESSION}",
        ("Jhn", "Jn", "Jo", "Joh"),
    )
    ACTS = (
        44,
        "Acts",
        _build_book_regular_expression(
            r"Act\.*(?:s)?",
            suffix="of the Apostles",
        ),
        ("Act",),
    )
    ROMANS = 45, "Romans", r"Rom\.*(?:ans)?", ("Rom",)
    CORINTHIANS_1 = (
        46,
        "1 Corinthians",
        _build_book_regular_expression(
            _CORINTHIANS_REGULAR_EXPRESSION,
            prefix=_FIRST_PAUL_EPISTLE,
        ),
        ("Co", "Cor"),
    )
    CORINTHIANS_2 = (
        47,
        "2 Corinthians",
        _build_book_regular_expression(
            _CORINTHIANS_REGULAR_EXPRESSION,
            prefix=_SECOND_PAUL_EPISTLE,
        ),
        ("Co", "Cor"),
    )
    GALATIANS = 48, "Galatians", r"Gal\.*(?:atians)?", ("Gal",)
    EPHESIANS = 49, "Ephesians", r"(?<!Z)Eph\.*(?:es\.*(?:ians)?)?", ("Eph", "Ephes")
    PHILIPPIANS = (
        50,
        "Philippians",
        r"Ph(?:(p\.*)|(?:il\.*(?!e\.*(?:m\.*(?:on)?)?)(?:ippians)?))",
        ("Php", "Phil"),
    )
    COLOSSIANS = 51, "Colossians", r"Col\.*(?:ossians)?", ("Col",)
    THESSALONIANS_1 = (
        52,
        "1 Thessalonians",
        _build_book_regular_expression(
            _THESSALONIANS_REGULAR_EXPRESSION,
            prefix=_FIRST_PAUL_EPISTLE,
        ),
        ("Th", "Thes", "Thess", "Ths"),
    )
    THESSALONIANS_2 = (
        53,
        "2 Thessalonians",
        _build_book_regular_expression(
            _THESSALONIANS_REGULAR_EXPRESSION,
            prefix=_SECOND_PAUL_EPISTLE,
        ),
        ("Th", "Thes", "Thess", "Ths"),
    )
    TIMOTHY_1 = (
        54,
        "1 Timothy",
        _build_book_regular_expression(
            _TIMOTHY_REGULAR_EXPRESSION,
            prefix=_FIRST_PAUL_EPISTLE,
        ),
        ("Ti", "Tim"),
    )
    TIMOTHY_2 = (
        55,
        "2 Timothy",
        _build_book_regular_expression(
            _TIMOTHY_REGULAR_EXPRESSION,
            prefix=_SECOND_PAUL_EPISTLE,
        ),
        ("Ti", "Tim"),
    )
    TITUS = 56, "Titus", r"Tit\.*(?:us)?", ("Tit",)
    PHILEMON = (
        57,
        "Philemon",
        r"(Philemon|Philem\.*|Phile\.*|Phlm\.*|Phi\.*(?!l)|Phm\.*)",
        ("Phi", "Phile", "Philem", "Phlm", "Phm"),
    )
    HEBREWS = 58, "Hebrews", r"Heb\.*(?:rews)?", ("Heb",)
    JAMES = 59, "James", r"Ja(?:me)?s\.*", ("Jas",)
    PETER_1 = (
        60,
        "1 Peter",
        _build_book_regular_expression(
            _PETER_REGULAR_EXPRESSION,
            prefix=_FIRST_GENERAL_EPISTLE,
        ),
        ("Pe", "Pet", "Pt"),
    )
    PETER_2 = (
        61,
        "2 Peter",
        _build_book_regular_expression(
            _PETER_REGULAR_EXPRESSION,
            prefix=_SECOND_GENERAL_EPISTLE,
        ),
        ("Pe", "Pet", "Pt"),
    )
    JOHN_1 = (
        62,
        "1 John",
        _build_book_regular_expression(
            _JOHN_REGULAR_EXPRESSION,
            prefix=_FIRST_GENERAL_EPISTLE,
        ),
        ("Jhn", "Jn", "Jo", "Joh"),
    )
    JOHN_2 = (
        63,
        "2 John",
        _build_book_regular_expression(
            _JOHN_REGULAR_EXPRESSION,
            prefix=_SECOND_GENERAL_EPISTLE,
        ),
        ("Jhn", "Jn", "Jo", "Joh"),
    )
    JOHN_3 = (
        64,
        "3 John",
        _build_book_regular_expression(
            _JOHN_REGULAR_EXPRESSION,
            prefix=_THIRD_GENERAL_EPISTLE,
        ),
        ("Jhn", "Jn", "Jo", "Joh"),
    )
    JUDE = 65, "Jude", r"Jud\.*(:?e)?(?!ges)", ("Jud",)
    REVELATION = (
        66,
        "Revelation",
        _build_book_regular_expression(
            r"Rev\.*(?:elation)?",
            suffix="of ((Jesus Christ)|John|(St. John the Divine))",
        ),
        ("Rev",),
    )
    ESDRAS_1 = (
        67,
        "1 Esdras",
        _build_book_regular_expression(
            r"(Esdras|Esdr\.*|Esd\.*|Es\.*)",
            _FIRST,
        ),
        ("Es", "Esd", "Esdr"),
    )
    TOBIT = 68, "Tobit", r"(Tobit|Tob\.*|Tb\.*)", ("Tb", "Tob")
    WISDOM_OF_SOLOMON = (
        69,
        "Wisdom of Solomon",
        r"(Wisdom of Solomon|Wisdom|Wisd\.* of Sol\.*|Wis\.*|(?<!Hebre)Ws\.*)",
        ("Wis", "Wisd of Sol", "Ws"),
    )
    ECCLESIASTICUS = (
        70,
        "Ecclesiasticus",
        r"(Sirach|Sir\.*|Ecclesiasticus|Ecclus\.*)",
        ("Ecclus", "Sir"),
    )
    MACCABEES_1 = (
        71,
        "1 Maccabees",
        _build_book_regular_expression(
            _MACCABEES_REGULAR_EXPRESSION,
            _FIRST,
        ),
        ("M", "Ma", "Mac", "Macc"),
    )
    MACCABEES_2 = (
        72,
        "2 Maccabees",
        _build_book_regular_expression(
            _MACCABEES_REGULAR_EXPRESSION,
            _SECOND,
        ),
        ("M", "Ma", "Mac", "Macc"),
    )
