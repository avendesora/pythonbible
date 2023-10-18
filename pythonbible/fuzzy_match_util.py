from __future__ import annotations

import re

NUMBER_WORD_DIGIT_MAP = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19",
    "twenty": "20",
    "thirty": "30",
    "forty": "40",
    "fifty": "50",
    "sixty": "60",
    "seventy": "70",
    "eighty": "80",
    "ninety": "90",
    "hundred": "100",
    "thousand": "1000",
    "million": "1000000",
    "billion": "1000000000",
}


def words_to_digits(text: str) -> str:
    words = re.findall(r"[\w]+|[.,!?:;]", text)
    clean_text = []
    current_number = []

    for word in words:
        if word.lower() in NUMBER_WORD_DIGIT_MAP:
            current_number.append(NUMBER_WORD_DIGIT_MAP.get(word.lower(), ""))
            continue

        if word.lower() == "and":
            continue

        if current_number:
            clean_text.append("".join(current_number))
            current_number = []
        clean_text.append(word)

    if current_number:
        clean_text.append("".join(current_number))

    return " ".join(clean_text)


def clean_text_for_fuzzy_matching(text: str) -> str:
    clean_text = text.replace(" chapter ", " ")
    clean_text = clean_text.replace(", verses ", ": ")
    clean_text = clean_text.replace(", verse ", ": ")
    clean_text = clean_text.replace(" verses ", ": ")
    clean_text = clean_text.replace(" verse ", ": ")
    clean_text = clean_text.replace(" and ", ", ")
    clean_text = clean_text.replace(" & ", ", ")
    clean_text = clean_text.replace(" through ", "- ")
    clean_text = clean_text.replace(" number ", " ")
    return words_to_digits(clean_text)
