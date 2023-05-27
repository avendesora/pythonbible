from __future__ import annotations

from enum import Enum
from typing import Any
from typing import Type


# This comes from crosswire.org "Standard OSIS Codes for Bible Editions"
class Version(Enum):
    """Version of the Bible.

    Version is an Enum containing all the currently known Ancient Language
    and English versions of the Bible.

    :param name: the unique text identifier of the version
    :type name: str
    :param value: the unique abbreviated identifier of the version
    :type value: str
    :param title: the English title of the version
    :type title: str
    """

    def __new__(
        cls: Type[Version],
        *args: dict[str, Any],
        **kwargs: dict[str, Any],
    ) -> Version:
        obj: Version = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self: Version, _: str, title: str) -> None:
        """Set the title property."""
        self._title_ = title

    @property
    def title(self: Version) -> str:
        return self._title_

    # Ancient Language Editions
    STEPHANUS_GNT = "Steph", "Stephanus GNT"
    LATIN_VULGATE = "Vul", "Latin Vulgate"
    LATIN_ERASMUS = (
        "Erasmus",
        "Erasmus Latin translation by Desiderius Erasmus Roterodamus",
    )
    MASORETIC_TEXT = "MT", "Masoretic text"
    BIBLIA_HEBRAICA_STUTTGARTENSIA = "BHS", "Biblia Hebraica Stuttgartensia"
    NESTLE_ALAND = "NA", "Nestle-Aland Greek New Testament"
    GREEK_SEPTUAGINT = "LXX", "Greek Septuagint"

    # English Editions
    COMPLETE = (
        "AAT",
        "The Complete Bible: An American Translation, by Edgar Goodspeed and J. M. "
        "Powis Smith",
    )
    AFRO = "ABT", "The Afro Bible Translation"
    ALTERNATE_TRANSLATION = "ATB", "The Alternate Translation Bible"
    AMERICAN_STANDARD = "ASV", "American Standard Version"
    AMPLIFIED = "AB", "The Amplified Bible"
    ANALYTICAL_LITERAL = "ALT", "Analytical-Literal Translation"
    AMERICAN_SIGN_LANGUAGE = "ASL", "American Sign Language Translation"
    AUTHORIZED = "AV", "Authorized Version"
    BARCLAY = "BAR", "The New Testament: A New Translation, by William Barclay"
    BIKER = "BB", "The Biker Bible"
    WORLWIDE_ENGLISH = "BWE", "Bible in WorldWide English"
    CHRISTIAN_COMMUNITY = "CCB", "Christian Community Bible"
    COMMON = "COM", "The Common Edition: New Testament"
    COVENANT = "COV", "Covenant Edition New Testament"
    COMPLETE_JEWISH = "CJB", "Complete Jewish Bible"
    CONCORDANT = "CONC", "Concordant Version"
    CONTEMPORARY_ENGLISH = "CEV", "Contemporary English Version"
    COTTON_PATCH = "CPV", "Cotton Patch Version, tr. Clarence Jordan"
    DARBY = "DAR", "Darby"
    DOUAY_RHEIMS = "DR", "Douay-Rheims"
    DAVID_ROBERT_PALMER = "DRP", "David Robert Palmer's translations of the gospels"
    ENGLISH_MAJORITY_TEXT = "EMTV", "English Majority Text Version"
    EXTREME = "ENT", "Extreme New Testament"
    EASY_TO_READ = "ERV", "Easy-to-Read Version"
    ENGLISH_STANDARD = "ESV", "English Standard Version"
    FERRAR_FENTON = "FF", "Ferrar Fenton Bible"
    GODS_LIVING_WORD = "GLW", "God's Living Word"
    GODS_NEW_COVENANT = (
        "GNC",
        "God's New Covenant: A New Testament Translation, by Heinz W. Cassirer",
    )
    GODS_WORD = "GW", "God's Word"
    GOOD_NEWS = "GNB", "Good News Bible"
    HOLMAN_CHRISTIAN_STANDARD = "HCSB", "Holman Christian Standard Bible"
    INTERNATIONAL_CHILDRENS = "ICB", "International Children's Bible"
    INTERNATIONAL_STANDARD_BIBLE = "ISB", "International Standard Bible"
    INTERNATIONAL_STANDARD_VERSION = "ISV", "The International Standard Version"
    J_B_PHILLIPS = "JBP", "New Testament in Modern English, by J. B. Phillips"
    JEWISH_NEW_TESTAMENT = (
        "JNT",
        "Jewish New Testament: A Translation of the New Testament That Expresses Its "
        "Jewishness",
    )
    KING_JAMES = "KJV", "King James Version"
    KING_JAMES_DEFINED = "DKJB", "Defined King James Version"
    KING_JAMES_II = "KJII", "King James Version II"
    KING_JAMES_21 = "KJ21", "King James for the 21st Century"
    KING_JAMES_2000 = "KJ2000", "King James 2000"
    LITERAL = "LITV", "The Literal Translation of the Holy Bible"
    KING_JAMES_MODERN = "MKJV", "Modern King James Version"
    REVISED_AUTHORISED = "RAV", "Revised Authorised Version"
    KING_JAMES_REVISED = "RKJV", "Revised King James New Testament"
    THIRD_MILLENIUM = "TMB", "The Third Millenium Bible"
    KING_JAMES_UPDATED = "UKJV", "Updated King James Version"
    LIVING = "LB", "Living Bible"
    MODERN_AMERICAN_ENGLISH_VERNACULAR = "MAEV", "Modern American English Vernacular"
    MODERN_LANGUAGE = "MLB", "Modern Language Bible: New Berkeley Version"
    JAMES_MOFFATT = "Mof", "Bible: James Moffatt Translation"
    NEW_AMERICAN = "NAB", "New American Bible"
    NEW_AMERICAN_STANDARD = "NASB", "New American Standard Bible"
    NEW_CENTURY = "NCV", "New Century Version"
    NEW_ENGLISH_BIBLE = "NEB", "New English Bible"
    NEW_ENGLISH_TRANSLATION = "NET", "New English Translation"
    NEW_EVANGELICAL = "NEvT", "New Evangelical Translation"
    NEW_INTERNATIONAL_READERS = "NIrV", "New International Reader's Version"
    NEW_INTERNATIONAL = "NIV", "New International Version"
    NEW_JERUSALEM = "NJB", "New Jerusalem Bible"
    NEW_KING_JAMES = "NKJV", "New King James Version"
    NEW_LIFE = "NLV", "New Life Version"
    NEW_LIVING = "NLT", "New Living Translation"
    NEW_REVISED_STANDARD = "NRSV", "New Revised Standard Bible"
    NEW_WORLD = "NWT", "New World Translation"
    ORIGINAL_BIBLE_PROJECT = "OBP", "The Original Bible Project"
    ORTHODOX_STUDY = "OSB", "Orthodox Study Bible"
    ORIGINAL_NEW_TESTAMENT = (
        "ONT",
        "The Original New Testament: The First Definitive Translation of the New "
        "Testament in 2000 Years, by Hugh Schonfield",
    )
    POSTMODERN = "PMB", "Postmodern Bible - Amos"
    RECOVERY = "Rec", "Recovery Version"
    REVISED_ENGLISH = "REB", "The Revised English Bible"
    REVISED_STANDARD = "RSV", "The Revised Standard Version"
    REVISED = "RV", "Revised Version"
    SCHOCKEN = "Sch", "The Schocken Bible"
    SIMPLE_ENGLISH = "SEB", "The Simple English Bible"
    MESSAGE = "TM", "The Message"
    TODAYS_ENGLISH = "TEV", "Today's English Version"
    TODAYS_NEW_INTERNATIONAL = "TNIV", "Today's New International Version"
    TYNDALE = "Tyn", "Tyndale"
    WEYMOUTH = "Wey", "Weymouth"
    WORLD_ENGLISH = "WEB", "World English Bible"
    CHARLES_B_WILLIAMS = "Wms", "The New Testament in the Language of the People"
    WESLEYS = "WNT", "Wesley's New Testament"
    WUEST = "Wuest", "The New Testament (An Expanded Translation)"
    WYCLIFFE = "Wyc", "Wycliffe"
    YES_WORD = "Yes", "Yes Word"
    YOUNGS_LITERAL = "YLT", "Young's Literal Translation of the Bible"


DEFAULT_VERSION: Version = Version.AMERICAN_STANDARD
