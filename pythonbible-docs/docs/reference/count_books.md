---
sidebar_position: 7
---

# count_books

The `count_books` function, given a `string` containing one or more Scripture references or a `NormalizedReference` object or a `List` of `NormalizedReference` objects, returns the `int` count of the books of the Bible included in the given reference(s).

## Input

The `count_books` function accepts a single argument of one of the following three types:

* `string`
* `NormalizedReference`
* `List[NormalizedReference]`

## Output

The `count_books` function returns an `int` greater than or equal to 0 that represents the number of books of the Bible contained in the given reference(s).

## Examples

### String Input Example

```python title="Code"
import pythonbible as bible

# Genesis - Deuteronomy
bible.count_books("The first five books of the Bible are Genesis - Deuteronomy.")
```

```python title="Result"
5
```

### NormalizedReference Input Example

```python title="Code"
import pythonbible as bible

# Matthew - John (i.e. bible.get_references("Matthew - John")
reference = bible.NormalizedReference(
    book=bible.Book.MATTHEW,
    start_chapter=1,
    start_verse=1,
    end_chapter=21,
    end_verse=25,
    end_book=bible.Book.JOHN
)
bible.count_books(reference)
```

```python title="Result"
4
```

### List of NormalizedReferences Input Example

```python title="Code"
import pythonbible as bible

# Genesis and Matthew - John (i.e. bible.get_references("Genesis, Matthew - John"))
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
        end_chapter=21,
        end_verse=25,
        end_book=bible.Book.JOHN
    ),
]
bible.count_books(references)
```

```python title="Result"
5
```