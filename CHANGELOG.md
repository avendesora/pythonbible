# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.15.0] - 2025-11-11

### Added

- Added several new English version/translation Bibles:
  - American King James Version (AKJV)
  - Bible in Basic English (BBE)
  - Bible in Worldwide English NT (BWE)
  - Darby (DAR)
  - Diaglot NT - 1865 (DIAGLOT)
  - Douay-Rheims (DR)
  - The Emphasized Bible by J. B. Rotherham (ROTHERHAM)
  - Geneva Bible (GB)
  - Leeser Old Testament (LEESER)
  - Living Oracles NT (LONT)
  - Modern KJV 1963 (MKJV1963)
  - Montgomery New Testament (MONT)
  - New Heart English Bible (NHEB)
  - Open English Bible (OEB)
  - The Peschito Syriac New Testament (ETHERIDGE)
  - Revised 1833 Webster Version (RWEBSTER)
  - Revised Young's Literal Translation NT (RYLT)
  - Updated King James Version (UKJV)
  - Webster (WBS)
  - Wesley's New Testament (WESLEY)
  - Weymouth NT (WMTH)
  - Willam Tyndale Bible (TYN)
  - World English Bible (WEB)
  - Wycliffe Bible (WYC)
  - Young's Literal Translation of the Bible (YLT)
- Added functionality to the Bible class to be able to get the books, chapter numbers, and verse numbers for the given version/translation.

### Changed

- **BREAKING CHANGE**: Modified the NormalizedReference class to allow start chapter, start verse, end chapter, and end verse to be None.
  - The parser has also been updated to set those values to None unless they are explicitly set in the reference string. As we added more version/translation Bible texts, we realized the differences in chapter and verse numbers between versions/translations was much greater than initially assumed. This change allows for more flexibility in handling those differences.
  - The formatter has also been updated to get the appropriate start chapter, start verse, end chapter, and end verse at format time rather than parse time.

## [0.14.0] - 2025-11-09

### Added

- Added Python 3.14 to the list of supported Python versions.

### Changed

- Modified the header image url to be an absolute url so that it hopefully shows up in PyPI correctly.
- Switched package build and publish tool from flit to uv.
- Updated GitHub Actions workflow to use uv for building and publishing to PyPI.

### Removed

- Removed Python 3.8 from the list of supported Python versions.
- Removed Python 3.9 from the list of supported Python versions.

## [0.13.1] - 2024-05-21

### Changed

- Modified max verses dictionary with chapter/verse info from multiple versions/translations.

## [0.13.0] - 2024-05-21

### Added

- Official support for Python 3.12
- Additional English Versions

### Changed

- Modified some Version names and values to match their OSIS values

## [0.12.0] - 2023-10-03

### Added

- Official support for Python 3.12

## [0.11.1] - 2023-10-02

