import json
import os

from pythonbible.bible.osis.parser import OSISParser
from pythonbible.errors import InvalidBibleParserError
from pythonbible.verses import VERSE_DATA_FOLDER, VERSE_IDS


class JSONConverter:
    def __init__(self, parser, **kwargs):
        self.parser = parser
        self.data_folder = kwargs.get("data_folder", VERSE_DATA_FOLDER)
        self.verse_ids = kwargs.get("verse_ids", VERSE_IDS)
        self.verses = {}

    def generate_json_file(self):
        if self.parser is None:
            raise InvalidBibleParserError("Parser instance is None.")

        instance_identified = False

        if isinstance(self.parser, OSISParser):
            instance_identified = True

        if not instance_identified:
            raise InvalidBibleParserError("Parser instance is not a valid type.")

        self.get_verses()
        self.print_file()

    def get_verses(self):
        for verse_id in self.verse_ids:
            verse_text = self.parser.get_verse_text(
                verse_id, include_verse_number=False
            )

            if verse_text is None or len(verse_text.strip()) == 0:
                print(f"Verse {verse_id} is empty.")

            self.verses[verse_id] = verse_text

    def print_file(self):
        version = self.parser.version
        filename = f"{version.value.lower()}.json"

        with open(os.path.join(self.data_folder, filename), "w") as json_file:
            json.dump(self.verses, json_file)
