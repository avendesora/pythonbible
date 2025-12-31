from __future__ import annotations

import re
from typing import Pattern

from pythonbible import Book

DIGIT: str = r"(\d{1,3})"
SPACE: str = r"\s*"
COLON: str = f"{SPACE}([:.]){SPACE}"
DASH = f"{SPACE}-{SPACE}"
COMMA = f"{SPACE},{SPACE}"

BOOK: str = rf"\b({'|'.join(book.regular_expression for book in Book)})\b\.*"
CHAPTER: str = DIGIT
VERSE: str = DIGIT

CHAPTER_AND_VERSE: str = f"({CHAPTER}(?:{COLON}{VERSE})?)"

# Possibly range regular expressions are:
# 1. Book - Book (with optional chapter/verse)
# 2. Chapter - Book (with optional chapter/verse)
# 3. Chapter - Chapter (with optional verse)
# 4. Verse - Book (with optional chapter/verse)
# 5. Verse - Chapter:Verse (verse is required)
# 6. Verse - Verse

# TODO - this regex may have some false positives for ranges given the above rules.
RANGE: str = (
    f"{DASH}(({BOOK}{SPACE}(?:{CHAPTER_AND_VERSE})?)|{CHAPTER_AND_VERSE}|{VERSE})"
)

ADDITIONAL_REFERENCE: str = f"({COMMA}({CHAPTER_AND_VERSE}(?:{RANGE})?|{VERSE}))"
FULL_CHAPTER_AND_VERSE: str = (
    f"({CHAPTER_AND_VERSE}(?:{RANGE})?({ADDITIONAL_REFERENCE})*)"
)
FULL_BOOK = f"({BOOK}){SPACE}(?:{FULL_CHAPTER_AND_VERSE})?"
CROSS_BOOK = f"({FULL_BOOK}(?:{DASH}({FULL_BOOK}))?)"

SCRIPTURE_REFERENCE_REGULAR_EXPRESSION: Pattern[str] = re.compile(
    CROSS_BOOK,
    re.IGNORECASE | re.UNICODE,
)
