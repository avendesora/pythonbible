import pythonbible as bible


def test_format_scripture_references(
    normalized_references_complex, formatted_reference
):
    # Given a list of normalized references
    # When we format them into a reference string
    reference = bible.format_scripture_references(normalized_references_complex)

    # Then the reference string is correctly formatted.
    assert reference == formatted_reference


def test_format_scripture_references_null():
    # Given a null references object
    # When we attempt to format it into a reference string
    formatted_reference = bible.format_scripture_references(None)

    # Then the result is null
    assert formatted_reference is None


def test_format_scripture_references_sorting(
    normalized_references_complex, formatted_reference
):
    # Given a list of normalized references that are not in proper order
    normalized_references_complex.reverse()

    # When we format them into a reference string
    reference = bible.format_scripture_references(normalized_references_complex)

    # Then the reference string is correctly formatted.
    assert reference == formatted_reference
