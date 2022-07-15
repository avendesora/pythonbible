Technical Reference
===================

.. _Book:

Book
----

.. py:class:: Book

    Book is an ``IntEnum`` that contains all of the books of the Bible

    :param name: the unique text identifier of the book
    :type name: str
    :param value: the unique numerical identifier of the book
    :type value: int
    :param title: the common English name of the book
    :type title: str


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

.. py:class:: BookGroup

    BookGroup is an ``Enum`` containing the default Bible book groupings

    :param name: the unique text identifier of the book group
    :type name: str
    :param value: the unique numerical identifier of the book group
    :type value: int
    :param regular_expression: the regular expression used to find mentions of the book group when searching for references
    :type regular_expression: str
    :param books: the list of books included in the book group
    :type books: List[str]

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

.. py:function:: pythonbible.convert_reference_to_verse_ids(reference)

    Converts the given :ref:`NormalizedReference` object into a list of verse id integers.

    :param reference: A normalized reference
    :type reference: :ref:`NormalizedReference`
    :return: The list of verse ids associated with the reference
    :rtype: List[int]

.. _convert_references_to_verse_ids:

convert_references_to_verse_ids
-------------------------------

.. py:function:: pythonbible.convert_references_to_verse_ids(references)

    Converts the given list of :ref:`NormalizedReference` objects into a list of verse id integers.

    :param references: A list of normalized references
    :type references: List[:ref:`NormalizedReference`]
    :return: The list of verse ids associated with the references
    :rtype: List[int]

.. _convert_verse_ids_to_references:

convert_verse_ids_to_references
-------------------------------

.. py:function:: pythonbible.convert_verse_ids_to_references(verse_ids)

    Converts the given list of verse id integers into a list of :ref:`NormalizedReference` objects.

    :param verse_ids: A list of verse ids
    :type verse_ids: List[int]
    :return: The list of normalized references associated with the verse ids
    :rtype: List[:ref:`NormalizedReference`]
    :raises InvalidVerseError: if one or more of the verse_ids does not correspond to a valid verse

.. _count_books:

count_books
-----------

.. py:function:: pythonbible.count_books(references)

    Returns the count of books of the Bible included in the given list of references.

    :param references: A list of normalized references
    :type references: List[:ref:`NormalizedReference`]
    :return: The count of books of the Bible included in the given list of references
    :rtype: int

.. _count_chapters:

count_chapters
--------------

.. py:function:: pythonbible.count_chapters(references)

    Returns the count of chapters of books the Bible included in the given list of references.

    :param references: A list of normalized references
    :type references: List[:ref:`NormalizedReference`]
    :return: The count of chapters of books of the Bible included in the given list of references
    :rtype: int

.. _count_verses:

count_verses
------------

.. py:function:: pythonbible.count_verses(references)

    Returns the count of verses included in the given list of references.

    :param references: A list of normalized references
    :type references: List[:ref:`NormalizedReference`]
    :return: The count of verses included in the given list of references
    :rtype: int

.. _format_scripture_references:

format_scripture_references
---------------------------

.. py:function:: pythonbible.format_scripture_references(references, **kwargs)

    Returns a human-readable string of the given normalized scripture references

    :param references: A list of normalized scripture references
    :type references: List[:ref:`NormalizedReference`]
    :return: A human-readable string of the given normalized scripture references
    :rtype: str

.. _format_scripture_text:

format_scripture_text
---------------------

.. py:function:: pythonbible.format_scripture_text(verse_ids, **kwargs)

    Returns the formatted scripture text for the given list of verse IDs.

    :param verse_ids: A list of integer verse ids
    :type verse_ids: List[int]
    :return: The formatted scripture text for the verse ids
    :rtype: str

.. _format_single_reference:

format_single_reference
-----------------------

.. py:function:: pythonbible.format_single_reference(reference, include_books, include_chapters)

    Returns a human-readable string of the given normalized scripture reference

    :param reference: A normalized scripture reference
    :type reference: :ref:`NormalizedReference`
    :param include_books: If True includes the book title(s) in the returned reference string, defaults to True
    :type include_books: bool
    :param include_chapters: If True includes the chapter number(s) in the returned reference string, defaults to True
    :type include_chapters: bool
    :return: A human-readable string of the given normalized scripture reference
    :rtype: str

