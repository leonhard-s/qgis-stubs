# Type Stubs for QGIS

This package defines Python stub files (.pyi) for the PyQGIS wrapper module available in [QGIS](https://qgis.org/).

## Overview

The bulk of the `qgis` module is a [SIP](https://www.riverbankcomputing.com/software/sip/)-generated wrapper over a C++ source, which cannot be introspected by the user or development utilities.

Python type stubs are a declaration-only replication of the C/C++ endpoints that can be parsed by IDEs, linters, or static type checkers to provide the same functionality available for regular Python sources.

While type stubs are primarily intended for use with static type checkers like [Mypy](http://mypy-lang.org/) or [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), they are also used by some linters like [pylint](https://pylint.org/) and will silence error messages like `import-error` or `no-name-in-module`.

## Installation

qgis-stubs can be installed through pip:

```sh
$ python -m pip install qgis-stubs
```

Alternatively, you can clone and install them straight from this repository:

```sh
$ python -m pip install git+https://github.com/leonhard-s/qgis-stubs.git
```

## Limitations

This project is in early stages and does not yet cover the full interface. This is largely due to QGIS doing a lot of monkey-patching that is not yet automatically replicated in the stub files.

Here is a likely incomplete list of known limitations/omissions:

- Compatibility fallbacks and non-standard attributes may be missing (as they are monkey patched).
- Most methods do not contain docstrings (these too are monkey-patched).
- None of the types and utilities defined in the `core.additions` namespace are available as they mostly serve to allow for more monkey-patching.
- QGIS enumerators clutter the parent namespace, which can lead to name collisions.

  For example: The value `QgsAggregateMappingModel.ColumnDataIndex.Aggregate` instead escalates to `QgsAggregateMappingModel.Aggregate`, which is subsequently overwritten by an inner class of the same qualified name.

  Such names are inaccessible in the stubs and possibly even at runtime. I did not yet have time to investigate further.

## Contributing

If you encounter any issues such as missing or incorrect hints or other unexpected behaviour, please do not hesitate to [create an issue](https://github.com/leonhard-s/qgis-stubs/issues) or start hacking away.

The current version of this package was created with copious amounts of RegEx-based edits and refactoring tools, though I did end up manually merging files and adding missing types a lot.

If this utility is useful to you, please let me know and I will happily look into automating the entire workflow to keep this package synchronised with QGIS releases.
