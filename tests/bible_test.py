from __future__ import annotations

import pytest

import pythonbible as bible
import pythonbible.bible.errors

ASV_HTML = bible.get_bible(bible.Version.AMERICAN_STANDARD, "html")
ASV_HTML_READERS = bible.get_bible(bible.Version.AMERICAN_STANDARD, "html_readers")


def test_get_scripture_end_verse_invalid() -> None:
    with pytest.raises(bible.InvalidVerseError):
        ASV_HTML.get_scripture(1001001, 99999999)


def test_get_scripture_cross_chapter() -> None:
    scripture = ASV_HTML.get_scripture(1001031, 1002001)
    assert scripture == (
        "<p><sup>31</sup> And God saw everything that he had made, and, behold, it "
        "was very good. And there was evening and there was morning, the sixth "
        "day.</p><p><sup>1</sup> And the heavens and the earth were finished, and all "
        "the host of them.</p>"
    )


def test_get_scripture_cross_book() -> None:
    scripture = ASV_HTML.get_scripture(64001014, 65001001)
    assert scripture == (
        "<p><sup>14</sup> but I hope shortly to see thee, and we shall speak face to "
        "face. Peace [be] unto thee. The friends salute thee. Salute the friends by "
        "name.</p><p><sup>1</sup> Jude, a servant of Jesus Christ, and brother of "
        "James, to them that are called, beloved in God the Father, and kept for "
        "Jesus Christ:</p>"
    )


def test_get_scripture_missing_verse_in_version() -> None:
    scripture = ASV_HTML_READERS.get_scripture(40017021, 40017021)
    assert not scripture


def test_get_scripture_missing_book_in_version_start_index() -> None:
    with pytest.raises(pythonbible.bible.errors.VersionMissingVerseError):
        ASV_HTML_READERS.get_scripture(67001001, 67001001)


def test_get_scripture_missing_book_in_version_end_index() -> None:
    with pytest.raises(pythonbible.bible.errors.VersionMissingVerseError):
        ASV_HTML_READERS.get_scripture(66001001, 67001001)


def test_get_bible_bad_type() -> None:
    # Given a good version and a bad type
    # When getting the Bible
    # Then a MissingVerseFileError is raised.
    with pytest.raises(pythonbible.errors.MissingVerseFileError):
        bible.get_bible(bible.Version.AMERICAN_STANDARD, "bad_type")


def test_add_bible() -> None:
    # Given a Bible instance
    version = bible.Version.MESSAGE
    bible_type = "test-type"
    bible_instance = bible.Bible(
        version,
        "content",
        {1: 1},
        {1: 1},
        {bible.Book.GENESIS: {1: 1}},
    )

    # When adding the Bible instance to the Bible class
    bible.add_bible(version, bible_type, bible_instance)

    # Then the Bible instance is in the Bible class
    assert bible.get_bible(version, bible_type) == bible_instance


def test_get_long_title_init_version() -> None:
    # Given a version that has not yet been initialized and a valid book
    version = bible.Version.WEYMOUTH_NT
    book = bible.Book.MATTHEW

    # When getting the long title for the book
    long_title = bible.get_long_title(version, book)

    # Then the version is initialized and the long title is returned
    assert long_title == book.title
