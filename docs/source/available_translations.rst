Available Translations
======================

The ``pythonbible`` package supports multiple Bible translations with the following goals:

* Provide all open source and public domain translations of the Bible as optional packages that can be installed with ``pythonbible`` or separately.
* Provide a consistent API for accessing Bible text across all translations.
* Allow users to bring their own translations by extending the :ref:`Bible` class and using the :ref:`add_bible` function. This would allow users to use copyrighted translations with ``pythonbible`` assuming they have the proper license to do so.


The following table lists the Bible translations that are currently available for installation via pip extras, along with their corresponding installation codes and version enum values. We hope to add more translations, especially in languages other than English, in the future.

.. csv-table:: Available Translations
    :header: "Title", "Code (for installation)", "Version Enum Value", "PyPI Package Name"
    :widths: 2, 1, 1, 1

    "American King James Version", "AKJV", "AMERICAN_KING_JAMES", "pythonbible-akjv"
    "American Standard Version", "ASV", "AMERICAN_STANDARD", "pythonbible-asv"
    "Bible in Basic English", "BBE", "BIBLE_IN_BASIC_ENGLISH", "pythonbible-bbe"
    "Bible in WorldWide English NT", "BWE", "WORLDWIDE_ENGLISH", "pythonbible-bwe"
    "Darby", "DAR", "DARBY", "pythonbible-darby"
    "Diaglot NT - 1865", "Diaglot", "DIAGLOT_NT", "pythonbible-diaglot"
    "Douay-Rheims", "DR", "DOUAY_RHEIMS", "pythonbible-dr"
    "The Emphasized Bible by J. B. Rotherham", "ROTH", "ROTHERHAM", "pythonbible-roth"
    "Geneva Bible", "GB", "GENEVA", "pythonbible-gb"
    "King James Version", "KJV", "KING_JAMES", "pythonbible-kjv"
    "Leeser Old Testament", "LEESER", "LEESER", "pythonbible-leeser"
    "Living Oracles NT", "LONT", LIVING_ORACLES_NT, "pythonbible-lont"
    "Modern KJV 1963", "MKJV1963", "KING_JAMES_MODERN_1963", "pythonbible-mkjv1963"
    "Montgomery New Testament", "MONT", "MONTGOMERY_NT", "pythonbible-mont"
    "New Heart English Bible", "NHEB", "NEW_HEART", "pythonbible-nheb"
    "Open English Bible", "OEB", "OPEN_ENGLISH", "pythonbible-oeb"
    "The Peschito Syriac New Testament", "ETHERIDGE", "ETHERIDGE", "pythonbible-etheridge"
    "Revised 1833 Webster Version", "RWEBSTER", "REVISED_WEBSTER", "pythonbible-rwebster"
    "Revised Young's Literal Translation NT", "RYLT", "REVISED_YOUNGS", "pythonbible-rylt"
    "Updated King James Version", "UKJV", "KING_JAMES_UPDATED", "pythonbible-ukjv"
    "Webster", "WBS", "WEBSTER", "pythonbible-wbs"
    "Wesley's New Testament", "WESLEY", "WESLEYS_NT", "pythonbible-wesley"
    "Weymouth NT", "WMTH", "WEYMOUTH_NT", "pythonbible-wmth"
    "Willam Tyndale Bible", "TYN", "TYNDALE", "pythonbible-tyn"
    "World English Bible", "WEB", "WORLD_ENGLISH", "pythonbible-web"
    "Wycliffe Bible", "WYC", "WYCLIFFE", "pythonbible-wyc"
    "Young's Literal Translation of the Bible", "YLT", "YOUNGS", "pythonbible-ylt"
