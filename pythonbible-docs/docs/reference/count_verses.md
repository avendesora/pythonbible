---
sidebar_position: 9
---

# count_verses

The `count_verses` function, given a `string` containing one or more Scripture references or a `NormalizedReference` object or a `List` of `NormalizedReference` objects, returns the `int` count of the verses included in the given reference(s).

## Input

The `count_verses` function accepts a single argument of one of the following three types:

* `string`
* `NormalizedReference`
* `List[NormalizedReference]`

## Output

The `count_verses` function returns an `int` greater than or equal to 0 that represents the number of verses contained in the given reference(s).

## Examples

### String Input Example

```python title="Code"
import pythonbible as bible

# Matthew 6:9-13
bible.count_verses("The Lord's prayer is in Matthew 6:9-13.")
```

```python title="Result"
5
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
bible.count_verses(reference)
```

```python title="Result"
3779
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
bible.count_verses(references)
```

```python title="Result"
6319
```