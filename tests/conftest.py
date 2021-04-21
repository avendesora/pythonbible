from collections import OrderedDict
from typing import Dict, List

import pytest

import pythonbible as bible
from pythonbible.bible.bible_parser import BibleParser


@pytest.fixture
def verse_id() -> int:
    return 1001001


@pytest.fixture
def invalid_verse_id() -> int:
    return 1100100


@pytest.fixture
def book() -> bible.Book:
    return bible.Book.GENESIS


@pytest.fixture
def chapter() -> int:
    return 1


@pytest.fixture
def verse() -> int:
    return 1


@pytest.fixture
def invalid_chapter() -> int:
    return 100


@pytest.fixture
def invalid_verse() -> int:
    return 100


@pytest.fixture
def text_with_reference() -> str:
    return "The parable of the lost sheep is told in Matthew 18:12-14 and Luke 15:3-7."


@pytest.fixture
def text_with_reference_complex() -> str:
    return "You should read Psalm 130:4,8, Jeremiah 29:32-30:10,31:12, Matthew 1:18 - 2:18, and Luke 3: 5-7."


@pytest.fixture
def normalized_references_complex() -> List[bible.NormalizedReference]:
    return [
        bible.NormalizedReference(bible.Book.PSALMS, 130, 4, 130, 4),
        bible.NormalizedReference(bible.Book.PSALMS, 130, 8, 130, 8),
        bible.NormalizedReference(bible.Book.JEREMIAH, 29, 32, 30, 10),
        bible.NormalizedReference(bible.Book.JEREMIAH, 31, 12, 31, 12),
        bible.NormalizedReference(bible.Book.MATTHEW, 1, 18, 2, 18),
        bible.NormalizedReference(bible.Book.LUKE, 3, 5, 3, 7),
    ]


@pytest.fixture
def non_normalized_reference() -> str:
    return "Matthew 18:12-14"


@pytest.fixture
def reference_without_verse_numbers() -> str:
    return "Exodus 20"


@pytest.fixture
def reference_range_without_verse_numbers() -> str:
    return "Genesis 1-4"


@pytest.fixture
def reference() -> bible.NormalizedReference:
    return bible.NormalizedReference(bible.Book.GENESIS, 1, 1, 3, 4)


@pytest.fixture
def invalid_reference() -> bible.NormalizedReference:
    return bible.NormalizedReference(bible.Book.GENESIS, 1, 1, 100, 100)


@pytest.fixture
def reference_string() -> str:
    return "Genesis 1:1-3:4"


@pytest.fixture
def references() -> List[bible.NormalizedReference]:
    return [
        bible.NormalizedReference(bible.Book.MATTHEW, 18, 12, 18, 14),
        bible.NormalizedReference(bible.Book.LUKE, 15, 3, 15, 7),
    ]


@pytest.fixture
def verse_ids() -> List[int]:
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
def verse_ids_multiple_chapters() -> List[int]:
    return [
        40018012,
        40018013,
        40018014,
        40019001,
    ]


@pytest.fixture
def verse_ids_complex() -> List[int]:
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
def formatted_reference() -> str:
    return "Psalms 130:4,8;Jeremiah 29:32-30:10,31:12;Matthew 1:18-2:18;Luke 3:5-7"


@pytest.fixture
def roman_numeral_references() -> str:
    return "Psalm cxxx.4,8, Jeremiah xxix. 32 - xxx. 10, xxxi. 12, Matthew i. 18 - ii. 18, and Luke iii. 5-7."


