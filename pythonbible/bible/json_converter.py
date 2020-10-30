import json
import os

from pythonbible import OSISParser
from pythonbible.errors import InvalidBibleParserError
from pythonbible.verses import VERSE_IDS

CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))
VERSE_DATA_FOLDER = os.path.join(CURRENT_FOLDER, "verse_data")


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
            print(verse_id)
            self.verses[verse_id] = self.parser.get_verse_text(
                verse_id, include_verse_number=False
            )

    def print_file(self):
        version = self.parser.version
        filename = f"{version.value.lower()}.json"

        with open(os.path.join(self.data_folder, filename), "w") as json_file:
            json.dump(self.verses, json_file)
