Technical Reference
===================

.. _Book:

Book
----

.. autoclass:: pythonbible.Book
    :members:


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

.. _BookGroup:

BookGroup
---------

.. autoclass:: pythonbible.BookGroup
    :members:

.. csv-table:: Book Group Members
    :header: "Name", "Value", "Regular Expression", "Books"
    :widths: 3, 1, 2, 3

    OLD_TESTAMENT, 1, "Old Testament", "Genesis, Exodus, Leviticus, Numbers, Deuteronomy, Joshua, Judges, Ruth, 1 Samuel, 2 Samuel, 1 Kings, 2 Kings, 1 Chronicles, 2 Chronicles, Ezra, Nehemiah, Esther, Job, Psalms, Proverbs, Ecclesiastes, Song of Songs, Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel, Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi"
    OLD_TESTAMENT_LAW, 2, "Law", "Genesis, Exodus, Leviticus, Numbers, Deuteronomy"
    OLD_TESTAMENT_HISTORY, 3, "History", "Joshua, Judges, Ruth, 1 Samuel, 2 Samuel, 1 Kings, 2 Kings, 1 Chronicles, 2 Chronicles, Ezra, Nehemiah, Esther"
    OLD_TESTAMENT_POETRY_WISDOM, 4, "Poetry|Wisdom", "Job, Psalms, Proverbs, Ecclesiastes, Song of Songs"
    OLD_TESTAMENT_PROPHECY, 5, "Prophecy", "Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel, Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi"
    OLD_TESTAMENT_MAJOR_PROPHETS, 6, "Major Prophets", "Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel"
    OLD_TESTAMENT_MINOR_PROPHETS, 7, "Minor Prophets", "Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi"
    NEW_TESTAMENT, 8, "New Testament", "Matthew, Mark, Luke, John, Acts, Romans, 1 Corinthians, 2 Corinthians, Galatians, Ephesians, Philippians, Colossians, 1 Thessalonians, 2 Thessalonians, 1 Timothy, 2 Timothy, Titus, Philemon, Hebrews, James, 1 Peter, 2 Peter, 1 John, 2 John, 3 John, Jude, Revelation"
    NEW_TESTAMENT_GOSPELS, 9, "Gospels", "Matthew, Mark, Luke, John"
    NEW_TESTAMENT_HISTORY, 10, "History", "Acts"
    NEW_TESTAMENT_EPISTLES, 11, "Epistles", "Romans, 1 Corinthians, 2 Corinthians, Galatians, Ephesians, Philippians, Colossians, 1 Thessalonians, 2 Thessalonians, 1 Timothy, 2 Timothy, Titus, Philemon, Hebrews, James, 1 Peter, 2 Peter, 1 John, 2 John, 3 John, Jude"
    NEW_TESTAMENT_PAUL_EPISTLES, 12, "Pauline Epistles|Paul's Epistles|Epistles of Paul", "Romans, 1 Corinthians, 2 Corinthians, Galatians, Ephesians, Philippians, Colossians, 1 Thessalonians, 2 Thessalonians, 1 Timothy, 2 Timothy, Titus, Philemon"
    NEW_TESTAMENT_GENERAL_EPISTLES, 13, "General Epistles", "Hebrews, James, 1 Peter, 2 Peter, 1 John, 2 John, 3 John, Jude"
    NEW_TESTAMENT_APOCALYPTIC, 14, "Apocalyptic", "Revelation"

.. _BOOK_GROUPS:

BOOK_GROUPS
-----------

``BOOK_GROUPS`` is a provided "constant" containing the default dictionary of book groups to be used when allowing book groups to be considered when getting all of the references contained within a text.

For each entry in this dictionary, the key is the regular expression string associated with the given book group, and the value is the list of :ref:`Book` objects associated with the given book group.

``BOOK_GROUPS`` contains all of the :ref:`BookGroup` values listed in the table above.

.. _convert_reference_to_verse_ids:

convert_reference_to_verse_ids
------------------------------

.. autofunction:: pythonbible.convert_reference_to_verse_ids

.. _convert_references_to_verse_ids:

convert_references_to_verse_ids
-------------------------------

.. autofunction:: pythonbible.convert_references_to_verse_ids

.. _convert_verse_ids_to_references:

convert_verse_ids_to_references
-------------------------------

.. autofunction:: pythonbible.convert_verse_ids_to_references

.. _count_books:

count_books
-----------

.. autofunction:: pythonbible.count_books

.. _count_chapters:

count_chapters
--------------

.. autofunction:: pythonbible.count_chapters

.. _count_verses:

count_verses
------------

.. autofunction:: pythonbible.count_verses

.. _format_scripture_references:

format_scripture_references
---------------------------

.. autofunction:: pythonbible.format_scripture_references

.. _format_scripture_text:

format_scripture_text
---------------------

.. autofunction:: pythonbible.format_scripture_text

.. _format_single_reference:

format_single_reference
-----------------------

.. autofunction:: pythonbible.format_single_reference

.. _get_book_chapter_verse:

get_book_chapter_verse
----------------------

.. autofunction:: pythonbible.get_book_chapter_verse

.. _get_book_number:

get_book_number
---------------

.. autofunction:: pythonbible.get_book_number

.. _get_book_titles:

get_book_titles
---------------

.. autofunction:: pythonbible.get_book_titles

.. _get_chapter_number:

get_chapter_number
------------------

.. autofunction:: pythonbible.get_chapter_number

.. _get_number_of_chapters:

get_number_of_chapters
----------------------

.. autofunction:: pythonbible.get_number_of_chapters

.. _get_number_of_verses:

get_number_of_verses
--------------------

.. autofunction:: pythonbible.get_number_of_verses

.. _get_references:

get_references
--------------

.. autofunction:: pythonbible.get_references

.. _get_verse_id:

get_verse_id
------------

.. autofunction:: pythonbible.get_verse_id

.. _get_verse_number:

get_verse_number
----------------

.. autofunction:: pythonbible.get_verse_number

.. _get_verse_text:

get_verse_text
--------------

.. autofunction:: pythonbible.get_verse_text

.. _InvalidBookError:

InvalidBookError
----------------

.. autoexception:: pythonbible.InvalidBookError
    :members:

.. _InvalidChapterError:

InvalidChapterError
-------------------

.. autoexception:: pythonbible.InvalidChapterError
    :members:

.. _InvalidVerseError:

InvalidVerseError
-----------------

.. autoexception:: pythonbible.InvalidVerseError
    :members:

.. _is_valid_book:

is_valid_book
-------------

.. autofunction:: pythonbible.is_valid_book

.. _is_valid_chapter:

is_valid_chapter
----------------

.. autofunction:: pythonbible.is_valid_chapter

is_valid_reference
------------------

.. autofunction:: pythonbible.is_valid_reference

.. _is_valid_verse:

is_valid_verse
--------------

.. autofunction:: pythonbible.is_valid_verse

.. _is_valid_verse_id:

is_valid_verse_id
-----------------

.. autofunction:: pythonbible.is_valid_verse_id

.. _MissingBookFileError:

MissingBookFileError
--------------------

.. autoexception:: pythonbible.MissingBookFileError
    :members:

.. _MissingVerseFileError:

MissingVerseFileError
---------------------

.. autoexception:: pythonbible.MissingVerseFileError
    :members:

.. _NormalizedReference:

NormalizedReference
-------------------

.. autoclass:: pythonbible.NormalizedReference

.. _Version:

Version
-------

.. autoclass:: pythonbible.Version
    :members:
