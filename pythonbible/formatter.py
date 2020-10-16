from pythonbible.converter import (
    convert_references_to_verse_ids,
    convert_verse_ids_to_references,
)


# TODO - handle Psalms vs Psalm appropriately
# TODO - handle single chapter books appropriately (e.g. Obadiah 1-4 rather than Obadiah 1:1-4)
def format_scripture_references(references):
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
                book, start_chapter, start_verse, end_chapter, end_verse
            )
            previous_reference = reference
            continue

        previous_book = previous_reference[0]

        # Reference with a new book
        if previous_book != book:
            formatted_reference += ";"
            formatted_reference += format_single_reference(
                book, start_chapter, start_verse, end_chapter, end_verse
            )
            previous_reference = reference
            continue

        previous_end_chapter = previous_reference[3]

        # Reference with a new chapter
        if previous_end_chapter != start_chapter or end_chapter > start_chapter:
            formatted_reference += ","
            formatted_reference += format_single_reference(
                None, start_chapter, start_verse, end_chapter, end_verse
            )
            continue

        # Reference with same book and chapter as previous reference
        formatted_reference += ","
        formatted_reference += format_single_reference(
            None, None, start_verse, None, end_verse
        )
        previous_reference = reference

    return formatted_reference


def format_single_reference(book, start_chapter, start_verse, end_chapter, end_verse):
    formatted_reference = ""

    if book:
        formatted_reference += f"{book.title} "

    if start_chapter:
        formatted_reference += f"{start_chapter}:{start_verse}"
    else:
        formatted_reference += f"{start_verse}"

    if end_chapter and end_chapter > start_chapter:
        formatted_reference += f"-{end_chapter}:{end_verse}"
    elif end_verse > start_verse:
        formatted_reference += f"-{end_verse}"

    return formatted_reference
