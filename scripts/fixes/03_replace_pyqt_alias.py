"""Replace uses of the qgis.PyQt re-export with explicit PyQt5/6 imports.

Type checkers do not evaluate the runtime aliasing of qgis.PyQt and therefore
will not resolve symbols coming from the corresponding PyQt5/6-stubs package.

This script removes the PyQt re-export from qgis and replaces all uses with
explicit references to PyQt5 or PyQt6 modules.

Note that QGIS 3 uses Qt5 while QGIS 4 uses Qt6. This script defaults to the
latter.
"""

import argparse
import pathlib
import re
import shutil

_QGIS_PYQT_IMPORT_RE = re.compile(
	r'^([ \t]*from )qgis\.PyQt((?:\.\w+)*)([ \t]+import\b)',
	re.MULTILINE,
)


def replace_pyqt_alias(stub_path: pathlib.Path, qt_version: int) -> int:
	"""Replace qgis.PyQt imports with explicit PyQt5/6 ones; return count."""
	source = stub_path.read_text(encoding='utf-8')
	updated, count = _QGIS_PYQT_IMPORT_RE.subn(
		rf'\1PyQt{qt_version}\2\3', source
	)
	if count:
		stub_path.write_text(updated, encoding='utf-8')
	return count


def iter_stubs(path: pathlib.Path) -> list[pathlib.Path]:
	"""Return `path` itself, or all `.py`/`.pyi` files under it if it's a directory."""
	if path.is_dir():
		return sorted(
			p for pattern in ('*.py', '*.pyi') for p in path.rglob(pattern)
		)
	return [path]


def remove_pyqt_package(path: pathlib.Path) -> bool:
	"""Delete the vendored qgis.PyQt package under `path`, if present."""
	pyqt_dir = path / 'PyQt' if path.is_dir() else path.parent / 'PyQt'
	if pyqt_dir.is_dir():
		shutil.rmtree(pyqt_dir)
		return True
	return False


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument(
		'path',
		type=pathlib.Path,
		nargs='?',
		default=pathlib.Path('qgis-stubs'),
		help='Stub file or directory to fix (default: qgis-stubs)',
	)
	parser.add_argument(
		'--qt-version',
		type=int,
		choices=(5, 6),
		default=6,
		help='PyQt major version to import instead of qgis.PyQt (default: 6)',
	)
	args = parser.parse_args()

	total = 0
	for stub in iter_stubs(args.path):
		count = replace_pyqt_alias(stub, args.qt_version)
		if count:
			print(f'Replaced {count} qgis.PyQt imports in {stub}.')
		total += count
	print(f'Replaced {total} qgis.PyQt imports total.')

	if remove_pyqt_package(args.path):
		print(f'Removed vendored PyQt package under {args.path}.')


if __name__ == '__main__':
	main()


