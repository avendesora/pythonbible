from __future__ import annotations

import pytest


@pytest.fixture
def formatted_reference() -> str:
    return "Psalms 130:4,8;Jeremiah 29:32-30:10,31:12;Matthew 1:18-2:18;Luke 3:5-7"


@pytest.fixture
def html_scripture_text() -> str:
    return (
        "<h1>Matthew</h1>\n"
        "<h2>Chapter 18</h2>\n"
        "<p><sup>12</sup> How think ye? if a man have an hundred sheep, and one of "
        "them be gone astray, doth he not leave the ninety and nine, and goeth into "
        "the mountains, and seeketh that which is gone astray? <sup>13</sup> And if so "
        "be that he find it, verily I say unto you, he rejoiceth more of that "
        "[sheep], than of the ninety and nine which went not astray. <sup>14</sup> "
        "Even so it is not the will of your Father which is in heaven, that one of "
        "these little ones should perish.</p>\n"
        "<h1>Luke</h1>\n"
        "<h2>Chapter 15</h2>\n"
        "<p><sup>3</sup> And he spake this parable unto them, saying, <sup>4</sup> "
        "What man of you, having an hundred sheep, if he lose one of them, doth not "
        "leave the ninety and nine in the wilderness, and go after that which is "
        "lost, until he find it? <sup>5</sup> And when he hath found [it], he layeth "
        "[it] on his shoulders, rejoicing. <sup>6</sup> And when he cometh home, he "
        "calleth together [his] friends and neighbours, saying unto them, Rejoice "
        "with me; for I have found my sheep which was lost. <sup>7</sup> I say unto "
        "you, that likewise joy shall be in heaven over one sinner that repenteth, "
        "more than over ninety and nine just persons, which need no repentance.</p>\n"
    )


@pytest.fixture
def non_html_scripture_text() -> str:
    return (
        "Matthew\n"
        "\n"
        "Chapter 18\n"
        "\n"
        "12. How think ye? if a man have an hundred sheep, and one of them be gone "
        "astray, doth he not leave the ninety and nine, and goeth into the mountains, "
        "and seeketh that which is gone astray? 13. And if so be that he find it, "
        "verily I say unto you, he rejoiceth more of that [sheep], than of the ninety "
        "and nine which went not astray. 14. Even so it is not the will of your "
        "Father which is in heaven, that one of these little ones should perish.\n"
        "\n"
        "\n"
        "Luke\n"
        "\n"
        "Chapter 15\n"
        "\n"
        "3. And he spake this parable unto them, saying, 4. What man of you, having "
        "an hundred sheep, if he lose one of them, doth not leave the ninety and nine "
        "in the wilderness, and go after that which is lost, until he find it? 5. And "
        "when he hath found [it], he layeth [it] on his shoulders, rejoicing. 6. And "
        "when he cometh home, he calleth together [his] friends and neighbours, "
        "saying unto them, Rejoice with me; for I have found my sheep which was lost. "
        "7. I say unto you, that likewise joy shall be in heaven over one sinner that "
        "repenteth, more than over ninety and nine just persons, which need no "
        "repentance.\n"
    )


@pytest.fixture
def non_html_scripture_text_readers() -> str:
    return (
        "Matthew\n"
        "\n"
        "Chapter 18\n"
        "\n"
        "How think ye? if a man have an hundred sheep, and one of them be gone "
        "astray, doth he not leave the ninety and nine, and goeth into the mountains, "
        "and seeketh that which is gone astray? And if so be that he find it, verily "
        "I say unto you, he rejoiceth more of that [sheep], than of the ninety and "
        "nine which went not astray. Even so it is not the will of your Father which "
        "is in heaven, that one of these little ones should perish.\n"
        "\n"
        "\n"
        "Luke\n"
        "\n"
        "Chapter 15\n"
        "\n"
        "And he spake this parable unto them, saying, What man of you, having an "
        "hundred sheep, if he lose one of them, doth not leave the ninety and nine in "
        "the wilderness, and go after that which is lost, until he find it? And when "
        "he hath found [it], he layeth [it] on his shoulders, rejoicing. And when he "
        "cometh home, he calleth together [his] friends and neighbours, saying unto "
        "them, Rejoice with me; for I have found my sheep which was lost. I say unto "
        "you, that likewise joy shall be in heaven over one sinner that repenteth, "
        "more than over ninety and nine just persons, which need no repentance.\n"
    )


@pytest.fixture
def html_scripture_text_one_verse_per_paragraph() -> str:
    return (
        "<h1>Matthew</h1>\n"
        "<h2>Chapter 18</h2>\n"
        "<p><sup>12</sup> How think ye? if a man have an hundred sheep, and one of "
        "them be gone astray, doth he not leave the ninety and nine, and goeth into "
        "the mountains, and seeketh that which is gone astray?</p>\n"
        "<p><sup>13</sup> And if so be that he find it, verily I say unto you, he "
        "rejoiceth more of that [sheep], than of the ninety and nine which went not "
        "astray.</p>\n"
        "<p><sup>14</sup> Even so it is not the will of your Father which is in "
        "heaven, that one of these little ones should perish.</p>\n"
        "<h2>Chapter 19</h2>\n"
        "<p><sup>1</sup> And it came to pass, [that] when Jesus had finished these "
        "sayings, he departed from Galilee, and came into the coasts of Judaea beyond "
        "Jordan;</p>\n"
    )


@pytest.fixture
def non_html_scripture_text_one_verse_per_paragraph() -> str:
    return (
        "Matthew\n"
        "\n"
        "Chapter 18\n"
        "\n"
        "12. How think ye? if a man have an hundred sheep, and one of them be gone "
        "astray, doth he not leave the ninety and nine, and goeth into the mountains, "
        "and seeketh that which is gone astray?\n"
        "13. And if so be that he find it, verily I say unto you, he rejoiceth more "
        "of that [sheep], than of the ninety and nine which went not astray.\n"
        "14. Even so it is not the will of your Father which is in heaven, that one "
        "of these little ones should perish.\n"
        "\n"
        "\n"
        "Luke\n"
        "\n"
        "Chapter 15\n"
        "\n"
        "3. And he spake this parable unto them, saying,\n"
        "4. What man of you, having an hundred sheep, if he lose one of them, doth "
        "not leave the ninety and nine in the wilderness, and go after that which is "
        "lost, until he find it?\n"
        "5. And when he hath found [it], he layeth [it] on his shoulders, rejoicing.\n"
        "6. And when he cometh home, he calleth together [his] friends and "
        "neighbours, saying unto them, Rejoice with me; for I have found my sheep "
        "which was lost.\n"
        "7. I say unto you, that likewise joy shall be in heaven over one sinner that "
        "repenteth, more than over ninety and nine just persons, which need no "
        "repentance.\n"
    )


@pytest.fixture
def verse_text_no_verse_number() -> str:
    return "In the beginning God created the heaven and the earth."


@pytest.fixture
def verse_ids_multiple_chapters() -> list[int]:
    return [
        40018012,
        40018013,
        40018014,
        40019001,
    ]
