use once_cell::sync::Lazy;
use regex::escape;
use std::collections::HashMap;

pub const FIRST: &str = r"1|I\s+|1st\s+|First\s+";
pub const SECOND: &str = r"2|II|2nd\s+|Second\s+";
pub const THIRD: &str = r"3|III|3rd\s+|Third\s+";
pub static FIRST_BOOK: Lazy<String> = Lazy::new(|| format!(r"{}|(First\s+Book\s+of(?:\s+the)?)", FIRST));
pub static SECOND_BOOK: Lazy<String> = Lazy::new(|| format!(r"{}|(Second\s+Book\s+of(?:\s+the)?)", SECOND));

lazy_static::lazy_static! {
    static ref JOHN_REGULAR_EXPRESSION: String = {
        // excluded suffixes from Python: "shua", "b", "nah", "n", "el"
        let jo_exclude_suffixes = ["shua", "b", "nah", "n", "el"];
        // escape each suffix for regex and join with '|'
        let escaped = jo_exclude_suffixes
            .iter()
            .map(|s| regex::escape(s))
            .collect::<Vec<_>>()
            .join("|");
        // build the negative lookahead like Python: (?!...)
        let jo_negative_lookahead = format!(r"(?!{})", escaped);
        // abbreviations: Joh\.*, Jhn\.*, Jo\.*(negative lookahead), Jn\.*
        let abbreviations = vec![
            r"Joh\.*".to_string(),
            r"Jhn\.*".to_string(),
            format!(r"Jo\.*{}", jo_negative_lookahead),
            r"Jn\.*".to_string(),
        ];
        // final pattern: (John|Joh\.*|Jhn\.*|Jo\.*(?!... )|Jn\.*)
        format!(r"(John|{})", abbreviations.join("|"))
    };
}

/// Helper routines to assemble regex fragments similar to the Python functions.
fn build_book_regular_expression(book: &str, prefix: Option<&str>, suffix: Option<&str>) -> String {
    add_suffix(&add_prefix(book, prefix), suffix)
}

fn add_prefix(regex: &str, prefix: Option<&str>) -> String {
    match prefix {
        None => regex.to_string(),
        Some(p) => format!(r"(?:{})(?:\s)?{}", p, regex),
    }
}

fn add_suffix(regex: &str, suffix: Option<&str>) -> String {
    match suffix {
        None => regex.to_string(),
        Some(s) => format!(r"{}(?:\s*{})?", regex, s),
    }
}

/// Regular-expression fragments used to build book regexes.
const _SAMUEL_REGULAR_EXPRESSION: &str = r"(Samuel|Sam\.*|Sa\.*|Sm\.*)";
const _KINGS_REGULAR_EXPRESSION: &str = r"(Kings|Kgs\.*|Kin\.*|Ki\.*)";
const _CHRONICLES_REGULAR_EXPRESSION: &str = r"(Chronicles|Chron\.*|Chro\.*|Chr\.*|Ch\.*)";
const _CORINTHIANS_REGULAR_EXPRESSION: &str = r"Co\.*(?:r\.*(?:inthians)?)?";
const _THESSALONIANS_REGULAR_EXPRESSION: &str = r"Th\.*(?:(s|(es(?:s)?))\.*(?:alonians)?)?";
const _TIMOTHY_REGULAR_EXPRESSION: &str = r"Ti\.*(?:m\.*(?:othy)?)?";
const _PETER_REGULAR_EXPRESSION: &str = r"(Pe\.*(?:t\.*(?:er)?)?|Pt\.*)";
const _MACCABEES_REGULAR_EXPRESSION: &str = r"(Maccabees|Macc\.*|Mac\.*|Ma\.*|M\.*)";

const _EPISTLE_OF_PAUL_TO: &str = r"Epistle\s+of\s+Paul\s+(?:the\s+Apostle\s+)?to(?:\s+the)?";
const _GENERAL_EPISTLE_OF: &str = r"(?:General\s+)?Epistle\s+(?:General\s+)?of";

