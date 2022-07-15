from __future__ import annotations

from enum import Enum, auto
from types import MappingProxyType

from pythonbible.books import Book


class BookGroup(Enum):
    """
    BookGroup is an ``Enum`` containing the default Bible book groupings.

    :param name: the unique text identifier of the book group
    :type name: str
    :param value: the unique numerical identifier of the book group
    :type value: int
    :param regular_expression: the regular expression used to find mentions of the
                               book group when searching for references
    :type regular_expression: str
    :param books: the list of books included in the book group
    :type books: tuple[Book, ...]
    """

    OLD_TESTAMENT = auto()
    OLD_TESTAMENT_LAW = auto()
    OLD_TESTAMENT_HISTORY = auto()
    OLD_TESTAMENT_POETRY_WISDOM = auto()
    OLD_TESTAMENT_PROPHECY = auto()
    OLD_TESTAMENT_MAJOR_PROPHETS = auto()
    OLD_TESTAMENT_MINOR_PROPHETS = auto()
    NEW_TESTAMENT = auto()
    NEW_TESTAMENT_GOSPELS = auto()
    NEW_TESTAMENT_HISTORY = auto()
    NEW_TESTAMENT_EPISTLES = auto()
    NEW_TESTAMENT_PAUL_EPISTLES = auto()
    NEW_TESTAMENT_GENERAL_EPISTLES = auto()
    NEW_TESTAMENT_APOCALYPTIC = auto()

    @property
    def books(self: BookGroup) -> tuple[Book, ...]:
        return _BOOK_GROUP_BOOKS.get(self, ())

    @property
    def regular_expression(self: BookGroup) -> str:
        return _BOOK_GROUP_REGULAR_EXPRESSIONS.get(self, "")


_OLD_TESTAMENT_LAW_BOOKS: tuple[Book, ...] = (
    Book.GENESIS,
    Book.EXODUS,
    Book.LEVITICUS,
    Book.NUMBERS,
    Book.DEUTERONOMY,
)

_OLD_TESTAMENT_HISTORY_BOOKS: tuple[Book, ...] = (
    Book.JOSHUA,
    Book.JUDGES,
    Book.RUTH,
    Book.SAMUEL_1,
    Book.SAMUEL_2,
    Book.KINGS_1,
    Book.KINGS_2,
    Book.CHRONICLES_1,
    Book.CHRONICLES_2,
    Book.EZRA,
    Book.NEHEMIAH,
    Book.ESTHER,
)

_OLD_TESTAMENT_POETRY_WISDOM_BOOKS: tuple[Book, ...] = (
    Book.JOB,
    Book.PSALMS,
    Book.PROVERBS,
    Book.ECCLESIASTES,
    Book.SONG_OF_SONGS,
)

_OLD_TESTAMENT_MAJOR_PROPHETS_BOOKS: tuple[Book, ...] = (
    Book.ISAIAH,
    Book.JEREMIAH,
    Book.LAMENTATIONS,
    Book.EZEKIEL,
    Book.DANIEL,
)

_OLD_TESTAMENT_MINOR_PROPHETS_BOOKS: tuple[Book, ...] = (
    Book.HOSEA,
    Book.JOEL,
    Book.AMOS,
    Book.OBADIAH,
    Book.JONAH,
    Book.MICAH,
    Book.NAHUM,
    Book.HABAKKUK,
    Book.ZEPHANIAH,
    Book.HAGGAI,
    Book.ZECHARIAH,
    Book.MALACHI,
)

_OLD_TESTAMENT_PROPHECY_BOOKS: tuple[Book, ...] = (
    _OLD_TESTAMENT_MAJOR_PROPHETS_BOOKS + _OLD_TESTAMENT_MINOR_PROPHETS_BOOKS
)

_OLD_TESTAMENT_BOOKS: tuple[Book, ...] = (
    _OLD_TESTAMENT_LAW_BOOKS
    + _OLD_TESTAMENT_HISTORY_BOOKS
    + _OLD_TESTAMENT_POETRY_WISDOM_BOOKS
    + _OLD_TESTAMENT_PROPHECY_BOOKS
)

_NEW_TESTAMENT_GOSPELS_BOOKS: tuple[Book, ...] = (
    Book.MATTHEW,
    Book.MARK,
    Book.LUKE,
    Book.JOHN,
)

_NEW_TESTAMENT_HISTORY_BOOKS: tuple[Book, ...] = (Book.ACTS,)

