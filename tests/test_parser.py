from typing import Dict, List

import pythonbible as bible


def test_get_references(text_with_reference: str) -> None:
    # Given a text string with at least one scripture reference
    # When parsing that text
    references: List[bible.NormalizedReference] = bible.get_references(
        text_with_reference
    )

    # Then the references are found and returned in a list of normalized reference tuples
    assert len(references) == 2
    assert references[0] == bible.NormalizedReference(
        bible.Book.MATTHEW, 18, 12, 18, 14
    )
    assert references[1] == bible.NormalizedReference(bible.Book.LUKE, 15, 3, 15, 7)


def test_get_references_complex(
    text_with_reference_complex: str,
    normalized_references_complex: List[bible.NormalizedReference],
) -> None:
    # Given a text string with multiple complex references
    # When parsing that text
    references: List[bible.NormalizedReference] = bible.get_references(
        text_with_reference_complex
    )

    # Then the references are found and returned in a list of normalized reference tuples
    assert references == normalized_references_complex


def test_normalize_reference(non_normalized_reference: str) -> None:
    # Given a non-normalized reference (just a string)
    # When we normalize that reference
    normalized_references: List[bible.NormalizedReference] = bible.normalize_reference(
        non_normalized_reference
    )

    # Then the reference is returned as a list of tuples with the book enum,
    # start chapter, start verse, end chapter, and end verse
    assert len(normalized_references) == 1
    assert normalized_references[0] == bible.NormalizedReference(
        bible.Book.MATTHEW, 18, 12, 18, 14
    )


def test_normalize_reference_without_verse_numbers(
    reference_without_verse_numbers: str,
) -> None:
    # Given a non-normalized reference that does not contain verse numbers (just book and chapters)
    # When we normalize that reference
    normalized_references: List[bible.NormalizedReference] = bible.normalize_reference(
        reference_without_verse_numbers
    )

    # Then the resulting normalized references contain the proper verse numbers
    assert len(normalized_references) == 1
    assert normalized_references[0] == bible.NormalizedReference(
        bible.Book.EXODUS, 20, 1, 20, 26
    )


def test_normalize_reference_range_without_verse_numbers(
    reference_range_without_verse_numbers: str,
) -> None:
    # Given a non-normalized reference that does not contain verse numbers (just book and chapters)
    # When we normalize that reference
    normalized_references: List[bible.NormalizedReference] = bible.normalize_reference(
        reference_range_without_verse_numbers
    )

    # Then the resulting normalized references contain the proper verse numbers
    assert len(normalized_references) == 1
    assert normalized_references[0] == bible.NormalizedReference(
        bible.Book.GENESIS, 1, 1, 4, 26
    )


def test_get_references_roman_numerals(
    roman_numeral_references: str,
    normalized_references_complex: List[bible.NormalizedReference],
) -> None:
    # Given a text string with multiple references with roman numerals
    # When parsing that text
    references: List[bible.NormalizedReference] = bible.get_references(
        roman_numeral_references
    )

    # Then the references are found and returned in a list of normalized reference tuples
    assert references == normalized_references_complex


def test_philemon_vs_philippians() -> None:
    """Test for https://github.com/avendesora/pythonbible/issues/2!"""
    # Given a text string with a reference in the book of Philemon
    text: str = "Philemon 1:9"

    # When we parse the references from that text
    references: List[bible.NormalizedReference] = bible.get_references(text)

    # Then the parser does not raise an error and returns the appropriate reference
    assert references == [bible.NormalizedReference(bible.Book.PHILEMON, 1, 9, 1, 9)]


def test_book_alternative_names(book_alternative_names) -> None:
    # Given the books of the Bible with their alternative names/abbreviations

    for book, alternative_names in book_alternative_names.items():
        references = bible.get_references(f"{book.title} 1:1-2")

        for alternative_name in alternative_names:
            # When we parse the references with the alternative name
            alternative_references = bible.get_references(f"{alternative_name} 1:1-2")

            # Then the alternative references match the baseline references
            print(alternative_name)
            assert alternative_references == references


