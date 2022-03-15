Advanced Usage
==============

Single Chapter Books
--------------------

Several books of the Bible only contain one chapter, and there is some special functionality in pythonbible related to this.

Finding References
^^^^^^^^^^^^^^^^^^

When parsing a given text to find all the references contained within, if we find a reference for a single chapter book that contains only one number, rather than both chapter and verse numbers, we assume that number to be the verse number.

Example: Obadiah 1 vs Genesis 1
""""""""""""""""""""""""""""""""""

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    references = bible.get_references("Obadiah 1")
    references[0]

.. output-cell:: python
    :execution-count: 1

    NormalizedReference(
        book=<Book.OBADIAH: 31>,
        start_chapter=1,
        start_verse=1,
        end_chapter=1,
        end_verse=1,
        end_book=None
    )

If a reference like this was found for a non single chapter book, the number would be assumed to be a chapter number rather than a verse number.

.. code-cell:: python
    :execution-count: 2

    references = bible.get_references("Genesis 1")
    references[0]

.. output-cell:: python
    :execution-count: 2

    NormalizedReference(
        book=<Book.GENESIS: 1>,
        start_chapter=1,
        start_verse=1,
        end_chapter=1,
        end_verse=31,
        end_book=None
    )

Rather than being interpreted as Genesis 1:1, this would be interpreted as Genesis 1:1-31.

Example: Philemon 3-6 vs Genesis 3-6
"""""""""""""""""""""""""""""""""""""""

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    references = bible.get_references("Philemon 3-6")
    references[0]

.. output-cell:: python
    :execution-count: 1

    NormalizedReference(
        book=<Book.PHILEMON: 57>,
        start_chapter=1,
        start_verse=3,
        end_chapter=1,
        end_verse=6,
        end_book=None
    )

This is interpreted as Philemon 1:3-6. If a similar reference were encountered for a non single chapter book, both numbers would be assumed to be chapter numbers rather than verse numbers.

.. code-cell:: python
    :execution-count: 2

    import pythonbible as bible

    references = bible.get_references("Genesis 3-6")
    references[0]

.. output-cell:: python
    :execution-count: 2

    NormalizedReference(
        book=<Book.GENESIS: 1>,
        start_chapter=3,
        start_verse=1,
        end_chapter=6,
        end_verse=22,
        end_book=None
    )

Rather than being interpreted as Genesis 1:3-6, this would be interpreted as Genesis 3:1-6:22.

Converting References to Verse IDs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because normalized references in pythonbible always explicitly include chapter and verse numbers, there is no difference in how references are converted to verse ids for single chapter books.

Converting Verse IDs to References
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because verse ids in pythonbible always explicitly include chapter and verse numbers, there is no difference in how verse ids are converted to references for single chapter books.

Formatting References for Print/Display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, when formatting references for print/display for references of a single chapter book, the chapter number will not be included.

For example:

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    references = bible.get_references("Jude 2-8")
    bible.format_references(references)

.. output-cell:: python
    :execution-count: 1

    'Jude 2-8'

The result should be the same even if the the chapter number is included in the original reference string.

.. code-cell:: python
    :execution-count: 2

    references = bible.get_references("Jude 1:2-8")
    bible.format_references(references)

.. output-cell:: python
    :execution-count: 2

    'Jude 2-8'

Always Include Chapter Numbers
""""""""""""""""""""""""""""""

If you want to force **pythonbible** to include the chapter numbers even for single chapter books, you can use the ``always_include_chapter_numbers`` optional parameter of the :ref:`format_scripture_references` or :ref:`format_single_reference` functions, setting that optional parameter to be ``True``.

For example:

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    references = bible.get_references("Jude 2-8")
    bible.format_references(references, always_include_chapter_numbers=True)

.. output-cell:: python
    :execution-count: 1

    'Jude 1:2-8'

Multi Book References
---------------------

It is possible for a single reference to be a range that spans more than one book of the Bible.

For example, the following references are all equally referencing the entire first five books of the Bible:

* Genesis - Deuteronomy
* Genesis 1 - Deuteronomy 34
* Genesis 1:1 - Deuteronomy 34:12

Finding References
^^^^^^^^^^^^^^^^^^

When parsing a given text to find all the references contained within, if we find a ranged reference like those above that span multiple books of the Bible, we should parse that into a single normalized reference that includes the optional end_book attribute.

For example, "Genesis - Deuteronomy" vs "Genesis;Exodus;Numbers;Leviticus;Deuteronomy":

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    bible.get_references("Genesis - Deuteronomy")

