---
sidebar_position: 5
---

# Format Scripture Text

This is still a work in progress, but there is some existing functionality related to this.

The pythonbible library currently includes a parser to parse [OSIS](https://ebible.org/osis/) formatted XML files. Future plans are to support other formats (namely [USFM](https://paratext.org/usfm/)) and to separate this functionality out into a separate library that parses these files and converts them into a more efficient format for use in Python. The pythonbible library could then use the output of that parsing library.

We have used the OSIS parser to convert the King James and American Standard versions into JSON. This allows for very efficient lookups to get the text for a given verse id. However, it doesn't currently support paragraph formatting, poetry structure, notes, etc. It only supports the raw text. Those JSON files have been added to this library and can be currently used to retrieve the text for a single verse:

```python
import pythonbible as bible

verse_text = bible.get_verse_text(1001001, version=bible.Version.KING_JAMES)
```

The resulting verse_text would be:

```python
'In the beginning God created the heaven and the earth.'
```

The version argument is optional and currently defaults to ``KING_JAMES``. Ideally, that default will be configurable in a future release.