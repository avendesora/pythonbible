use once_cell::sync::Lazy;
use regex::Regex;

/// Convert all Roman numerals (1-150 range using C, XC, L, XL, X, IX, V, IV, I)
/// found as whole-word tokens in `text` into their integer representations.
///
/// Examples:
/// - "Chapter IV" -> "Chapter 4"
/// - "i, ii, III" -> "i, ii, 3" (only uppercase/lowercase roman-letter words are matched)
pub fn convert_all_roman_numerals_to_integers(text: &str) -> String {
    static ROMAN_WORD_REGEX: Lazy<Regex> =
        Lazy::new(|| Regex::new(r"(?i)\b[CLXVI]+\b").expect("invalid regex"));

    ROMAN_WORD_REGEX
        .replace_all(text, |caps: &regex::Captures| {
            let orig = caps.get(0).map(|m| m.as_str()).unwrap_or("");
            match convert_roman_numeral_to_integer(orig) {
                Some(n) => n.to_string(),
                None => orig.to_string(),
            }
        })
        .into_owned()
}

/// Convert a single roman numeral string to an integer (1..=150).
/// Returns `None` if the string is not a valid roman numeral in our supported range.
fn convert_roman_numeral_to_integer(roman: &str) -> Option<u32> {
    // Define numerals from big to small for greedy matching.
    static ROMAN_MAP: &[(&str, u32)] = &[
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    ];

    let s = roman.to_uppercase();
    let bytes = s.as_bytes();
    let mut pos = 0usize;
    let len = bytes.len();
    let mut value: u32 = 0;

    while pos < len {
        let mut matched = false;
        for &(sym, val) in ROMAN_MAP {
            let sym_bytes = sym.as_bytes();
            let end = pos + sym_bytes.len();
            if end <= len && &bytes[pos..end] == sym_bytes {
                value += val;
                pos = end;
                matched = true;
                break;
            }
        }
        if !matched {
            // couldn't match any symbol at current position -> invalid numeral
            return None;
        }
    }

    // Optionally enforce an upper bound (here 150) if needed.
    if value == 0 || value > 150 {
        return None;
    }

    // Verify canonical form: re-encode value and ensure it matches the input.
    let mut rem = value;
    let mut encoded = String::new();
    for &(sym, val) in ROMAN_MAP {
        while rem >= val {
            encoded.push_str(sym);
            rem -= val;
        }
    }

    if encoded == s {
        Some(value)
    } else {
        None
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn single_conversion() {
        assert_eq!(convert_roman_numeral_to_integer("IV"), Some(4));
        assert_eq!(convert_roman_numeral_to_integer("xc"), Some(90));
        assert_eq!(convert_roman_numeral_to_integer("C"), Some(100));
        assert_eq!(convert_roman_numeral_to_integer("IC"), None); // invalid
    }

    #[test]
    fn replace_in_text() {
        let s = "Chapter IV — Sections I to X.";
        let got = convert_all_roman_numerals_to_integers(s);
        assert_eq!(got, "Chapter 4 — Sections 1 to 10.");
    }
}
