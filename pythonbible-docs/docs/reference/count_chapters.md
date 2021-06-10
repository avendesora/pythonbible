---
sidebar_position: 8
---

# count_chapters

The `count_chapters` function, given a `string` containing one or more Scripture references or a `NormalizedReference` object or a `List` of `NormalizedReference` objects, returns the `int` count of the chapters included in the given reference(s).

## Input

The `count_chapters` function accepts a single argument of one of the following three types:

* `string`
* `NormalizedReference`
* `List[NormalizedReference]`

## Output

The `count_chapters` function returns an `int` greater than or equal to 0 that represents the number of chapters contained in the given reference(s).

## Examples

### String Input Example

```python title="Code"
import pythonbible as bible

# Genesis - Deuteronomy
bible.count_chapters("Genesis has 50 chapters, but Exodus has 40.")
```

```python title="Result"
90
```

### NormalizedReference Input Example

```python title="Code"
import pythonbible as bible

# Matthew - John (i.e. bible.get_references("Matthew - John"))
reference = bible.NormalizedReference(
    book=bible.Book.MATTHEW,
    start_chapter=1,
    start_verse=1,
    end_chapter=21,
    end_verse=25,
    end_book=bible.Book.JOHN
)
bible.count_chapters(reference)
```

```python title="Result"
89
```

### List of NormalizedReferences Input Example

```python title="Code"
import pythonbible as bible

# Genesis and Matthew - Acts (ie. bible.get_references("Genesis, Matthew - Acts"))
references = [
    bible.NormalizedReference(
        book=bible.Book.GENESIS,
        start_chapter=1,
        start_verse=1,
        end_chapter=50,
        end_verse=26,
        end_book=None
    ),
    bible.NormalizedReference(
        book=bible.Book.MATTHEW,
        start_chapter=1,
        start_verse=1,
        end_chapter=28,
        end_verse=31,
        end_book=bible.Book.ACTS
    ),
]
bible.count_chapters(references)
```

```python title="Result"
167
```