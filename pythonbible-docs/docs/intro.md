---
sidebar_position: 1
---

# Getting Started

pythonbible is a Python library serving several purposes related to Biblical Scripture references:

 * finding all Scripture references contained within text
 * converting Scripture references to a list of unique verse ids, and vice versa
 * retrieving Scripture text by reference or verse ids
 * formatting Scripture references for display/print
 * formatting Scripture text for display/print

## Requirements

The only required dependency for the pythonbible library is [Python](https://www.python.org/downloads/) 3.6+.

However, if using Python 3.6, you must have the [dataclasses](https://github.com/ericvsmith/dataclasses) library installed.

```shell script
pip install dataclasses
```

If using Python 3.7+, the standard library includes dataclasses, and it does not need to be installed separately.

## Installation

```shell script
pip install pythonbible
```

## Optional Dependencies

If the [defusedxml](https://github.com/tiran/defusedxml) library is installed, pythonbible will use it to parse XML files rather than the builtin xml.etree library.

To install pythonbible with all optional dependencies, use the following command.

```shell script
pip install pythonbible[all]
```