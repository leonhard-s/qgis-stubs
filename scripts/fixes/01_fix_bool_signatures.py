"""Replace __bool__ methods erroneously annotated with int return type."""

import argparse
import pathlib
import re

_BOOL_INT_RE = re.compile(
	r'^([ \t]*def __bool__\([^)]*\)[ \t]*->[ \t]*)int\b',
	re.MULTILINE,
)


def fix_bool_signatures(stub_path: pathlib.Path) -> int:
	"""Replace int with bool on __bool__ signatures; return replacements made."""
	source = stub_path.read_text(encoding='utf-8')
	updated, count = _BOOL_INT_RE.subn(r'\1bool', source)
	if count:
		stub_path.write_text(updated, encoding='utf-8')
	return count


def iter_stubs(path: pathlib.Path) -> list[pathlib.Path]:
	"""Return `path` itself, or all `.pyi` files under it if it's a directory."""
	if path.is_dir():
		return sorted(path.rglob('*.pyi'))
	return [path]


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument(
		'path',
		type=pathlib.Path,
		nargs='?',
		default=pathlib.Path('qgis-stubs'),
		help='Stub file or directory to fix (default: qgis-stubs)',
	)
	args = parser.parse_args()

	total = 0
	for stub in iter_stubs(args.path):
		count = fix_bool_signatures(stub)
		if count:
			print(f'Fixed {count} __bool__ signatures in {stub}.')
		total += count
	print(f'Fixed {total} __bool__ signatures total.')


if __name__ == '__main__':
	main()
