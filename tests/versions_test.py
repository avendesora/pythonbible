from __future__ import annotations

import pythonbible as bible


def test_get_version_title() -> None:
    assert bible.Version.KING_JAMES.title == "King James Version"
    assert bible.Version.AMERICAN_STANDARD.title == "American Standard Version"
    assert bible.Version.BEREAN_STANDARD.title == "Berean Standard Bible"
    assert bible.Version.WORLD_ENGLISH.title == "World English Bible"
