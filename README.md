# pythonbible

The pythonbible library serves several purposes related to the Christian Bible and Scripture references.

[![PyPI version](https://img.shields.io/pypi/v/pythonbible?color=blue&logo=pypi&logoColor=lightgray)](https://pypi.org/project/pythonbible/)
[![license MIT](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)

![Test](https://github.com/avendesora/pythonbible/workflows/Test/badge.svg)
![CodeQL](https://github.com/avendesora/pythonbible/workflows/CodeQL/badge.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/dc1333c64b434f7bb813d08750462921)](https://www.codacy.com/gh/avendesora/pythonbible/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=avendesora/pythonbible&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/dc1333c64b434f7bb813d08750462921)](https://www.codacy.com/gh/avendesora/pythonbible/dashboard?utm_source=github.com&utm_medium=referral&utm_content=avendesora/pythonbible&utm_campaign=Badge_Coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Python 3.9](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue?logo=python&logoColor=lightgray)](https://www.python.org/downloads/release/python-390/)

## Documentation

The full documentation for pythonbible can be found at [docs.python.bible](https://docs.python.bible/docs/intro).

## Installation

```shell script
pip install pythonbible
```

### Optional Dependencies

If the [defusedxml](https://github.com/tiran/defusedxml) library is installed, pythonbible will use it to parse XML files rather than the builtin xml.etree library.

To install pythonbible with all optional dependencies, use the following command.

```shell script
pip install pythonbible[all]
```

### Python 3.6

Python 3.6 is not officially supported (pythonbible is only tested on Python 3.7+). However, pythonbible should work on Python 3.6 if you have the dataclasses library installed:

```shell script
pip install dataclasses
```

If you are using Python 3.7+, the dataclasses library is included in the Python standard library, and you do not need to explicitly install the dataclasses library.

## Features

### Searching text for scripture references
Given a text, search for scripture references and return any that are found in a list of NormalizedReferences.

For example, given the following text:

```python
import pythonbible as bible

text = "The parable of the lost sheep is told in Matthew 18:12-14 and Luke 15:3-7."
references = bible.get_references(text)
```

The search functionality should return the following list of scripture references:

```python
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

### Converting a normalized scripture reference into a list of integer verse ids
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

### Converting a list of verse id integers into a list of normalized scripture references
The reverse of the above feature, we can take a list of integer verse ids and convert it back into a list of normalized scripture references.

For example, the following list of verse ids represents the references Matthew 18:12-14 and Luke 15:3-7.

```python
import pythonbible as bible

verse_ids = [40018012, 40018013, 40018014, 42015003, 42015004, 42015005, 42015006, 42015007, ]
references = bible.convert_verse_ids_to_references(verse_ids)
```

The conversion functionality would return the following list of normalized scripture references.

```python
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

### Converting a list of normalized scripture references into a formatted string scripture reference
Given a list of normalized references, this feature formats them into a human-readable scripture reference string.

It sorts the list so that the references appear in the order they would in the Bible. 
It also combines verses into ranges when possible.

For example:

```python
import pythonbible as bible

text = "My favorite verses are Philippians 4:8, Isaiah 55:13, and Philippians 4:4-7."
references = bible.get_references(text)
formatted_reference = bible.format_scripture_references(references)
```

The resulting formatted reference should be:

```python
'Isaiah 55:13;Philippians 4:4-8'
```

There are a couple of reference formatting features not yet implemented:
*   Smarter pluralization of the book of Psalms (i.e. If just one Psalm is referenced, the singular "Psalm" should be used, but if more than one Psalm is referenced, the plural "Psalms" should be used.)
*   Optional exclusion of the chapter number for books that contain only one chapter (e.g. Some prefer references like Obadiah 1-4 rather than Obadiah 1:1-4, since Obadiah contains only one chapter.)

### Formatting Biblical text for print or web display in one or more open-source or public domain versions

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