lazy_static::lazy_static! {
    // Derived complex fragments (constructed as Strings because they interpolate other constants).
    static ref _FIRST_PAUL_EPISTLE: String = format!(r"{}|(First\s+{})", FIRST, _EPISTLE_OF_PAUL_TO);
    static ref _SECOND_PAUL_EPISTLE: String = format!(r"{}|(Second\s+{})", SECOND, _EPISTLE_OF_PAUL_TO);

    static ref _FIRST_GENERAL_EPISTLE: String = format!(r"{}|(First\s+{})", FIRST, _GENERAL_EPISTLE_OF);
    static ref _SECOND_GENERAL_EPISTLE: String = format!(r"{}|(Second\s+{})", SECOND, _GENERAL_EPISTLE_OF);
    static ref _THIRD_GENERAL_EPISTLE: String = format!(r"{}|(Third\s+{})", THIRD, _GENERAL_EPISTLE_OF);
}

/// Simple book representation.
#[derive(Clone, Debug)]
pub struct BookItem {
    /// canonical short name, e.g. `John`
    pub(crate) name: &'static str,
    /// canonical book number
    pub(crate) number: u8,
    /// canonical matching regular expression (compiled/constructed)
    pub(crate) regular_expression: String,
    /// allowed abbreviations
    pub(crate) abbreviations: &'static [&'static str],
}