.. output-cell:: python
    :execution-count: 1

    [
        NormalizedReference(book=<Book.GENESIS: 1>, start_chapter=1, start_verse=1, end_chapter=34, end_verse=12, end_book=<Book.DEUTERONOMY: 5>),
    ]

If rather than using the range, the text specified each book of the Bible separated by a comma or semi-colon (or just about anything), then the result would be a list of five normalized references, one for each of the five books referenced.

.. code-cell:: python
    :execution-count: 2

    bible.get_references("Genesis;Exodus;Leviticus;Numbers;Deuteronomy")

.. output-cell:: python
    :execution-count: 2

    [
        NormalizedReference(book=<Book.GENESIS: 1>, start_chapter=1, start_verse=1, end_chapter=50, end_verse=26, end_book=None),
        NormalizedReference(book=<Book.EXODUS: 2>, start_chapter=1, start_verse=1, end_chapter=40, end_verse=38, end_book=None),
        NormalizedReference(book=<Book.LEVITICUS: 3>, start_chapter=1, start_verse=1, end_chapter=27, end_verse=34, end_book=None),
        NormalizedReference(book=<Book.NUMBERS: 4>, start_chapter=1, start_verse=1, end_chapter=36, end_verse=13, end_book=None),
        NormalizedReference(book=<Book.DEUTERONOMY: 5>, start_chapter=1, start_verse=1, end_chapter=34, end_verse=12, end_book=None),
    ]

That list can optionally be optimized by converting it to verse ids and then back into references if so desired.

.. code-cell:: python
    :execution-count: 3

    references = bible.get_references("Genesis;Exodus;Leviticus;Numbers;Deuteronomy")
    verse_ids = bible.convert_references_to_verse_ids(references)
    bible.convert_verse_ids_to_references(verse_ids)

.. output-cell:: python
    :execution-count: 3

    [
        NormalizedReference(book=<Book.GENESIS: 1>, start_chapter=1, start_verse=1, end_chapter=34, end_verse=12, end_book=<Book.DEUTERONOMY: 5>),
    ]

That optimization is optional as it can degrade performance for processing large ranges if that particular optimization is not necessary. This optimization will be run automatically when the list of references is formatted into a Scripture reference string.

Converting References to Verse IDs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Whether a multi book range reference is in a single normalized reference or a list of one normalized reference for each book does not affect the results of converting that reference into a list of verse ids.

Converting Verse Ids to References
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When converting a list of verse ids into a list of references, multi book range references will always be optimized into a single normalized reference when possible.

Formatting References for Print/Display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As mentioned earlier, when formatting references for print/display, pythonbible always optimizes the list of references into as few references as possible by using multi book range references.

By default, chapter numbers will not be included when the entire book is included in the reference.

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    references = bible.get_references("Genesis - Deuteronomy")
    bible.format_scripture_references(references)

.. output-cell:: python
    :execution-count: 1

    'Genesis - Deuteronomy'

Always Include Chapter Numbers
""""""""""""""""""""""""""""""

If you want to force **pythonbible** to include the chapter numbers even when the entire book is covered by the reference, you can use the ``always_include_chapter_numbers`` optional parameter of the :ref:`format_scripture_references` or :ref:`format_single_reference` functions, setting that optional parameter to be ``True``.

For example:

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    references = bible.get_references("Genesis - Deuteronomy")
    bible.format_scripture_references(references, always_include_chapter_numbers=True)

.. output-cell:: python
    :execution-count: 1

    'Genesis 1:1 - Deuteronomy 34:12'

Book Groups
-----------

The books of the Bible can be categorized into different groups.

The first and biggest categorization is dividing the books into the Old Testament (Genesis - Malachi) and the New Testament (Matthew - Revelation).

Within the Old Testament, the books can be further divided as follows:

* Law (Genesis - Deuteronomy)
* History (Joshua - Esther)
* Poetry/Wisdom (Job - Song of Solomon)
* Prophecy (Isaiah - Malachi)

The Prophecy books can be further divided into:

* Major Prophets (Isaiah - Daniel)
* Minor Prophets (Hosea - Malachi)

Within the New Testament, the books can be divided as follows:

* Gospel (Matthew - John)
* History (Acts)
* Epistles (Romans - Jude)
* Apocalyptic (Revelation)

The Epistles can be further divided into:

* Pauline Epistles (Romans - Philemon)
* General Epistles (Hebrews - Jude)

Finding References by Book Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, when pythonbible parses text to find all references contained within, it does not take book groups into consideration.

For example:

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    bible.get_references("What are all of the books of the Old Testament?")

.. output-cell:: python
    :execution-count: 1

    []

