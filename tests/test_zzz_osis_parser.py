import time
from typing import Dict, List, Optional

import pytest

import pythonbible as bible
from pythonbible.bible.bible_parser import BibleParser
from pythonbible.formatter import DEFAULT_PARSER


def test_get_scripture_passage_text(
    verse_ids_complex: List[int], kjv_passage: Dict[bible.Book, Dict[int, List[str]]]
) -> None:
    # Given a list of verse ids
    # When we get the scripture passage for those verses
    passage: Dict[
        bible.Book, Dict[int, List[str]]
    ] = DEFAULT_PARSER.get_scripture_passage_text(verse_ids_complex)

    # Then the scripture passage is correct.
    assert passage == kjv_passage


def test_get_scripture_passage_text_no_numbers(
    verse_ids_complex: List[int],
    kjv_passage_no_verse_numbers: Dict[bible.Book, Dict[int, List[str]]],
):
    # Given a list of verse ids
    # When we get the scripture passage for those verses
    passage: Dict[
        bible.Book, Dict[int, List[str]]
    ] = DEFAULT_PARSER.get_scripture_passage_text(
        verse_ids_complex, include_verse_number=False
    )

    # Then the scripture passage is correct.
    assert passage == kjv_passage_no_verse_numbers


def test_get_asv_scripture_passage_text(
    verse_ids_complex: List[int], asv_passage: Dict[bible.Book, Dict[int, List[str]]]
):
    # Given a list of verse ids
    # When we get the ASV scripture passage for those verses
    parser: BibleParser = bible.OSISParser(bible.Version.AMERICAN_STANDARD)
    passage: Dict[bible.Book, Dict[int, List[str]]] = parser.get_scripture_passage_text(
        verse_ids_complex
    )

    # Then the scripture passage is correct.
    assert passage == asv_passage


def test_get_scripture_passage_ellipsis() -> None:
    passage: Dict[
        bible.Book, Dict[int, List[str]]
    ] = DEFAULT_PARSER.get_scripture_passage_text(
        [
            1001003,
            1001005,
        ]
    )

    genesis_paragraphs: Optional[Dict[int, List[str]]] = passage.get(bible.Book.GENESIS)

    assert genesis_paragraphs is not None

    chapter_1_paragraphs: Optional[List[str]] = genesis_paragraphs.get(1)

    assert chapter_1_paragraphs is not None

    assert "..." in chapter_1_paragraphs[0]


def test_get_book_title() -> None:
    book_title: str = DEFAULT_PARSER.get_book_title(bible.Book.GENESIS)
    assert book_title == "The First Book of Moses, called Genesis"


def test_get_short_book_title() -> None:
    book_title: str = DEFAULT_PARSER.get_short_book_title(bible.Book.GENESIS)
    assert book_title == "Genesis"


def test_get_scripture_passage_null() -> None:
    assert len(DEFAULT_PARSER.get_scripture_passage_text(None)) == 0


def test_get_verse_text(verse_id: int, verse_text: str) -> None:
    # Given a verse id
    # When we get the scripture text for that verse id
    actual_text: str = DEFAULT_PARSER.get_verse_text(verse_id)

    # Then it is what we expect it to be.
    assert actual_text == verse_text


def test_get_verse_text_null() -> None:
    # Given a null verse id
    # When we attempt to get the scripture text for that verse id
    # Then it raise an InvalidVerseError
    with pytest.raises(bible.InvalidVerseError):
        DEFAULT_PARSER.get_verse_text(None)


def test_get_verse_text_invalid_verse(invalid_verse_id: int) -> None:
    # Given an invalid verse id
    # When we attempt to get the scripture text for that verse id
    # Then it raise an InvalidVerseError
    with pytest.raises(bible.InvalidVerseError):
        DEFAULT_PARSER.get_verse_text(invalid_verse_id)


def test_exodus_20_3_asv() -> None:
    """Test for https://github.com/avendesora/pythonbible/issues/9!"""
    # Given the reference Exodus 20:3
    text: str = "Exodus 20:3"

    # When we get the verse text using the ASV parser
    references: List[bible.NormalizedReference] = bible.get_references(text)
    verse_id: int = bible.convert_references_to_verse_ids(references)[0]
    parser: BibleParser = bible.get_parser(version=bible.Version.AMERICAN_STANDARD)
    verse_text: str = parser.get_verse_text(verse_id)

    # Then the verse text is not missing any words.
    assert verse_text == "3. Thou shalt have no other gods before me."