/// Public static slice of books constructed lazily.
pub static BOOKS: Lazy<Vec<BookItem>> = Lazy::new(|| {
    vec![
        BookItem {
            name: "Genesis",
            number: 1,
            regular_expression: r"Gen\.*(?:esis)?".to_string(),
            abbreviations: &["Gen"],
        },
        BookItem {
            name: "Exodus",
            number: 2,
            regular_expression: r"Exo\.*(?:d\.*)?(?:us)?".to_string(),
            abbreviations: &["Exo", "Exod"],
        },
        BookItem {
            name: "Leviticus",
            number: 3,
            regular_expression: r"Lev\.*(?:iticus)?".to_string(),
            abbreviations: &["Lev"],
        },
        BookItem {
            name: "Numbers",
            number: 4,
            regular_expression: r"Num\.*(?:bers)?".to_string(),
            abbreviations: &["Num"],
        },
        BookItem {
            name: "Deuteronomy",
            number: 5,
            regular_expression: r"Deu\.*(?:t\.*)?(?:eronomy)?".to_string(),
            abbreviations: &["Deu", "Deut"],
        },
        BookItem {
            name: "Joshua",
            number: 6,
            regular_expression: r"(Joshua|Josh\.*|Jos\.*|Jsh\.*)".to_string(),
            abbreviations: &["Jos", "Jsh", "Josh"],
        },
        BookItem {
            name: "Judges",
            number: 7,
            regular_expression: r"(Judges|Judg\.*|Jdgs\.*|Jdg\.*)".to_string(),
            abbreviations: &["Jdg", "Jdgs", "Judg"],
        },
        BookItem {
            name: "Ruth",
            number: 8,
            regular_expression: r"(Ruth|Rut\.*|Rth\.*)".to_string(),
            abbreviations: &["Rth", "Rut"],
        },
        BookItem {
            name: "1 Samuel",
            number: 9,
            regular_expression: build_book_regular_expression(
                _SAMUEL_REGULAR_EXPRESSION,
                Some(&*FIRST_BOOK),
                Some(r"Otherwise\s+Called\s+The\s+First\s+Book\s+of\s+the\s+Kings"),
            ),
            abbreviations: &["Sa", "Sam", "Sm"],
        },
        BookItem {
            name: "2 Samuel",
            number: 10,
            regular_expression: build_book_regular_expression(
                _SAMUEL_REGULAR_EXPRESSION,
                Some(&*SECOND_BOOK),
                Some(r"Otherwise\s+Called\s+The\s+Second\s+Book\s+of\s+the\s+Kings"),
            ),
            abbreviations: &["Sa", "Sam", "Sm"],
        },
        BookItem {
            name: "1 Kings",
            number: 11,
            regular_expression: build_book_regular_expression(
                _KINGS_REGULAR_EXPRESSION,
                Some(&*FIRST_BOOK),
                Some(r"\,\s+Commonly\s+Called\s+the\s+Third\s+Book\s+of\s+the\s+Kings"),
            ),
            abbreviations: &["Kgs", "Ki", "Kin"],
        },
        BookItem {
            name: "2 Kings",
            number: 12,
            regular_expression: build_book_regular_expression(
                _KINGS_REGULAR_EXPRESSION,
                Some(&*SECOND_BOOK),
                Some(r"\,\s+Commonly\s+Called\s+the\s+Fourth\s+Book\s+of\s+the\s+Kings"),
            ),
            abbreviations: &["Kgs", "Ki", "Kin"],
        },
        BookItem {
            name: "1 Chronicles",
            number: 13,
            regular_expression: build_book_regular_expression(_CHRONICLES_REGULAR_EXPRESSION, Some(&*FIRST_BOOK), None),
            abbreviations: &["Ch", "Chr", "Chro", "Chron"],
        },
        BookItem {
            name: "2 Chronicles",
            number: 14,
            regular_expression: build_book_regular_expression(_CHRONICLES_REGULAR_EXPRESSION, Some(&*SECOND_BOOK), None),
            abbreviations: &["Ch", "Chr", "Chro", "Chron"],
        },
        BookItem {
            name: "Ezra",
            number: 15,
            regular_expression: r"Ezr\.*(?:a)?".to_string(),
            abbreviations: &["Ezr"],
        },
        BookItem {
            name: "Nehemiah",
            number: 16,
            regular_expression: r"Neh\.*(?:emiah)?".to_string(),
            abbreviations: &["Neh"],
        },
        BookItem {
            name: "Esther",
            number: 17,
            regular_expression: r"Est\.*(?:h\.*)?(?:er)?".to_string(),
            abbreviations: &["Est", "Esth"],
        },
        BookItem {
            name: "Job",
            number: 18,
            regular_expression: r"Job".to_string(),
            abbreviations: &[],
        },
        BookItem {
            name: "Psalms",
            number: 19,
            regular_expression: r"(Psalms|Psalm|Pslm\.*|Psa\.*|Psm\.*|Pss\.*|Ps\.*)".to_string(),
            abbreviations: &["Ps", "Psa", "Pslm", "Psm", "Pss"],
        },
        BookItem {
            name: "Proverbs",
            number: 20,
            regular_expression: r"(Proverbs|Prov\.*|Pro\.*|Prv\.*)".to_string(),
            abbreviations: &["Pro", "Prov", "Prv"],
        },
        BookItem {
            name: "Ecclesiastes",
            number: 21,
            regular_expression: r"(Ecclesiastes(?:\s+or\,\s+the\s+Preacher)?|Eccles\.*(?!iasticus?)|Eccle\.*(?!siasticus?)|Eccl\.*(?!esiasticus?)(?!us?)|Ecc\.*(?!lesiasticus?)(?!lus?)|(?<!Z)Ec\.*(?!clesiasticus?)(?!clus?)|Qoh\.*)".to_string(),
            abbreviations: &["Ec", "Ecc", "Eccl", "Eccle", "Eccles", "Qoh"],
        },
        BookItem {
            name: "Song of Songs",
            number: 22,
            regular_expression: r"(Song(?: of (Solomon|Songs|Sol\.*))?)|Canticles|(Canticle(?: of Canticles)?)|SOS|Cant".to_string(),
            abbreviations: &["Cant", "Canticle", "Canticles", "Song", "Song of Sol", "SOS"],
        },
        BookItem {
            name: "Isaiah",
            number: 23,
            regular_expression: r"Isa\.*(?:iah)?".to_string(),
            abbreviations: &["Isa"],
        },
        BookItem {
            name: "Jeremiah",
            number: 24,
            regular_expression: r"Jer\.*(?:emiah)?".to_string(),
            abbreviations: &["Jer"],
        },
        BookItem {
            name: "Lamentations",
            number: 25,
            regular_expression: build_book_regular_expression(r"Lam\.*(?:entations)?", None, Some(r"of\s+Jeremiah")),
            abbreviations: &["Lam"],
        },
        BookItem {
            name: "Ezekiel",
            number: 26,
            regular_expression: r"(Ezekiel|Ezek\.*|Eze\.*|Ezk\.*)".to_string(),
            abbreviations: &["Eze", "Ezek", "Ezk"],
        },
        BookItem {
            name: "Daniel",
            number: 27,
            regular_expression: r"Dan\.*(?:iel)?".to_string(),
            abbreviations: &["Dan"],
        },
        BookItem {
            name: "Hosea",
            number: 28,
            regular_expression: r"Hos\.*(?:ea)?".to_string(),
            abbreviations: &["Hos"],
        },
        BookItem {
            name: "Joel",
            number: 29,
            regular_expression: r"Joe\.*(?:l)?".to_string(),
            abbreviations: &["Joe"],
        },
        BookItem {
            name: "Amos",
            number: 30,
            regular_expression: r"Amo\.*(?:s)?".to_string(),
            abbreviations: &["Amo"],
        },
        BookItem {
            name: "Obadiah",
            number: 31,
            regular_expression: r"Oba\.*(?:d\.*(?:iah)?)?".to_string(),
            abbreviations: &["Oba", "Obad"],
        },
        BookItem {
            name: "Jonah",
            number: 32,
            regular_expression: r"Jonah|Jon\.*|Jnh\.*".to_string(),
            abbreviations: &["Jnh", "Jon"],
        },
        BookItem {
            name: "Micah",
            number: 33,
            regular_expression: r"Mic\.*(?:ah)?".to_string(),
            abbreviations: &["Mic"],
        },
        BookItem {
            name: "Nahum",
            number: 34,
            regular_expression: r"(?<!Jo)Nah\.*(?:um)?".to_string(),
            abbreviations: &["Nah"],
        },
        BookItem {
            name: "Habakkuk",
            number: 35,
            regular_expression: r"Hab\.*(?:akkuk)?".to_string(),
            abbreviations: &["Hab"],
        },
        BookItem {
            name: "Zephaniah",
            number: 36,
            regular_expression: r"Zep\.*(?:h\.*(?:aniah)?)?".to_string(),
            abbreviations: &["Zep", "Zeph"],
        },
        BookItem {
            name: "Haggai",
            number: 37,
            regular_expression: r"Hag\.*(?:gai)?".to_string(),
            abbreviations: &["Hag"],
        },
        BookItem {
            name: "Zechariah",
            number: 38,
            regular_expression: r"Zec\.*(?:h\.*(?:ariah)?)?".to_string(),
            abbreviations: &["Zec", "Zech"],
        },
        BookItem {
            name: "Malachi",
            number: 39,
            regular_expression: r"Mal\.*(?:achi)?".to_string(),
            abbreviations: &["Mal"],
        },
        BookItem {
            name: "Matthew",
            number: 40,
            regular_expression: r"Mat\.*(?:t\.*(?:hew)?)?".to_string(),
            abbreviations: &["Mat", "Matt"],
        },
        BookItem {
            name: "Mark",
            number: 41,
            regular_expression: r"Mark|Mar\.*|Mrk\.*".to_string(),
            abbreviations: &["Mar", "Mrk"],
        },
        BookItem {
            name: "Luke",
            number: 42,
            regular_expression: r"Luk\.*(?:e)?".to_string(),
            abbreviations: &["Luk"],
        },
        BookItem {
            name: "John",
            number: 43,
            regular_expression: format!(r"(?<!(?:1|2|3|I)\s)(?<!(?:1|2|3|I)){}", JOHN_REGULAR_EXPRESSION.as_str()),
            abbreviations: &["Jhn", "Jn", "Jo", "Joh"],
        },
        BookItem {
            name: "Acts",
            number: 44,
            regular_expression: build_book_regular_expression(r"Act\.*(?:s)?", None, Some("of the Apostles")),
            abbreviations: &["Act"],
        },
        BookItem {
            name: "Romans",
            number: 45,
            regular_expression: r"Rom\.*(?:ans)?".to_string(),
            abbreviations: &["Rom"],
        },
        BookItem {
            name: "1 Corinthians",
            number: 46,
            regular_expression: build_book_regular_expression(_CORINTHIANS_REGULAR_EXPRESSION, Some(&_FIRST_PAUL_EPISTLE), None),
            abbreviations: &["Co", "Cor"],
        },
        BookItem {
            name: "2 Corinthians",
            number: 47,
            regular_expression: build_book_regular_expression(_CORINTHIANS_REGULAR_EXPRESSION, Some(&_SECOND_PAUL_EPISTLE), None),
            abbreviations: &["Co", "Cor"],
        },
        BookItem {
            name: "Galatians",
            number: 48,
            regular_expression: r"Gal\.*(?:atians)?".to_string(),
            abbreviations: &["Gal"],
        },
        BookItem {
            name: "Ephesians",
            number: 49,
            regular_expression: r"(?<!Z)Eph\.*(?:es\.*(?:ians)?)?".to_string(),
            abbreviations: &["Eph", "Ephes"],
        },
        BookItem {
            name: "Philippians",
            number: 50,
            regular_expression: r"Ph(?:(p\.*)|(?:il\.*(?!e\.*(?:m\.*(?:on)?)?)(?:ippians)?))".to_string(),
            abbreviations: &["Php", "Phil"],
        },
        BookItem {
            name: "Colossians",
            number: 51,
            regular_expression: r"Col\.*(?:ossians)?".to_string(),
            abbreviations: &["Col"],
        },
        BookItem {
            name: "1 Thessalonians",
            number: 52,
            regular_expression: build_book_regular_expression(_THESSALONIANS_REGULAR_EXPRESSION, Some(&_FIRST_PAUL_EPISTLE), None),
            abbreviations: &["Th", "Thes", "Thess", "Ths"],
        },
        BookItem {
            name: "2 Thessalonians",
            number: 53,
            regular_expression: build_book_regular_expression(_THESSALONIANS_REGULAR_EXPRESSION, Some(&_SECOND_PAUL_EPISTLE), None),
            abbreviations: &["Th", "Thes", "Thess", "Ths"],
        },
        BookItem {
            name: "1 Timothy",
            number: 54,
            regular_expression: build_book_regular_expression(_TIMOTHY_REGULAR_EXPRESSION, Some(&_FIRST_PAUL_EPISTLE), None),
            abbreviations: &["Ti", "Tim"],
        },
        BookItem {
            name: "2 Timothy",
            number: 55,
            regular_expression: build_book_regular_expression(_TIMOTHY_REGULAR_EXPRESSION, Some(&_SECOND_PAUL_EPISTLE), None),
            abbreviations: &["Ti", "Tim"],
        },
        BookItem {
            name: "Titus",
            number: 56,
            regular_expression: r"Tit\.*(?:us)?".to_string(),
            abbreviations: &["Tit"],
        },
        BookItem {
            name: "Philemon",
            number: 57,
            regular_expression: r"(Philemon|Philem\.*|Phile\.*|Phlm\.*|Phi\.*(?!l)|Phm\.*)".to_string(),
            abbreviations: &["Phi", "Phile", "Philem", "Phlm", "Phm"],
        },
        BookItem {
            name: "Hebrews",
            number: 58,
            regular_expression: r"Heb\.*(?:rews)?".to_string(),
            abbreviations: &["Heb"],
        },
        BookItem {
            name: "James",
            number: 59,
            regular_expression: r"Ja(?:me)?s\.*".to_string(),
            abbreviations: &["Jas"],
        },
        BookItem {
            name: "1 Peter",
            number: 60,
            regular_expression: build_book_regular_expression(_PETER_REGULAR_EXPRESSION, Some(&_FIRST_GENERAL_EPISTLE), None),
            abbreviations: &["Pe", "Pet", "Pt"],
        },
        BookItem {
            name: "2 Peter",
            number: 61,
            regular_expression: build_book_regular_expression(_PETER_REGULAR_EXPRESSION, Some(&_SECOND_GENERAL_EPISTLE), None),
            abbreviations: &["Pe", "Pet", "Pt"],
        },
        BookItem {
            name: "1 John",
            number: 62,
            regular_expression: build_book_regular_expression(JOHN_REGULAR_EXPRESSION.as_str(), Some(&_FIRST_GENERAL_EPISTLE), None),
            abbreviations: &["Jhn", "Jn", "Jo", "Joh"],
        },
        BookItem {
            name: "2 John",
            number: 63,
            regular_expression: build_book_regular_expression(JOHN_REGULAR_EXPRESSION.as_str(), Some(&_SECOND_GENERAL_EPISTLE), None),
            abbreviations: &["Jhn", "Jn", "Jo", "Joh"],
        },
        BookItem {
            name: "3 John",
            number: 64,
            regular_expression: build_book_regular_expression(JOHN_REGULAR_EXPRESSION.as_str(), Some(&_THIRD_GENERAL_EPISTLE), None),
            abbreviations: &["Jhn", "Jn", "Jo", "Joh"],
        },
        BookItem {
            name: "Jude",
            number: 65,
            regular_expression: r"Jud\.*(:?e)?(?!ges)".to_string(),
            abbreviations: &["Jud"],
        },
        BookItem {
            name: "Revelation",
            number: 66,
            regular_expression: build_book_regular_expression(r"Rev\.*(?:elation)?", None, Some(r"of ((Jesus Christ)|John|(St. John the Divine))")),
            abbreviations: &["Rev"],
        },
        BookItem {
            name: "1 Esdras",
            number: 67,
            regular_expression: build_book_regular_expression(r"(Esdras|Esdr\.*|Esd\.*|Es\.*)", Some(FIRST), None),
            abbreviations: &["Es", "Esd", "Esdr"],
        },
        BookItem {
            name: "Tobit",
            number: 68,
            regular_expression: r"(Tobit|Tob\.*|Tb\.*)".to_string(),
            abbreviations: &["Tb", "Tob"],
        },
        BookItem {
            name: "Wisdom of Solomon",
            number: 69,
            regular_expression: r"(Wisdom of Solomon|Wisdom|Wisd\.* of Sol\.*|Wis\.*|(?<!Hebre)Ws\.*)".to_string(),
            abbreviations: &["Wis", "Wisd of Sol", "Ws"],
        },
        BookItem {
            name: "Ecclesiasticus",
            number: 70,
            regular_expression: r"(Sirach|Sir\.*|Ecclesiasticus|Ecclus\.*)".to_string(),
            abbreviations: &["Ecclus", "Sir"],
        },
        BookItem {
            name: "1 Maccabees",
            number: 71,
            regular_expression: build_book_regular_expression(_MACCABEES_REGULAR_EXPRESSION, Some(FIRST), None),
            abbreviations: &["M", "Ma", "Mac", "Macc"],
        },
        BookItem {
            name: "2 Maccabees",
            number: 72,
            regular_expression: build_book_regular_expression(_MACCABEES_REGULAR_EXPRESSION, Some(SECOND), None),
            abbreviations: &["M", "Ma", "Mac", "Macc"],
        },
    ]
});

