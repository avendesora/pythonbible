import json
import os
from typing import Dict, List, Tuple

from pythonbible.bible.bible_parser import BibleParser
from pythonbible.bible.osis.parser import OSISParser
from pythonbible.books import Book
from pythonbible.errors import InvalidBibleParserError
from pythonbible.formatter import DATA_FOLDER
from pythonbible.verses import VERSE_IDS, get_book_chapter_verse, get_book_number
from pythonbible.versions import Version


class JSONConverter:
    """Convert XML scripture files into faster verse and book title JSON files."""

    def __init__(self, parser: BibleParser, **kwargs) -> None:
        """
        Initialize with a BibleParser and optional data folder and list of verse ids.

        If no data folder is specified, the data folder in the same directory
        as this class will be used. If no verse ids are specified, the list of
        all verse ids will be used.

        :param parser: BibleParser instance with version
        :param kwargs: optional "data_folder" and "verse_ids"
        """
        self.parser: BibleParser = parser
        self.data_folder: str = kwargs.get("data_folder", DATA_FOLDER)
        self.verse_ids: List[int] = kwargs.get("verse_ids", VERSE_IDS)
        self.books: Dict[int, Tuple[str, str]] = {}
        self.verses: Dict[int, str] = {}

    def generate_book_file(self) -> None:
        """
        Generate the book title JSON file for the given version.

        :return: None
        """
        self._validate_parser()
        self._get_books()
        self._print_books_file()

    def generate_verse_file(self) -> None:
        """
        Generate the verse text JSON file for the given version.

        :return: None
        """
        self._validate_parser()
        self._get_verses()
        self._print_verses_file()

    def _validate_parser(self) -> None:
        if self.parser is None:
            raise InvalidBibleParserError("Parser instance is None.")

        instance_identified: bool = False

        if isinstance(self.parser, OSISParser):
            instance_identified = True

        if not instance_identified:
            raise InvalidBibleParserError("Parser instance is not a valid type.")

    def _get_books(self) -> None:
        for verse_id in self.verse_ids:
            book_id: int = get_book_number(verse_id)

            if book_id in self.books.keys():
                continue

            book: Book
            book, _, _ = get_book_chapter_verse(verse_id)

            if book:
                long_book_title: str = self.parser.get_book_title(book)
                short_book_title: str = self.parser.get_short_book_title(book)
                self.books[book_id] = (long_book_title, short_book_title)

    def _get_verses(self) -> None:
        for verse_id in self.verse_ids:
            verse_text: str = self.parser.get_verse_text(
                verse_id, include_verse_number=False
            )

            if verse_text is None or len(verse_text.strip()) == 0:
                print(f"Verse {verse_id} is empty.")

            self.verses[verse_id] = verse_text

    def _print_books_file(self) -> None:
        _print_file(self.data_folder, self.parser.version, "books.json", self.books)

    def _print_verses_file(self) -> None:
        _print_file(self.data_folder, self.parser.version, "verses.json", self.verses)


def _print_file(data_folder: str, version: Version, filename: str, data: dict) -> None:
    version_folder: str = os.path.join(data_folder, version.value.lower())

    _make_sure_directory_exists(data_folder)
    _make_sure_directory_exists(version_folder)

    with open(os.path.join(version_folder, filename), "w") as json_file:
        json.dump(data, json_file)


def _make_sure_directory_exists(directory) -> None:
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass
