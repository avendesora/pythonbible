---
sidebar_position: 1
---

# Book

``Book`` is an Enum containing all the books of the Bible as members.

## Members

| Name | Value | Title |
| ---- | ----- | ----- |
| GENESIS | 1 | Genesis |
| EXODUS | 2 | Exodus |
| LEVITICUS | 3 | Leviticus |
| NUMBERS | 4 | Numbers |
| DEUTERONOMY | 5 | Deuteronomy |
| JOSHUA | 6 | Joshua |
| JUDGES | 7 | Judges |
| RUTH | 8 | Ruth |
| SAMUEL_1 | 9 | 1 Samuel |
| SAMUEL_2 | 10 | 2 Samuel |
| KINGS_1 | 11 | 1 Kings |
| KINGS_2 | 12 | 2 Kings |
| CHRONICLES_1 | 13 | 1 Chronicles |
| CHRONICLES_2 | 14 | 2 Chronicles |
| EZRA | 15 | Ezra |
| NEHEMIAH | 16 | Nehemiah |
| ESTHER | 17 | Esther |
| JOB | 18 | Job |
| PSALMS | 19 | Psalms |
| PROVERBS | 20 | Proverbs |
| ECCLESIASTES | 21 | Ecclesiastes |
| SONG_OF_SONGS | 22 | Song of Songs |
| ISAIAH | 23 | Isaiah |
| JEREMIAH | 24 | Jeremiah |
| LAMENTATIONS | 25 | Lamentations |
| EZEKIEL | 26 | Ezekiel |
| DANIEL | 27 | Daniel |
| HOSEA | 28 | Hosea |
| JOEL | 29 | Joel |
| AMOS | 30 | Amos |
| OBADIAH | 31 | Obadiah |
| JONAH | 32 | Jonah |
| MICAH | 33 | Micah |
| NAHUM | 34 | Nahum |
| HABAKKUK | 35 | Habakkuk |
| ZEPHANIAH | 36 | Zephaniah |
| HAGGAI | 37 | Haggai |
| ZECHARIAH | 38 | Zechariah |
| MALACHI | 39 | Malachi |
| MATTHEW | 40 | Matthew |
| MARK | 41 | Mark |
| LUKE | 42 | Luke |
| JOHN | 43 | John |
| ACTS | 44 | Acts |
| ROMANS | 45 | Romans |
| CORINTHIANS_1 | 46 | 1 Corinthians |
| CORINTHIANS_2 | 47 | 2 Corinthians |
| GALATIANS | 48 | Galatians |
| EPHESIANS | 49 | Ephesians |
| PHILIPPIANS | 50 | Philippians |
| COLOSSIANS | 51 | Colossians |
| THESSALONIANS_1 | 52 | 1 Thessalonians |
| THESSALONIANS_2 | 53 | 2 Thessalonians |
| TIMOTHY_1 | 54 | 1 Timothy |
| TIMOTHY_2 | 55 | 2 Timothy |
| TITUS | 56 | Titus |
| PHILEMON | 57 | Philemon |
| HEBREWS | 58 | Hebrews |
| JAMES | 59 | James |
| PETER_1 | 60 | 1 Peter |
| PETER_2 | 61 | 2 Peter |
| JOHN_1 | 62 | 1 John |
| JOHN_2 | 63 | 2 John |
| JOHN_3 | 64 | 3 John |
| JUDE | 65 | Jude |
| REVELATION | 66 | Revelation |
| ESDRAS_1 | 67 | 1 Esdras |
| TOBIT | 68 | Tobit |
| WISDOM_OF_SOLOMON | 69 | Wisdom of Solomon |
| ECCLESIASTICUS | 70 | Ecclesiasticus |
| MACCABEES_1 | 71 | 1 Maccabees |
| MACCABEES_2 | 72 | 2 Maccabees |

## Properties

### name

The name property returns the string all-caps Enum name (e.g. 'GENESIS', 'EXODUS', etc.).

For example:

```python title="Code"
import pythonbible as bible

book = bible.Book.SAMUEL_1
print(book.name)
```

```python title="Result"
SAMUEL_1
```

### value

The value property returns the integer book id value.

For example:

```python title="Code"
import pythonbible as bible

book = bible.Book.SAMUEL_1
print(book.value)
```

```python title="Result"
9
```

This value matches the book id portion of a verse id. For example, the ``9`` in the verse id ``9001001`` represents the book of 1 Samuel. The verse id as a whole represents 1 Samuel 1:1.

### title

The title property returns the common English title of the given book (e.g. 'Genesis', 'Exodus', 'Leviticus', etc.).

For example:

```python title="Code"
import pythonbible as bible

book = bible.Book.SAMUEL_1
print(book.title)
```

```python title="Result"
1 Samuel
```

This title is not actually used when formatting a Scripture reference for print/display. In that scenario, the official titles associated with the specified version of the Bible (or the default version if none is specified) are used rather than this title property.

This title property can be used for situations when using a version's official titles is unnecessary, and a quicker/easier method is desired.

## Uses

The Book Enum is used for both the required ``start_book`` and the optional ``end_book`` attributes of the ``NormalizedReference`` class.

The ``value`` property of the Book Enum is used when converting between references and verse ids.