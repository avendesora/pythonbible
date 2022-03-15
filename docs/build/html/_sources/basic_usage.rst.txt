Basic Usage
===========

Finding Scripture References in Text
------------------------------------

Given a text, you can search for scripture references and return any that are found in a list of :ref:`NormalizedReferences <NormalizedReference>` using the :ref:`get_references` function.

For example, given the text "The parable of the lost sheep is told in Matthew 18:12-14 and Luke 15:3-7." the :ref:`get_references` function should return a list of two :ref:`NormalizedReferences <NormalizedReference>`: one for Matthew 18:12-14 and another for Luke 15:3-7.

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    bible.get_references(
        "The parable of the lost sheep is told in Matthew 18:12-14 and Luke 15:3-7."
    )

.. output-cell:: python
    :execution-count: 1

    [
        NormalizedReference(book=<Book.MATTHEW: 40>, start_chapter=18, start_verse=12, end_chapter=18, end_verse=14, end_book=None),
        NormalizedReference(book=<Book.LUKE: 42>, start_chapter=15, start_verse=3, end_chapter=15, end_verse=7, end_book=None)
    ]

Converting References to Verse IDs
----------------------------------

Any single verse can be identified by an integer that contains the book, chapter, and verse information. The first 1-2 digits of the integer verse id represent the book, the next 3 digits represent the chapter, and the last 3 digits represent the verse.

For example, "Genesis 1:1" would be represented as the integer ``1001001``.

"John 3:16" would be represented as ``43003016``. The book of John is the 43rd book of the Bible, ``003`` represents the 3rd chapter, and ``016`` represents the 16th verse.

Since the book, chapter, and verses are standardized and unlikely to change, this allows us to reference verses in a very efficient way.

Converting a Single Reference to a List of Verse IDs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given a normalized scripture reference, which can contain one or more verses, the :ref:`convert_reference_to_verse_ids` function will convert that normalized scripture reference into a list of verse id integers.

For example, given the following normalized scripture reference for Genesis 1:1-4:

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    bible.convert_reference_to_verse_ids(
        bible.NormalizedReference(bible.Book.GENESIS, 1, 1, 1, 4)
    )

The conversion functionality would return the following list of verse id integers:

.. output-cell:: python
    :execution-count: 1

    [1001001, 1001002, 1001003, 1001004]

Converting a List of References to a List of Verse IDs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you need to convert a list of references (rather than a single reference) to a list of verse ids, use the :ref:`convert_references_to_verse_ids` function rather than the :ref:`convert_reference_to_verse_ids` function.

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    bible.convert_references_to_verse_ids([
        bible.NormalizedReference(bible.Book.MATTHEW, 18, 12, 18, 14),
        bible.NormalizedReference(bible.Book.LUKE, 15, 3, 15, 7),
    ])

.. output-cell:: python
    :execution-count: 1

    [40018012, 40018013, 40018014, 42015003, 42015004, 42015005, 42015006, 42015007]

Converting Verse IDs to References
----------------------------------

We can also take a list of integer verse ids and convert it back into a list of normalized references using the :ref:`convert_verse_ids_to_references` function.

For example, the following list of verse ids represents the references Matthew 18:12-14 and Luke 15:3-7.

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    bible.convert_verse_ids_to_references(
        [40018012, 40018013, 40018014, 42015003, 42015004, 42015005, 42015006, 42015007]
    )

The conversion functionality would return the following list of normalized scripture references.

.. output-cell:: python
    :execution-count: 1

    [
        NormalizedReference(book=<Book.MATTHEW: 40>, start_chapter=18, start_verse=12, end_chapter=18, end_verse=14. end_book=None),
        NormalizedReference(book=<Book.LUKE: 42>, start_chapter=15, start_verse=3, end_chapter=15, end_verse=7, end_book=None),
    ]

Formatting Scripture References
-------------------------------

The **pythonbible** library includes functionality to format normalized scripture references into a human-readable string for display/print through the :ref:`format_scripture_references` function.

This functionality sorts the list of references so that they appear in the same order they would in the Bible and also combines verses into ranges when possible.

For example:

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    bible.format_scripture_references(
        bible.get_references(
            "My favorite verses are Philippians 4:8, Isaiah 55:13, and Philippians 4:4-7."
        )
    )

.. output-cell:: python
    :execution-count: 1

    'Isaiah 55:13;Philippians 4:4-8'

Formatting Scripture Text - BETA
--------------------------------

This is still a work in progress, but there is some exising functionality related to this.

There is a separate Python library **pythonbible-parser** that parses OSIS formatted XML files (and potentially other formats in the future) and generates python objects that contain the text of the Scripture. In the future it should also contain additional formatting and notes. That output for certain versions (namely American Standard Version) have been added to the **pythonbible** library in order to format scripture text for display and print.

To format a single version, use the :ref:`get_verse_text` function.

For example:

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    bible.get_verse_text(1001001)

.. output-cell:: python
    :execution-count: 1

    'In the beginning God created the heavens and the earth.'
