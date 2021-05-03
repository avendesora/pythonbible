---
sidebar_position: 2
---

# References -> Verse IDs

## Representing a Single Verse Reference as a Unique Integer ID

Any single verse can be identified by an integer that contains the book, chapter, and verse information.
The first 1-2 digits of the integer id represent the book, the next 3 digits represent the chapter, and the last 3 digits represent the verse.

For example, "Genesis 1:1" would be represented as:

```python
1001001
```

"John 3:16" would be represented as:

```python
43003016
```

The book of John is the 43rd book of the Bible, "003" represents the 3rd chapter, and "016" represents the sixteenth verse.

Since the book, chapter, and verses are standardized and unlikely to change, this allows us to reference verses in a very efficient way.

## Converting a Single Reference to a List of Verse IDs

Given a normalized scripture reference, which can contain one or more verses, the conversion functionality will convert that normalized scripture reference into a list of verse id integers.

For example, given the following normalized scripture reference for Genesis 1:1-4:

```python
import pythonbible as bible

reference = bible.NormalizedReference(bible.Book.GENESIS, 1, 1, 1, 4)
verse_ids = bible.convert_reference_to_verse_ids(reference)
```

The conversion functionality would return the following list of verse id integers:

```python
[1001001, 1001002, 1001003, 1001004]
```

## Converting a List of References to a List of Verse IDs

If you need to convert a list of references (rather than a single reference) to a list of verse ids, use the ``convert_references_verse_ids`` function rather than the ``convert_reference_to_verse_ids`` function.

```python
import pythonbible as bible

references = [
    bible.NormalizedReference(
        book=bible.Book.MATTHEW,
        start_chapter=18,
        start_verse=12,
        end_chapter=18,
        end_verse=14,
        end_book=None
    ),
    bible.NormalizedReference(
        book=bible.Book.LUKE,
        start_chapter=15,
        start_verse=3,
        end_chapter=15,
        end_verse=7,
        end_book=None
    )
]
verse_ids = bible.convert_references_to_verse_ids(references)
```

The conversion functionality would return the following list of verse id integers:

```python
[40018012, 40018013, 40018014, 42015003, 42015004, 42015005, 42015006, 42015007]
```