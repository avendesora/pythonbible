class InvalidChapterError(Exception):
    """
    Raised when the chapter number is not a valid chapter number for the given book of the Bible.
    """


class InvalidVerseError(Exception):
    """
    Raised when the verse id or book, chapter, and verse number being processed is not a valid Bible verse.
    """

    def __init__(self, message=None, **kwargs):
        self.message = message
        self.verse_id = kwargs.get("verse_id")
        self.book = kwargs.get("book")
        self.chapter = kwargs.get("chapter")
        self.verse = kwargs.get("verse")

        if not self.message:
            if self.book and self.chapter and self.verse:
                self.message = f"{self.book.name()} {self.chapter}:{self.verse} is not a valid verse."
            else:
                self.message = f"{self.verse_id} is not a valid verse."

        super(InvalidVerseError, self).__init__(self.message)
