"""Contains the BibleParser generic parser class."""

from collections import OrderedDict


class BibleParser:
    """
    Parse files containing scripture text.

    BibleParser is a generic parser to provide common functionality for specific
    parsers (e.g. OSIS, USFM, USFX, etc.) for parsing scripture text.
    """

    def __init__(self, version):
        """
        Initialize the Bible parser with the version.

        :param version:
        """
        self.version = version


def sort_paragraphs(paragraphs):
    """
    Sort paragraphs of scripture text.

    Given a structured collection of paragraphs organized by book, chapter, and
    list of paragraphs, return that collection in an ordered dictionary with the
    books and chapters sorted appropriately. (Assume the list of paragraphs is
    already sorted appropriately.)

    :param paragraphs:
    :return: an OrderedDict(Book, OrderedDict(int, list(string)))
    """
    ordered_paragraphs = OrderedDict()

    book_keys = list(paragraphs.keys())
    book_keys.sort()

    for book in book_keys:
        chapters = paragraphs.get(book)
        ordered_chapters = OrderedDict()

        chapter_keys = list(chapters.keys())
        chapter_keys.sort()

        for chapter in chapter_keys:
            ordered_chapters[chapter] = chapters.get(chapter)

        ordered_paragraphs[book] = ordered_chapters

    return ordered_paragraphs