@pytest.fixture
def kjv_passage() -> Dict[bible.Book, Dict[int, List[str]]]:
    return OrderedDict(
        [
            (
                bible.Book.PSALMS,
                OrderedDict(
                    [
                        (
                            130,
                            [
                                "4. But there is forgiveness with thee, that thou mayest be feared.",
                                "8. And he shall redeem Israel from all his iniquities.",
                            ],
                        )
                    ]
                ),
            ),
            (
                bible.Book.JEREMIAH,
                OrderedDict(
                    [
                        (
                            29,
                            [
                                "32. Therefore thus saith the Behold, I will punish Shemaiah the Nehelamite, and his seed: he shall not have a man to dwell among this people; neither shall he behold the good that I will do for my people, saith the because he hath taught rebellion against the"
                            ],
                        ),
                        (
                            30,
                            [
                                "1. The word that came to Jeremiah from the saying, 2. Thus speaketh the God of Israel, saying, Write thee all the words that I have spoken unto thee in a book. 3. For, lo, the days come, saith the that I will bring again the captivity of my people Israel and Judah, saith the and I will cause them to return to the land that I gave to their fathers, and they shall possess it.",
                                "4. And these are the words that the spake concerning Israel and concerning Judah. 5. For thus saith the We have heard a voice of trembling, of fear, and not of peace. 6. Ask ye now, and see whether a man doth travail with child? wherefore do I see every man with his hands on his loins, as a woman in travail, and all faces are turned into paleness? 7. Alas! for that day is great, so that none is like it: it is even the time of Jacob’s trouble; but he shall be saved out of it. 8. For it shall come to pass in that day, saith the of hosts, that I will break his yoke from off thy neck, and will burst thy bonds, and strangers shall no more serve themselves of him: 9. But they shall serve the their God, and David their king, whom I will raise up unto them.",
                                "10. Therefore fear thou not, O my servant Jacob, saith the neither be dismayed, O Israel: for, lo, I will save thee from afar, and thy seed from the land of their captivity; and Jacob shall return, and shall be in rest, and be quiet, and none shall make him afraid.",
                            ],
                        ),
                        (
                            31,
                            [
                                "12. Therefore they shall come and sing in the height of Zion, and shall flow together to the goodness of the for wheat, and for wine, and for oil, and for the young of the flock and of the herd: and their soul shall be as a watered garden; and they shall not sorrow any more at all."
                            ],
                        ),
                    ]
                ),
            ),
            (
                bible.Book.MATTHEW,
                OrderedDict(
                    [
                        (
                            1,
                            [
                                "18. Now the birth of Jesus Christ was on this wise: When as his mother Mary was espoused to Joseph, before they came together, she was found with child of the Holy Ghost. 19. Then Joseph her husband, being a just man, and not willing to make her a publick example, was minded to put her away privily. 20. But while he thought on these things, behold, the angel of the Lord appeared unto him in a dream, saying, Joseph, thou son of David, fear not to take unto thee Mary thy wife: for that which is conceived in her is of the Holy Ghost. 21. And she shall bring forth a son, and thou shalt call his name JESUS: for he shall save his people from their sins. 22. Now all this was done, that it might be fulfilled which was spoken of the Lord by the prophet, saying, 23. Behold, a virgin shall be with child, and shall bring forth a son, and they shall call his name Emmanuel, which being interpreted is, God with us. 24. Then Joseph being raised from sleep did as the angel of the Lord had bidden him, and took unto him his wife: 25. And knew her not till she had brought forth her firstborn son: and he called his name JESUS."
                            ],
                        ),
                        (
                            2,
                            [
                                "1. Now when Jesus was born in Bethlehem of Judaea in the days of Herod the king, behold, there came wise men from the east to Jerusalem, 2. Saying, Where is he that is born King of the Jews? for we have seen his star in the east, and are come to worship him. 3. When Herod the king had heard these things, he was troubled, and all Jerusalem with him. 4. And when he had gathered all the chief priests and scribes of the people together, he demanded of them where Christ should be born. 5. And they said unto him, In Bethlehem of Judaea: for thus it is written by the prophet, 6. And thou Bethlehem, in the land of Juda, art not the least among the princes of Juda: for out of thee shall come a Governor, that shall rule my people Israel. 7. Then Herod, when he had privily called the wise men, enquired of them diligently what time the star appeared. 8. And he sent them to Bethlehem, and said, Go and search diligently for the young child; and when ye have found him, bring me word again, that I may come and worship him also. 9. When they had heard the king, they departed; and, lo, the star, which they saw in the east, went before them, till it came and stood over where the young child was. 10. When they saw the star, they rejoiced with exceeding great joy.",
                                "11. And when they were come into the house, they saw the young child with Mary his mother, and fell down, and worshipped him: and when they had opened their treasures, they presented unto him gifts; gold, and frankincense, and myrrh. 12. And being warned of God in a dream that they should not return to Herod, they departed into their own country another way. 13. And when they were departed, behold, the angel of the Lord appeareth to Joseph in a dream, saying, Arise, and take the young child and his mother, and flee into Egypt, and be thou there until I bring thee word: for Herod will seek the young child to destroy him. 14. When he arose, he took the young child and his mother by night, and departed into Egypt: 15. And was there until the death of Herod: that it might be fulfilled which was spoken of the Lord by the prophet, saying, Out of Egypt have I called my son.",
                                "16. Then Herod, when he saw that he was mocked of the wise men, was exceeding wroth, and sent forth, and slew all the children that were in Bethlehem, and in all the coasts thereof, from two years old and under, according to the time which he had diligently enquired of the wise men. 17. Then was fulfilled that which was spoken by Jeremy the prophet, saying, 18. In Rama was there a voice heard, lamentation, and weeping, and great mourning, Rachel weeping for her children, and would not be comforted, because they are not.",
                            ],
                        ),
                    ]
                ),
            ),
            (
                bible.Book.LUKE,
                OrderedDict(
                    [
                        (
                            3,
                            [
                                "5. Every valley shall be filled, and every mountain and hill shall be brought low; and the crooked shall be made straight, and the rough ways shall be made smooth; 6. And all flesh shall see the salvation of God. 7. Then said he to the multitude that came forth to be baptized of him, O generation of vipers, who hath warned you to flee from the wrath to come?"
                            ],
                        )
                    ]
                ),
            ),
        ]
    )


