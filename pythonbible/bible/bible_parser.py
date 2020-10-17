from collections import OrderedDict


class BibleParser:
    def __init__(self, version):
        self.version = version


def sort_paragraphs(paragraphs):
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
