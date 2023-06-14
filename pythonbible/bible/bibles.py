from __future__ import annotations

from typing import TYPE_CHECKING

import pythonbible.bible.asv.html as asv_html
import pythonbible.bible.asv.html_notes as asv_html_notes
import pythonbible.bible.asv.html_readers as asv_html_readers
import pythonbible.bible.asv.plain_text as asv_plain_text
import pythonbible.bible.asv.plain_text_notes as asv_plain_text_notes
import pythonbible.bible.asv.plain_text_readers as asv_plain_text_readers
import pythonbible.bible.kjv.html as kjv_html
import pythonbible.bible.kjv.html_notes as kjv_html_notes
import pythonbible.bible.kjv.html_readers as kjv_html_readers
import pythonbible.bible.kjv.plain_text as kjv_plain_text
import pythonbible.bible.kjv.plain_text_notes as kjv_plain_text_notes
import pythonbible.bible.kjv.plain_text_readers as kjv_plain_text_readers
from pythonbible.errors import MissingVerseFileError
from pythonbible.versions import Version

if TYPE_CHECKING:
    from pythonbible.bible.bible import Bible

BIBLES = {
    Version.AMERICAN_STANDARD: {
        "html": asv_html.bible,
        "html_notes": asv_html_notes.bible,
        "html_readers": asv_html_readers.bible,
        "plain_text": asv_plain_text.bible,
        "plain_text_notes": asv_plain_text_notes.bible,
        "plain_text_readers": asv_plain_text_readers.bible,
    },
    Version.KING_JAMES: {
        "html": kjv_html.bible,
        "html_notes": kjv_html_notes.bible,
        "html_readers": kjv_html_readers.bible,
        "plain_text": kjv_plain_text.bible,
        "plain_text_notes": kjv_plain_text_notes.bible,
        "plain_text_readers": kjv_plain_text_readers.bible,
    },
}


def get_bible(version: Version, bible_type: str) -> Bible:
    """Return the Bible for the given version and format.

    :param version: The version of the Bible
    :type version: Version
    :param bible_type: The type of the Bible
    :type bible_type: str
    :return: The Bible for the given version and type
    :rtype: Bible
    """
    try:
        return BIBLES[version][bible_type]
    except KeyError as error:
        raise MissingVerseFileError from error
