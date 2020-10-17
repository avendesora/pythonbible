import os
from xml.etree import ElementTree

from pythonbible.bible.osis.constants import BOOK_IDS, get_book_by_id
from pythonbible.verses import get_book_chapter_verse, get_verse_id

XML_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "versions")

XPATH_BOOK = ".//xmlns:div[@osisID='{}']"
XPATH_BOOK_TITLE = f"{XPATH_BOOK}/xmlns:title"
XPATH_CHAPTER = ".//xmlns:chapter[@osisRef='{}.{}']"
XPATH_VERSE = ".//xmlns:verse[@osisID='{}.{}.{}']"
XPATH_VERSE_PARENT = f"{XPATH_VERSE}/.."


class OSISParser:
    def __init__(self, version):
        self.version = version
        self.tree = ElementTree.parse(
            os.path.join(XML_FOLDER, f"{self.version.value.lower()}.xml")
        )
        self.namespaces = {"xmlns": _get_namespace(self.tree.getroot().tag)}

    def get_book_title(self, book):
        xpath = XPATH_BOOK_TITLE.format(BOOK_IDS.get(book))
        return self.tree.find(xpath, namespaces=self.namespaces).text

    def get_reference_text(self, verse_id):
        book, chapter, verse = get_book_chapter_verse(verse_id)
        book_title = self.get_book_title(book)
        return f"{book_title} {chapter}:{verse}"

    def get_verse_text(self, verse_id):
        book, chapter, verse = get_book_chapter_verse(verse_id)
        xpath = XPATH_VERSE.format(BOOK_IDS.get(book), chapter, verse)
        return self.tree.find(xpath, namespaces=self.namespaces).tail

    def get_scripture_passage_text(self, verse_ids, format_type="html"):
        paragraphs = _get_paragraphs(self.tree, self.namespaces, verse_ids)

        if format_type == "html":
            paragraphs = [f"<p>{paragraph}</p>" for paragraph in paragraphs]

        return "\n".join(paragraphs)


def _get_namespace(tag):
    try:
        return tag[tag.index("{") + 1 : tag.index("}")]
    except ValueError:
        return ""


def _strip_namespace_from_tag(tag):
    return tag.replace(_get_namespace(tag), "").replace("{", "").replace("}", "")


def _get_paragraphs(tree, namespaces, verse_ids):
    if verse_ids is None or len(verse_ids) == 0:
        return []

    paragraphs = []
    verse_ids.sort()

    current_verse_id = verse_ids[0]
    book, chapter, verse = get_book_chapter_verse(current_verse_id)
    paragraph_element = tree.find(
        XPATH_VERSE_PARENT.format(BOOK_IDS.get(book), chapter, verse), namespaces
    )
    paragraph = ""
    skip_till_next_verse = False

    for child_element in list(paragraph_element):
        tag = _strip_namespace_from_tag(child_element.tag)

        if tag == "verse":
            osis_id = child_element.get("osisID")

            if osis_id is None:
                continue

            book_id, chapter, verse = child_element.get("osisID").split(".")
            book = get_book_by_id(book_id)
            verse_id = get_verse_id(book, int(chapter), int(verse))

            if verse_id in verse_ids:
                current_verse_id = verse_id

                if skip_till_next_verse:
                    skip_till_next_verse = False

                    if len(paragraph) > 0:
                        paragraph += "... "

                paragraph += f"{verse}. "
                continue

            skip_till_next_verse = True
            continue

        if tag in ["w", "transChange"] and not skip_till_next_verse:
            paragraph += child_element.text.replace("\n", " ")
            paragraph += child_element.tail.replace("\n", " ")

    paragraph = paragraph.strip()
    paragraphs.append(paragraph)
    current_verse_index = verse_ids.index(current_verse_id) + 1

    if current_verse_index < len(verse_ids):
        paragraphs.extend(
            _get_paragraphs(tree, namespaces, verse_ids[current_verse_index:])
        )

    return paragraphs