pub enum Book {
    Genesis,
    Exodus,
    Leviticus,
    Numbers,
    Deuteronomy,
    Joshua,
    Judges,
    Ruth,
    Samuel1,
    Samuel2,
    Kings1,
    Kings2,
    Chronicles1,
    Chronicles2,
    Ezra,
    Nehemiah,
    Esther,
    Job,
    Psalms,
    Proverbs,
    Ecclesiastes,
    SongOfSongs,
    Isaiah,
    Jeremiah,
    Lamentations,
    Ezekiel,
    Daniel,
    Hosea,
    Joel,
    Amos,
    Obadiah,
    Jonah,
    Micah,
    Nahum,
    Habakkuk,
    Zephaniah,
    Haggai,
    Zechariah,
    Malachi,
    Matthew,
    Mark,
    Luke,
    John,
    Acts,
    Romans,
    Corinthians1,
    Corinthians2,
    Galatians,
    Ephesians,
    Philippians,
    Colossians,
    Thessalonians1,
    Thessalonians2,
    Timothy1,
    Timothy2,
    Titus,
    Philemon,
    Hebrews,
    James,
    Peter1,
    Peter2,
    John1,
    John2,
    John3,
    Jude,
    Revelation,
    Esdras1,
    Tobit,
    WisdomOfSolomon,
    Ecclesiasticus,
    Maccabees1,
    Maccabees2,
}

