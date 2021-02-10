import pythonbible as bible


def test_get_version_title() -> None:
    assert bible.Version.KING_JAMES.title == "King James Version"
