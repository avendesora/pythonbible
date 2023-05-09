from __future__ import annotations

import pytest

import pythonbible as bible
from pythonbible.bible.asv.html import bible as asv_html_bible
from pythonbible.bible.asv.html_readers import bible as asv_html_readers_bible


def test_get_scripture_end_verse_invalid() -> None:
    with pytest.raises(bible.InvalidVerseError):
        asv_html_bible.get_scripture(1001001, 99999999)


def test_get_scripture_cross_chapter() -> None:
    scripture = asv_html_bible.get_scripture(1001031, 1002001)
    assert scripture == (
        "<p><sup>31</sup> And God saw everything that he had made, and, behold, it "
        "was very good. And there was evening and there was morning, the sixth "
        "day.</p><p><sup>1</sup> And the heavens and the earth were finished, and all "
        "the host of them.</p>"
    )


def test_get_scripture_cross_book() -> None:
    scripture = asv_html_bible.get_scripture(64001014, 65001001)
    assert scripture == (
        "<p><sup>14</sup> but I hope shortly to see thee, and we shall speak face to "
        "face. Peace unto thee. The friends salute thee. Salute the friends by "
        "name.</p><p><sup>1</sup> Jude, a servant of Jesus Christ, and brother of "
        "James, to them that are called, beloved in God the Father, and kept for "
        "Jesus Christ:</p>"
    )


def test_get_scripture_missing_verse_in_version() -> None:
    scripture = asv_html_readers_bible.get_scripture(40017021, 40017021)
    assert not scripture
