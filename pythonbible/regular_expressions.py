import re
from typing import Dict, Pattern

from pythonbible.book_groups import BookGroup
from pythonbible.books import Book


def build_book_regex(book: str, prefix: str = None, suffix: str = None) -> str:
    return _add_suffix(_add_prefix(book, prefix), suffix)


def _add_prefix(regex: str, prefix: str = None) -> str:
    return regex if prefix is None else fr"(?:{prefix})(?:\s)?{regex}"


def _add_suffix(regex: str, suffix: str = None) -> str:
    return regex if suffix is None else fr"{regex}(?:\s*{suffix})?"


SAMUEL_REGEX = r"Sam\.*(?:uel)?"
KINGS_REGEX = r"K(?:in)?gs\.*"
# noinspection SpellCheckingInspection
CHRONICLES_REGEX = r"Chr\.*(?:o\.*(?:n\.*(?:icles)?)?)?"
# noinspection SpellCheckingInspection
CORINTHIANS_REGEX = r"Cor\.*(?:inthians)?"
# noinspection SpellCheckingInspection
THESSALONIANS_REGEX = r"Thess\.*(?:alonians)?"
# noinspection SpellCheckingInspection
TIMOTHY_REGEX = r"Tim\.*(?:othy)?"
PETER_REGEX = r"Pet\.*(?:er)?"

FIRST_REGEX = "1|I"
SECOND_REGEX = "2|II"
THIRD_REGEX = "3|III"

FIRST_BOOK = fr"{FIRST_REGEX}|(First\s+Book\s+of(?:\s+the)?)"
SECOND_BOOK = fr"{SECOND_REGEX}|(Second\s+Book\s+of(?:\s+the)?)"

EPISTLE_OF_PAUL_TO = r"Epistle\s+of\s+Paul\s+(?:the\s+Apostle\s+)?to(?:\s+the)?"
GENERAL_EPISTLE_OF = r"(?:General\s+)?Epistle\s+(?:General\s+)?of"

FIRST_PAUL_EPISTLE = fr"{FIRST_REGEX}|(First\s+{EPISTLE_OF_PAUL_TO})"
SECOND_PAUL_EPISTLE = fr"{SECOND_REGEX}|(Second\s+{EPISTLE_OF_PAUL_TO})"

FIRST_GENERAL_EPISTLE = fr"{FIRST_REGEX}|(First\s+{GENERAL_EPISTLE_OF})"
SECOND_GENERAL_EPISTLE = fr"{SECOND_REGEX}|(Second\s+{GENERAL_EPISTLE_OF})"
THIRD_GENERAL_EPISTLE = fr"{THIRD_REGEX}|(Third\s+{GENERAL_EPISTLE_OF})"


