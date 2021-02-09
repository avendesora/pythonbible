from enum import Enum

# This comes from crosswire.org "Standard OSIS Codes for Bible Editions"
# noinspection SpellCheckingInspection
from typing import Dict


class Version(Enum):
    # Ancient Language Editions
    STEPHANUS_GNT = "Steph"
    LATIN_VULGATE = "Vul"
    LATIN_ERASMUS = "Erasmus"
    MASORETIC_TEXT = "MT"
    BIBLIA_HEBRAICA_STUTTGARTENSIA = "BHS"
    NESTLE_ALAND = "NA"
    GREEK_SEPTUAGINT = "LXX"

    # English Editions
    COMPLETE = "AAT"
    AFRO = "ABT"
    ALTERNATE_TRANSLATION = "ATB"
    AMERICAN_STANDARD = "ASV"
    AMPLIFIED = "AB"
    ANALYTICAL_LITERAL = "ALT"
    AMERICAN_SIGN_LANGUAGE = "ASL"
    AUTHORIZED = "AV"
    BARCLAY = "BAR"
    BIKER = "BB"
    WORLWIDE_ENGLISH = "BWE"
    CHRISTIAN_COMMUNITY = "CCB"
    COMMON = "COM"
    COVENANT = "COV"
    COMPLETE_JEWISH = "CJB"
    CONCORDANT = "CONC"
    CONTEMPORARY_ENGLISH = "CEV"
    COTTON_PATCH = "CPV"
    DARBY = "DAR"
    DOUAY_RHEIMS = "DR"
    DAVID_ROBERT_PALMER = "DRP"
    ENGLISH_MAJORITY_TEXT = "EMTV"
    EXTREME = "ENT"
    EASY_TO_READ = "ERV"
    ENGLISH_STANDARD = "ESV"
    FERRAR_FENTON = "FF"
    GODS_LIVING_WORD = "GLW"
    GODS_NEW_COVENANT = "GNC"
    GODS_WORD = "GW"
    GOOD_NEWS = "GNB"
    HOLMAN_CHRISTIAN_STANDARD = "HCSB"
    INTERNATIONAL_CHILDRENS = "ICB"
    INTERNATIONAL_STANDARD_BIBLE = "ISB"
    INTERNATIONAL_STANDARD_VERSION = "ISV"
    J_B_PHILLIPS = "JBP"
    JEWISH_NEW_TESTAMENT = "JNT"
    KING_JAMES = "KJV"
    KING_JAMES_DEFINED = "DKJB"
    KING_JAMES_II = "KJII"
    KING_JAMES_21 = "KJ21"
    KING_JAMES_2000 = "KJ2000"
    LITERAL = "LITV"
    KING_JAMES_MODERN = "MKJV"
    REVISED_AUTHORISED = "RAV"
    KING_JAMES_REVISED = "RKJV"
    THIRD_MILLENIUM = "TMB"
    KING_JAMES_UPDATED = "UKJV"
    LIVING = "LB"
    MODERN_AMERICAN_ENGLISH_VERNACULAR = "MAEV"
    MODERN_LANGUAGE = "MLB"
    JAMES_MOFFATT = "Mof"
    NEW_AMERICAN = "NAB"
    NEW_AMERICAN_STANDARD = "NASB"
    NEW_CENTURY = "NCV"
    NEW_ENGLISH_BIBLE = "NEB"
    NEW_ENGLISH_TRANSLATION = "NET"
    NEW_EVANGELICAL = "NEvT"
    NEW_INTERNATIONAL_READERS = "NIrV"
    NEW_INTERNATIONAL = "NIV"
    NEW_JERUSALEM = "NJB"
    NEW_KING_JAMES = "NKJV"
    NEW_LIFE = "NLV"
    NEW_LIVING = "NLT"
    NEW_REVISED_STANDARD = "NRSV"
    NEW_WORLD = "NWT"
    ORIGINAL_BIBLE_PROJECT = "OBP"
    ORTHODOX_STUDY = "OSB"
    ORIGINAL_NEW_TESTAMENT = "ONT"
    POSTMODERN = "PMB"
    RECOVERY = "Rec"
    REVISED_ENGLISH = "REB"
    REVISED_STANDARD = "RSV"
    REVISED = "RV"
    SCHOCKEN = "Sch"
    SIMPLE_ENGLISH = "SEB"
    MESSAGE = "TM"
    TODAYS_ENGLISH = "TEV"
    TODAYS_NEW_INTERNATIONAL = "TNIV"
    TYNDALE = "Tyn"
    WEYMOUTH = "Wey"
    WORLD_ENGLISH = "WEB"
    CHARLES_B_WILLIAMS = "Wms"
    WESLEYS = "WNT"
    WUEST = "Wuest"
    WYCLIFFE = "Wyc"
    YES_WORD = "Yes"
    YOUNGS_LITERAL = "YLT"

    @property
    def title(self) -> str:
        return _VERSION_TITLES.get(self, "")


