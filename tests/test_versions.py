import pythonbible as bible


def test_get_version_title():
    assert bible.Version.KING_JAMES.title == "King James Version"