@pytest.fixture
def kjv_passage_no_verse_numbers() -> Dict[bible.Book, Dict[int, List[str]]]:
    return OrderedDict(
        [
            (
                bible.Book.PSALMS,
                OrderedDict(
                    [
                        (
                            130,
                            [
                                "But there is forgiveness with thee, that thou mayest be feared.",
                                "And he shall redeem Israel from all his iniquities.",
                            ],
                        )
                    ]
                ),
            ),
            (
                bible.Book.JEREMIAH,
                OrderedDict(
                    [
                        (
                            29,
                            [
                                "Therefore thus saith the Behold, I will punish Shemaiah the Nehelamite, and his seed: he shall not have a man to dwell among this people; neither shall he behold the good that I will do for my people, saith the because he hath taught rebellion against the"
                            ],
                        ),
                        (
                            30,
                            [
                                "The word that came to Jeremiah from the saying, Thus speaketh the God of Israel, saying, Write thee all the words that I have spoken unto thee in a book. For, lo, the days come, saith the that I will bring again the captivity of my people Israel and Judah, saith the and I will cause them to return to the land that I gave to their fathers, and they shall possess it.",
                                "And these are the words that the spake concerning Israel and concerning Judah. For thus saith the We have heard a voice of trembling, of fear, and not of peace. Ask ye now, and see whether a man doth travail with child? wherefore do I see every man with his hands on his loins, as a woman in travail, and all faces are turned into paleness? Alas! for that day is great, so that none is like it: it is even the time of Jacob’s trouble; but he shall be saved out of it. For it shall come to pass in that day, saith the of hosts, that I will break his yoke from off thy neck, and will burst thy bonds, and strangers shall no more serve themselves of him: But they shall serve the their God, and David their king, whom I will raise up unto them.",
                                "Therefore fear thou not, O my servant Jacob, saith the neither be dismayed, O Israel: for, lo, I will save thee from afar, and thy seed from the land of their captivity; and Jacob shall return, and shall be in rest, and be quiet, and none shall make him afraid.",
                            ],
                        ),
                        (
                            31,
                            [
                                "Therefore they shall come and sing in the height of Zion, and shall flow together to the goodness of the for wheat, and for wine, and for oil, and for the young of the flock and of the herd: and their soul shall be as a watered garden; and they shall not sorrow any more at all."
                            ],
                        ),
                    ]
                ),
            ),
            (
                bible.Book.MATTHEW,
                OrderedDict(
                    [
                        (
                            1,
                            [
                                "Now the birth of Jesus Christ was on this wise: When as his mother Mary was espoused to Joseph, before they came together, she was found with child of the Holy Ghost. Then Joseph her husband, being a just man, and not willing to make her a publick example, was minded to put her away privily. But while he thought on these things, behold, the angel of the Lord appeared unto him in a dream, saying, Joseph, thou son of David, fear not to take unto thee Mary thy wife: for that which is conceived in her is of the Holy Ghost. And she shall bring forth a son, and thou shalt call his name JESUS: for he shall save his people from their sins. Now all this was done, that it might be fulfilled which was spoken of the Lord by the prophet, saying, Behold, a virgin shall be with child, and shall bring forth a son, and they shall call his name Emmanuel, which being interpreted is, God with us. Then Joseph being raised from sleep did as the angel of the Lord had bidden him, and took unto him his wife: And knew her not till she had brought forth her firstborn son: and he called his name JESUS."
                            ],
                        ),
                        (
                            2,
                            [
                                "Now when Jesus was born in Bethlehem of Judaea in the days of Herod the king, behold, there came wise men from the east to Jerusalem, Saying, Where is he that is born King of the Jews? for we have seen his star in the east, and are come to worship him. When Herod the king had heard these things, he was troubled, and all Jerusalem with him. And when he had gathered all the chief priests and scribes of the people together, he demanded of them where Christ should be born. And they said unto him, In Bethlehem of Judaea: for thus it is written by the prophet, And thou Bethlehem, in the land of Juda, art not the least among the princes of Juda: for out of thee shall come a Governor, that shall rule my people Israel. Then Herod, when he had privily called the wise men, enquired of them diligently what time the star appeared. And he sent them to Bethlehem, and said, Go and search diligently for the young child; and when ye have found him, bring me word again, that I may come and worship him also. When they had heard the king, they departed; and, lo, the star, which they saw in the east, went before them, till it came and stood over where the young child was. When they saw the star, they rejoiced with exceeding great joy.",
                                "And when they were come into the house, they saw the young child with Mary his mother, and fell down, and worshipped him: and when they had opened their treasures, they presented unto him gifts; gold, and frankincense, and myrrh. And being warned of God in a dream that they should not return to Herod, they departed into their own country another way. And when they were departed, behold, the angel of the Lord appeareth to Joseph in a dream, saying, Arise, and take the young child and his mother, and flee into Egypt, and be thou there until I bring thee word: for Herod will seek the young child to destroy him. When he arose, he took the young child and his mother by night, and departed into Egypt: And was there until the death of Herod: that it might be fulfilled which was spoken of the Lord by the prophet, saying, Out of Egypt have I called my son.",
                                "Then Herod, when he saw that he was mocked of the wise men, was exceeding wroth, and sent forth, and slew all the children that were in Bethlehem, and in all the coasts thereof, from two years old and under, according to the time which he had diligently enquired of the wise men. Then was fulfilled that which was spoken by Jeremy the prophet, saying, In Rama was there a voice heard, lamentation, and weeping, and great mourning, Rachel weeping for her children, and would not be comforted, because they are not.",
                            ],
                        ),
                    ]
                ),
            ),
            (
                bible.Book.LUKE,
                OrderedDict(
                    [
                        (
                            3,
                            [
                                "Every valley shall be filled, and every mountain and hill shall be brought low; and the crooked shall be made straight, and the rough ways shall be made smooth; And all flesh shall see the salvation of God. Then said he to the multitude that came forth to be baptized of him, O generation of vipers, who hath warned you to flee from the wrath to come?"
                            ],
                        )
                    ]
                ),
            ),
        ]
    )


