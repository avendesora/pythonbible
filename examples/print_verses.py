import argparse

import pythonbible as bible
from pythonbible.versions import DEFAULT_VERSION


def get_version(version: str) -> bible.Version:
    if version in ["BSB", "BEREAN_STANDARD", "0"]:
        return bible.Version.BEREAN_STANDARD
    elif version in ["WEB", "WORLD_ENGLISH", "1"]:
        return bible.Version.WORLD_ENGLISH
    elif version in ["ASV", "AMERICAN_STANDARD", "2"]:
        return bible.Version.AMERICAN_STANDARD
    elif version in ["KJV", "KING_JAMES", "3"]:
        return bible.Version.KING_JAMES
    else:
        raise NotImplementedError(f"Version {version} not implemented.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print chosen verses from the Bible.")
    parser.add_argument(
        "-r",
        "--references",
        required=True,
        type=str,
        help="Specify the references of the verses to print.",
    )

    parser.add_argument(
        "-v",
        "--version",
        type=str,
        default=DEFAULT_VERSION,
        help="Specify the version of the Bible to use.",
    )
    args = parser.parse_args()
    if type(args.version) is not bible.Version:
        VERSION = get_version(args.version)
    else:
        VERSION = args.version

    print(f"Using version: {VERSION}\n")

    references = args.references
    norm_references = bible.get_references(references)

    verse_ids_list = []
    for ref in norm_references:
        verse_ids_list.append(bible.convert_reference_to_verse_ids(ref))

    for i, verse_ids in enumerate(verse_ids_list):
        print(
            f"\nPrinting from {norm_references[i].book} "
            f"{norm_references[i].start_chapter}:{norm_references[i].start_verse} "
            f"to {norm_references[i].end_chapter}:{norm_references[i].end_verse}\n"
        )
        for verse_id in verse_ids:
            verse = bible.get_verse_text(verse_id, VERSION)
            print(verse)
