Technical Reference
===================

Book
----

``Book`` is an ``Enum`` containing all of the books of the Bible as members.


.. py:class:: Book

    :name: The string identifier of the book
    :value: The integer value of the book
    :title: The common English name of the book


.. csv-table:: Book Members
    :header: "Name", "Value", "Title"
    :widths: 3, 1, 3
    
    GENESIS, 1, Genesis
    EXODUS, 2, Exodus
    LEVITICUS, 3, Leviticus
    NUMBERS, 4, Numbers
    DEUTERONOMY, 5, Deuteronomy
    JOSHUA, 6, Joshua
    JUDGES, 7, Judges
    RUTH, 8, Ruth
    SAMUEL_1, 9, 1 Samuel
    SAMUEL_2, 10, 2 Samuel
    KINGS_1, 11, 1 Kings
    KINGS_2, 12, 2 Kings
    CHRONICLES_1, 13, 1 Chronicles
    CHRONICLES_2, 14, 2 Chronicles
    EZRA, 15, Ezra
    NEHEMIAH, 16, Nehemiah
    ESTHER, 17, Esther
    JOB, 18, Job
    PSALMS, 19, Psalms
    PROVERBS, 20, Proverbs
    ECCLESIASTES, 21, Ecclesiastes
    SONG_OF_SONGS, 22, Song of Songs
    ISAIAH, 23, Isaiah
    JEREMIAH, 24, Jeremiah
    LAMENTATIONS, 25, Lamentations
    EZEKIEL, 26, Ezekiel
    DANIEL, 27, Daniel
    HOSEA, 28, Hosea
    JOEL, 29, Joel
    AMOS, 30, Amos
    OBADIAH, 31, Obadiah
    JONAH, 32, Jonah
    MICAH, 33, Micah
    NAHUM, 34, Nahum
    HABAKKUK, 35, Habakkuk
    ZEPHANIAH, 36, Zephaniah
    HAGGAI, 37, Haggai
    ZECHARIAH, 38, Zechariah
    MALACHI, 39, Malachi
    MATTHEW, 40, Matthew
    MARK, 41, Mark
    LUKE, 42, Luke
    JOHN, 43, John
    ACTS, 44, Acts
    ROMANS, 45, Romans
    CORINTHIANS_1, 46, 1 Corinthians
    CORINTHIANS_2, 47, 2 Corinthians
    GALATIANS, 48, Galatians
    EPHESIANS, 49, Ephesians
    PHILIPPIANS, 50, Philippians
    COLOSSIANS, 51, Colossians
    THESSALONIANS_1, 52, 1 Thessalonians
    THESSALONIANS_2, 53, 2 Thessalonians
    TIMOTHY_1, 54, 1 Timothy
    TIMOTHY_2, 55, 2 Timothy
    TITUS, 56, Titus
    PHILEMON, 57, Philemon
    HEBREWS, 58, Hebrews
    JAMES, 59, James
    PETER_1, 60, 1 Peter
    PETER_2, 61, 2 Peter
    JOHN_1, 62, 1 John
    JOHN_2, 63, 2 John
    JOHN_3, 64, 3 John
    JUDE, 65, Jude
    REVELATION, 66, Revelation
    ESDRAS_1, 67, 1 Esdras
    TOBIT, 68, Tobit
    WISDOM_OF_SOLOMON, 69, Wisdom of Solomon
    ECCLESIASTICUS, 70, Ecclesiasticus
    MACCABEES_1, 71, 1 Maccabees
    MACCABEES_2, 72, 2 Maccabees

Book Abbreviations
------------------

The following abbreviations and alternate titles are currently supported when searching a given text for scripture references.

The search for references is case-insensitive; and, generally, a period trailing the abbreviation is optional (e.g. "Gen", "Gen.", "gen", and "gen." should all evaluate to "Genesis").

This list is subject to change (especially in pre 1.0 releases). If you see anything that needs to be changed, removed, and/or added, please submit an issue in GitHub (or submit a pull request - contributions are welcome).

