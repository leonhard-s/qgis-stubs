"""Inject docstrings from the runtime QGIS modules into the .pyi stubs.

The SIP-generated stubs only contain signatures, while the documentation
lives in the compiled extension modules. This script imports those modules,
so it must be run with a Python interpreter that has the targeted QGIS
version installed.

Each stub ``_<name>.pyi`` is matched against the runtime module
``qgis._<name>``. Docstrings are injected for:

- classes, including nested classes and enums
- functions and methods; overloads are matched to their section of the
  runtime docstring by parameter names, and the signature lines SIP prepends
  to each section are dropped
- enum members with their own docstring (monkey-patched by QGIS's runtime
  __init__.py files)

Sphinx cross-references such as ``:py:class:`~QgsPointXY``` are reduced to
inline code, since most editors render them verbatim.

Existing docstrings are left untouched, so running the script twice is a
no-op. Dunder methods, signals and attributes are skipped as they carry no
useful runtime documentation.
"""

import argparse
import ast
import enum
import importlib
import pathlib
import re
import textwrap
import typing
from collections import Counter

# Public packages whose __init__.py monkey-patches docstrings onto the native
# modules. Imported before reading any docstring.
_PUBLIC_PACKAGES = ('qgis.core', 'qgis.gui', 'qgis.analysis', 'qgis.server', 'qgis._3d')

_ROLE_RE = re.compile(r':py:\w+:`~?([^`]+)`')

_GENERIC_DOC_PREFIXES = ('Initialize self.', 'An enumeration.')


class _Edit(typing.NamedTuple):
	"""Docstring lines to insert after `line` (1-based).

	If `body` is set, it is the byte range of a one-line body (``...``) on
	that line, which the docstring replaces.
	"""
	line: int
	lines: list[str]
	body: tuple[int, int] | None = None


def clean_doc(text: str) -> str:
	"""Dedent, strip and simplify Sphinx roles in a docstring."""
	text = textwrap.dedent(text).strip()
	return _ROLE_RE.sub(r'`\1`', text)


def is_useful(doc: object) -> typing.TypeGuard[str]:
	"""Whether a runtime docstring is worth injecting."""
	return (
		isinstance(doc, str)
		and bool(doc.strip())
		and not doc.startswith(_GENERIC_DOC_PREFIXES)
	)


def runtime_attr(obj: object, name: str) -> object | None:
	"""Return `obj.name`, or None if it is missing or raises."""
	try:
		return getattr(obj, name)
	except Exception:  # SIP descriptors raise for instance-only attributes
		return None


def param_names(func: ast.FunctionDef) -> tuple[str, ...]:
	"""Return the names of all parameters of `func`, in order."""
	args = func.args
	names = [a.arg for a in args.posonlyargs + args.args]
	if args.vararg:
		names.append(args.vararg.arg)
	names += [a.arg for a in args.kwonlyargs]
	if args.kwarg:
		names.append(args.kwarg.arg)
	return tuple(names)


def signature_params(signature: str) -> tuple[str, ...] | None:
	"""Return the parameter names of a SIP signature line, if it parses."""
	try:
		node = ast.parse(f'def {signature}: ...').body[0]
	except SyntaxError:
		return None
	assert isinstance(node, ast.FunctionDef)
	return param_names(node)


def split_overloads(name: str, doc: str) -> list[tuple[str | None, str]]:
	"""Split a SIP docstring into (signature, text) sections, one per overload."""
	signature_re = re.compile(rf'^{re.escape(name)}\(.*\)(?: -> .+)?$')
	sections: list[tuple[str | None, str]] = []
	signature: str | None = None
	body: list[str] = []
	for line in doc.splitlines():
		if signature_re.match(line):
			if signature is not None or any(l.strip() for l in body):
				sections.append((signature, '\n'.join(body)))
			signature, body = line, []
		else:
			body.append(line)
	sections.append((signature, '\n'.join(body)))
	return [(sig, clean_doc(text)) for sig, text in sections]


def match_overloads(
	defs: list[ast.FunctionDef],
	sections: list[tuple[str | None, str]],
) -> list[str]:
	"""Return the docstring text for each of the overloads in `defs`."""
	if len(sections) == 1:
		return [sections[0][1]] * len(defs)

	unused = [(signature_params(sig) if sig else None, text) for sig, text in sections]
	matched: list[str | None] = []
	for func in defs:
		params = param_names(func)
		index = next((i for i, (p, _) in enumerate(unused) if p == params), None)
		matched.append(unused.pop(index)[1] if index is not None else None)
	if all(m is not None for m in matched):
		return typing.cast(list[str], matched)

	if len(defs) == len(sections):
		return [text for _, text in sections]

	# Overloads that cannot be paired get every section, headed by its signature.
	combined = '\n\n'.join(f'{sig}\n{text}' if sig else text for sig, text in sections)
	return [m if m is not None else combined for m in matched]


def format_docstring(text: str, indent: str) -> list[str]:
	"""Render `text` as a docstring literal, one string per source line."""
	text = text.replace('\\', '\\\\').replace('"""', '\\"\\"\\"')
	if text.endswith('"'):
		text = text[:-1] + '\\"'
	lines = [line.rstrip() for line in text.splitlines()]
	if len(lines) == 1:
		return [f'{indent}"""{lines[0]}"""']
	return (
		[f'{indent}"""{lines[0]}']
		+ [f'{indent}{line}' if line else '' for line in lines[1:]]
		+ [f'{indent}"""']
	)


