---
sidebar_position: 3
---

# Book Groups

## What Are Book Groups?

The books of the Bible can be categorized into different groups.

The first and biggest categorization is dividing the books into the ``Old Testament`` (Genesis - Malachi) and the ``New Testament`` (Matthew - Revelation).

Within the Old Testament, the books can be further divided as follows:

 * ``Law`` (Genesis - Deuteronomy)
 * ``History`` (Joshua - Esther)
 * ``Poetry/Wisdom`` (Job - Song of Solomon)
 * ``Prophecy`` (Isaiah - Malachi)

The Prophecy books can be further divided into:

 * ``Major Prophets`` (Isaiah - Daniel)
 * ``Minor Prophets`` (Hosea - Malachi)

Within the New Testament, the books can be divided as follows:

 * ``Gospel`` (Matthew - John)
 * ``History`` (Acts)
 * ``Epistles`` (Romans - Jude)
 * ``Apocalyptic`` (Revelation)

The Epistles can be further divided into:

 * ``Pauline Epistles`` (Romans - Philemon)
 * ``General Epistles`` (Hebrews - Jude)

## Finding References by Book Groups

By default, when pythonbible parses text to find all references contained within, it does not take book groups into consideration.

For example:

```python title="Code"
import pythonbible as bible

references = bible.get_references("What are all of the books of the Old Testament?")
```

```python title="Result"
[]
```

### Finding References by Default Book Groups

When parsing text to find all references contained within, you can pass in an optional ``book_groups`` parameter telling pythonbible what book groups to take into consideration.

The pythonbible library includes a ``book_groups`` value for you to use that includes all the book groups described above. To use that, pass ``bible.BOOK_GROUPS`` as the value for the optional ``book_groups`` argument.

For example:

```python title="Code"
import pythonbible as bible

references = bible.get_references(
    "What are all of the books of the Old Testament?",
    book_groups=bible.BOOK_GROUPS
)
```

```python title="Result"
[
    NormalizedReference(
        book=<Book.GENESIS: 1>,
        start_chapter=1,
        start_verse=1,
        end_chapter=4,
        end_verse=6,
        end_book=<Book.MALACHI: 39>
    )
]
```

When formatting the resulting reference for print/display, the reference text will use the books (and chapters and verses, if needed) rather than the book group.

For example:

```python title="Code"
import pythonbible as bible

references = bible.get_references(
    "What are all of the books of the Old Testament?",
    book_groups=bible.BOOK_GROUPS
)
reference_string = bible.format_scripture_references(references)
```

```python title="Result"
'Genesis - Malachi'
```

If you want to include the chapter and verse numbers, set the optional ``always_include_chapter_numbers`` argument to ``True`` for the ``format_scripture_references`` (or ``format_single_reference``) function.

```python title="Code"
import pythonbible as bible

references = bible.get_references(
    "What are all of the books of the Old Testament?",
    book_groups=bible.BOOK_GROUPS
)
reference_string = bible.format_scripture_references(
    references,
    always_include_chapter_numbers=True
)
```

```python title="Result"
'Genesis 1:1 - Malachi 4:6'
```

### Finding References by Custom Book Groups

If you don't want to use the book groups as defined above but rather a subset of them or additional categorizations or completely custom categorizations, you can do that by passing in a custom value for the ``book_groups`` optional argument of the ``get_references`` function.

The expected type of the ``book_groups`` argument is a ``Dict[str, List[Book]]`` where the string key is a regular expression to be used to match to that particular book group, and the list of Book objects are the books of the Bible associated with that book group.

There is a ``BookGroup`` Enum included to help with this.

For example, if you wanted to only use the ``Old Testament`` and ``New Testament`` book groups, the following example using the default book groups would return too many references.

```python title="Code"
import pythonbible as bible

references = bible.get_references(
    "I want to find the Old Testament books, not the Gospels.",
    book_groups=bible.BOOK_GROUPS
)
```

```python title="Result"
[
    NormalizedReference(
        book=<Book.GENESIS: 1>,
        start_chapter=1,
        start_verse=1,
        end_chapter=4,
        end_verse=6,
        end_book=<Book.MALACHI: 39>
    ),
    NormalizedReference(
        book=<Book.MATTHEW: 40>,
        start_chapter=1,
        start_verse=1,
        end_chapter=21,
        end_verse=25,
        end_book=<Book.JOHN: 43
    )
]
```

Instead, you will need to define a custom ``book_groups`` value containing only the Old and New Testament information.

```python title="Code"
import pythonbible as bible

book_groups_subset = {
    bible.BookGroup.OLD_TESTAMENT.regular_expression: bible.BookGroup.OLD_TESTAMENT.books,
    bible.BookGroup.NEW_TESTAMENT.regular_expression: bible.BookGroup.NEW_TESTAMENT.books,
}
references = bible.get_references(
    "I want to find the Old Testament books, not the Gospels.",
    book_groups=book_groups_subset
)
```

```python title="Result"
[
    NormalizedReference(
        book=<Book.GENESIS: 1>,
        start_chapter=1,
        start_verse=1,
        end_chapter=4,
        end_verse=6,
        end_book=<Book.MALACHI: 39>
    )
]
```

With the custom subset book groups definition, only the Old Testament reference is included in the results and not the Gospels reference.

You can also define your own completely custom book groups definition. For example:

```python title="Code"
import pythonbible as bible

custom_book_groups = {
    "my favorite books": [
        bible.Book.PSALMS,
        bible.Book.PROVERBS,
        bible.Book.JOHN,
        bible.Book.PHILIPPIANS,
        bible.Book.JAMES,
    ],
}
references = bible.get_references(
    "What are my favorite books of the Bible?",
    book_groups=custom_book_groups
)

print(f"My favorite books of the Bible are {bible.format_scripture_references(references)}!")
```

```python title="Result"
My favorite books of the Bible are Psalms - Proverbs;John;Philippians;James!
```