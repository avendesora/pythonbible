from pythonbible.bible.osis.parser import OSISParser
from pythonbible.converter import (
    convert_references_to_verse_ids,
    convert_verse_ids_to_references,
)
from pythonbible.versions import Version

VERSION_MAP = {Version.AMERICAN_STANDARD: OSISParser, Version.KING_JAMES: OSISParser}

DEFAULT_VERSION = Version.KING_JAMES


def get_parser(**kwargs):
    version = kwargs.get("version", DEFAULT_VERSION)
    version_map = kwargs.get("version_map", VERSION_MAP)
    return version_map.get(version)(version)


DEFAULT_PARSER = get_parser()


# TODO - handle Psalms vs Psalm appropriately
# TODO - handle single chapter books appropriately (e.g. Obadiah 1-4 rather than Obadiah 1:1-4)
def format_scripture_references(references, **kwargs):
    """

    :param references: a list of normalized scripture references
    :return: a string version of the references formatted to be human-readable
    """
    if references is None:
        return None

    verse_ids = convert_references_to_verse_ids(references)
    verse_ids.sort()
    sorted_references = convert_verse_ids_to_references(verse_ids)

    formatted_reference = ""

    previous_reference = None

    for reference in sorted_references:
        book, start_chapter, start_verse, end_chapter, end_verse = reference

        # First reference
        if previous_reference is None:
            formatted_reference += format_single_reference(
                book, start_chapter, start_verse, end_chapter, end_verse, **kwargs
            )
            previous_reference = reference
            continue

        previous_book = previous_reference[0]

        # Reference with a new book
        if previous_book != book:
            formatted_reference += ";"
            formatted_reference += format_single_reference(
                book, start_chapter, start_verse, end_chapter, end_verse, **kwargs
            )
            previous_reference = reference
            continue

        previous_end_chapter = previous_reference[3]

        # Reference with a new chapter
        if previous_end_chapter != start_chapter or end_chapter > start_chapter:
            formatted_reference += ","
            formatted_reference += format_single_reference(
                None, start_chapter, start_verse, end_chapter, end_verse, **kwargs
            )
            continue

        # Reference with same book and chapter as previous reference
        formatted_reference += ","
        formatted_reference += format_single_reference(
            None, None, start_verse, None, end_verse, **kwargs
        )
        previous_reference = reference

    return formatted_reference


def format_single_reference(
    book, start_chapter, start_verse, end_chapter, end_verse, **kwargs
):
    formatted_reference = ""

    if book:
        parser = kwargs.get("parser", DEFAULT_PARSER)
        full_title = kwargs.get("full_title", False)

        title = (
            parser.get_book_title(book)
            if full_title
            else parser.get_short_book_title(book)
        )

        formatted_reference += f"{title} "

    if start_chapter:
        formatted_reference += f"{start_chapter}:{start_verse}"
    else:
        formatted_reference += f"{start_verse}"

    if end_chapter and end_chapter > start_chapter:
        formatted_reference += f"-{end_chapter}:{end_verse}"
    elif end_verse > start_verse:
        formatted_reference += f"-{end_verse}"

    return formatted_reference


def format_scripture_text(verse_ids, **kwargs):
    parser = kwargs.get("parser", DEFAULT_PARSER)
    full_title = kwargs.get("full_title", False)
    title_function = (
        parser.get_book_title if full_title else parser.get_short_book_title
    )
    format_type = kwargs.get("format_type", "html")
    text = ""

    paragraphs = parser.get_scripture_passage_text(verse_ids, **kwargs)

    for book, chapters in paragraphs.items():
        title = title_function(book)

        if format_type == "html":
            text += f"<h1>{title}</h1>\n"
        else:
            if len(text) > 0:
                text += "\n\n"

            text += f"{title}\n\n"

        for chapter, paragraphs in chapters.items():
            if format_type == "html":
                text += f"<h2>Chapter {chapter}</h2>\n"
            else:
                text += f"Chapter {chapter}\n\n"

            for paragraph in paragraphs:
                if format_type == "html":
                    text += f"<p>{paragraph}</p>\n"
                else:
                    text += f"   {paragraph}\n"

    return text