# noinspection SpellCheckingInspection
BOOK_REGULAR_EXPRESSIONS: Dict[Book, str] = {
    Book.GENESIS: r"Gen\.*(?:esis)?",
    Book.EXODUS: r"Exod\.*(?:us)?",
    Book.LEVITICUS: r"Lev\.*(?:iticus)?",
    Book.NUMBERS: r"Num\.*(?:bers)?",
    Book.DEUTERONOMY: r"Deut\.*(?:eronomy)?",
    Book.JOSHUA: r"Josh\.*(?:ua)?",
    Book.JUDGES: r"Judg\.*(?:es)?",
    Book.RUTH: "Ruth",
    Book.SAMUEL_1: build_book_regex(
        SAMUEL_REGEX,
        prefix=FIRST_BOOK,
        suffix=fr"Otherwise\s+Called\s+The\s+First\s+Book\s+of\s+the\s+Kings",
    ),
    Book.SAMUEL_2: build_book_regex(
        SAMUEL_REGEX,
        prefix=SECOND_BOOK,
        suffix=fr"Otherwise\s+Called\s+The\s+Second\s+Book\s+of\s+the\s+Kings",
    ),
    Book.KINGS_1: build_book_regex(
        KINGS_REGEX,
        prefix=FIRST_BOOK,
        suffix=fr"\,\s+Commonly\s+Called\s+the\s+Third\s+Book\s+of\s+the\s+Kings",
    ),
    Book.KINGS_2: build_book_regex(
        KINGS_REGEX,
        prefix=SECOND_BOOK,
        suffix=fr"\,\s+Commonly\s+Called\s+the\s+Fourth\s+Book\s+of\s+the\s+Kings",
    ),
    Book.CHRONICLES_1: build_book_regex(
        CHRONICLES_REGEX,
        prefix=FIRST_BOOK,
    ),
    Book.CHRONICLES_2: build_book_regex(
        CHRONICLES_REGEX,
        prefix=SECOND_BOOK,
    ),
    Book.EZRA: "Ezra",
    Book.NEHEMIAH: r"Neh\.*(?:emiah)?",
    Book.ESTHER: r"Esth\.*(?:er)?",
    Book.JOB: "Job",
    Book.PSALMS: r"Ps\.*(?:a\.*)?(?:lm(?:s)?)?",
    Book.PROVERBS: r"Prov\.*(?:erbs)?",
    Book.ECCLESIASTES: build_book_regex(
        r"Ecc\.*(?:l\.*(?:es\.*(?:iastes)?)?)?", suffix=r"or\,\s+the\s+Preacher"
    ),
    Book.SONG_OF_SONGS: build_book_regex(
        "Song", suffix=r"of ((Sol\.*(?:omon)?)|Songs)"
    ),
    Book.ISAIAH: r"Isa\.*(?:iah)?",
    Book.JEREMIAH: r"Jer\.*(?:emiah)?",
    Book.LAMENTATIONS: build_book_regex(
        r"Lam\.*(?:entations)?", suffix=r"of\s+Jeremiah"
    ),
    Book.EZEKIEL: r"Ezek\.*(?:iel)?",
    Book.DANIEL: r"Dan\.*(?:iel)?",
    Book.HOSEA: r"Hos\.*(?:ea)?",
    Book.JOEL: "Joel",
    Book.AMOS: "Amos",
    Book.OBADIAH: r"Obad\.*(?:iah)?",
    Book.JONAH: r"Jon\.*(?:ah)?",
    Book.MICAH: r"Mic\.*(?:ah)?",
    Book.NAHUM: r"Nah\.*(?:um)?",
    Book.HABAKKUK: r"Hab\.*(?:akkuk)?",
    Book.ZEPHANIAH: r"Zeph\.*(?:aniah)?",
    Book.HAGGAI: r"Hag\.*(?:gai)?",
    Book.ZECHARIAH: r"Zech\.*(?:ariah)?",
    Book.MALACHI: r"Mal\.*(?:achi)?",
    Book.MATTHEW: r"Matt\.*(?:hew)?",
    Book.MARK: "Mark",
    Book.LUKE: "Luke",
    Book.JOHN: r"(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I))John",
    Book.ACTS: build_book_regex("Acts", suffix="of the Apostles"),
    Book.ROMANS: r"Rom\.*(?:ans)?",
    Book.CORINTHIANS_1: build_book_regex(CORINTHIANS_REGEX, prefix=FIRST_PAUL_EPISTLE),
    Book.CORINTHIANS_2: build_book_regex(CORINTHIANS_REGEX, prefix=SECOND_PAUL_EPISTLE),
    Book.GALATIANS: r"Gal\.*(?:atians)?",
    Book.EPHESIANS: r"Eph\.*(?:esians)?",
    Book.PHILIPPIANS: r"Phil\.*(?!emon)(?:ippians)?",
    Book.COLOSSIANS: r"Col\.*(?:ossians)?",
    Book.THESSALONIANS_1: build_book_regex(
        THESSALONIANS_REGEX, prefix=FIRST_PAUL_EPISTLE
    ),
    Book.THESSALONIANS_2: build_book_regex(
        THESSALONIANS_REGEX, prefix=SECOND_PAUL_EPISTLE
    ),
    Book.TIMOTHY_1: build_book_regex(TIMOTHY_REGEX, prefix=FIRST_PAUL_EPISTLE),
    Book.TIMOTHY_2: build_book_regex(TIMOTHY_REGEX, prefix=SECOND_PAUL_EPISTLE),
    Book.TITUS: r"Tit\.*(?:us)?",
    Book.PHILEMON: r"(Phlm|Phile)\.*(?:m(?:on)?)?",
    Book.HEBREWS: r"Heb\.*(?:rews)?",
    Book.JAMES: r"Ja(?:me)?s\.*",
    Book.PETER_1: build_book_regex(PETER_REGEX, prefix=FIRST_GENERAL_EPISTLE),
    Book.PETER_2: build_book_regex(PETER_REGEX, prefix=SECOND_GENERAL_EPISTLE),
    Book.JOHN_1: build_book_regex("John", prefix=FIRST_GENERAL_EPISTLE),
    Book.JOHN_2: build_book_regex("John", prefix=SECOND_GENERAL_EPISTLE),
    Book.JOHN_3: build_book_regex("John", prefix=THIRD_GENERAL_EPISTLE),
    Book.JUDE: "Jude",
    Book.REVELATION: build_book_regex(
        r"Rev\.*(?:elation)?", suffix="of ((Jesus Christ)|John|(St. John the Divine))"
    ),
    # Book.ESDRAS_1: None,
    # Book.TOBIT: None,
    # Book.WISDOM_OF_SOLOMON: None,
    # Book.ECCLESIASTICUS: None,
    # Book.MACCABEES_1: None,
    # Book.MACCABEES_2: None,
}

