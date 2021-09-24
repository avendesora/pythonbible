try:
    import regex as re
except ModuleNotFoundError:
    import re


from typing import Dict, Pattern

from pythonbible.books import Book


def build_book_regular_expression(
    book: str, prefix: str = None, suffix: str = None
) -> str:
    return _add_suffix(_add_prefix(book, prefix), suffix)


def _add_prefix(regex: str, prefix: str = None) -> str:
    return regex if prefix is None else fr"(?:{prefix})(?:\s)?{regex}"


def _add_suffix(regex: str, suffix: str = None) -> str:
    return regex if suffix is None else fr"{regex}(?:\s*{suffix})?"


SAMUEL_REGULAR_EXPRESSION = r"Sam\.*(?:uel)?"
KINGS_REGULAR_EXPRESSION = r"K(?:in)?gs\.*"
# noinspection SpellCheckingInspection
CHRONICLES_REGULAR_EXPRESSION = r"Chr\.*(?:o\.*(?:n\.*(?:icles)?)?)?"
JOHN_REGULAR_EXPRESSION = r"Joh\.*(?:n)?"
# noinspection SpellCheckingInspection
CORINTHIANS_REGULAR_EXPRESSION = r"Cor\.*(?:inthians)?"
# noinspection SpellCheckingInspection
THESSALONIANS_REGULAR_EXPRESSION = r"Th\.*(?:e\.*)?(?:ss\.*(?:alonians)?)?"
# noinspection SpellCheckingInspection
TIMOTHY_REGULAR_EXPRESSION = r"Tim\.*(?:othy)?"
PETER_REGULAR_EXPRESSION = r"Pet\.*(?:er)?"

FIRST = "1|I"
SECOND = "2|II"
THIRD = "3|III"

FIRST_BOOK = fr"{FIRST}|(First\s+Book\s+of(?:\s+the)?)"
SECOND_BOOK = fr"{SECOND}|(Second\s+Book\s+of(?:\s+the)?)"

EPISTLE_OF_PAUL_TO = r"Epistle\s+of\s+Paul\s+(?:the\s+Apostle\s+)?to(?:\s+the)?"
GENERAL_EPISTLE_OF = r"(?:General\s+)?Epistle\s+(?:General\s+)?of"

FIRST_PAUL_EPISTLE = fr"{FIRST}|(First\s+{EPISTLE_OF_PAUL_TO})"
SECOND_PAUL_EPISTLE = fr"{SECOND}|(Second\s+{EPISTLE_OF_PAUL_TO})"

FIRST_GENERAL_EPISTLE = fr"{FIRST}|(First\s+{GENERAL_EPISTLE_OF})"
SECOND_GENERAL_EPISTLE = fr"{SECOND}|(Second\s+{GENERAL_EPISTLE_OF})"
THIRD_GENERAL_EPISTLE = fr"{THIRD}|(Third\s+{GENERAL_EPISTLE_OF})"

