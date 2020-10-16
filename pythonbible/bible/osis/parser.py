import os
import xml.etree.ElementTree as ET

from pythonbible import get_book_chapter_verse
from pythonbible.bible.osis.constants import BOOK_IDS

XML_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "versions")

XPATH_BOOK = ".//xmlns:div[@osisID='{}']"
XPATH_BOOK_TITLE = f"{XPATH_BOOK}/xmlns:title"
XPATH_CHAPTER = ".//xmlns:chapter[@osisRef='{}.{}']"
XPATH_VERSE = ".//xmlns:verse[@osisID='{}.{}.{}']"


class OSISParser:
    def __init__(self, version):
        self.version = version
        self.tree = ET.parse(
            os.path.join(XML_FOLDER, f"{self.version.value.lower()}.xml")
        )
        self.namespaces = {"xmlns": get_namespace(self.tree.getroot().tag)}

    def get_verse_text(self, verse_id):
        book, chapter, verse = get_book_chapter_verse(verse_id)
        xpath = XPATH_VERSE.format(BOOK_IDS.get(book), chapter, verse)
        return self.tree.find(xpath, namespaces=self.namespaces).tail

    def get_verse_reference(self, verse_id):
        book, chapter, verse = get_book_chapter_verse(verse_id)
        book_title = self.get_book_title(book)
        return f"{book_title} {chapter}:{verse}"

    def get_book_title(self, book):
        xpath = XPATH_BOOK_TITLE.format(BOOK_IDS.get(book))
        return self.tree.find(xpath, namespaces=self.namespaces).text


def get_namespace(tag):
    try:
        return tag[tag.index("{") + 1 : tag.index("}")]
    except ValueError:
        return ""