impl Book {
    pub fn item(&self) -> &'static BookItem {
        match *self {
            Book::Genesis => &BOOKS[0],
            Book::Exodus => &BOOKS[1],
            Book::Leviticus => &BOOKS[2],
            Book::Numbers => &BOOKS[3],
            Book::Deuteronomy => &BOOKS[4],
            Book::Joshua => &BOOKS[5],
            Book::Judges => &BOOKS[6],
            Book::Ruth => &BOOKS[7],
            Book::Samuel1 => &BOOKS[8],
            Book::Samuel2 => &BOOKS[9],
            Book::Kings1 => &BOOKS[10],
            Book::Kings2 => &BOOKS[11],
            Book::Chronicles1 => &BOOKS[12],
            Book::Chronicles2 => &BOOKS[13],
            Book::Ezra => &BOOKS[14],
            Book::Nehemiah => &BOOKS[15],
            Book::Esther => &BOOKS[16],
            Book::Job => &BOOKS[17],
            Book::Psalms => &BOOKS[18],
            Book::Proverbs => &BOOKS[19],
            Book::Ecclesiastes => &BOOKS[20],
            Book::SongOfSongs => &BOOKS[21],
            Book::Isaiah => &BOOKS[22],
            Book::Jeremiah => &BOOKS[23],
            Book::Lamentations => &BOOKS[24],
            Book::Ezekiel => &BOOKS[25],
            Book::Daniel => &BOOKS[26],
            Book::Hosea => &BOOKS[27],
            Book::Joel => &BOOKS[28],
            Book::Amos => &BOOKS[29],
            Book::Obadiah => &BOOKS[30],
            Book::Jonah => &BOOKS[31],
            Book::Micah => &BOOKS[32],
            Book::Nahum => &BOOKS[33],
            Book::Habakkuk => &BOOKS[34],
            Book::Zephaniah => &BOOKS[35],
            Book::Haggai => &BOOKS[36],
            Book::Zechariah => &BOOKS[37],
            Book::Malachi => &BOOKS[38],
            Book::Matthew => &BOOKS[39],
            Book::Mark => &BOOKS[40],
            Book::Luke => &BOOKS[41],
            Book::John => &BOOKS[42],
            Book::Acts => &BOOKS[43],
            Book::Romans => &BOOKS[44],
            Book::Corinthians1 => &BOOKS[45],
            Book::Corinthians2 => &BOOKS[46],
            Book::Galatians => &BOOKS[47],
            Book::Ephesians => &BOOKS[48],
            Book::Philippians => &BOOKS[49],
            Book::Colossians => &BOOKS[50],
            Book::Thessalonians1 => &BOOKS[51],
            Book::Thessalonians2 => &BOOKS[52],
            Book::Timothy1 => &BOOKS[53],
            Book::Timothy2 => &BOOKS[54],
            Book::Titus => &BOOKS[55],
            Book::Philemon => &BOOKS[56],
            Book::Hebrews => &BOOKS[57],
            Book::James => &BOOKS[58],
            Book::Peter1 => &BOOKS[59],
            Book::Peter2 => &BOOKS[60],
            Book::John1 => &BOOKS[61],
            Book::John2 => &BOOKS[62],
            Book::John3 => &BOOKS[63],
            Book::Jude => &BOOKS[64],
            Book::Revelation => &BOOKS[65],
            Book::Esdras1 => &BOOKS[66],
            Book::Tobit => &BOOKS[67],
            Book::WisdomOfSolomon => &BOOKS[68],
            Book::Ecclesiasticus => &BOOKS[69],
            Book::Maccabees1 => &BOOKS[70],
            Book::Maccabees2 => &BOOKS[71],
        }
    }
}

