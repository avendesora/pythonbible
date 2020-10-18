# python-bible

This python library serves several purposes related to the Christian Bible and Scripture references.

![Test](https://github.com/avendesora/python-bible/workflows/Test/badge.svg)
![CodeQL](https://github.com/avendesora/python-bible/workflows/CodeQL/badge.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/dc1333c64b434f7bb813d08750462921)](https://www.codacy.com/gh/avendesora/python-bible/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=avendesora/python-bible&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/dc1333c64b434f7bb813d08750462921)](https://www.codacy.com/gh/avendesora/python-bible/dashboard?utm_source=github.com&utm_medium=referral&utm_content=avendesora/python-bible&utm_campaign=Badge_Coverage)
[![PyPI version](https://badge.fury.io/py/pythonbible.svg)](https://badge.fury.io/py/pythonbible)

## Installation

```shell script
pip install pythonbible
```

### Optional Dependencies

If the [defusedxml](https://github.com/tiran/defusedxml) library is installed, pythonbible will use it to parse XML files rather than the builtin xml.etree libary. Execute the following command if you choose to install the defusedxml python library.

```shell script
pip install defusedxml
```

## Features

### Searching text for scripture references
Given a text, search for scripture references and return any that are found in a list of tuples.

For example, given the following text:

```python
import pythonbible as bible

text = "The parable of the lost sheep is told in Matthew 18:12-14 and Luke 15:3-7."
references = bible.get_references(text)
```

The search functionality should return the following list of scripture reference tuples:

```python
[(<Book.MATTHEW: 40>, 18, 12, 18, 14), (<Book.LUKE: 42>, 15, 3, 15, 7)]
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

Given a normalized scripture reference, which can contain one or more verses, the conversion functionality will convert that normalized scripture reference tuple into a list of verse id integers.

For example, given the following normalized scripture reference for Genesis 1:1-4:

```python
import pythonbible as bible

reference = (bible.Book.GENESIS, 1, 1, 1, 4)
verse_ids = bible.convert_reference_to_verse_ids(reference)
```

The conversion functionality would return the following list of verse id integers:

```python
[1001001, 1001002, 1001003, 1001004]
```

### Converting a list of verse id integers into a list of normalized scripture reference tuples
The reverse of the above feature, we can take a list of integer verse ids and convert it back into a list of normalized scripture reference tuples.

For example, the following list of verse ids represent the references Matthew 18:12-14 and Luke 15:3-7.

```python
import pythonbible as bible

verse_ids = [40018012, 40018013, 40018014, 42015003, 42015004, 42015005, 42015006, 42015007, ]
references = bible.convert_verse_ids_to_references(verse_ids)
```

The conversion functionality would return the following list of normalized scripture reference tuples.

```python
[(<Book.MATTHEW: 40>, 18, 12, 18, 14), (<Book.LUKE: 42>, 15, 3, 15, 7)]
```

### Converting a list of normalized scripture reference tuples into a formatted string scripture reference
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
*  Smarter pluralization of the book of Psalms (i.e. If just one Psalm is referenced, the singular "Psalm" should be used, but if more than one Psalm is referenced, the plural "Psalms" should be used.)
*  Optional exclusion of the chapter number for books that contain only one chapter (e.g. Some prefer references like Obadiah 1-4 rather than Obadiah 1:1-4, since Obadiah contains only one chapter.)

### Given a list of verse id integers, formatting the related Biblical text for print or web display in one or more open source or public domain versions

coming soon...