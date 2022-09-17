# Type Stubs for QGIS

Python stubs for the [PyQGIS](https://qgis.org/pyqgis/master/) module used in [QGIS](https://qgis.org/). Compatible with and tested on [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)/[pyright](https://github.com/Microsoft/pyright) and [MyPy](http://mypy-lang.org/).

## Overview

The bulk of the `qgis` module is a [SIP](https://www.riverbankcomputing.com/software/sip/)-generated wrapper over a C++ source that is only available at runtime. This means that developers are "flying blind" when writing code that uses the `qgis` module.

Type stubs are a declaration-only replication of the module interface that can be parsed by IDEs, linters, or static type checkers like [Mypy](http://mypy-lang.org/) or [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) to provide the same functionality available for regular Python sources.

## Installation

The qgis-stubs package can be installed through pip:

```sh
python -m pip install qgis-stubs
```

Alternatively, you may clone and install the latest version using the repository link:

```sh
python -m pip install git+https://github.com/leonhard-s/qgis-stubs.git
```

## Caveats & Limitations

The Python modules used by QGIS are not without issues. Most of these are shared by the runtime implementation but are explicitly listed here to avoid confusion.

- The `qgis.3d` namespace is not valid Python syntax as it starts with a number. At runtime, this module is instead available under the `qgis._3d` name, and the stub files replicate this behaviour.

  This may lead to errors/warnings due to apparent protected access of client code, which must be silenced using `# type: ignore` and/or `# pylint: disable=protected-access` comments.

- Some classes use `None` as the name of a member, leading to invalid Python syntax such as `DataResamplingMethod.None`.

  Use of the built-in `getattr()` function together with custom type annotations can be used to work around this issue:

  ```py
  None_: DataResamplingMethod = getattr(DataResamplingMethod, 'None')
  ```

- Compatibility fallback names for unscoped enumerators are not available as they are "monkey-patched" at runtime.

  It was decided not to include these patches in the stubs as they lead to naming collisions and are almost all flagged as deprecated for QGIS 4.

## Contributing

This repository contains an automated type stub generator, but new releases still require some manual edits depending on the version of QGIS targeted. Support for new QGIS versions is therefore not automatic.

If you encounter any issues such as missing or incorrect type hints or wish for this utility to be updated for a new version of QGIS, please do [create an issue](https://github.com/leonhard-s/qgis-stubs/issues).