_NEW_TESTAMENT_PAUL_EPISTLES_BOOKS: tuple[Book, ...] = (
    Book.ROMANS,
    Book.CORINTHIANS_1,
    Book.CORINTHIANS_2,
    Book.GALATIANS,
    Book.EPHESIANS,
    Book.PHILIPPIANS,
    Book.COLOSSIANS,
    Book.THESSALONIANS_1,
    Book.THESSALONIANS_2,
    Book.TIMOTHY_1,
    Book.TIMOTHY_2,
    Book.TITUS,
    Book.PHILEMON,
)

_NEW_TESTAMENT_GENERAL_EPISTLES_BOOKS: tuple[Book, ...] = (
    Book.HEBREWS,
    Book.JAMES,
    Book.PETER_1,
    Book.PETER_2,
    Book.JOHN_1,
    Book.JOHN_2,
    Book.JOHN_3,
    Book.JUDE,
)

_NEW_TESTAMENT_EPISTLES_BOOKS: tuple[Book, ...] = (
    _NEW_TESTAMENT_PAUL_EPISTLES_BOOKS + _NEW_TESTAMENT_GENERAL_EPISTLES_BOOKS
)

_NEW_TESTAMENT_APOCALYPTIC_BOOKS: tuple[Book, ...] = (Book.REVELATION,)

_NEW_TESTAMENT_BOOKS: tuple[Book, ...] = (
    _NEW_TESTAMENT_GOSPELS_BOOKS
    + _NEW_TESTAMENT_HISTORY_BOOKS
    + _NEW_TESTAMENT_EPISTLES_BOOKS
    + _NEW_TESTAMENT_APOCALYPTIC_BOOKS
)

_BOOK_GROUP_BOOKS: dict[BookGroup, tuple[Book, ...]] = MappingProxyType(
    {
        BookGroup.OLD_TESTAMENT: _OLD_TESTAMENT_BOOKS,
        BookGroup.OLD_TESTAMENT_LAW: _OLD_TESTAMENT_LAW_BOOKS,
        BookGroup.OLD_TESTAMENT_HISTORY: _OLD_TESTAMENT_HISTORY_BOOKS,
        BookGroup.OLD_TESTAMENT_POETRY_WISDOM: _OLD_TESTAMENT_POETRY_WISDOM_BOOKS,
        BookGroup.OLD_TESTAMENT_PROPHECY: _OLD_TESTAMENT_PROPHECY_BOOKS,
        BookGroup.OLD_TESTAMENT_MAJOR_PROPHETS: _OLD_TESTAMENT_MAJOR_PROPHETS_BOOKS,
        BookGroup.OLD_TESTAMENT_MINOR_PROPHETS: _OLD_TESTAMENT_MINOR_PROPHETS_BOOKS,
        BookGroup.NEW_TESTAMENT: _NEW_TESTAMENT_BOOKS,
        BookGroup.NEW_TESTAMENT_GOSPELS: _NEW_TESTAMENT_GOSPELS_BOOKS,
        BookGroup.NEW_TESTAMENT_HISTORY: _NEW_TESTAMENT_HISTORY_BOOKS,
        BookGroup.NEW_TESTAMENT_EPISTLES: _NEW_TESTAMENT_EPISTLES_BOOKS,
        BookGroup.NEW_TESTAMENT_PAUL_EPISTLES: _NEW_TESTAMENT_PAUL_EPISTLES_BOOKS,
        BookGroup.NEW_TESTAMENT_GENERAL_EPISTLES: _NEW_TESTAMENT_GENERAL_EPISTLES_BOOKS,
        BookGroup.NEW_TESTAMENT_APOCALYPTIC: _NEW_TESTAMENT_APOCALYPTIC_BOOKS,
    },
)

_BOOK_GROUP_REGULAR_EXPRESSIONS: dict[BookGroup, str] = MappingProxyType(
    {
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
        BookGroup.NEW_TESTAMENT_PAUL_EPISTLES: "Pauline Epistles|"
        "Paul's Epistles|"
        "Epistles of Paul",
        BookGroup.NEW_TESTAMENT_GENERAL_EPISTLES: "General Epistles",
        BookGroup.NEW_TESTAMENT_EPISTLES: "Epistles",
        BookGroup.NEW_TESTAMENT_APOCALYPTIC: "Apocalyptic",
    },
)

BOOK_GROUPS: dict[str, tuple[Book, ...]] = MappingProxyType(
    {book_group.regular_expression: book_group.books for book_group in BookGroup},
)
