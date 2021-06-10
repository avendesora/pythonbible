from typing import List

import pythonbible as bible


def test_count_books_single_book() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references("James 1:4-6")

    # When we get the count of books in the references
    number_of_books: int = bible.count_books(references[0])

    # Then the count is correct
    assert number_of_books == 1


def test_count_books_two_books() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references(
        "Matthew 19:3 - Mark 6:9"
    )

    # When we get the count of books in the references
    number_of_books: int = bible.count_books(references[0])

    # Then the count is correct
    assert number_of_books == 2


def test_count_books_multiple_books() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references(
        "Genesis - Deuteronomy"
    )

    # When we get the count of books in the references
    number_of_books: int = bible.count_books(references[0])

    # Then the count is correct
    assert number_of_books == 5


def test_count_books_multiple_references() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references(
        "Genesis - Deuteronomy, Matthew 19:3 - Mark 6:9, James 1:4-6"
    )

    # When we get the count of books in the references
    number_of_books: int = bible.count_books(references)

    # Then the count is correct
    assert number_of_books == 5 + 2 + 1


def test_count_books_string() -> None:
    # Given a string containing one or more Scripture references
    reference: str = "Genesis - Deuteronomy, Matthew 19:3 - Mark 6:9, James 1:4-6"

    # When we get the count of books in the references
    number_of_books: int = bible.count_books(reference)

    # Then the count is correct
    assert number_of_books == 5 + 2 + 1


def test_count_chapters_single_chapter() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references("James 1:4-6")

    # When we get the count of chapters in the references
    number_of_chapters: int = bible.count_chapters(references[0])

    # Then the count is correct
    assert number_of_chapters == 1


def test_count_chapters_two_chapters() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references("James 1-2")

    # When we get the count of chapters in the references
    number_of_chapters: int = bible.count_chapters(references[0])

    # Then the count is correct
    assert number_of_chapters == 2


def test_count_chapters_multiple_chapters() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references("James")

    # When we get the count of chapters in the references
    number_of_chapters: int = bible.count_chapters(references[0])

    # Then the count is correct
    assert number_of_chapters == 5


def test_count_chapters_multiple_books() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references(
        "Matthew 28:1 - Luke 1:10"
    )

    # When we get the count of chapters in the references
    number_of_chapters: int = bible.count_chapters(references[0])

    # Then the count is correct
    assert number_of_chapters == 1 + 16 + 1


def test_count_chapters_multiple_references() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references(
        "Genesis, Matthew - Acts"
    )

    # When we get the count of chapters in the references
    number_of_chapters: int = bible.count_chapters(references)

    # Then the count is correct
    assert number_of_chapters == 50 + 28 + 16 + 24 + 21 + 28  # 167 total


def test_count_chapters_string() -> None:
    # Given a string containing one or more Scripture references
    reference: str = "Genesis, Matthew - Acts"

    # When we get the count of chapters in the reference
    number_of_chapters: int = bible.count_chapters(reference)

    # Then the count is correct
    assert number_of_chapters == 50 + 28 + 16 + 24 + 21 + 28  # 167 total


def test_count_verses_single_verse() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references("Genesis 1:1")

    # When we get the count of verses in the references
    number_of_verses: int = bible.count_verses(references[0])

    # Then the count is correct
    assert number_of_verses == 1


def test_count_verses_multiple_verses() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references("Genesis 1:6-10")

    # When we get the count of verses in the references
    number_of_verses: int = bible.count_verses(references[0])

    # Then the count is correct
    assert number_of_verses == 5


def test_count_verses_multiple_chapters() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references(
        "Matthew 5:3-7:27"
    )

    # When we get the count of verses in the references
    number_of_verses: int = bible.count_verses(references[0])

    # Then the count is correct
    assert number_of_verses == 46 + 34 + 27


def test_count_verses_multiple_books() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references("1 John - Jude")

    # When we get the count of verses in the references
    number_of_verses: int = bible.count_verses(references[0])

    # Then the count is correct
    assert number_of_verses == (10 + 29 + 24 + 21 + 21) + 13 + 14 + 25


def test_count_verses_multiple_references() -> None:
    # Given a list of references
    references: List[bible.NormalizedReference] = bible.get_references(
        "Genesis 1:1; John 3:16; Romans 15:5-7,13"
    )

    # When we get the count of verses in the references
    number_of_verses: int = bible.count_verses(references)

    # Then the count is correct
    assert number_of_verses == 1 + 1 + (3 + 1)


def test_count_verses_string() -> None:
    # Given a string containing one or more Scripture references
    reference: str = "Genesis 1:1; John 3:16; Romans 15:5-7,13"

    # When we get the count of verses in the reference
    number_of_verses: int = bible.count_verses(reference)

    # Then the count is correct
    assert number_of_verses == 1 + 1 + (3 + 1)