@pytest.fixture
def asv_passage() -> Dict[bible.Book, Dict[int, List[str]]]:
    return OrderedDict(
        [
            (
                bible.Book.PSALMS,
                OrderedDict(
                    [
                        (
                            130,
                            [
                                "4. But there is forgiveness with thee,",
                                "8. And he will redeem Israel",
                            ],
                        )
                    ]
                ),
            ),
            (
                bible.Book.JEREMIAH,
                OrderedDict(
                    [
                        (
                            29,
                            [
                                "32. therefore thus saith Jehovah, Behold, I will punish Shemaiah the Nehelamite, and his seed; he shall not have a man to dwell among this people, neither shall he behold the good that I will do unto my people, saith Jehovah, because he hath spoken rebellion against Jehovah."
                            ],
                        ),
                        (
                            30,
                            [
                                "1. The word that came to Jeremiah from Jehovah, saying, 2. Thus speaketh Jehovah, the God of Israel, saying, Write thee all the words that I have spoken unto thee in a book. 3. For, lo, the days come, saith Jehovah, that I will turn again the captivity of my people Israel and Judah, saith Jehovah; and I will cause them to return to the land that I gave to their fathers, and they shall possess it.",
                                "4. And these are the words that Jehovah spake concerning Israel and concerning Judah. 5. For thus saith Jehovah: We have heard a voice of trembling, of fear, and not of peace. 6. Ask ye now, and see whether a man doth travail with child: wherefore do I see every man with his hands on his loins, as a woman in travail, and all faces are turned into paleness? 7. Alas! for that day is great, so that none is like it: it is even the time of Jacob’s trouble; but he shall be saved out of it. 8. And it shall come to pass in that day, saith Jehovah of hosts, that I will break his yoke from off thy neck, and will burst thy bonds; and strangers shall no more make him their bondman; 9. but they shall serve Jehovah their God, and David their king, whom I will raise up unto them. 10. Therefore fear thou not, O Jacob my servant, saith Jehovah; neither be dismayed, O Israel: for, lo, I will save thee from afar, and thy seed from the land of their captivity; and Jacob shall return, and shall be quiet and at ease, and none shall make him afraid.",
                            ],
                        ),
                        (
                            31,
                            [
                                "12. And they shall come and sing in the height of Zion, and shall flow unto the goodness of Jehovah, to the grain, and to the new wine, and to the oil, and to the young of the flock and of the herd: and their soul shall be as a watered garden; and they shall not sorrow any more at all."
                            ],
                        ),
                    ]
                ),
            ),
            (
                bible.Book.MATTHEW,
                OrderedDict(
                    [
                        (
                            1,
                            [
                                "18. Now the birth of Jesus Christ was on this wise: When his mother Mary had been betrothed to Joseph, before they came together she was found with child of the Holy Spirit. 19. And Joseph her husband, being a righteous man, and not willing to make her a public example, was minded to put her away privily. 20. But when he thought on these things, behold, an angel of the Lord appeared unto him in a dream, saying, Joseph, thou son of David, fear not to take unto thee Mary thy wife: for that which is conceived in her is of the Holy Spirit. 21. And she shall bring forth a son; and thou shalt call his name JESUS; for it is he that shall save his people from their sins. 22. Now all this is come to pass, that it might be fulfilled which was spoken by the Lord through the prophet, saying,",
                                "23. Behold, the virgin shall be with child, and shall bring forth a son,",
                                "which is, being interpreted, God with us. 24. And Joseph arose from his sleep, and did as the angel of the Lord commanded him, and took unto him his wife; 25. and knew her not till she had brought forth a son: and he called his name JESUS.",
                            ],
                        ),
                        (
                            2,
                            [
                                "1. Now when Jesus was born in Bethlehem of Judæa in the days of Herod the king, behold, Wise-men from the east came to Jerusalem, saying, 2. Where is he that is born King of the Jews? for we saw his star in the east, and are come to worship him. 3. And when Herod the king heard it, he was troubled, and all Jerusalem with him. 4. And gathering together all the chief priests and scribes of the people, he inquired of them where the Christ should be born. 5. And they said unto him, In Bethlehem of Judæa: for thus it is written through the prophet,",
                                "6. And thou Bethlehem, land of Judah,",
                                "7. Then Herod privily called the Wise-men, and learned of them exactly what time the star appeared. 8. And he sent them to Bethlehem, and said, Go and search out exactly concerning the young child; and when ye have found , bring me word, that I also may come and worship him. 9. And they, having heard the king, went their way; and lo, the star, which they saw in the east, went before them, till it came and stood over where the young child was. 10. And when they saw the star, they rejoiced with exceeding great joy. 11. And they came into the house and saw the young child with Mary his mother; and they fell down and worshipped him; and opening their treasures they offered unto him gifts, gold and frankincense and myrrh. 12. And being warned in a dream that they should not return to Herod, they departed into their own country another way.",
                                "13. Now when they were departed, behold, an angel of the Lord appeareth to Joseph in a dream, saying, Arise and take the young child and his mother, and flee into Egypt, and be thou there until I tell thee: for Herod will seek the young child to destroy him. 14. And he arose and took the young child and his mother by night, and departed into Egypt; 15. and was there until the death of Herod: that it might be fulfilled which was spoken by the Lord through the prophet, saying, Out of Egypt did I call my son.",
                                "16. Then Herod, when he saw that he was mocked of the Wise-men, was exceeding wroth, and sent forth, and slew all the male children that were in Bethlehem, and in all the borders thereof, from two years old and under, according to the time which he had exactly learned of the Wise-men. 17. Then was fulfilled that which was spoken through Jeremiah the prophet, saying,",
                                "18. A voice was heard in Ramah,",
                            ],
                        ),
                    ]
                ),
            ),
            (
                bible.Book.LUKE,
                OrderedDict(
                    [
                        (
                            3,
                            [
                                "5. Every valley shall be filled,",
                                "6. And all flesh shall see the salvation of God.",
                                "7. He said therefore to the multitudes that went out to be baptized of him, Ye offspring of vipers, who warned you to flee from the wrath to come?",
                            ],
                        )
                    ]
                ),
            ),
        ]
    )