# noinspection SpellCheckingInspection
BOOK_REGULAR_EXPRESSIONS: Dict[Book, str] = {
    Book.GENESIS: r"Gen\.*(?:esis)?",
    Book.EXODUS: r"Exo\.*(?:d\.*)?(?:us)?",
    Book.LEVITICUS: r"Lev\.*(?:iticus)?",
    Book.NUMBERS: r"Num\.*(?:bers)?",
    Book.DEUTERONOMY: r"Deu\.*(?:t\.*)?(?:eronomy)?",
    Book.JOSHUA: r"Jos\.*(?:h\.*(?:ua)?)?",
    Book.JUDGES: r"J\.*(?:(?:dg)|(?:udg\.*(?:es)?))",
    Book.RUTH: r"Rut\.*(?:h)?",
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
    Book.PSALMS: r"Ps\.*(?:a\.*)?(?:lm(?:s)?)?",
    Book.PROVERBS: r"Pro\.*(?:v\.*)?(?:erbs)?",
    Book.ECCLESIASTES: build_book_regular_expression(
        r"Ecc\.*(?:l\.*(?:es\.*(?:iastes)?)?)?", suffix=r"or\,\s+the\s+Preacher"
    ),
    Book.SONG_OF_SONGS: build_book_regular_expression(
        "Song", suffix=r"of ((Sol\.*(?:omon)?)|Songs)"
    ),
    Book.ISAIAH: r"Isa\.*(?:iah)?",
    Book.JEREMIAH: r"Jer\.*(?:emiah)?",
    Book.LAMENTATIONS: build_book_regular_expression(
        r"Lam\.*(?:entations)?", suffix=r"of\s+Jeremiah"
    ),
    Book.EZEKIEL: r"Eze\.*(?:k\.*(?:iel)?)?",
    Book.DANIEL: r"Dan\.*(?:iel)?",
    Book.HOSEA: r"Hos\.*(?:ea)?",
    Book.JOEL: r"Joe\.*(?:l)?",
    Book.AMOS: r"Amo\.*(?:s)?",
    Book.OBADIAH: r"Oba\.*(?:d\.*(?:iah)?)?",
    Book.JONAH: r"Jon\.*(?:ah)?",
    Book.MICAH: r"Mic\.*(?:ah)?",
    Book.NAHUM: r"Nah\.*(?:um)?",
    Book.HABAKKUK: r"Hab\.*(?:akkuk)?",
    Book.ZEPHANIAH: r"Zep\.*(?:h\.*(?:aniah)?)?",
    Book.HAGGAI: r"Hag\.*(?:gai)?",
    Book.ZECHARIAH: r"Zec\.*(?:h\.*(?:ariah)?)?",
    Book.MALACHI: r"Mal\.*(?:achi)?",
    Book.MATTHEW: r"Mat\.*(?:t\.*(?:hew)?)?",
    Book.MARK: r"Mar\.*(?:k)?",
    Book.LUKE: r"Luk\.*(?:e)?",
    Book.JOHN: r"(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I))"+JOHN_REGULAR_EXPRESSION,
    Book.ACTS: build_book_regular_expression(r"Act\.*(?:s)?", suffix="of the Apostles"),
    Book.ROMANS: r"Rom\.*(?:ans)?",
    Book.CORINTHIANS_1: build_book_regular_expression(
        CORINTHIANS_REGULAR_EXPRESSION, prefix=FIRST_PAUL_EPISTLE
    ),
    Book.CORINTHIANS_2: build_book_regular_expression(
        CORINTHIANS_REGULAR_EXPRESSION, prefix=SECOND_PAUL_EPISTLE
    ),
    Book.GALATIANS: r"Gal\.*(?:atians)?",
    Book.EPHESIANS: r"Eph\.*(?:esians)?",
    Book.PHILIPPIANS: r"Ph(?:p|(?:il\.*(?!e\.*(?:m\.*(?:on)?)?)(?:ippians)?))",
    Book.COLOSSIANS: r"Col\.*(?:ossians)?",
    Book.THESSALONIANS_1: build_book_regular_expression(
        THESSALONIANS_REGULAR_EXPRESSION, prefix=FIRST_PAUL_EPISTLE
    ),
    Book.THESSALONIANS_2: build_book_regular_expression(
        THESSALONIANS_REGULAR_EXPRESSION, prefix=SECOND_PAUL_EPISTLE
    ),
    Book.TIMOTHY_1: build_book_regular_expression(
        TIMOTHY_REGULAR_EXPRESSION, prefix=FIRST_PAUL_EPISTLE
    ),
    Book.TIMOTHY_2: build_book_regular_expression(
        TIMOTHY_REGULAR_EXPRESSION, prefix=SECOND_PAUL_EPISTLE
    ),
    Book.TITUS: r"Tit\.*(?:us)?",
    # assume 'Phi' is Philemon if Philippians failed?
    Book.PHILEMON: r"(Phi|Phlm|Phile)\.*(?:m\.*(?:on)?)?", 
    Book.HEBREWS: r"Heb\.*(?:rews)?",
    Book.JAMES: r"Ja(?:me)?s\.*",
    Book.PETER_1: build_book_regular_expression(
        PETER_REGULAR_EXPRESSION, prefix=FIRST_GENERAL_EPISTLE
    ),
    Book.PETER_2: build_book_regular_expression(
        PETER_REGULAR_EXPRESSION, prefix=SECOND_GENERAL_EPISTLE
    ),
    Book.JOHN_1: build_book_regular_expression(
        JOHN_REGULAR_EXPRESSION, prefix=FIRST_GENERAL_EPISTLE
    ),
    Book.JOHN_2: build_book_regular_expression(
        JOHN_REGULAR_EXPRESSION, prefix=SECOND_GENERAL_EPISTLE
    ),
    Book.JOHN_3: build_book_regular_expression(
        JOHN_REGULAR_EXPRESSION, prefix=THIRD_GENERAL_EPISTLE
    ),
    Book.JUDE: r"Jud\.*(:?e)?",
    Book.REVELATION: build_book_regular_expression(
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
    fr"\b{value}\b\.?" for value in BOOK_REGULAR_EXPRESSIONS.values()
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
