from enum import IntEnum
from typing import Dict


class Book(IntEnum):
    GENESIS = 1
    EXODUS = 2
    LEVITICUS = 3
    NUMBERS = 4
    DEUTERONOMY = 5
    JOSHUA = 6
    JUDGES = 7
    RUTH = 8
    SAMUEL_1 = 9
    SAMUEL_2 = 10
    KINGS_1 = 11
    KINGS_2 = 12
    CHRONICLES_1 = 13
    CHRONICLES_2 = 14
    EZRA = 15
    NEHEMIAH = 16
    ESTHER = 17
    JOB = 18
    PSALMS = 19
    PROVERBS = 20
    ECCLESIASTES = 21
    SONG_OF_SONGS = 22
    ISAIAH = 23
    JEREMIAH = 24
    LAMENTATIONS = 25
    EZEKIEL = 26
    DANIEL = 27
    HOSEA = 28
    JOEL = 29
    AMOS = 30
    OBADIAH = 31
    JONAH = 32
    MICAH = 33
    NAHUM = 34
    HABAKKUK = 35
    ZEPHANIAH = 36
    HAGGAI = 37
    ZECHARIAH = 38
    MALACHI = 39
    MATTHEW = 40
    MARK = 41
    LUKE = 42
    JOHN = 43
    ACTS = 44
    ROMANS = 45
    CORINTHIANS_1 = 46
    CORINTHIANS_2 = 47
    GALATIANS = 48
    EPHESIANS = 49
    PHILIPPIANS = 50
    COLOSSIANS = 51
    THESSALONIANS_1 = 52
    THESSALONIANS_2 = 53
    TIMOTHY_1 = 54
    TIMOTHY_2 = 55
    TITUS = 56
    PHILEMON = 57
    HEBREWS = 58
    JAMES = 59
    PETER_1 = 60
    PETER_2 = 61
    JOHN_1 = 62
    JOHN_2 = 63
    JOHN_3 = 64
    JUDE = 65
    REVELATION = 66
    ESDRAS_1 = 67
    TOBIT = 68
    WISDOM_OF_SOLOMON = 69
    ECCLESIASTICUS = 70
    MACCABEES_1 = 71
    MACCABEES_2 = 72

    @property
    def title(self) -> str:
        return _BOOK_TITLES.get(self, "")


_BOOK_TITLES: Dict[Book, str] = {
    Book.GENESIS: "Genesis",
    Book.EXODUS: "Exodus",
    Book.LEVITICUS: "Leviticus",
    Book.NUMBERS: "Numbers",
    Book.DEUTERONOMY: "Deuteronomy",
    Book.JOSHUA: "Joshua",
    Book.JUDGES: "Judges",
    Book.RUTH: "Ruth",
    Book.SAMUEL_1: "1 Samuel",
    Book.SAMUEL_2: "2 Samuel",
    Book.KINGS_1: "1 Kings",
    Book.KINGS_2: "2 Kings",
    Book.CHRONICLES_1: "1 Chronicles",
    Book.CHRONICLES_2: "2 Chronicles",
    Book.EZRA: "Ezra",
    Book.NEHEMIAH: "Nehemiah",
    Book.ESTHER: "Esther",
    Book.JOB: "Job",
    Book.PSALMS: "Psalms",
    Book.PROVERBS: "Proverbs",
    Book.ECCLESIASTES: "Ecclesiastes",
    Book.SONG_OF_SONGS: "Song of Songs",
    Book.ISAIAH: "Isaiah",
    Book.JEREMIAH: "Jeremiah",
    Book.LAMENTATIONS: "Lamentations",
    Book.EZEKIEL: "Ezekiel",
    Book.DANIEL: "Daniel",
    Book.HOSEA: "Hosea",
    Book.JOEL: "Joel",
    Book.AMOS: "Amos",
    Book.OBADIAH: "Obadiah",
    Book.JONAH: "Jonah",
    Book.MICAH: "Micah",
    Book.NAHUM: "Nahum",
    Book.HABAKKUK: "Habakkuk",
    Book.ZEPHANIAH: "Zephaniah",
    Book.HAGGAI: "Haggai",
    Book.ZECHARIAH: "Zechariah",
    Book.MALACHI: "Malachi",
    Book.MATTHEW: "Matthew",
    Book.MARK: "Mark",
    Book.LUKE: "Luke",
    Book.JOHN: "John",
    Book.ACTS: "Acts",
    Book.ROMANS: "Romans",
    Book.CORINTHIANS_1: "1 Corinthians",
    Book.CORINTHIANS_2: "2 Corinthians",
    Book.GALATIANS: "Galatians",
    Book.EPHESIANS: "Ephesians",
    Book.PHILIPPIANS: "Philippians",
    Book.COLOSSIANS: "Colossians",
    Book.THESSALONIANS_1: "1 Thessalonians",
    Book.THESSALONIANS_2: "2 Thessalonians",
    Book.TIMOTHY_1: "1 Timothy",
    Book.TIMOTHY_2: "2 Timothy",
    Book.TITUS: "Titus",
    Book.PHILEMON: "Philemon",
    Book.HEBREWS: "Hebrews",
    Book.JAMES: "James",
    Book.PETER_1: "1 Peter",
    Book.PETER_2: "2 Peter",
    Book.JOHN_1: "1 John",
    Book.JOHN_2: "2 John",
    Book.JOHN_3: "3 John",
    Book.JUDE: "Jude",
    Book.REVELATION: "Revelation",
    Book.ESDRAS_1: "1 Esdras",
    Book.TOBIT: "Tobit",
    Book.WISDOM_OF_SOLOMON: "Wisdom of Solomon",
    Book.ECCLESIASTICUS: "Ecclesiasticus",
    Book.MACCABEES_1: "1 Maccabees",
    Book.MACCABEES_2: "2 Maccabees",
}