@pytest.fixture
def html_scripture_text() -> str:
    return (
        "<h1>Matthew</h1>\n"
        "<h2>Chapter 18</h2>\n"
        "<p>12. How think ye? if a man have an hundred sheep, and one of them "
        "be gone astray, doth he not leave the ninety and nine, and goeth into "
        "the mountains, and seeketh that which is gone astray? 13. And if so be "
        "that he find it, verily I say unto you, he rejoiceth more of that "
        "sheep, than of the ninety and nine which went not astray. 14. Even so "
        "it is not the will of your Father which is in heaven, that one of "
        "these little ones should perish.</p>\n"
        "<h1>Luke</h1>\n"
        "<h2>Chapter 15</h2>\n"
        "<p>3. And he spake this parable unto them, saying, 4. What man of you, "
        "having an hundred sheep, if he lose one of them, doth not leave the "
        "ninety and nine in the wilderness, and go after that which is lost, "
        "until he find it? 5. And when he hath found it, he layeth it on his "
        "shoulders, rejoicing. 6. And when he cometh home, he calleth together "
        "his friends and neighbours, saying unto them, Rejoice with me; for I "
        "have found my sheep which was lost. 7. I say unto you, that likewise "
        "joy shall be in heaven over one sinner that repenteth, more than over "
        "ninety and nine just persons, which need no repentance.</p>\n"
    )


@pytest.fixture
def non_html_scripture_text() -> str:
    return (
        "Matthew\n\n"
        "Chapter 18\n\n"
        "   12. How think ye? if a man have an hundred sheep, and one of them "
        "be gone astray, doth he not leave the ninety and nine, and goeth into "
        "the mountains, and seeketh that which is gone astray? 13. And if so be "
        "that he find it, verily I say unto you, he rejoiceth more of that "
        "sheep, than of the ninety and nine which went not astray. 14. Even so "
        "it is not the will of your Father which is in heaven, that one of "
        "these little ones should perish.\n\n\n"
        "Luke\n\n"
        "Chapter 15\n\n"
        "   3. And he spake this parable unto them, saying, 4. What man of you, "
        "having an hundred sheep, if he lose one of them, doth not leave the "
        "ninety and nine in the wilderness, and go after that which is lost, "
        "until he find it? 5. And when he hath found it, he layeth it on his "
        "shoulders, rejoicing. 6. And when he cometh home, he calleth together "
        "his friends and neighbours, saying unto them, Rejoice with me; for I "
        "have found my sheep which was lost. 7. I say unto you, that likewise "
        "joy shall be in heaven over one sinner that repenteth, more than over "
        "ninety and nine just persons, which need no repentance.\n"
    )


@pytest.fixture
def html_scripture_text_one_verse_per_paragraph() -> str:
    return (
        "<h1>Matthew</h1>\n"
        "<h2>Chapter 18</h2>\n"
        "<p>12. How think ye? if a man have an hundred sheep, and one of them "
        "be gone astray, doth he not leave the ninety and nine, and goeth into "
        "the mountains, and seeketh that which is gone astray?</p>\n"
        "<p>13. And if so be that he find it, verily I say unto you, he rejoiceth "
        "more of that sheep, than of the ninety and nine which went not astray.</p>\n"
        "<p>14. Even so it is not the will of your Father which is in heaven, "
        "that one of these little ones should perish.</p>\n"
        "<h2>Chapter 19</h2>\n"
        "<p>1. And it came to pass, that when Jesus had finished these sayings, he "
        "departed from Galilee, and came into the coasts of Judaea beyond "
        "Jordan;</p>\n"
    )


