"""John book regular expression definitions."""

import re

_JO_EXCLUDE_SUFFIXES: tuple[str, ...] = (
    "shua",  # Joshua
    "b",  # Job
    "nah",  # Jonah
    "n",  # Jonah (abbreviation)
    "el",  # Joel
)

_JO_EXCLUDED_SUFFIXES_PATTERN = "|".join(map(re.escape, _JO_EXCLUDE_SUFFIXES))
_JO_NEGATIVE_LOOKAHEAD = f"(?!{_JO_EXCLUDED_SUFFIXES_PATTERN})"

_ABBREVIATIONS: tuple[str, ...] = (
    r"Joh\.*",
    r"Jhn\.*",
    r"Jo\.*" + _JO_NEGATIVE_LOOKAHEAD,
    r"Jn\.*",
)

JOHN_REGULAR_EXPRESSION = rf"(John|{'|'.join(_ABBREVIATIONS)})"