.. _get_book_chapter_verse:

get_book_chapter_verse
----------------------

.. py:function:: pythonbible.get_book_chapter_verse(verse_id)

    Returns the :ref:`Book`, chapter number, and verse number for the given verse id

    :param verse_id: a verse id
    :type verse_id: int
    :return: A tuple containing the :ref:`Book`, chapter number, and verse number for the given verse id
    :rtype: Tuple[:ref:`Book`, int, int]
    :raises InvalidVerseError: if the verse id does not correspond to a valid verse

.. _get_book_number:

get_book_number
---------------

.. py:function:: pythonbible.get_book_number(verse_id)

    Returns the book number for the given verse id

    :param verse_id: a verse id
    :type verse_id: int
    :return: The book number for the given verse id
    :rtype: int

.. _get_book_titles:

get_book_titles
---------------

.. py:function:: pythonbible.get_book_titles(book, version)

    Returns the book titles for the given :ref:`Book` and optional :ref:`Version`

    :param book: a book of the Bible
    :type book: :ref:`Book`
    :param version: a version of the Bible, defaults to American Standard
    :type version: :ref:`Version`
    :return: the long and short titles of the given book and version
    :rtype: Optional[BookTitles]
    :raises MissingBookFileError: if the book file for the given book and version does not exist

.. _get_chapter_number:

get_chapter_number
------------------

.. py:function:: pythonbible.get_chapter_number(verse_id)

    Returns the chapter number for the given verse id

    :param verse_id: a verse id
    :type verse_id: int
    :return: The chapter number for the given verse id
    :rtype: int

.. _get_number_of_chapters:

get_number_of_chapters
----------------------

.. py:function:: pythonbible.get_number_of_chapters(book)

    Return the number of chapters in a :ref:`Book` of the Bible

    :param book: a book of the Bible
    :type book: :ref:`Book`
    :return: the number of chapters in the given book of the Bible
    :rtype: int

.. _get_number_of_verses:

get_number_of_verses
------------------------

.. py:function:: pythonbible.get_number_of_verses(book, chapter)

    Return the number of verses in a :ref:`Book` and chapter

    :param book: a book of the Bible
    :type book: :ref:`Book`
    :param chapter: a chapter of the given book of the Bible
    :type chapter: int
    :return: the number of verses in the given book and chapter
    :rtype: int
    :raises InvalidChapterError: if the given chapter isn't a valid chapter for the given book

.. _get_references:

get_references
--------------

.. py:function:: pythonbible.get_references(text, book_groups=None)

    Searches the text for scripture references and returns any that are found in a list of normalized tuple references.

    :param text: String that may contain zero or more scripture references
    :type text: str
    :param book_groups: Optional dictionary of :ref:`BookGroup` (e.g. Old Testament) to its related regular expression
    :type book_groups: Dict[str, List[:ref:`Book`]] or None
    :return: The list of found scripture references
    :rtype: List[:ref:`NormalizedReference`]

.. _get_verse_id:

get_verse_id
------------

.. py:function:: pythonbible.get_verse_id(book, chapter, verse)

    Return the verse id for the given :ref:`Book`, chapter number, and verse number

    :param book: a book of the Bible
    :type book: :ref:`Book`
    :param chapter: a chapter number for the given book of the Bible
    :type chapter: int
    :param verse: a verse number for the given book and chapter
    :type verse: int
    :return: the verse id for the given book, chapter, and verse
    :rtype: int
    :raises InvalidVerseError: if the verse doesn't exist for the given book, chapter, and verse

.. _get_verse_number:

get_verse_number
----------------

.. py:function:: pythonbible.get_verse_number(verse_id)

    Returns the verse number for the given verse id

    :param verse_id: a verse id
    :type verse_id: int
    :return: The verse number for the given verse id
    :rtype: int

.. _get_verse_text:

get_verse_text
--------------

.. py:function:: pythonbible.get_verse_text(verse_id, version)

    Returns the scripture text of the given verse id and version of the Bible.

    :param verse_id: a verse id
    :type verse_id: int
    :param version: a version of the Bible, defaults to American Standard
    :type version: :ref:`Version`
    :return: The scripture text of the given verse id and version
    :rtype: str
    :raises InvalidVerseError: if the given verse id does not correspond to a valid verse
    :raises MissingVerseFileError: if the verse file for the given verse_id and version does not exist