def test_mark_9_38_kjv() -> None:
    """Test for https://github.com/avendesora/pythonbible/issues/12!"""
    # Given the verse id for Mark 9:38
    verse_id: int = 41009038

    # When we get the verse text using the KJV parser
    parser: BibleParser = bible.get_parser(version=bible.Version.KING_JAMES)
    verse_text: str = parser.get_verse_text(verse_id)

    # Then there are no errors and the verse text is as expected
    assert (
        verse_text == "38. And John answered him, saying, Master, we saw one "
        "casting out devils in thy name, and he followeth not us: "
        "and we forbad him, because he followeth not us."
    )


def test_mark_9_43_kjv() -> None:
    """Test for https://github.com/avendesora/pythonbible/issues/16!"""
    # Given the verse id for Mark 9:43
    verse_id: int = 41009043

    # When we get the verse text using the KJV parser
    parser: BibleParser = bible.get_parser(version=bible.Version.KING_JAMES)
    verse_text: str = parser.get_verse_text(verse_id)

    # Then there are no errors and the verse text is as expected
    assert (
        verse_text == "43. And if thy hand offend thee, cut it off: it is "
        "better for thee to enter into life maimed, than having two hands "
        "to go into hell, into the fire that never shall be quenched:"
    )


def test_matthew_17_21_asv() -> None:
    """Test for https://github.com/avendesora/pythonbible/issues/19!"""
    # Given the verse id for Matthew 17:21
    verse_id: int = 40017021

    # When we get the verse text using the ASV parser
    parser: BibleParser = bible.get_parser(version=bible.Version.AMERICAN_STANDARD)
    verse_text: str = parser.get_verse_text(verse_id)

    # Then there are no errors and the verse text is as expected
    assert verse_text == "21. But this kind goeth not out save by prayer and fasting."


def test_scripture_text_caching() -> None:
    # Given a lengthy reference
    references: List[bible.NormalizedReference] = bible.get_references("James")
    verse_ids: List[int] = bible.convert_references_to_verse_ids(references)

    # When getting the scripture text multiple times
    parser: BibleParser = bible.get_parser()

    first_start_time: float = time.time()
    first_text: Dict[
        bible.Book, Dict[int, List[str]]
    ] = parser.get_scripture_passage_text(verse_ids)
    second_start_time: float = time.time()
    second_text: Dict[
        bible.Book, Dict[int, List[str]]
    ] = parser.get_scripture_passage_text(verse_ids)
    end_time: float = time.time()

    first_time: float = second_start_time - first_start_time
    second_time: float = end_time - second_start_time

    # Then the results are cached, so we get the same results much faster the second time
    assert first_time * 0.1 > second_time
    assert first_text == second_text


def test_scripture_text_caching_across_versions() -> None:
    # Given a lengthy reference
    references: List[bible.NormalizedReference] = bible.get_references("Ephesians")
    verse_ids: List[int] = bible.convert_references_to_verse_ids(references)

    # When getting the scripture text multiple times from multiple versions
    kjv_parser: BibleParser = bible.get_parser(version=bible.Version.KING_JAMES)
    asv_parser: BibleParser = bible.get_parser(version=bible.Version.AMERICAN_STANDARD)

    first_start_time: float = time.time()
    first_text: Dict[
        bible.Book, Dict[int, List[str]]
    ] = kjv_parser.get_scripture_passage_text(verse_ids)
    second_start_time: float = time.time()
    second_text: Dict[
        bible.Book, Dict[int, List[str]]
    ] = asv_parser.get_scripture_passage_text(verse_ids)
    third_start_time: float = time.time()
    third_text: Dict[
        bible.Book, Dict[int, List[str]]
    ] = kjv_parser.get_scripture_passage_text(verse_ids)
    end_time: float = time.time()

    first_time: float = second_start_time - first_start_time
    second_time: float = third_start_time - second_start_time
    third_time: float = end_time - third_start_time

    # Then the caching only works within a version and not across versions
    assert first_time * 0.1 < second_time
    assert first_text != second_text
    assert first_time * 0.1 > third_time
    assert first_text == third_text


def test_verse_text_caching() -> None:
    # Given a lengthy reference
    references: List[bible.NormalizedReference] = bible.get_references("Jude")
    verse_ids: List[int] = bible.convert_references_to_verse_ids(references)

    # When getting the scripture text multiple times
    parser: BibleParser = bible.get_parser()

    first_start_time: float = time.time()
    first_verses: List[str] = [
        parser.get_verse_text(verse_id) for verse_id in verse_ids
    ]
    second_start_time: float = time.time()
    second_verses: List[str] = [
        parser.get_verse_text(verse_id) for verse_id in verse_ids
    ]
    end_time: float = time.time()

    first_time: float = second_start_time - first_start_time
    second_time: float = end_time - second_start_time

    # Then the results are cached, so we get the same results much faster the second time
    assert first_time * 0.1 > second_time
    assert first_verses == second_verses
