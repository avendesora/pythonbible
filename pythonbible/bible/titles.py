from __future__ import annotations

import pythonbible.bible.asv.titles as asv_titles
import pythonbible.bible.kjv.titles as kjv_titles
from pythonbible.versions import Version

SHORT_TITLES = {
    Version.AMERICAN_STANDARD: asv_titles.short_titles,
    Version.KING_JAMES: kjv_titles.short_titles,
}

LONG_TITLES = {
    Version.AMERICAN_STANDARD: asv_titles.long_titles,
    Version.KING_JAMES: kjv_titles.long_titles,
}