.. csv-table:: Book Abbreviations
    :header: "Book", "Abbreviations and Alternate Titles"
    :widths: 1, 3

    Genesis, "Gen"
    Exodus, "Exod, Exo"
    Leviticus, "Lev"
    Numbers, "Num"
    Deuteronomy, "Deut, Deu"
    Joshua, "Josh, Jos, Jsh"
    Judges, "Judg, Jdgs, Jdg"
    Ruth, "Rut, Rth"
    1 Samuel, "1Samuel, I Samuel, 1st Samuel, First Samuel, 1 Sam, 1Sam, I Sam, 1st Sam, First Sam, 1 Sa, 1Sa, I Sa, 1st Sa, First Sa, 1 Sm, 1Sm, I Sm, 1st Sm, First Sm"
    2 Samuel, "2Samuel, II Samuel, 2nd Samuel, Second Samuel, 2 Sam, 2Sam, II Sam, 2nd Sam, Second Sam, 2 Sa, 2Sa, II Sa, 2nd Sa, Second Sa, 2 Sm, 2Sm, II Sm, 2nd Sm, Second Sm"
    1 Kings, "1Kings, I Kings, 1st Kings, First Kings, 1 Kgs, 1Kgs, I Kgs, 1st Kgs, First Kgs, 1 Kin, 1Kin, I Kin, 1st Kin, First Kin, 1 Ki, 1Ki, I Ki, 1st Ki, First Ki"
    2 Kings, "2Kings, II Kings, 2nd Kings, Second Kings, 2 Kgs, 2Kgs, II Kgs, 2nd Kgs, Second Kgs, 2 Kin, 2Kin, II Kin, 2nd Kin, Second Kin, 2 Ki, 2KI, I Ki, 2nd Ki, Second Ki"
    1 Chronicles, "1Chronicles, I Chronicles, 1st Chronicles, First Chronicles, 1 Chron, 1Chron, I Chron, 1st Chron, First Chron, 1 Chro, 1Chro, I Chro, 1st Chro, First Chro, 1 Chr, 1Chr, I Chr, 1st Chr, First Chr, 1 Ch, 1Ch, I Ch, 1st Ch, First Ch"
    2 Chronicles, "2Chronicles, II Chronicles, 2nd Chronicles, Second Chronicles, 2 Chron, 2Chron, II Chron, 2nd Chron, Second Chron, 2 Chro, 2Chro, II Chro, 2nd Chro, Second Chro, 2 Chr, 2Chr, II Chr, 2nd Chr, Second Chr, 2 Ch, 2Ch, II Ch, 2nd Ch, Second Ch"
    Ezra, "Ezr"
    Nehemiah, "Neh"
    Esther, "Esth, Est"
    Job, ""
    Psalms, "Psalm, Pslm, Psa, Psm, Pss, Ps"
    Proverbs, "Prov, Pro, Prv"
    Ecclesiastes, "Eccles, Eccle, Eccl, Ecc, Ec, Qoh"
    Song of Songs, "Song of Solomon, Song of Sol, Canticle of Canticles, Canticles, Cant, SOS"
    Isaiah, "Isa"
    Jeremiah, "Jer"
    Lamentations, "Lamentations of Jeremiah, Lam"
    Ezekiel, "Ezek, Eze, Ezk"
    Daniel, "Dan"
    Hosea, "Hos"
    Joel, "Joe"
    Amos, "Amo"
    Obadiah, "Obad, Oba"
    Jonah, "Jon, Jnh"
    Micah, "Mic"
    Nahum, "Nah"
    Habakkuk, "Hab"
    Zephaniah, "Zeph, Zep"
    Haggai, "Hag"
    Zechariah, "Zech, Zec"
    Malachi, "Mal"
    Matthew, "Matt, Mat"
    Mark, "Mar, Mrk"
    Luke, "Luk"
    John, "Joh, Jhn, Jo, Jn"
    Acts, "Acts of the Apostles, Act"
    Romans, "Rom"
    1 Corinthians, "1Corinthians, I Corinthians, 1st Corinthians, First Corinthians, 1 Cor, 1Cor, I Cor, 1st Cor, First Cor, 1 Co, 1Co, I Co, 1st Co, First Co"
    2 Corinthians, "2Corinthians, II Corinthians, 2nd Corinthians, Second Corinthians, 2 Cor, 2Cor, II Cor, 2nd Cor, Second Cor, 2 Co, 2Co, II Co, 2nd Co, Second Co"
    Galatians, "Gal"
    Ephesians, "Ephes, Eph"
    Philippians, "Phil, Php"
    Colossians, "Col"
    1 Thessalonians, "1Thessalonians, I Thessalonians, 1st Thessalonians, First Thessalonians, 1 Thess, 1Thess, I Thess, 1st Thess, First Thess, 1 Thes, 1Thes, I Thes, 1st Thes, First Thes, 1 Ths, 1Ths, I Ths, 1st Ths, First Ths"
    2 Thessalonians, "2Thessalonians, II Thessalonians, 2nd Thessalonians, Second Thessalonians, 2 Thess, 2Thess, II Thess, 2nd Thess, Second Thess, 2 Thes, 2Thes, II Thes, 2nd Thes, Second Thes, 2 Ths, 2Ths, II Ths, 2nd Ths, Second Ths"
    1 Timothy, "1Timothy, I Timothy, 1st Timothy, First Timothy, 1 Tim, 1Tim, I Tim, 1st Tim, First Tim, 1 Ti, 1Ti, I Ti, 1st Ti, First Ti"
    2 Timothy, "2Timothy, II Timothy, 2nd Timothy, Second Timothy, 2 Tim, 2Tim, II Tim, 2nd Tim, Second Tim, 2 Ti, 2Ti, II Ti, 2nd Ti, Second Ti"
    Titus, "Tit"
    Philemon, "Philem, Phile, Phlm, Phi, Phm"
    Hebrews, "Heb"
    James, "Jas"
    1 Peter, "1Peter, I Peter, 1st Peter, First Peter, 1 Pet, 1Pet, I Pet, 1st Pet, First Pet, 1 Pe, 1Pe, I Pe, 1st Pe, First Pe, 1 Pt, 1Pt, I Pt, 1st Pt, First Pt"
    2 Peter, "2Peter, II Peter, 2nd Peter, Second Peter, 2 Pet, 2Pet, II Pet, 2nd Pet, Second Pet, 2 Pe, 2Pe, II Pe, 2nd Pe, Second Pe, 2 Pt, 2Pt, II Pt, 2nd Pt, Second Pt"
    1 John, "1John, I John, 1st John, First John, 1 Joh, 1Joh, I Joh, 1st Joh, First Joh, 1 Jhn, 1Jhn, I Jhn, 1st Jhn, First Jhn, 1 Jo, 1Jo, I Jo, 1st Jo, First Jo, 1 Jn, 1Jn, I Jn, 1st Jn, First Jn"
    2 John, "2John, II John, 2nd John, Second John, 2 Joh, 2Joh, II Joh, 2nd Joh, Second Joh, 2 Jhn, 2Jhn, II Jhn, 2nd Jhn, Second Jhn, 2 Jo, 2Jo, II Jo, 2nd Jo, Second Jo, 2 Jn, 2Jn, II Jn, 2nd Jn, Second Jn"
    3 John, "3John, III John, 3rd John, Third John, 3 Joh, 3Joh, III Joh, 3rd Joh, Third Joh, 3 Jhn, 3Jhn, III Jhn, 3rd Jhn, Third Jhn, 3 Jo, 3Jo, III Jo, 3rd Jo, Third Jo, 3 Jn, 3Jn, III Jn, 3rd Jn, Third Jn"
    Jude, "Jud"
    Revelation, "Revelation of Jesus Christ, Revelation of John, Revelation of St. John the Divine, Rev, Rev of Jesus Christ, Rev of John, Rev of St. John the Divine"

