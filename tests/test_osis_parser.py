import pythonbible as bible


def test_get_scripture_passage_text(verse_ids_complex):
    # Given a list of verse ids
    # When we get the scripture passage for those verses
    parser = bible.OSISParser(bible.Version.KING_JAMES)
    passage = parser.get_scripture_passage_text(verse_ids_complex)

    # Then the scripture passage is correct.
    assert len(passage) == 4
    assert list(passage.keys()) == [
        bible.Book.PSALMS,
        bible.Book.JEREMIAH,
        bible.Book.MATTHEW,
        bible.Book.LUKE,
    ]

    psalms = passage.get(bible.Book.PSALMS)
    assert len(psalms) == 1
    assert list(psalms.keys()) == [
        130,
    ]

    psalm_130 = psalms.get(130)
    assert len(psalm_130) == 2
    assert psalm_130 == [
        "4. there is forgiveness with thee, that thou mayest be feared.",
        "8. And he shall redeem Israel from all his iniquities.",
    ]

    jeremiah = passage.get(bible.Book.JEREMIAH)
    assert len(jeremiah) == 3
    assert list(jeremiah.keys()) == [
        29,
        30,
        31,
    ]

    jeremiah_29 = jeremiah.get(29)
    assert len(jeremiah_29) == 1
    assert jeremiah_29 == [
        "32. Therefore thus saith the Behold, I will punish Shemaiah the Nehelamite, and his seed: he shall not have a man to dwell among this people; neither shall he behold the good that I will do for my people, saith the because he hath taught rebellion against the"
    ]

    jeremiah_30 = jeremiah.get(30)
    assert len(jeremiah_30) == 3
    assert jeremiah_30 == [
        "1. The word that came to Jeremiah from the saying, 2. Thus speaketh the God of Israel, saying, Write thee all the words that I have spoken unto thee in a book. 3. For, lo, the days come, saith the that I will bring again the captivity of my people Israel and Judah, saith the and I will cause them to return to the land that I gave to their fathers, and they shall possess it.",
        "4. are the words that the spake concerning Israel and concerning Judah. 5. For thus saith the We have heard a voice of trembling, of fear, and not of peace. 6. Ask ye now, and see whether a man doth travail with child? wherefore do I see every man with his hands on his loins, as a woman in travail, and all faces are turned into paleness? 7. Alas! for that day is great, so that none is like it: it is even the time of Jacob’s trouble; but he shall be saved out of it. 8. For it shall come to pass in that day, saith the of hosts, that I will break his yoke from off thy neck, and will burst thy bonds, and strangers shall no more serve themselves of him: 9. But they shall serve the their God, and David their king, whom I will raise up unto them.",
        "10. Therefore fear thou not, O my servant Jacob, saith the neither be dismayed, O Israel: for, lo, I will save thee from afar, and thy seed from the land of their captivity; and Jacob shall return, and shall be in rest, and be quiet, and none shall make him afraid.",
    ]

    jeremiah_31 = jeremiah.get(31)
    assert len(jeremiah_31) == 1
    assert jeremiah_31 == [
        "12. Therefore they shall come and sing in the height of Zion, and shall flow together to the goodness of the for wheat, and for wine, and for oil, and for the young of the flock and of the herd: and their soul shall be as a watered garden; and they shall not sorrow any more at all."
    ]

    matthew = passage.get(bible.Book.MATTHEW)
    assert len(matthew) == 2
    assert list(matthew.keys()) == [
        1,
        2,
    ]

    matthew_1 = matthew.get(1)
    assert len(matthew_1) == 1
    assert matthew_1 == [
        "18. Now the birth of Jesus Christ was on this wise: When as his mother Mary was espoused to Joseph, before they came together, she was found with child of the Holy Ghost. 19. Then Joseph her husband, being a just man, and not willing to make her a publick example, was minded to put her away privily. 20. But while he thought on these things, behold, the angel of the Lord appeared unto him in a dream, saying, Joseph, thou son of David, fear not to take unto thee Mary thy wife: for that which is conceived in her is of the Holy Ghost. 21. And she shall bring forth a son, and thou shalt call his name JESUS: for he shall save his people from their sins. 22. Now all this was done, that it might be fulfilled which was spoken of the Lord by the prophet, saying, 23. Behold, a virgin shall be with child, and shall bring forth a son, and they shall call his name Emmanuel, which being interpreted is, God with us. 24. Then Joseph being raised from sleep did as the angel of the Lord had bidden him, and took unto him his wife: 25. And knew her not till she had brought forth her firstborn son: and he called his name JESUS."
    ]

    matthew_2 = matthew.get(2)
    assert len(matthew_2) == 3
    assert matthew_2 == [
        "1. Now when Jesus was born in Bethlehem of Judaea in the days of Herod the king, behold, there came wise men from the east to Jerusalem, 2. Saying, Where is he that is born King of the Jews? for we have seen his star in the east, and are come to worship him. 3. When Herod the king had heard these things, he was troubled, and all Jerusalem with him. 4. And when he had gathered all the chief priests and scribes of the people together, he demanded of them where Christ should be born. 5. And they said unto him, In Bethlehem of Judaea: for thus it is written by the prophet, 6. And thou Bethlehem, in the land of Juda, art not the least among the princes of Juda: for out of thee shall come a Governor, that shall rule my people Israel. 7. Then Herod, when he had privily called the wise men, enquired of them diligently what time the star appeared. 8. And he sent them to Bethlehem, and said, Go and search diligently for the young child; and when ye have found him, bring me word again, that I may come and worship him also. 9. When they had heard the king, they departed; and, lo, the star, which they saw in the east, went before them, till it came and stood over where the young child was. 10. When they saw the star, they rejoiced with exceeding great joy.",
        "11. And when they were come into the house, they saw the young child with Mary his mother, and fell down, and worshipped him: and when they had opened their treasures, they presented unto him gifts; gold, and frankincense, and myrrh. 12. And being warned of God in a dream that they should not return to Herod, they departed into their own country another way. 13. And when they were departed, behold, the angel of the Lord appeareth to Joseph in a dream, saying, Arise, and take the young child and his mother, and flee into Egypt, and be thou there until I bring thee word: for Herod will seek the young child to destroy him. 14. When he arose, he took the young child and his mother by night, and departed into Egypt: 15. And was there until the death of Herod: that it might be fulfilled which was spoken of the Lord by the prophet, saying, Out of Egypt have I called my son.",
        "16. Then Herod, when he saw that he was mocked of the wise men, was exceeding wroth, and sent forth, and slew all the children that were in Bethlehem, and in all the coasts thereof, from two years old and under, according to the time which he had diligently enquired of the wise men. 17. Then was fulfilled that which was spoken by Jeremy the prophet, saying, 18. In Rama was there a voice heard, lamentation, and weeping, and great mourning, Rachel weeping for her children, and would not be comforted, because they are not.",
    ]

    luke = passage.get(bible.Book.LUKE)
    assert len(luke) == 1
    assert list(luke.keys()) == [
        3,
    ]

    luke_3 = luke.get(3)
    assert len(luke_3) == 1
    assert luke_3 == [
        "5. Every valley shall be filled, and every mountain and hill shall be brought low; and the crooked shall be made straight, and the rough ways shall be made smooth; 6. And all flesh shall see the salvation of God. 7. Then said he to the multitude that came forth to be baptized of him, O generation of vipers, who hath warned you to flee from the wrath to come?"
    ]


