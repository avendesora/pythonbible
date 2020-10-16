import re

W_LEMMA_OPEN_REGEX = re.compile(
    r'<w( lemma="(strong:[GH]\d+\s*)+")?( morph="([\d\sA-Za-z\-:]+\s*)+")?>'
)
W_LEMMA_CLOSE_REGEX = re.compile(r"</w>")

TRANS_CHANGE_OPEN_REGEX = re.compile(r'<transChange type="[A-Za-z]+">')
TRANS_CHANGE_CLOSE_REGEX = re.compile(r"</transChange>")

REGEX_CLEANERS = [
    W_LEMMA_OPEN_REGEX,
    W_LEMMA_CLOSE_REGEX,
    TRANS_CHANGE_OPEN_REGEX,
    TRANS_CHANGE_CLOSE_REGEX,
]


def clean_xml_file(filename):
    with (open(filename, "r", encoding="utf-8")) as xml_file:
        content = xml_file.read()

    cleaned_content = clean_text(content)

    with (open(filename, "w", encoding="utf-8")) as xml_file:
        xml_file.write(cleaned_content)


def clean_text(text):
    cleaned_text = text

    for cleaner in REGEX_CLEANERS:
        cleaned_text = re.sub(cleaner, "", cleaned_text)

    while True:
        start_index = cleaned_text.find("<note")

        if start_index == -1:
            break

        end_index = cleaned_text.find("</note>")

        first_string = cleaned_text[:start_index]
        last_string = cleaned_text[end_index + len("</note>") :]

        cleaned_text = first_string + last_string

    return cleaned_text
