"""Common constants used in Book regular expressions."""

FIRST = r"1|I\s+|1st\s+|First\s+"
SECOND = r"2|II|2nd\s+|Second\s+"
THIRD = r"3|III|3rd\s+|Third\s+"

FIRST_BOOK = rf"{FIRST}|(First\s+Book\s+of(?:\s+the)?)"
SECOND_BOOK = rf"{SECOND}|(Second\s+Book\s+of(?:\s+the)?)"