.. _InvalidBookError:

InvalidBookError
----------------

.. py:exception:: pythonbible.InvalidBookError

    Raised when the book id is not valid

.. _InvalidChapterError:

InvalidChapterError
-------------------

.. py:exception:: pythonbible.InvalidChapterError

    Raised when the chapter number is not a valid chapter number for the given book of the Bible

.. _InvalidVerseError:

InvalidVerseError
-----------------

.. py:exception:: pythonbible.InvalidVerseError

    Raised when the verse id or book, chapter, and verse number being processed is not a valid Bible verse

.. _is_valid_book:

is_valid_book
-------------

.. py:function:: pythonbible.is_valid_book(book)

    Checks to see if the given :ref:`Book` is a valid book of the Bible

    :param book: a book of the Bible
    :type book: :ref:`Book`
    :return: True if the given book is valid; otherwise, False
    :rtype: bool

.. _is_valid_chapter:

is_valid_chapter
----------------

.. py:function:: pythonbible.is_valid_chapter(book, chapter)

    Checks to see if the given :ref:`Book` is a valid book of the Bible; and, if so, checks to see if the given chapter number is a valid chapter number for the given book

    :param book: a book of the Bible
    :type book: :ref:`Book`
    :param chapter: a chapter number for the given book of the Bible
    :type chapter: int
    :return: True if the given book and chapter are valid; otherwise, False
    :rtype: bool

.. _is_valid_reference:

is_valid_reference
------------------

.. py:function:: pythonbible.is_valid_reference(reference)

    Checks to see if the given :ref:`NormalizedReference` is a valid scripture reference (i.e. all of the verses in the reference are valid verses)

    :param reference: a normalized reference
    :type reference: :ref:`NormalizedReference`
    :return: True if the reference is valid; otherwise, False
    :rtype: bool

.. _is_valid_verse:

is_valid_verse
--------------

.. py:function:: pythonbible.is_valid_verse(book, chapter, verse)

    Checks to see if the given :ref:`Book` is a valid book of the Bible, then checks to see if the given chapter number is a valid chapter number for the given book, then checks to see if the given verse number is a valid verse number for the given book and chapter

    :param book: a book of the Bible
    :type book: :ref:`Book`
    :param chapter: a chapter number for the given book of the Bible
    :type chapter: int
    :param verse: a verse number for the given book and chapter
    :type verse: int
    :return: True if the given book, chapter, and verse are valid; otherwise, False
    :rtype: bool

.. _is_valid_verse_id:

is_valid_verse_id
-----------------

.. py:function:: pythonbible.is_valid_verse_id(verse_id)

    Checks to see if the given verse_id corresponds to a valid verse in the Bible

    :param verse_id: a verse id
    :type verse_id: int
    :return: True if the verse_id is in the list of valid verse ids; otherwise, False
    :rtype: bool

.. _MissingBookFileError:

MissingBookFileError
--------------------

.. py:exception:: pythonbible.MissingBookFileError

    Raised when the book file for a given version is not found

.. _MissingVerseFileError:

MissingVerseFileError
---------------------

.. py:exception:: pythonbible.MissingVerseFileError

    Raised when the verse file for a given version is not found

.. _NormalizedReference:

NormalizedReference
-------------------

.. py:class:: pythonbible.NormalizedReference

    NormalizedReference is a dataclass that represents a single scripture reference that contains one or more consecutive verses

    :param book: the first book of the Bible in the reference
    :type book: :ref:`Book`
    :param start_chapter: the number of the first chapter in the reference
    :type start_chapter: int
    :param start_verse: the number of the first verse in the reference
    :type start_verse: int
    :param end_chapter: the number of the last chapter in the reference
    :type end_chapter: int
    :param end_verse: the number of the last verse in the reference
    :type end_verse: int
    :param end_book: the last book of the Bible in the reference if the reference contains more than one book, defaults to None
    :type end_book: :ref:`Book`


.. _Version:

Version
-------

.. py:class:: pythonbible.Version

    Version is an ``Enum`` containing all of the currently known Ancient Language and English versions of the Bible

    :param name: the unique text identifier of the version
    :type name: str
    :param value: the unique numerical identifier of the version
    :type value: int
    :param title: the English title of the version
    :type title: str