# noinspection SpellCheckingInspection
_VERSION_TITLES: Dict[Version, str] = {
    # Ancient Language Editions
    Version.STEPHANUS_GNT: "Stephanus GNT",
    Version.LATIN_VULGATE: "Latin Vulgate",
    Version.LATIN_ERASMUS: "Erasmus Latin translation by Desiderius Erasmus Roterodamus",
    Version.MASORETIC_TEXT: "Masoretic text",
    Version.BIBLIA_HEBRAICA_STUTTGARTENSIA: "Biblia Hebraica Stuttgartensia",
    Version.NESTLE_ALAND: "Nestle-Aland Greek New Testament",
    Version.GREEK_SEPTUAGINT: "Greek Septuagint",
    # English Editions
    Version.COMPLETE: "The Complete Bible: An American Translation, by Edgar Goodspeed and J. M. Powis Smith",
    Version.AFRO: "The Afro Bible Translation",
    Version.ALTERNATE_TRANSLATION: "The Alternate Translation Bible",
    Version.AMERICAN_STANDARD: "American Standard Version",
    Version.AMPLIFIED: "The Amplified Bible",
    Version.ANALYTICAL_LITERAL: "Analytical-Literal Translation",
    Version.AMERICAN_SIGN_LANGUAGE: "American Sign Language Translation",
    Version.AUTHORIZED: "Authorized Version",
    Version.BARCLAY: "The New Testament: A New Translation, by William Barclay",
    Version.BIKER: "The Biker Bible",
    Version.WORLWIDE_ENGLISH: "Bible in WorldWide English",
    Version.CHRISTIAN_COMMUNITY: "Christian Community Bible",
    Version.COMMON: "The Common Edition: New Testament",
    Version.COVENANT: "Covenant Edition New Testament",
    Version.COMPLETE_JEWISH: "Complete Jewish Bible",
    Version.CONCORDANT: "Concordant Version",
    Version.CONTEMPORARY_ENGLISH: "Contemporary English Version",
    Version.COTTON_PATCH: "Cotton Patch Version, tr. Clarence Jordan",
    Version.DARBY: "Darby",
    Version.DOUAY_RHEIMS: "Douay-Rheims",
    Version.DAVID_ROBERT_PALMER: "David Robert Palmer's translations of the gospels",
    Version.ENGLISH_MAJORITY_TEXT: "English Majority Text Version",
    Version.EXTREME: "Extreme New Testament",
    Version.EASY_TO_READ: "Easy-to-Read Version",
    Version.ENGLISH_STANDARD: "English Standard Version",
    Version.FERRAR_FENTON: "Ferrar Fenton Bible",
    Version.GODS_LIVING_WORD: "God's Living Word",
    Version.GODS_NEW_COVENANT: "God's New Covenant: A New Testament Translation, by Heinz W. Cassirer",
    Version.GODS_WORD: "God's Word",
    Version.GOOD_NEWS: "Good News Bible",
    Version.HOLMAN_CHRISTIAN_STANDARD: "Holman Christian Standard Bible",
    Version.INTERNATIONAL_CHILDRENS: "International Children's Bible",
    Version.INTERNATIONAL_STANDARD_BIBLE: "International Standard Bible",
    Version.INTERNATIONAL_STANDARD_VERSION: "The International Standard Version",
    Version.J_B_PHILLIPS: "New Testament in Modern English, by J. B. Phillips",
    Version.JEWISH_NEW_TESTAMENT: "Jewish New Testament: A Translation of the New Testament That Expresses Its Jewishness",
    Version.KING_JAMES: "King James Version",
    Version.KING_JAMES_DEFINED: "Defined King James Version",
    Version.KING_JAMES_II: "King James Version II",
    Version.KING_JAMES_21: "King James for the 21st Century",
    Version.KING_JAMES_2000: "King James 2000",
    Version.LITERAL: "The Literal Translation of the Holy Bible",
    Version.KING_JAMES_MODERN: "Modern King James Version",
    Version.REVISED_AUTHORISED: "Revised Authorised Version",
    Version.KING_JAMES_REVISED: "Revised King James New Testament",
    Version.THIRD_MILLENIUM: "The Third Millenium Bible",
    Version.KING_JAMES_UPDATED: "Updated King James Version",
    Version.LIVING: "Living Bible",
    Version.MODERN_AMERICAN_ENGLISH_VERNACULAR: "Modern American English Vernacular",
    Version.MODERN_LANGUAGE: "Modern Language Bible: New Berkeley Version",
    Version.JAMES_MOFFATT: "Bible: James Moffatt Translation",
    Version.NEW_AMERICAN: "New American Bible",
    Version.NEW_AMERICAN_STANDARD: "New American Standard Bible",
    Version.NEW_CENTURY: "New Century Version",
    Version.NEW_ENGLISH_BIBLE: "New English Bible",
    Version.NEW_ENGLISH_TRANSLATION: "New English Translation",
    Version.NEW_INTERNATIONAL_READERS: "New International Reader's Version",
    Version.NEW_INTERNATIONAL: "New International Version",
    Version.NEW_JERUSALEM: "New Jerusalem Bible",
    Version.NEW_KING_JAMES: "New King James Version",
    Version.NEW_LIFE: "New Life Version",
    Version.NEW_LIVING: "New Living Translation",
    Version.NEW_REVISED_STANDARD: "New Revised Standard Bible",
    Version.NEW_WORLD: "New World Translation",
    Version.ORIGINAL_BIBLE_PROJECT: "The Original Bible Project",
    Version.ORTHODOX_STUDY: "Orthodox Study Bible",
    Version.ORIGINAL_NEW_TESTAMENT: "The Original New Testament: The First Definitive Translation of the New Testament in 2000 Years, by Hugh Schonfield",
    Version.POSTMODERN: "Postmodern Bible - Amos",
    Version.RECOVERY: "Recovery Version",
    Version.REVISED_ENGLISH: "The Revised English Bible",
    Version.REVISED_STANDARD: "The Revised Standard Version",
    Version.REVISED: "Revised Version",
    Version.SCHOCKEN: "The Schocken Bible",
    Version.SIMPLE_ENGLISH: "The Simple English Bible",
    Version.MESSAGE: "The Message",
    Version.TODAYS_ENGLISH: "Today's English Version",
    Version.TODAYS_NEW_INTERNATIONAL: "Today's New International Version",
    Version.TYNDALE: "Tyndale",
    Version.WEYMOUTH: "Weymouth",
    Version.WORLD_ENGLISH: "World English Bible",
    Version.CHARLES_B_WILLIAMS: "The New Testament in the Language of the People",
    Version.WESLEYS: "Wesley's New Testament",
    Version.WUEST: "The New Testament (An Expanded Translation)",
    Version.WYCLIFFE: "Wycliffe",
    Version.YES_WORD: "Yes Word",
    Version.YOUNGS_LITERAL: "Young's Literal Translation of the Bible",
}

DEFAULT_VERSION: Version = Version.KING_JAMES
