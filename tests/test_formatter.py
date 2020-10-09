import bible


def test_format_scripture_references(normalized_references_complex):
    # Given a list of normalized references
    # When we format them into a reference string
    formatted_reference = bible.format_scripture_references(normalized_references_complex)

    # Then the reference string is correctly formatted.
    assert formatted_reference == "Psalms 130:4,8;Jeremiah 29:32-30:10,31:12;Matthew 1:18-2:18;Luke 3:5-7"


def test_format_scripture_references_null():
    # Given a null references object
    # When we attempt to format it into a reference string
    formatted_reference = bible.format_scripture_references(None)

    # Then the result is null
    assert formatted_reference is None