@pytest.fixture
def verse_text() -> str:
    return "1. In the beginning God created the heaven and the earth."


@pytest.fixture
def verse_text_no_verse_number() -> str:
    return "In the beginning God created the heaven and the earth."


@pytest.fixture
def kjv_parser() -> BibleParser:
    return bible.get_parser(version=bible.Version.KING_JAMES)


@pytest.fixture
def asv_parser() -> BibleParser:
    return bible.get_parser(version=bible.Version.AMERICAN_STANDARD)


@pytest.fixture
def short_verse_id_list() -> List[int]:
    return [
        1001001,
        2020003,
        41009038,
        41009046,
    ]


@pytest.fixture
def short_verse_data_json() -> Dict[str, str]:
    return {
        "1001001": "In the beginning God created the heaven and the earth.",
        "2020003": "Thou shalt have no other gods before me.",
        "41009038": "And John answered him, saying, Master, we saw one casting "
        "out devils in thy name, and he followeth not us: and we "
        "forbad him, because he followeth not us.",
        "41009046": "Where their worm dieth not, and the fire is not quenched.",
    }


@pytest.fixture
def short_verse_data_json_asv() -> Dict[str, str]:
    return {
        "1001001": "In the beginning God created the heavens and the earth.",
        "2020003": "Thou shalt have no other gods before me.",
        "41009038": "John said unto him, Teacher, we saw one casting out demons in "
        "thy name; and we forbade him, because he followed not us.",
        "41009046": "",
    }


@pytest.fixture
def short_book_title_data_json() -> Dict[str, List[str]]:
    return {
        "1": ["The First Book of Moses, called Genesis", "Genesis"],
        "2": ["The Second Book of Moses, called Exodus", "Exodus"],
        "41": ["THE GOSPEL ACCORDING TO ST. MARK", "Mark"],
    }


@pytest.fixture
def short_book_title_data_json_asv() -> Dict[str, List[str]]:
    return {
        "1": ["The First Book of Moses, Commonly Called Genesis", "Genesis"],
        "2": ["The Second Book of Moses, Commonly Called Exodus", "Exodus"],
        "41": ["The Gospel According to Mark", "Mark"],
    }


@pytest.fixture
def long_book_title() -> str:
    return "The First Book of Moses, called Genesis"


@pytest.fixture
def short_book_title() -> str:
    return "Genesis"


