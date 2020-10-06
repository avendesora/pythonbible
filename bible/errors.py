class InvalidVerseError(Exception):
    """
    Raised when the verse id or book, chapter, and verse number being processed is not a valid Bible verse.
    """