/// Map from canonical name lowercase -> index for quick lookup.
static BOOKS_BY_NAME: Lazy<HashMap<String, usize>> = Lazy::new(|| {
    let mut m = HashMap::new();
    for (i, b) in BOOKS.iter().enumerate() {
        m.insert(b.name.to_lowercase(), i);
    }
    m
});

/// Build a regex-ready string that matches any abbreviation for a book.
/// Escapes literal abbreviations; returns an uncompiled string like `(?:John|Jn)\b`.
pub fn build_book_abbreviations_regex(book: &BookItem) -> String {
    let escaped: Vec<String> = book
        .abbreviations
        .iter()
        .map(|a| escape(a))
        .collect();
    format!(r"(?<!\w)(?:{})\b", escaped.join("|"))
}

/// Build a combined regex string to match any abbreviation across all books.
pub fn build_all_books_abbreviations_regex() -> String {
    let parts: Vec<String> = BOOKS
        .iter()
        .flat_map(|b| b.abbreviations.iter().map(|a| escape(a)))
        .collect();
    format!(r"(?<!\w)(?:{})\b", parts.join("|"))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn abbreviations_regex_string() {
        let john = Book::John;
        let re_str = build_book_abbreviations_regex(john.item());
        assert!(re_str.contains("Jn") || re_str.contains("John"));
    }

    #[test]
    fn all_abbreviations_regex_string() {
        let s = build_all_books_abbreviations_regex();
        assert!(s.starts_with("(?<!\\w)"));
    }
}