class _Injector:
	"""Collect docstring edits for one stub file."""

	def __init__(self, source_lines: list[str]) -> None:
		self.lines = source_lines
		self.edits: list[_Edit] = []
		self.counts: Counter[str] = Counter()

	def indent_of(self, line: int) -> str:
		text = self.lines[line - 1]
		return text[:len(text) - len(text.lstrip())]

	def add_body_docstring(
		self,
		node: ast.ClassDef | ast.FunctionDef,
		text: str,
		header_end: int,
	) -> None:
		"""Make `text` the first statement of `node`'s body."""
		first = node.body[0]
		line = self.lines[first.lineno - 1].encode('utf-8')
		if line[:first.col_offset].strip():
			# One-liner such as `def f(self) -> int: ...`
			assert first.end_col_offset is not None
			indent = self.indent_of(node.lineno) + '    '
			body = (first.col_offset, first.end_col_offset)
			self.edits.append(_Edit(first.lineno, format_docstring(text, indent), body))
		else:
			indent = self.indent_of(first.lineno)
			if not self.lines[header_end - 1].rstrip().endswith(':'):
				header_end = first.lineno - 1
			self.edits.append(_Edit(header_end, format_docstring(text, indent)))

	def visit_body(self, body: list[ast.stmt], runtime: object) -> None:
		overloads: dict[str, list[ast.FunctionDef]] = {}
		is_enum = isinstance(runtime, enum.EnumMeta)
		for index, node in enumerate(body):
			if isinstance(node, ast.ClassDef):
				self.visit_class(node, runtime)
			elif isinstance(node, ast.FunctionDef):
				overloads.setdefault(node.name, []).append(node)
			elif is_enum and isinstance(node, ast.Assign):
				self.visit_enum_member(node, body[index + 1:], runtime)
		for name, defs in overloads.items():
			self.visit_function(name, defs, runtime)

	def visit_class(self, node: ast.ClassDef, parent: object) -> None:
		runtime = runtime_attr(parent, node.name)
		if not isinstance(runtime, type):
			return
		doc = vars(runtime).get('__doc__')
		if is_useful(doc) and ast.get_docstring(node) is None:
			header_end = max(
				[node.lineno]
				+ [n.end_lineno or n.lineno for n in node.bases + node.keywords]
			)
			self.add_body_docstring(node, clean_doc(doc), header_end)
			self.counts['classes'] += 1
		self.visit_body(node.body, runtime)

	def visit_function(self, name: str, defs: list[ast.FunctionDef], parent: object) -> None:
		if name.startswith('__') and name.endswith('__'):
			return
		doc = runtime_attr(runtime_attr(parent, name), '__doc__')
		if not is_useful(doc):
			return
		texts = match_overloads(defs, split_overloads(name, doc))
		for func, text in zip(defs, texts):
			if text and ast.get_docstring(func) is None:
				header_end = (func.returns or func).end_lineno or func.lineno
				self.add_body_docstring(func, text, header_end)
				self.counts['functions'] += 1

	def visit_enum_member(
		self,
		node: ast.Assign,
		following: list[ast.stmt],
		enum_class: object,
	) -> None:
		if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
			return
		name = node.targets[0].id
		doc = runtime_attr(runtime_attr(enum_class, name), '__doc__')
		if not is_useful(doc) or doc.strip() in (name, getattr(enum_class, '__doc__', None)):
			return
		already_documented = (
			following
			and isinstance(following[0], ast.Expr)
			and isinstance(following[0].value, ast.Constant)
			and isinstance(following[0].value.value, str)
		)
		if already_documented:
			return
		assert node.end_lineno is not None
		lines = format_docstring(clean_doc(doc), self.indent_of(node.lineno))
		self.edits.append(_Edit(node.end_lineno, lines))
		self.counts['enum members'] += 1

	def apply(self) -> list[str]:
		"""Return the source lines with all edits applied."""
		lines = list(self.lines)
		for edit in sorted(self.edits, key=lambda e: e.line, reverse=True):
			if edit.body is not None:
				raw = lines[edit.line - 1].encode('utf-8')
				start, end = edit.body
				head = raw[:start].rstrip().decode('utf-8')
				tail = raw[end:].strip().decode('utf-8')
				lines[edit.line - 1] = f'{head}  {tail}' if tail else head
			lines[edit.line:edit.line] = edit.lines
		return lines


def inject_docstrings(stub_path: pathlib.Path) -> Counter[str] | None:
	"""Inject docstrings into `stub_path`; return counts, or None if skipped."""
	module_name = f'qgis.{stub_path.stem}'
	try:
		module = importlib.import_module(module_name)
	except ImportError as exc:
		print(f'Skipping {stub_path}: cannot import {module_name} ({exc}).')
		return None

	source = stub_path.read_text(encoding='utf-8')
	injector = _Injector(source.splitlines())
	injector.visit_body(ast.parse(source).body, module)
	if injector.edits:
		updated = '\n'.join(injector.apply()) + '\n'
		stub_path.write_text(updated, encoding='utf-8')
	return injector.counts


def iter_stubs(path: pathlib.Path) -> list[pathlib.Path]:
	"""Return `path` itself, or the native module stubs (`_*.pyi`) in it."""
	if path.is_dir():
		return sorted(path.glob('_*.pyi'))
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

	for package in _PUBLIC_PACKAGES:
		try:
			importlib.import_module(package)
		except ImportError as exc:
			print(f'Warning: cannot import {package} ({exc}).')

	total: Counter[str] = Counter()
	for stub in iter_stubs(args.path):
		counts = inject_docstrings(stub)
		if counts is None:
			continue
		summary = ', '.join(f'{n} {kind}' for kind, n in sorted(counts.items()))
		print(f'Injected docstrings in {stub}: {summary or "none"}.')
		total += counts
	print(f'Injected {sum(total.values())} docstrings total.')


if __name__ == '__main__':
	main()
