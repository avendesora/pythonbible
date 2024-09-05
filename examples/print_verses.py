import pythonbible as bible
from pythonbible.versions import DEFAULT_VERSION as version

## select from among the below implemented versions by uncommenting:
# version = bible.Version.AMERICAN_STANDARD
# version = bible.Version.BEREAN_STANDARD
# version = bible.Version.KING_JAMES
# version = bible.Version.WORLD_ENGLISH

references = "Romans 14:1-23;Matthew 7:1-12"
norm_references = bible.get_references(references)
verse_ids_list = []
for ref in norm_references:
    verse_ids_list.append(bible.convert_reference_to_verse_ids(ref))

print(f"Using version: {version}\n")

for i, verse_ids in enumerate(verse_ids_list):
    print(f"\nPrinting from {norm_references[i].book} {norm_references[i].start_chapter}:{norm_references[i].start_verse} to {norm_references[i].end_chapter}:{norm_references[i].end_verse}\n")
    for verse_id in verse_ids:
        verse = bible.get_verse_text(verse_id, version)
        print(verse)