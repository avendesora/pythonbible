import pytest

import pythonbible as bible


@pytest.fixture
def verse_id():
    return 1001001


@pytest.fixture
def invalid_verse_id():
    return 1100100


@pytest.fixture
def book():
    return bible.Book.GENESIS


@pytest.fixture
def chapter():
    return 1


@pytest.fixture
def verse():
    return 1


@pytest.fixture
def invalid_chapter():
    return 100


@pytest.fixture
def invalid_verse():
    return 100


@pytest.fixture
def text_with_reference():
    return "The parable of the lost sheep is told in Matthew 18:12-14 and Luke 15:3-7."


@pytest.fixture
def text_with_reference_complex():
    return "You should read Psalm 130:4,8, Jeremiah 29:32-30:10,31:12, Matthew 1:18 - 2:18, and Luke 3: 5-7."


@pytest.fixture
def normalized_references_complex():
    return [
        (bible.Book.PSALMS, 130, 4, 130, 4),
        (bible.Book.PSALMS, 130, 8, 130, 8),
        (bible.Book.JEREMIAH, 29, 32, 30, 10),
        (bible.Book.JEREMIAH, 31, 12, 31, 12),
        (bible.Book.MATTHEW, 1, 18, 2, 18),
        (bible.Book.LUKE, 3, 5, 3, 7),
    ]


@pytest.fixture
def non_normalized_reference():
    return "Matthew 18:12-14"


@pytest.fixture
def reference_without_verse_numbers():
    return "Exodus 20"


@pytest.fixture
def reference_range_without_verse_numbers():
    return "Genesis 1-4"


@pytest.fixture
def reference():
    return bible.Book.GENESIS, 1, 1, 3, 4


@pytest.fixture
def invalid_reference():
    return bible.Book.GENESIS, 1, 1, 100, 100


@pytest.fixture
def reference_string():
    return "Genesis 1:1-3:4"


@pytest.fixture
def references():
    return [(bible.Book.MATTHEW, 18, 12, 18, 14), (bible.Book.LUKE, 15, 3, 15, 7)]


@pytest.fixture
def verse_ids():
    return [
        40018012,
        40018013,
        40018014,
        42015003,
        42015004,
        42015005,
        42015006,
        42015007,
    ]


@pytest.fixture
def verse_ids_complex():
    return [
        19130004,
        19130008,
        24029032,
        24030001,
        24030002,
        24030003,
        24030004,
        24030005,
        24030006,
        24030007,
        24030008,
        24030009,
        24030010,
        24031012,
        40001018,
        40001019,
        40001020,
        40001021,
        40001022,
        40001023,
        40001024,
        40001025,
        40002001,
        40002002,
        40002003,
        40002004,
        40002005,
        40002006,
        40002007,
        40002008,
        40002009,
        40002010,
        40002011,
        40002012,
        40002013,
        40002014,
        40002015,
        40002016,
        40002017,
        40002018,
        42003005,
        42003006,
        42003007,
    ]


@pytest.fixture
def formatted_reference():
    return "Psalms 130:4,8;Jeremiah 29:32-30:10,31:12;Matthew 1:18-2:18;Luke 3:5-7"


@pytest.fixture
def roman_numeral_references():
    return "Psalm cxxx.4,8, Jeremiah xxix. 32 - xxx. 10, xxxi. 12, Matthew i. 18 - ii. 18, and Luke iii. 5-7."
