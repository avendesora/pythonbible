---
sidebar_position: 3
---

# Verse IDs -> References

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

## Converting a List of Verse IDs to a List of References

We can take a list of integer verse ids and convert it back into a list of normalized scripture references.

For example, the following list of verse ids represents the references Matthew 18:12-14 and Luke 15:3-7.

```python
import pythonbible as bible

verse_ids = [40018012, 40018013, 40018014, 42015003, 42015004, 42015005, 42015006, 42015007, ]
references = bible.convert_verse_ids_to_references(verse_ids)
```

The conversion functionality would return the following list of normalized scripture references.

```
[
    NormalizedReference(
        book=<Book.MATTHEW: 40>, 
        start_chapter=18, 
        start_verse=12, 
        end_chapter=18, 
        end_verse=14.
        end_book=None
    ),
    NormalizedReference(
        book=<Book.LUKE: 42>, 
        start_chapter=15, 
        start_verse=3, 
        end_chapter=15, 
        end_verse=7,
        end_book=None
    )
]
```