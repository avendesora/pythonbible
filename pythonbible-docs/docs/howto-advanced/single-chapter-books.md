---
sidebar_position: 1
---

# Single Chapter Books

Several books of the Bible only contain one chapter, and there is some special functionality in pythonbible related to this.

## Finding References

When parsing a given text to find all the references contained within, if we find a reference for a single chapter book that contains only one number, rather than both chapter and verse numbers, we assume that number to be the verse number.

### Examples

#### Example - Obadiah 1 vs Genesis 1:

```python title="Code"
import pythonbible as bible

references = bible.get_references("Obadiah 1")
```

```python title="Result"
[
    NormalizedReference(
        book=<Book.OBADIAH: 31>,
        start_chapter=1,
        start_verse=1,
        end_chapter=1,
        end_verse=1,
        end_book=None
    )
]
```

If a reference like this was found for a non single chapter book, the number would be assumed to be a chapter number rather than a verse number.

```python title="Code"
import pythonbible as bible

references = bible.get_references("Genesis 1")
```

```python title="Result"
[
    NormalizedReference(
        book=<Book.GENESIS: 1>,
        start_chapter=1,
        start_verse=1,
        end_chapter=1,
        end_verse=31,
        end_book=None
    )
]
```

Rather than being interpreted as Genesis 1:1, this would be interpreted as Genesis 1:1-31.

#### Example - Philemon 3-6 vs Genesis 3-6:

```python title="Code"
import pythonbible as bible

references = bible.get_references("Philemon 3-6")
```

```python title="Result"
[
    NormalizedReference(
        book=<Book.PHILEMON: 57>,
        start_chapter=1,
        start_verse=3,
        end_chapter=1,
        end_verse=6,
        end_book=None
    )
]
```

This is interpreted as Philemon 1:3-6. If a similar reference were encountered for a non single chapter book, both numbers would be assumed to be chapter numbers rather than verse numbers.

```python title="Code"
import pythonbible as bible

references = bible.get_references("Genesis 3-6")
```

```python title="Result"
[
    NormalizedReference(
        book=<Book.GENESIS: 1>,
        start_chapter=3,
        start_verse=1,
        end_chapter=6,
        end_verse=22,
        end_book=None
    )
]
```

Rather than being interpreted as Genesis 1:3-6, this would be interpreted as Genesis 3:1-6:22.

## Converting References to Verse IDs

Because normalized references in pythonbible always explicitly include chapter and verse numbers, there is no difference in how references are converted to verse ids for single chapter books.

## Converting Verse IDs to References

Because verse ids in pythonbible always explicitly include chapter and verse numbers, there is no difference in how verse ids are converted to references for single chapter books.

## Formatting References for Print/Display

By default, when formatting references for print/display for references of a single chapter book, the chapter number will not be included.

For example:

```python title="Code"
import pythonbible as bible

references = bible.get_references("Jude 2-8")
reference_text = bible.format_scripture_references(references)
```

```python title="Result"
'Jude 2-8'
```

The result should be the same even if we are including the chapter number in the original reference string.

```python title="Code"
import pythonbible as bible

references = bible.get_references("Jude 1:2-8")
reference_text = bible.format_scripture_references(references)
```

```python title="Result"
'Jude 2-8'
```

### Always Include Chapter Numbers

If you want to force pythonbible to include the chapter numbers even for single chapter books, you can use the optional ``always_include_chapter_numbers`` optional parameter of the ``format_scripture_references`` or ``format_single_reference`` functions, setting that optional parameter to be ``True``.

For example:

```python title="Code"
import pythonbible as bible

references = bible.get_references("Jude 2-8")
reference_text = bible.format_scripture_references(
    references, 
    always_include_chapter_numbers=True
)
```

```python title="Result"
'Jude 1:2-8'
```