Finding References by Default Book Groups
"""""""""""""""""""""""""""""""""""""""""

When parsing text to find all references contained within, you can pass in an optional ``book_groups`` parameter telling **pythonbible** what book groups to take into consideration.

The **pythonbible** library includes a ``book_groups`` value for you to use that includes all the book groups described above. To use that, pass :ref:`BOOK_GROUPS` as the value for the optional ``book_groups`` argument.

For example:

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    bible.get_references(
        "What are all of the books of the Old Testament?",
        book_groups=bible.BOOK_GROUPS
    )

.. output-cell:: python
    :execution-count: 1

    [
        NormalizedReference(book=<Book.GENESIS: 1>, start_chapter=1, start_verse=1, end_chapter=4, end_verse=6, end_book=<Book.MALACHI: 39>)
    ]

When formatting the resulting reference for print/display, the reference text will use the books (and chapters and verses, if needed) rather than the book group.

For example:

.. code-cell:: python
    :execution-count: 2

    references = bible.get_references(
        "What are all of the books of the Old Testament?",
        book_groups=bible.BOOK_GROUPS
    )
    bible.format_scripture_references(references)

.. output-cell:: python
    :execution-count: 2

    'Genesis - Malachi'

If you want to include the chapter and verse numbers, set the optional ``always_include_chapter_numbers`` argument to ``True`` for the :ref:`format_scripture_references` (or :ref:`format_single_reference`) function.

.. code-cell:: python
    :execution-count: 3

    bible.format_scripture_references(
        references,
        always_include_chapter_numbers=True
    )

.. output-cell:: python
    :execution-count: 3

    'Genesis 1:1 - Malachi 4:6'

Finding References by Custom Book Groups
""""""""""""""""""""""""""""""""""""""""

If you don't want to use the book groups as defined above but rather a subset of them or additional categorizations or completely custom categorizations, you can do that by passing in a custom value for the ``book_groups`` optional argument of the ``get_references`` function.

The expected type of the ``book_groups`` argument is a ``Dict[str, List[Book]]`` where the string key is a regular expression to be used to match to that particular book group, and the list of :ref:`Book` objects are the books of the Bible associated with that book group.

There is a :ref:`BookGroup` ``Enum`` included to help with this.

For example, if you wanted to only use the Old Testament and New Testament book groups, the following example using the default book groups would return too many references.

.. code-cell:: python
    :execution-count: 1

    import pythonbible as bible

    bible.get_references(
        "I want to find the Old Testament books, not the Gospels.",
        book_groups=bible.BOOK_GROUPS
    )

.. output-cell:: python
    :execution-count: 1

    [
        NormalizedReference(book=<Book.GENESIS: 1>, start_chapter=1, start_verse=1, end_chapter=4, end_verse=6, end_book=<Book.MALACHI: 39>),
        NormalizedReference(book=<Book.MATTHEW: 40>, start_chapter=1, start_verse=1, end_chapter=21, end_verse=25, end_book=<Book.JOHN: 43),
    ]

Instead, you will need to define a custom ``book_groups`` value containing only the Old and New Testament information.

.. code-cell:: python
    :execution-count: 2

    book_groups_subset = {
        bible.BookGroup.OLD_TESTAMENT.regular_expression: bible.BookGroup.OLD_TESTAMENT.books,
        bible.BookGroup.NEW_TESTAMENT.regular_expression: bible.BookGroup.NEW_TESTAMENT.books,
    }
    bible.get_references(
        "I want to find the Old Testament books, not the Gospels.",
        book_groups=book_groups_subset
    )

.. output-cell:: python
    :execution-count: 2

    [
        NormalizedReference(book=<Book.GENESIS: 1>, start_chapter=1, start_verse=1, end_chapter=4, end_verse=6, end_book=<Book.MALACHI: 39>),
    ]

With the custom subset book groups definition, only the Old Testament reference is included in the results and not the Gospels reference.

You can also define your own completely custom book groups definition. For example:

.. code-cell:: python
    :execution-count: 3

    custom_book_groups = {
        "my favorite books": [bible.Book.PSALMS, bible.Book.PROVERBS, bible.Book.JOHN, bible.Book.PHILIPPIANS, bible.Book.JAMES],
    }
    references = bible.get_references(
        "What are my favorite books of the Bible?",
        book_groups=custom_book_groups
    )

    print(f"My favorite books of the Bible are {bible.format_scripture_references(references)}!")

.. output-cell:: python
    :execution-count: 3

    'My favorite books of the Bible are Psalms - Proverbs;John;Philippians;James!'
