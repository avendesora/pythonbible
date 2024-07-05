import pythonbible as bible

# version = bible.Version.AMERICAN_STANDARD
# version = bible.Version.KING_JAMES
version = bible.Version.WORLD_ENGLISH

reference = bible.NormalizedReference(bible.Book.ROMANS, 14, 1, 14, 26)
verse_ids = bible.convert_reference_to_verse_ids(reference)

for verse_id in verse_ids:
    verse = bible.get_verse_text(verse_id, version)
    print(verse)
