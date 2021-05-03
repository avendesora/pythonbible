try:
    import regex as re
except ModuleNotFoundError:
    import re

from enum import IntEnum
from typing import List, Match, Pattern

# We only need to support numbers 1-150 for our purposes. If we needed more it might
# make sense to use an existing roman numeral library.


class RomanNumeral(IntEnum):
    C = 100
    XC = 90
    L = 50
    XL = 40
    X = 10
    IX = 9
    V = 5
    IV = 4
    I = 1


ROMAN_NUMERAL_REGEX: Pattern[str] = re.compile(
    r"\b(?=[CLXVI]+\b)(C?)(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\b",
    re.IGNORECASE | re.UNICODE,
)

ROMAN_NUMERALS_BIG_TO_SMALL: List[RomanNumeral] = [
    RomanNumeral.C,
    RomanNumeral.XC,
    RomanNumeral.L,
    RomanNumeral.XL,
    RomanNumeral.X,
    RomanNumeral.IX,
    RomanNumeral.V,
    RomanNumeral.IV,
    RomanNumeral.I,
]


def convert_all_roman_numerals_to_integers(text: str) -> str:
    return ROMAN_NUMERAL_REGEX.sub(_convert_roman_numeral_match_to_integer, text)


def _convert_roman_numeral_match_to_integer(match: Match[str]):
    return str(_convert_roman_numeral_to_integer(match.group(0)))


def _convert_roman_numeral_to_integer(roman_numeral_string):
    roman_numeral_string = roman_numeral_string.upper()
    i = result = 0

    for roman_numeral in ROMAN_NUMERALS_BIG_TO_SMALL:
        while (
            roman_numeral_string[i : i + len(roman_numeral.name)] == roman_numeral.name
        ):
            result += roman_numeral.value
            i += len(roman_numeral.name)

    return result
