import json
import os

from pythonbible import OSISParser
from pythonbible.verses import VERSE_IDS

CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))


class JSONConverter:
    def __init__(self, parser):
        self.parser = parser
        self.data_folder = None
        self.verses = {}

    def generate_json_file(self):
        if self.parser is None:
            return

        instance_identified = False

        if isinstance(self.parser, OSISParser):
            instance_identified = True
            self.data_folder = os.path.join(os.path.join(CURRENT_FOLDER, "osis"), "versions")

        if not instance_identified:
            return

        self.get_verses()
        self.print_file()

    def get_verses(self):
        for verse_id in VERSE_IDS:
            print(verse_id)
            self.verses[verse_id] = self.parser.get_verse_text(verse_id, include_verse_number=False)

    def print_file(self):
        version = self.parser.version
        filename = f"{version.value.lower()}.json"

        with open(os.path.join(self.data_folder, filename), "w") as json_file:
            json.dump(self.verses, json_file)
