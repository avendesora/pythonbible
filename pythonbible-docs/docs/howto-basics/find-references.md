---
sidebar_position: 1
---

# Find References

Given a text, search for scripture references and return any that are found in a list of NormalizedReferences.

For example, given the following text:

```py
import pythonbible as bible

text = "The parable of the lost sheep is told in Matthew 18:12-14 and Luke 15:3-7."
references = bible.get_references(text)
```

The search functionality should return the following list of scripture references:

```
[
    NormalizedReference(
        book=<Book.MATTHEW: 40>, 
        start_chapter=18, 
        start_verse=12, 
        end_chapter=18, 
        end_verse=14,
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