The goal of this release was to address [Issue #118] (When trying to get the scripture text for a verse that is in a book that is not included in the given version, the entire scripture text for that version was returned.)

### Added

- VersionMissingVerseError exception

### Fixed

- Raise an error when trying to get scripture text for a verse that is in a book that is not included in the given version.

## [0.11.0] - 2023-06-27

### Changed

- Updated README to more accurately describe current OSIS parser and Bible text formatting functionality
- Minor code quality improvements based on static code analysis

### Removed

- Python 3.7 support (due to official end of life on June 27, 2021)

## [0.10.0] - 2023-05-27

The goal of this release was to address [Issue #90], and to make things related to Books, BookGroups, and Versions structured in a more object-oriented way.

### Added

- started this Changelog
- new abbreviations list property of Book Enum
- Jupyter notebook for Basic Usage documentation
- Jupyter notebook for Advanced Usage, Single Chapter Books documentation
- Jupyter notebook for Advanced Usage, Multi Book References documentation
- Jupyter notebook for Advanced Usage, Book Groups documentation

### Changed

- moved book specific regular expressions to new regular_expression property of Book
- moved book default titles to be encapsulated within the Book Enum and updated the title property to use them
- moved book group regular expressions to be encapsulated within the BookGroup Enum and updated the regular_expression property to use them
- moved book group books tuple to be encapsulated within the BookGroup Enum and updated the books property to use them
- moved version titles to be encapsulated within the Version Enum and updated the title property to use them
- updated Technical Reference documentation to use autodocs (generate documentation from docstrings)

### Fixed

- changed the default Version to AMERICAN_STANDARD in order to match the existing documentation
- updated Advanced Usage documentation to reference the format_scripture_references function rather than the format_references function (which doesn't exist)
- fixed a typo on the documentation index page

## [0.9.1] - 2023-05-09

## [0.9.0] - 2023-05-09

## [0.8.0] - 2023-04-27

## [0.7.4] - 2022-07-15

## [0.7.3] - 2022-07-14

## [0.7.2] - 2022-06-27

## [0.7.1] - 2022-06-23

## [0.7.0] - 2022-04-29

## [0.6.1] - 2021-09-28

## [0.6.0] - 2021-09-28

## [0.5.0] - 2021-06-09

## [0.4.1] - 2021-05-04

## [0.4.0] - 2021-05-03

## [0.3.1] - 2021-02-25

## [0.3.0] - 2021-02-10

## [0.2.2] - 2020-11-30

## [0.2.1] - 2020-11-20

## [0.2.0] - 2010-11-18

## [0.1.5] - 2020-11-02

## [0.1.4] - 2020-10-29

## [0.1.3] - 2020-10-27

## [0.1.2] - 2020-10-27

## [0.1.1] - 2020-10-20

## [0.1.0] - 2020-10-19

## [0.0.4] - 2020-10-15

## [0.0.3] - 2020-10-10

## [0.0.2] - 2020-10-08

## [0.0.1] - 2020-10-08

[unreleased]: https://github.com/avendesora/pythonbible/compare/v0.15.0...HEAD
[0.15.0]: https://github.com/avendesora/pythonbible/compare/v0.14.0...v0.15.0
[0.14.0]: https://github.com/avendesora/pythonbible/compare/v0.13.1...v0.14.0
[0.13.1]: https://github.com/avendesora/pythonbible/compare/v0.13.0...v0.13.1
[0.13.0]: https://github.com/avendesora/pythonbible/compare/v0.12.0...v0.13.0
[0.12.0]: https://github.com/avendesora/pythonbible/compare/v0.11.1...v0.12.0
[0.11.1]: https://github.com/avendesora/pythonbible/compare/v0.11.0...v0.11.1
[0.11.0]: https://github.com/avendesora/pythonbible/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/avendesora/pythonbible/compare/v0.9.1...v0.10.0
[0.9.1]: https://github.com/avendesora/pythonbible/compare/v0.9.0...v0.9.1
[0.9.0]: https://github.com/avendesora/pythonbible
[0.8.0]: https://github.com/avendesora/pythonbible
[0.7.4]: https://github.com/avendesora/pythonbible
[0.7.3]: https://github.com/avendesora/pythonbible
[0.7.2]: https://github.com/avendesora/pythonbible
[0.7.1]: https://github.com/avendesora/pythonbible
[0.7.0]: https://github.com/avendesora/pythonbible
[0.6.1]: https://github.com/avendesora/pythonbible
[0.6.0]: https://github.com/avendesora/pythonbible
[0.5.0]: https://github.com/avendesora/pythonbible
[0.4.1]: https://github.com/avendesora/pythonbible
[0.4.0]: https://github.com/avendesora/pythonbible
[0.3.1]: https://github.com/avendesora/pythonbible
[0.3.0]: https://github.com/avendesora/pythonbible
[0.2.2]: https://github.com/avendesora/pythonbible
[0.2.1]: https://github.com/avendesora/pythonbible
[0.2.0]: https://github.com/avendesora/pythonbible
[0.1.5]: https://github.com/avendesora/pythonbible
[0.1.4]: https://github.com/avendesora/pythonbible
[0.1.3]: https://github.com/avendesora/pythonbible
[0.1.2]: https://github.com/avendesora/pythonbible
[0.1.1]: https://github.com/avendesora/pythonbible
[0.1.0]: https://github.com/avendesora/pythonbible
[0.0.4]: https://github.com/avendesora/pythonbible
[0.0.3]: https://github.com/avendesora/pythonbible
[0.0.2]: https://github.com/avendesora/pythonbible
[0.0.1]: https://github.com/avendesora/pythonbible

[issue #90]: https://github.com/avendesora/pythonbible/issues/90
[issue #118]: https://github.com/avendesora/pythonbible/issues/118
