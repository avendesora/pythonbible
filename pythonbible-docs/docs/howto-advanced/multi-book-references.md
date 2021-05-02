---
sidebar_position: 2
---

# Multi Book References

It is possible for a single reference to be a range than spans more than one book of the Bible.

For example, the following references are all equally referencing the entire first five books of the Bible:

 * Genesis - Deuteronomy
 * Genesis 1 - Deuteronomy 34
 * Genesis 1:1 - Deuteronomy 34:12

## Finding References

When parsing a given text to find all the references contained within, if we find a ranged reference like those above that span multiple books of the Bible, we should parse that into a single normalized reference that includes the optional ``end_book`` attribute.

For example, "Genesis - Deuteronomy" vs "Genesis;Exodus;Numbers;Leviticus;Deuteronomy":

```python title="Code"
import pythonbible as bible

references = bible.get_references("Genesis - Deuteronomy")
```

```python title="Result"
[
    NormalizedReference(
        book=<Book.GENESIS: 1>, 
        start_chapter=1, 
        start_verse=1, 
        end_chapter=34, 
        end_verse=12, 
        end_book=<Book.DEUTERONOMY: 5>
    )
]
```

If rather than using the range, the text specified each book of the Bible separated by a comma or semi-colon (or just about anything), then the result would be a list of five normalized references, one for each of the five books referenced.

```python title="Code"
import pythonbible as bible

references = bible.get_references("Genesis;Exodus;Leviticus;Numbers;Deuteronomy")
```

```python title="Result"
[
    NormalizedReference(
        book=<Book.GENESIS: 1>,
        start_chapter=1,
        start_verse=1,
        end_chapter=50,
        end_verse=26,
        end_book=None
    ),
    NormalizedReference(
        book=<Book.EXODUS: 2>,
        start_chapter=1,
        start_verse=1,
        end_chapter=40,
        end_verse=38,
        end_book=None
    ),
    NormalizedReference(
        book=<Book.LEVITICUS: 3>,
        start_chapter=1,
        start_verse=1,
        end_chapter=27,
        end_verse=34,
        end_book=None
    ),
    NormalizedReference(
        book=<Book.NUMBERS: 4>,
        start_chapter=1,
        start_verse=1,
        end_chapter=36,
        end_verse=13,
        end_book=None
    ),
    NormalizedReference(
        book=<Book.DEUTERONOMY: 5>,
        start_chapter=1,
        start_verse=1,
        end_chapter=34,
        end_verse=12,
        end_book=None
    )
]
```

That list can optionally be optimized by converting it to verse ids and then back into references if so desired.

```python title="Code"
import pythonbible as bible

references = bible.get_references("Genesis;Exodus;Leviticus;Numbers;Deuteronomy")
verse_ids = bible.convert_references_to_verse_ids(references)
references = bible.convert_verse_ids_to_references(verse_ids)
```

```python title="Result"
[
    NormalizedReference(
        book=<Book.GENESIS: 1>, 
        start_chapter=1, 
        start_verse=1, 
        end_chapter=34, 
        end_verse=12, 
        end_book=<Book.DEUTERONOMY: 5>
    )
]
```

That optimization is optional as it can degrade performance for processing large ranges if that particular optimization is not necessary. This optimization will be run automatically when the list of references is formatted into a Scripture reference string.

## Converting References to Verse IDs

Whether a multi book range reference is in a single normalized reference or a list of one normalized reference for each book does not affect the results of converting that reference into a list of verse ids.

## Converting Verse IDs to References

When converting a list of verse ids into a list of references, multi book range references will always be optimized into a single normalized reference when possible.

## Formatting References for Print/Display

As mentioned earlier, when formatting references for print/display, pythonbible always optimizes the list of references into as few references as possible by using multi book range references.

By default, chapter numbers will not be included when the entire book is included in the reference.

```python title="Code"
import pythonbible as bible

references = bible.get_references("Genesis - Deuteronomy")
reference_text = bible.format_scripture_references(references)
```

```python title="Result"
'Genesis - Deuteronomy'
```

### Always Include Chapter Numbers

If you want to force pythonbible to include the chapter numbers even when the entire book is covered by the reference, you can use the optional ``always_include_chapter_numbers`` optional parameter of the ``format_scripture_references`` or ``format_single_reference`` functions, setting that optional parameter to be ``True``.

For example:

```python title="Code"
import pythonbible as bible

references = bible.get_references("Genesis - Deuteronomy")
reference_text = bible.format_scripture_references(
    references,
    always_include_chapter_numbers=True
)
```

```python title="Result"
'Genesis 1:1 - Deuteronomy 34:12'
```