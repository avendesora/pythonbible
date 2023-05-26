from __future__ import annotations

from enum import Enum
from enum import auto
from typing import Any
from typing import Type

from pythonbible.books import Book

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

_NEW_TESTAMENT_APOCALYPTIC_BOOKS: tuple[Book, ...] = (Book.REVELATION,)


class BookGroup(Enum):
    """BookGroup is an ``Enum`` containing the default Bible book groupings.

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

    def __new__(
        cls: Type[BookGroup],
        *args: dict[str, Any],
        **kwargs: dict[str, Any],
    ) -> BookGroup:
        obj: BookGroup = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(
        self: BookGroup,
        _: int,
        regular_expression: str,
        books: tuple[Book, ...],
    ) -> None:
        """Set the regular expression and books."""
        self._regular_expression_ = regular_expression
        self._books_ = books

    @property
    def books(self: BookGroup) -> tuple[Book, ...]:
        return self._books_

    @property
    def regular_expression(self: BookGroup) -> str:
        return self._regular_expression_

    OLD_TESTAMENT = (
        auto(),
        "Old Testament",
        _OLD_TESTAMENT_LAW_BOOKS
        + _OLD_TESTAMENT_HISTORY_BOOKS
        + _OLD_TESTAMENT_POETRY_WISDOM_BOOKS
        + _OLD_TESTAMENT_MAJOR_PROPHETS_BOOKS
        + _OLD_TESTAMENT_MINOR_PROPHETS_BOOKS,
    )
    OLD_TESTAMENT_LAW = auto(), "Law", _OLD_TESTAMENT_LAW_BOOKS
    OLD_TESTAMENT_HISTORY = auto(), "History", _OLD_TESTAMENT_HISTORY_BOOKS
    OLD_TESTAMENT_POETRY_WISDOM = (
        auto(),
        "Poetry|Wisdom",
        _OLD_TESTAMENT_POETRY_WISDOM_BOOKS,
    )
    OLD_TESTAMENT_PROPHECY = (
        auto(),
        "Prophecy",
        _OLD_TESTAMENT_MAJOR_PROPHETS_BOOKS + _OLD_TESTAMENT_MINOR_PROPHETS_BOOKS,
    )
    OLD_TESTAMENT_MAJOR_PROPHETS = (
        auto(),
        "Major Prophets",
        _OLD_TESTAMENT_MAJOR_PROPHETS_BOOKS,
    )
    OLD_TESTAMENT_MINOR_PROPHETS = (
        auto(),
        "Minor Prophets",
        _OLD_TESTAMENT_MINOR_PROPHETS_BOOKS,
    )
    NEW_TESTAMENT = (
        auto(),
        "New Testament",
        _NEW_TESTAMENT_GOSPELS_BOOKS
        + _NEW_TESTAMENT_HISTORY_BOOKS
        + _NEW_TESTAMENT_PAUL_EPISTLES_BOOKS
        + _NEW_TESTAMENT_GENERAL_EPISTLES_BOOKS
        + _NEW_TESTAMENT_APOCALYPTIC_BOOKS,
    )
    NEW_TESTAMENT_GOSPELS = auto(), "Gospels", _NEW_TESTAMENT_GOSPELS_BOOKS
    NEW_TESTAMENT_HISTORY = auto(), "History", _NEW_TESTAMENT_HISTORY_BOOKS
    NEW_TESTAMENT_EPISTLES = (
        auto(),
        "Epistles",
        _NEW_TESTAMENT_PAUL_EPISTLES_BOOKS + _NEW_TESTAMENT_GENERAL_EPISTLES_BOOKS,
    )
    NEW_TESTAMENT_PAUL_EPISTLES = (
        auto(),
        "Pauline Epistles|Paul's Epistles|Epistles of Paul",
        _NEW_TESTAMENT_PAUL_EPISTLES_BOOKS,
    )
    NEW_TESTAMENT_GENERAL_EPISTLES = (
        auto(),
        "General Epistles",
        _NEW_TESTAMENT_GENERAL_EPISTLES_BOOKS,
    )
    NEW_TESTAMENT_APOCALYPTIC = auto(), "Apocalyptic", _NEW_TESTAMENT_APOCALYPTIC_BOOKS


BOOK_GROUPS: dict[str, tuple[Book, ...]] = {
    book_group.regular_expression: book_group.books for book_group in BookGroup
}