# noinspection SpellCheckingInspection
@pytest.fixture
def book_alternative_names() -> Dict[bible.Book, List[str]]:
    return {
        bible.Book.GENESIS: [
            "Gen",
            "Gen.",
            "The First Book of Moses, called Genesis",
            "The First Book of Moses, Commonly Called Genesis",
        ],
        bible.Book.EXODUS: [
            # "Ex",  # This may match too many things
            # "Ex.",  # This may match too many things
            # "Exo",  # This may match too many things
            # "Exo.",  # This may match too many things
            "Exod",
            "Exod.",
            "The Second Book of Moses, called Exodus",
            "The Second Book of Moses, Commonly Called Exodus",
        ],
        bible.Book.LEVITICUS: [
            "Lev",
            "Lev.",
            "The Third Book of Moses, called Leviticus",
            "The Third Book of Moses, Commonly Called Leviticus",
        ],
        bible.Book.NUMBERS: [
            "Num",
            "Num.",
            "The Fourth Book of Moses, called Numbers",
            "The Fourth Book of Moses, Commonly Called Numbers",
        ],
        bible.Book.DEUTERONOMY: [
            "Deut",
            "Deut.",
            "The Fifth Book of Moses, Commonly Called Deuteronomy",
            "The Fifth Book of Moses, called Deuteronomy",
        ],
        bible.Book.JOSHUA: [
            "Josh",
            "Josh.",
            "The Book of Joshua",
        ],
        bible.Book.JUDGES: [
            "The Book of Judges",
        ],
        bible.Book.RUTH: [
            "The Book of Ruth",
        ],
        bible.Book.SAMUEL_1: [
            "1 Sam",
            "1 Sam.",
            "I Sam",
            "I Sam.",
            "I Samuel",
            "The First Book of Samuel",
            "The First Book of Samuel Otherwise Called The First Book of the Kings",
        ],
        bible.Book.SAMUEL_2: [
            "2 Sam",
            "2 Sam.",
            "II Sam",
            "II Sam.",
            "II Samuel",
            "The Second Book of Samuel",
            "The Second Book of Samuel Otherwise Called The Second Book of the Kings",
        ],
        bible.Book.KINGS_1: [
            "1 Kgs",
            "1 Kgs.",
            "I Kgs",
            "I Kgs.",
            "I Kings",
            "The First Book of the Kings",
            "The First Book of the Kings, Commonly Called the Third Book of the Kings",
        ],
        bible.Book.KINGS_2: [
            "2 Kgs",
            "2 Kgs.",
            "II Kgs",
            "II Kgs.",
            "II Kings",
            "The Second Book of the Kings",
            "The Second Book of the Kings, Commonly Called the Fourth Book of the Kings",
        ],
        bible.Book.CHRONICLES_1: [
            "1 Chr",
            "1 Chr.",
            "1 Chro",
            "1 Chro.",
            "1 Chron",
            "1 Chron.",
            "I Chr",
            "I Chr.",
            "I Chro",
            "I Chro.",
            "I Chron",
            "I Chron.",
            "I Chronicles",
            "The First Book of the Chronicles",
        ],
        bible.Book.CHRONICLES_2: [
            "2 Chr",
            "2 Chr.",
            "2 Chro",
            "2 Chro.",
            "2 Chron",
            "2 Chron.",
            "II Chr",
            "II Chr.",
            "II Chro",
            "II Chro.",
            "II Chron",
            "II Chron.",
            "II Chronicles",
            "The Second Book of the Chronicles",
        ],
        bible.Book.EZRA: [
            "The Book of Ezra",
        ],
        bible.Book.NEHEMIAH: [
            "Neh",
            "Neh.",
            "The Book of Nehemiah",
        ],
        bible.Book.ESTHER: [
            "Esth",
            "Esth.",
            "The Book of Esther",
        ],
        bible.Book.JOB: [
            "The Book of Job",
        ],
        bible.Book.PSALMS: [
            "Ps",
            "Ps.",
            "Psa",
            "Psa.",
            "Psalm",
            "The Psalms",
            "The Book of Psalms",
        ],
        bible.Book.PROVERBS: [
            "Prov",
            "Prov.",
            "The Proverbs",
        ],
        bible.Book.ECCLESIASTES: [
            "Ecc",
            "Ecc.",
            "Eccl",
            "Eccl.",
            "Eccles",
            "Eccles.",
            "Ecclesiastes or, the Preacher",
        ],
        bible.Book.SONG_OF_SONGS: [
            "Song",
            "Song of Sol",
            "Song of Sol.",
            "Song of Solomon",
            "THE SONG OF SOLOMON",
        ],
        bible.Book.ISAIAH: [
            "Isa",
            "Isa.",
            "The Book of Isaiah",
            "The Book of the Prophet Isaiah",
        ],
        bible.Book.JEREMIAH: [
            "Jer",
            "Jer.",
            "The Book of Jeremiah",
            "The Book of the Prophet Jeremiah",
        ],
        bible.Book.LAMENTATIONS: [
            "Lam",
            "Lam.",
            "The Lamentations of Jeremiah",
        ],
        bible.Book.EZEKIEL: [
            "Ezek",
            "Ezek.",
            "The Book of Ezekiel",
            "The Book of the Prophet Ezekiel",
        ],
        bible.Book.DANIEL: [
            "Dan",
            "Dan.",
            "The Book of Daniel",
        ],
        bible.Book.HOSEA: [
            "Hos",
            "Hos.",
            "The Book of Hosea",
        ],
        bible.Book.JOEL: [
            "The Book of Joel",
        ],
        bible.Book.AMOS: [
            "The Book of Amos",
        ],
        bible.Book.OBADIAH: [
            "Obad",
            "Obad.",
            "The Book of Obadiah",
        ],
        bible.Book.JONAH: [
            "Jon",
            "Jon.",
            "The Book of Jonah",
        ],
        bible.Book.MICAH: [
            "Mic",
            "Mic.",
            "The Book of Micah",
        ],
        bible.Book.NAHUM: [
            "Nah",
            "Nah.",
            "The Book of Nahum",
        ],
        bible.Book.HABAKKUK: [
            "Hab",
            "Hab.",
            "The Book of Habakkuk",
        ],
        bible.Book.ZEPHANIAH: [
            "Zeph",
            "Zeph.",
            "The Book of Zephaniah",
        ],
        bible.Book.HAGGAI: [
            "Hag",
            "Hag.",
            "The Book of Haggai",
        ],
        bible.Book.ZECHARIAH: [
            "Zech",
            "Zech.",
            "The Book of Zechariah",
        ],
        bible.Book.MALACHI: [
            "Mal",
            "Mal.",
            "The Book of Malachi",
        ],
        bible.Book.MATTHEW: [
            "Matt",
            "Matt.",
            "The Gospel According to Matthew",
            "The Gospel According to St. Matthew",
        ],
        bible.Book.MARK: [
            "The Gospel According to Mark",
            "The Gospel According to St. Mark",
        ],
        bible.Book.LUKE: [
            "The Gospel According to Luke",
            "The Gospel According to St. Luke",
        ],
        bible.Book.JOHN: [
            "The Gospel According to John",
            "The Gospel According to St. John",
        ],
        bible.Book.ACTS: [
            "The Acts",
            "Acts of the Apostles",
            "The Acts of the Apostles",
        ],
        bible.Book.ROMANS: [
            "Rom",
            "Rom.",
            "The Epistle of Paul to the Romans",
            "THE EPISTLE OF PAUL THE APOSTLE TO THE ROMANS",
        ],
        bible.Book.CORINTHIANS_1: [
            "1 Cor",
            "1 Cor.",
            "I Cor",
            "I Cor.",
            "I Corinthians",
            "The First Epistle of Paul to the Corinthians",
            "THE FIRST EPISTLE OF PAUL THE APOSTLE TO THE CORINTHIANS",
        ],
        bible.Book.CORINTHIANS_2: [
            "2 Cor",
            "2 Cor.",
            "II Cor",
            "II Cor.",
            "II Corinthians",
            "The Second Epistle of Paul to the Corinthians",
            "THE SECOND EPISTLE OF PAUL THE APOSTLE TO THE CORINTHIANS",
        ],
        bible.Book.GALATIANS: [
            "Gal",
            "Gal.",
            "The Epistle of Paul to the Galatians",
            "THE EPISTLE OF PAUL THE APOSTLE TO THE GALATIANS",
        ],
        bible.Book.EPHESIANS: [
            "Eph",
            "Eph.",
            "The Epistle of Paul to the Ephesians",
            "THE EPISTLE OF PAUL THE APOSTLE TO THE EPHESIANS",
        ],
        bible.Book.PHILIPPIANS: [
            "Phil",
            "Phil.",
            "The Epistle of Paul to the Philippians",
            "THE EPISTLE OF PAUL THE APOSTLE TO THE PHILIPPIANS",
        ],
        bible.Book.COLOSSIANS: [
            "Col",
            "Col.",
            "The Epistle of Paul to the Colossians",
            "THE EPISTLE OF PAUL THE APOSTLE TO THE COLOSSIANS",
        ],
        bible.Book.THESSALONIANS_1: [
            "1 Th",
            "1 Th.",
            "1 Thess",
            "1 Thess.",
            "I Th",
            "I Th.",
            "I Thess",
            "I Thess.",
            "I Thessalonians",
            "The First Epistle of Paul to the Thessalonians",
            "THE FIRST EPISTLE OF PAUL THE APOSTLE TO THE THESSALONIANS",
        ],
        bible.Book.THESSALONIANS_2: [
            "2 Th",
            "2 Th.",
            "2 Thess",
            "2 Thess.",
            "II Th",
            "II Th.",
            "II Thess",
            "II Thess.",
            "II Thessalonians",
            "The Second Epistle of Paul to the Thessalonians",
            "THE SECOND EPISTLE OF PAUL THE APOSTLE TO THE THESSALONIANS",
        ],
        bible.Book.TIMOTHY_1: [
            "1 Tim",
            "1 Tim.",
            "I Tim",
            "I Tim.",
            "I Timothy",
            "The First Epistle of Paul to Timothy",
            "THE FIRST EPISTLE OF PAUL THE APOSTLE TO TIMOTHY",
        ],
        bible.Book.TIMOTHY_2: [
            "2 Tim",
            "2 Tim.",
            "II Tim",
            "II Tim.",
            "II Timothy",
            "The Second Epistle of Paul to Timothy",
            "THE SECOND EPISTLE OF PAUL THE APOSTLE TO TIMOTHY",
        ],
        bible.Book.TITUS: [
            "Tit",
            "Tit.",
            "The Epistle of Paul to Titus",
            "THE EPISTLE OF PAUL THE APOSTLE TO TITUS",
        ],
        bible.Book.PHILEMON: [
            "Phlm",
            "Phlm.",
            "Phile",
            "Phile.",
            "Philem",
            "Philem.",
            "The Epistle of Paul to Philemon",
            "THE EPISTLE OF PAUL THE APOSTLE TO PHILEMON",
        ],
        bible.Book.HEBREWS: [
            "Heb",
            "Heb.",
            "The Epistle to the Hebrews",
            "THE EPISTLE OF PAUL THE APOSTLE TO THE HEBREWS",
        ],
        bible.Book.JAMES: [
            "Jas",
            "Jas.",
            "The Epistle of James",
            "THE GENERAL EPISTLE OF JAMES",
        ],
        bible.Book.PETER_1: [
            "1 Pet",
            "1 Pet.",
            "I Pet",
            "I Pet.",
            "I Peter",
            "The First Epistle of Peter",
            "THE FIRST EPISTLE GENERAL OF PETER",
        ],
        bible.Book.PETER_2: [
            "2 Pet",
            "2 Pet.",
            "II Pet",
            "II Pet.",
            "II Peter",
            "The Second Epistle of Peter",
            "THE SECOND EPISTLE GENERAL OF PETER",
        ],
        bible.Book.JOHN_1: [
            "I John",
            "The First Epistle of John",
            "THE FIRST EPISTLE GENERAL OF JOHN",
        ],
        bible.Book.JOHN_2: [
            "II John",
            "The Second Epistle of John",
            "THE SECOND EPISTLE OF JOHN",
        ],
        bible.Book.JOHN_3: [
            "III John",
            "The Third Epistle of John",
            "THE THIRD EPISTLE OF JOHN",
        ],
        bible.Book.JUDE: [
            "The Epistle of Jude",
            "THE GENERAL EPISTLE OF JUDE",
        ],
        bible.Book.REVELATION: [
            "Rev",
            "Rev.",
            "Revelation of Jesus Christ",
            "The Revelation of John",
            "THE REVELATION OF ST. JOHN THE DIVINE",
        ],
    }