def test_cross_book_reference_just_books() -> None:
    # Given a text string with a reference that ranges over multiple books of the Bible
    text: str = "Genesis - Deuteronomy"

    # When we parse the references from that text
    references: List[bible.NormalizedReference] = bible.get_references(text)

    # Then the parser does not raise an error and returns the appropriate reference
    deuteronomy: bible.Book = bible.Book.DEUTERONOMY
    max_chapter: int = bible.get_number_of_chapters(deuteronomy)
    max_verse: int = bible.get_max_number_of_verses(deuteronomy, max_chapter)
    assert references == [
        bible.NormalizedReference(
            bible.Book.GENESIS, 1, 1, max_chapter, max_verse, deuteronomy
        )
    ]


def test_cross_book_reference_complex() -> None:
    # Given a text string with a complex reference that ranges over multiple books of the Bible
    text: str = "Genesis 1:1-5, 50:3 - Exodus 1:14, 2:3-20:5"

    # When we parse the references from that text
    references: List[bible.NormalizedReference] = bible.get_references(text)

    # Then the parser does not raise an error and returns the appropriate reference
    assert references == [
        bible.NormalizedReference(bible.Book.GENESIS, 1, 1, 1, 5, None),
        bible.NormalizedReference(bible.Book.GENESIS, 50, 3, 1, 14, bible.Book.EXODUS),
        bible.NormalizedReference(bible.Book.EXODUS, 2, 3, 20, 5, None),
    ]


def test_book_group_reference() -> None:
    # Given a text string with a book group reference
    text: str = "This class is a survey of the Old Testament of the Bible."

    # When we parse the references from that text using the optional book_groups parameter
    references: List[bible.NormalizedReference] = bible.get_references(
        text, book_groups=bible.BOOK_GROUPS
    )

    # Then the parser returns the appropriate book group reference
    malachi: bible.Book = bible.Book.MALACHI
    max_chapter: int = bible.get_number_of_chapters(malachi)
    max_verse: int = bible.get_max_number_of_verses(malachi, max_chapter)
    assert references == [
        bible.NormalizedReference(
            bible.Book.GENESIS, 1, 1, max_chapter, max_verse, malachi
        ),
    ]


def test_book_group_reference_custom() -> None:
    # Given a custom dictionary of book group regular expressions
    book_groups: Dict[str, List[bible.Book]] = {
        "my custom book group": [
            bible.Book.GENESIS,
            bible.Book.EXODUS,
            bible.Book.MATTHEW,
            bible.Book.MARK,
            bible.Book.JUDE,
        ]
    }

    # and a text string containing a custom book group reference
    text: str = "Can you find my custom book group?"

    # When we parse the references from that text
    references: List[bible.NormalizedReference] = bible.get_references(
        text, book_groups=book_groups
    )

    # Then the parser returns the appropriate book group references
    assert references == [
        bible.NormalizedReference(bible.Book.GENESIS, 1, 1, 40, 38, bible.Book.EXODUS),
        bible.NormalizedReference(bible.Book.MATTHEW, 1, 1, 16, 20, bible.Book.MARK),
        bible.NormalizedReference(bible.Book.JUDE, 1, 1, 1, 25, bible.Book.JUDE),
    ]


def test_single_chapter_book_without_chapter_number() -> None:
    # Given a reference string that does not include the chapter number for a book that only has one chapter
    text: str = "Obadiah 3-6"

    # When we parse the references from that text
    references: List[bible.NormalizedReference] = bible.get_references(text)

    # Then the parser returns the appropriate normalized reference with chapter and verse numbers
    assert references == [
        bible.NormalizedReference(bible.Book.OBADIAH, 1, 3, 1, 6, None)
    ]


def test_book_alternative_names_verbum(book_alternative_names_verbum) -> None:
    # Given the books of the Bible with their alternative names/abbreviations

    for book, alternative_names in book_alternative_names_verbum.items():
        references = bible.get_references(f"{book.title} 1:1-2")

        for alternative_name in alternative_names:
            if len(alternative_name.replace(" ", "")) < 3:
                continue

            # When we parse the references with the alternative name
            alternative_references = bible.get_references(f"{alternative_name} 1:1-2")

            # Then the alternative references match the baseline references
            print(alternative_name)
            assert alternative_references == references
