import re

from pythonbible.books import Book

# noinspection SpellCheckingInspection
BOOK_REGULAR_EXPRESSIONS = {
    Book.GENESIS: "Gen(?:esis)?",
    Book.EXODUS: "Exod(?:us)?",
    Book.LEVITICUS: "Lev(?:iticus)?",
    Book.NUMBERS: "Num(?:bers)?",
    Book.DEUTERONOMY: "Deut(?:eronomy)?",
    Book.JOSHUA: "Josh(?:ua)?",
    Book.JUDGES: "Judg(?:es)?",
    Book.RUTH: "Ruth",
    Book.SAMUEL_1: r"(?:1|I)(?:\s)?Sam(?:uel)?",
    Book.SAMUEL_2: r"(?:2|II)(?:\s)?Sam(?:uel)?",
    Book.KINGS_1: r"(?:1|I)(?:\s)?K(?:in)?gs",
    Book.KINGS_2: r"(?:2|II)(?:\s)?K(?:in)?gs",
    Book.CHRONICLES_1: r"(?:1|I)(?:\s)?Chr(?:o(?:n(?:icles)?)?)?",
    Book.CHRONICLES_2: r"(?:2|II)(?:\s)?Chr(?:o(?:n(?:icles)?)?)?",
    Book.EZRA: "Ezra",
    Book.NEHEMIAH: "Neh(?:emiah)?",
    Book.ESTHER: "Esth(?:er)?",
    Book.JOB: "Job",
    Book.PSALMS: "Ps(?:a)?(?:lm(?:s)?)?",
    Book.PROVERBS: "Prov(?:erbs)?",
    Book.ECCLESIASTES: "Ecc(?:l(?:es(?:iastes)?)?)?",
    Book.SONG_OF_SONGS: "Song(?: of Sol(?:omon)?)?",
    Book.ISAIAH: "Isa(?:iah)?",
    Book.JEREMIAH: "Jer(?:emiah)?",
    Book.LAMENTATIONS: "Lam(?:entations)?",
    Book.EZEKIEL: "Ezek(?:iel)?",
    Book.DANIEL: "Dan(?:iel)?",
    Book.HOSEA: "Hos(?:ea)?",
    Book.JOEL: "Joel",
    Book.AMOS: "Amos",
    Book.OBADIAH: "Obad(?:iah)?",
    Book.JONAH: "Jon(?:ah)?",
    Book.MICAH: "Mic(?:ah)?",
    Book.NAHUM: "Nah(?:um)?",
    Book.HABAKKUK: "Hab(?:akkuk)?",
    Book.ZEPHANIAH: "Zeph(?:aniah)?",
    Book.HAGGAI: "Hag(?:gai)?",
    Book.ZECHARIAH: "Zech(?:ariah)?",
    Book.MALACHI: "Mal(?:achi)?",
    Book.MATTHEW: "Matt(?:hew)?",
    Book.MARK: "Mark",
    Book.LUKE: "Luke",
    Book.JOHN: r"(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I))John",
    Book.ACTS: "Acts",
    Book.ROMANS: "Rom(?:ans)?",
    Book.CORINTHIANS_1: r"(?:1|I)(?:\s)?Cor(?:inthians)?",
    Book.CORINTHIANS_2: r"(?:2|II)(?:\s)?Cor(?:inthians)?",
    Book.GALATIANS: "Gal(?:atians)?",
    Book.EPHESIANS: "Eph(?:esians)?",
    Book.PHILIPPIANS: "Phil(?:ippians)?",
    Book.COLOSSIANS: "Col(?:ossians)?",
    Book.THESSALONIANS_1: r"(?:1|I)(?:\s)?Thess(?:alonians)?",
    Book.THESSALONIANS_2: r"(?:2|II)(?:\s)?Thess(?:alonians)?",
    Book.TIMOTHY_1: r"(?:1|I)(?:\s)?Tim(?:othy)?",
    Book.TIMOTHY_2: r"(?:2|II)(?:\s)?Tim(?:othy)?",
    Book.TITUS: "Tit(?:us)?",
    Book.PHILEMON: "Phlm|Phile(?:m(?:on)?)?",
    Book.HEBREWS: "Heb(?:rews)?",
    Book.JAMES: "Ja(?:me)?s",
    Book.PETER_1: r"(?:1|I)(?:\s)?Pet(?:er)?",
    Book.PETER_2: r"(?:2|II)(?:\s)?Pet(?:er)?",
    Book.JOHN_1: r"(?:(?:1|I)(?:\s)?)John",
    Book.JOHN_2: r"(?:(?:2|II)(?:\s)?)John",
    Book.JOHN_3: r"(?:(?:3|III)(?:\s)?)John",
    Book.JUDE: "Jude",
    Book.REVELATION: r"Rev(?:elation)?(?:\sof Jesus Christ)?",
    # Book.ESDRAS_1: None,
    # Book.TOBIT: None,
    # Book.WISDOM_OF_SOLOMON: None,
    # Book.ECCLESIASTICUS: None,
    # Book.MACCABEES_1: None,
    # Book.MACCABEES_2: None,
}

BOOK_REGEX = "|".join(BOOK_REGULAR_EXPRESSIONS.values())
CHAPTER_REGEX = r"(\d{1,3})"
VERSE_REGEX = r"(\d{1,3})"
CHAPTER_AND_VERSE_REGEX = fr"({CHAPTER_REGEX}(\s*:\s*{VERSE_REGEX})?)"
RANGE_REGEX = (
    fr"({CHAPTER_AND_VERSE_REGEX}(\s*-\s*({CHAPTER_REGEX}\s*:\s*)?{VERSE_REGEX})?)"
)
ADDITIONAL_REFERENCE_REGEX = fr"(\s*,\s*({RANGE_REGEX}|{VERSE_REGEX}))"
FULL_CHAPTER_AND_VERSE_REGEX = f"({RANGE_REGEX}({ADDITIONAL_REFERENCE_REGEX})*)"

SCRIPTURE_REFERENCE_REGULAR_EXPRESSION = re.compile(
    fr"({BOOK_REGEX})\s*({FULL_CHAPTER_AND_VERSE_REGEX})?", re.IGNORECASE | re.UNICODE
)