def test_get_scripture_passage_text_no_numbers(verse_ids_complex):
    # Given a list of verse ids
    # When we get the scripture passage for those verses
    parser = bible.OSISParser(bible.Version.KING_JAMES)
    passage = parser.get_scripture_passage_text(
        verse_ids_complex, include_verse_number=False
    )

    # Then the scripture passage is correct.
    assert len(passage) == 4
    assert list(passage.keys()) == [
        bible.Book.PSALMS,
        bible.Book.JEREMIAH,
        bible.Book.MATTHEW,
        bible.Book.LUKE,
    ]

    psalms = passage.get(bible.Book.PSALMS)
    assert len(psalms) == 1
    assert list(psalms.keys()) == [
        130,
    ]

    psalm_130 = psalms.get(130)
    assert len(psalm_130) == 2
    assert psalm_130 == [
        "there is forgiveness with thee, that thou mayest be feared.",
        "And he shall redeem Israel from all his iniquities.",
    ]

    jeremiah = passage.get(bible.Book.JEREMIAH)
    assert len(jeremiah) == 3
    assert list(jeremiah.keys()) == [
        29,
        30,
        31,
    ]

    jeremiah_29 = jeremiah.get(29)
    assert len(jeremiah_29) == 1
    assert jeremiah_29 == [
        "Therefore thus saith the Behold, I will punish Shemaiah the Nehelamite, and his seed: he shall not have a man to dwell among this people; neither shall he behold the good that I will do for my people, saith the because he hath taught rebellion against the"
    ]

    jeremiah_30 = jeremiah.get(30)
    assert len(jeremiah_30) == 3
    assert jeremiah_30 == [
        "The word that came to Jeremiah from the saying, Thus speaketh the God of Israel, saying, Write thee all the words that I have spoken unto thee in a book. For, lo, the days come, saith the that I will bring again the captivity of my people Israel and Judah, saith the and I will cause them to return to the land that I gave to their fathers, and they shall possess it.",
        "are the words that the spake concerning Israel and concerning Judah. For thus saith the We have heard a voice of trembling, of fear, and not of peace. Ask ye now, and see whether a man doth travail with child? wherefore do I see every man with his hands on his loins, as a woman in travail, and all faces are turned into paleness? Alas! for that day is great, so that none is like it: it is even the time of Jacob’s trouble; but he shall be saved out of it. For it shall come to pass in that day, saith the of hosts, that I will break his yoke from off thy neck, and will burst thy bonds, and strangers shall no more serve themselves of him: But they shall serve the their God, and David their king, whom I will raise up unto them.",
        "Therefore fear thou not, O my servant Jacob, saith the neither be dismayed, O Israel: for, lo, I will save thee from afar, and thy seed from the land of their captivity; and Jacob shall return, and shall be in rest, and be quiet, and none shall make him afraid.",
    ]

    jeremiah_31 = jeremiah.get(31)
    assert len(jeremiah_31) == 1
    assert jeremiah_31 == [
        "Therefore they shall come and sing in the height of Zion, and shall flow together to the goodness of the for wheat, and for wine, and for oil, and for the young of the flock and of the herd: and their soul shall be as a watered garden; and they shall not sorrow any more at all."
    ]

    matthew = passage.get(bible.Book.MATTHEW)
    assert len(matthew) == 2
    assert list(matthew.keys()) == [
        1,
        2,
    ]

    matthew_1 = matthew.get(1)
    assert len(matthew_1) == 1
    assert matthew_1 == [
        "Now the birth of Jesus Christ was on this wise: When as his mother Mary was espoused to Joseph, before they came together, she was found with child of the Holy Ghost. Then Joseph her husband, being a just man, and not willing to make her a publick example, was minded to put her away privily. But while he thought on these things, behold, the angel of the Lord appeared unto him in a dream, saying, Joseph, thou son of David, fear not to take unto thee Mary thy wife: for that which is conceived in her is of the Holy Ghost. And she shall bring forth a son, and thou shalt call his name JESUS: for he shall save his people from their sins. Now all this was done, that it might be fulfilled which was spoken of the Lord by the prophet, saying, Behold, a virgin shall be with child, and shall bring forth a son, and they shall call his name Emmanuel, which being interpreted is, God with us. Then Joseph being raised from sleep did as the angel of the Lord had bidden him, and took unto him his wife: And knew her not till she had brought forth her firstborn son: and he called his name JESUS."
    ]

    matthew_2 = matthew.get(2)
    assert len(matthew_2) == 3
    assert matthew_2 == [
        "Now when Jesus was born in Bethlehem of Judaea in the days of Herod the king, behold, there came wise men from the east to Jerusalem, Saying, Where is he that is born King of the Jews? for we have seen his star in the east, and are come to worship him. When Herod the king had heard these things, he was troubled, and all Jerusalem with him. And when he had gathered all the chief priests and scribes of the people together, he demanded of them where Christ should be born. And they said unto him, In Bethlehem of Judaea: for thus it is written by the prophet, And thou Bethlehem, in the land of Juda, art not the least among the princes of Juda: for out of thee shall come a Governor, that shall rule my people Israel. Then Herod, when he had privily called the wise men, enquired of them diligently what time the star appeared. And he sent them to Bethlehem, and said, Go and search diligently for the young child; and when ye have found him, bring me word again, that I may come and worship him also. When they had heard the king, they departed; and, lo, the star, which they saw in the east, went before them, till it came and stood over where the young child was. When they saw the star, they rejoiced with exceeding great joy.",
        "And when they were come into the house, they saw the young child with Mary his mother, and fell down, and worshipped him: and when they had opened their treasures, they presented unto him gifts; gold, and frankincense, and myrrh. And being warned of God in a dream that they should not return to Herod, they departed into their own country another way. And when they were departed, behold, the angel of the Lord appeareth to Joseph in a dream, saying, Arise, and take the young child and his mother, and flee into Egypt, and be thou there until I bring thee word: for Herod will seek the young child to destroy him. When he arose, he took the young child and his mother by night, and departed into Egypt: And was there until the death of Herod: that it might be fulfilled which was spoken of the Lord by the prophet, saying, Out of Egypt have I called my son.",
        "Then Herod, when he saw that he was mocked of the wise men, was exceeding wroth, and sent forth, and slew all the children that were in Bethlehem, and in all the coasts thereof, from two years old and under, according to the time which he had diligently enquired of the wise men. Then was fulfilled that which was spoken by Jeremy the prophet, saying, In Rama was there a voice heard, lamentation, and weeping, and great mourning, Rachel weeping for her children, and would not be comforted, because they are not.",
    ]

    luke = passage.get(bible.Book.LUKE)
    assert len(luke) == 1
    assert list(luke.keys()) == [
        3,
    ]

    luke_3 = luke.get(3)
    assert len(luke_3) == 1
    assert luke_3 == [
        "Every valley shall be filled, and every mountain and hill shall be brought low; and the crooked shall be made straight, and the rough ways shall be made smooth; And all flesh shall see the salvation of God. Then said he to the multitude that came forth to be baptized of him, O generation of vipers, who hath warned you to flee from the wrath to come?"
    ]
