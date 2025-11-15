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

    # Open Source or Public Domain English Translations
    AMERICAN_KING_JAMES = "AKJV", "American King James Version"
    AMERICAN_STANDARD = "ASV", "American Standard Version"
    BIBLE_IN_BASIC_ENGLISH = "BBE", "Bible in Basic English"
    WORLWIDE_ENGLISH = "BWE", "Bible in WorldWide English NT"
    DARBY = "DAR", "Darby"
    DIAGLOT_NT = "Diaglot", "Diaglot NT - 1865"
    DOUAY_RHEIMS = "DR", "Douay-Rheims"
    ROTHERHAM = "ROTH", "The Emphasized Bible by J. B. Rotherham"
    GENEVA = "GB", "Geneva Bible"
    KING_JAMES = "KJV", "King James Version"
    LEESER = "LEESER", "Leeser Old Testament"
    LIVING_ORACLES_NT = "LONT", "Living Oracles NT"
    KING_JAMES_MODERN_1963 = "MKJV1963", "Modern KJV 1963"
    MONTGOMERY_NT = "MONT", "Montgomery New Testament"
    NEW_HEART = "NHEB", "New Heart English Bible"
    OPEN_ENGLISH = "OEB", "Open English Bible"
    ETHERIDGE = "ETHERIDGE", "The Peschito Syriac New Testament"
    REVISED_WEBSTER = "RWEBSTER", "Revised 1833 Webster Version"
    REVISED_YOUNGS = "RYLT", "Revised Young's Literal Translation NT"
    KING_JAMES_UPDATED = "UKJV", "Updated King James Version"
    WEBSTER = "WBS", "Webster"
    WESLEY_NT = "WESLEY", "Wesley's New Testament"
    WEYMOUTH_NT = "WMTH", "Weymouth NT"
    TYNDALE = "TYN", "Willam Tyndale Bible"
    WORLD_ENGLISH = "WEB", "World English Bible"
    WYCLIFFE = "WYC", "Wycliffe Bible"
    YOUNGS = "YLT", "Young's Literal Translation of the Bible"

    # Ancient Language Editions
    BIBLIA_HEBRAICA_STUTTGARTENSIA = "BHS", "Biblia Hebraica Stuttgartensia"
    LATIN_ERASMUS = (
        "Erasmus",
        "Erasmus Latin translation by Desiderius Erasmus Roterodamus",
    )
    GREEK_SEPTUAGINT = "LXX", "Greek Septuagint"
    LATIN_VULGATE = "Vul", "Latin Vulgate"
    MASORETIC_TEXT = "MT", "Masoretic text"
    NESTLE_ALAND = "NA", "Nestle-Aland Greek New Testament"
    STEPHANUS_GNT = "Steph", "Stephanus GNT"

    # Other English Translations
    AFRO = "ABT", "The Afro Bible Translation"
    ALTERNATE_TRANSLATION = "ATB", "The Alternate Translation Bible"
    AMERICAN_SIGN_LANGUAGE = "ASL", "American Sign Language Translation"
    AMPLIFIED = "AB", "The Amplified Bible"
    ANALYTICAL_LITERAL = "ALT", "Analytical-Literal Translation"
    AUTHORIZED = "AV", "Authorized Version"
    JAMES_MOFFATT = "Mof", "Bible: James Moffatt Translation"
    BIKER = "BB", "The Biker Bible"
    BRENTONS_ENGLISH_SEPTUAGINT = "LXXE", "Brenton's English Septuagint"
    CHRISTIAN_COMMUNITY = "CCB", "Christian Community Bible"
    COMMON = "COM", "The Common Edition: New Testament"
    COMPLETE = (
        "AAT",
        "The Complete Bible: An American Translation, by Edgar Goodspeed and J. M. "
        "Powis Smith",
    )
    COMPLETE_JEWISH = "CJB", "Complete Jewish Bible"
    CONCORDANT = "CONC", "Concordant Version"
    A_CONSERVATIVE_VERSION = "ACV", "A Conservative Version"
    CONTEMPORARY_ENGLISH = "CEV", "Contemporary English Version"
    COTTON_PATCH = "CPV", "Cotton Patch Version, tr. Clarence Jordan"
    COVENANT = "COV", "Covenant Edition New Testament"
    DAVID_ROBERT_PALMER = "DRP", "David Robert Palmer's translations of the gospels"
    KING_JAMES_DEFINED = "DKJB", "Defined King James Version"
    EASY_TO_READ = "ERV", "Easy-to-Read Version"
    JUBILEE_2000 = "JUBL2000", "English Jubilee 2000 Bible"
    ENGLISH_MAJORITY_TEXT = "EMTV", "English Majority Text Version"
    ENGLISH_STANDARD = "ESV", "English Standard Version"
    EXTREME = "ENT", "Extreme New Testament"
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
    JEWISH_NEW_TESTAMENT = (
        "JNT",
        "Jewish New Testament: A Translation of the New Testament That Expresses Its "
        "Jewishness",
    )
    JEWISH_OLD_TESTAMENT = "JPS", "Jewish Publication Society AT"
    KING_JAMES_2000 = "KJ2000", "King James 2000"
    KING_JAMES_21 = "KJ21", "King James for the 21st Century"
    KING_JAMES_II = "KJII", "King James Version II"
    LEXHAM_ENGLISH = "LEB", "The Lexham English Bible"
    LITERAL = "LITV", "The Literal Translation of the Holy Bible"
    LIVING = "LB", "Living Bible"
    MESSAGE = "TM", "The Message"
    KING_JAMES_MODERN = "MKJV", "Modern King James Version"
    MODERN_AMERICAN_ENGLISH_VERNACULAR = "MAEV", "Modern American English Vernacular"
    MODERN_LANGUAGE = "MLB", "Modern Language Bible: New Berkeley Version"
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
    NEW_SIMPLIFIED = "NSB", "New Simplified Bible"
    J_B_PHILLIPS = "JBP", "New Testament in Modern English, by J. B. Phillips"
    CHARLES_B_WILLIAMS = "Wms", "The New Testament in the Language of the People"
    WUEST = "WUEST", "The New Testament (An Expanded Translation)"
    BARCLAY = "BAR", "The New Testament: A New Translation, by William Barclay"
    NEW_WORLD = "NWT", "New World Translation"
    ORIGINAL_BIBLE_PROJECT = "OBP", "The Original Bible Project"
    ORIGINAL_NEW_TESTAMENT = (
        "ONT",
        "The Original New Testament: The First Definitive Translation of the New "
        "Testament in 2000 Years, by Hugh Schonfield",
    )
    ORTHODOX_STUDY = "OSB", "Orthodox Study Bible"
    POSTMODERN = "PMB", "Postmodern Bible - Amos"
    RECOVERY = "REC", "Recovery Version"
    REVISED_AUTHORISED = "RAV", "Revised Authorised Version"
    REVISED_ENGLISH = "REB", "The Revised English Bible"
    KING_JAMES_REVISED = "RKJV", "Revised King James New Testament"
    REVISED_STANDARD = "RSV", "The Revised Standard Version"
    REVISED = "RV", "Revised Version"
    RIVERSIDE_NT = "RNT", "The Riverside New Testament"
    SCHOCKEN = "SCH", "The Schocken Bible"
    SIMPLE_ENGLISH = "SEB", "The Simple English Bible"
    THIRD_MILLENIUM = "TMB", "The Third Millenium Bible"
    TODAYS_ENGLISH = "TEV", "Today's English Version"
    TODAYS_NEW_INTERNATIONAL = "TNIV", "Today's New International Version"
    UPDATED_BIBLE = "UPDV", "Updated Bible Version"
    VW_EDITION_2006 = "XXX", "VW-Edition 2006"
    YES_WORD = "YES", "Yes Word"


DEFAULT_VERSION: Version = Version.AMERICAN_STANDARD