BOOK_REGEX: str = "|".join(
    [fr"\b{value}\b\.?" for value in BOOK_REGULAR_EXPRESSIONS.values()]
)
CHAPTER_REGEX: str = r"(\d{1,3})"
CHAPTER_VERSE_SEPARATOR: str = r"([:.])"
VERSE_REGEX: str = r"(\d{1,3})"
CHAPTER_AND_VERSE_REGEX: str = (
    fr"({CHAPTER_REGEX}(\s*{CHAPTER_VERSE_SEPARATOR}\s*{VERSE_REGEX})?)"
)
RANGE_REGEX: str = fr"({CHAPTER_AND_VERSE_REGEX}(\s*-\s*({CHAPTER_REGEX}\s*{CHAPTER_VERSE_SEPARATOR}\s*)?{VERSE_REGEX})?)"
ADDITIONAL_REFERENCE_REGEX: str = fr"(\s*,\s*({RANGE_REGEX}|{VERSE_REGEX}))"
FULL_CHAPTER_AND_VERSE_REGEX: str = f"({RANGE_REGEX}({ADDITIONAL_REFERENCE_REGEX})*)"

FULL_BOOK_REGEX = fr"({BOOK_REGEX})\s*({FULL_CHAPTER_AND_VERSE_REGEX})?"
CROSS_BOOK_REGEX = fr"({FULL_BOOK_REGEX}(\s*-\s*({FULL_BOOK_REGEX}))?)"

SCRIPTURE_REFERENCE_REGULAR_EXPRESSION: Pattern[str] = re.compile(
    CROSS_BOOK_REGEX, re.IGNORECASE | re.UNICODE
)

BOOK_GROUP_REGULAR_EXPRESSIONS: Dict[BookGroup, str] = {
    BookGroup.OLD_TESTAMENT: "Old Testament",
    BookGroup.OLD_TESTAMENT_LAW: "Law",
    BookGroup.OLD_TESTAMENT_HISTORY: "History",
    BookGroup.OLD_TESTAMENT_POETRY_WISDOM: "Poetry|Wisdom",
    BookGroup.OLD_TESTAMENT_MAJOR_PROPHETS: "Major Prophets",
    BookGroup.OLD_TESTAMENT_MINOR_PROPHETS: "Minor Prophets",
    BookGroup.OLD_TESTAMENT_PROPHECY: "Prophecy",
    BookGroup.NEW_TESTAMENT: "New Testament",
    BookGroup.NEW_TESTAMENT_GOSPELS: "Gospels",
    BookGroup.NEW_TESTAMENT_HISTORY: "History",
    BookGroup.NEW_TESTAMENT_PAUL_EPISTLES: "Pauline Epistles|Paul's Epistles|Epistles of Paul",
    BookGroup.NEW_TESTAMENT_GENERAL_EPISTLES: "General Epistles",
    BookGroup.NEW_TESTAMENT_EPISTLES: "Epistles",
    BookGroup.NEW_TESTAMENT_APOCALYPTIC: "Apocalyptic",
}

BOOK_GROUP_REGEX: str = "|".join(BOOK_GROUP_REGULAR_EXPRESSIONS.values())

BOOK_GROUP_REGULAR_EXPRESSION: Pattern[str] = re.compile(
    fr"{BOOK_GROUP_REGEX}", re.IGNORECASE | re.UNICODE
)