BOOK_GROUPS
-----------

``BOOK_GROUPS`` is a provided "constant" containing the default dictionary of book groups to be used when allowing book groups to be considered when getting all of the references contained within a text.

For each entry in this dictionary, the key is the regular expression string associated with the given book group, and the value is the list of ``Book`` objects associated with the given book group.

The following book groups are included:

...

BookGroup
---------

...

convert_reference_to_verse_ids
------------------------------

...

convert_references_to_verse_ids
-------------------------------

...

convert_verse_ids_to_references
-------------------------------

...

count_books
-----------

...

count_chapters
--------------

...

count_verses
------------

...

format_scripture_references
---------------------------

...

format_scripture_text
---------------------

...

format_single_reference
-----------------------

...

get_book_chapter_verse
----------------------

...

get_book_number
---------------

...

get_book_titles
---------------

...

get_chapter_number
------------------

...

get_max_number_of_verses
------------------------

...

get_number_of_chapters
----------------------

...

get_references
--------------

...

get_verse_id
------------

...

get_verse_number
----------------

...

get_verse_text
--------------

...

InvalidBookError
----------------

...

InvalidChapterError
-------------------

...

InvalidVerseError
-----------------

...

is_valid_book
-------------

...

is_valid_chapter
----------------

...

is_valid_reference
------------------

...

is_valid_verse
--------------

...

is_valid_verse_id
-----------------

...

MissingBookFileError
--------------------

...

MissingVerseFileError
---------------------

...

NormalizedReference
-------------------

...

Version
-------

...