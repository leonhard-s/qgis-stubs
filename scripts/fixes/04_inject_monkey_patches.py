"""Inject monkey-patch alias annotations from a runtime __init__.py into a .pyi stub.

Handles the following assignment patterns found in QGIS's generated __init__.py:

    ClassName.attr = Name                   →  attr: type[Name]
    ClassName.attr = Outer.Inner            →  attr: type[Outer.Inner]
    ClassName.attr = Outer.Inner            →  attr: Outer      (if attr == 'Inner')
    ClassName.attr = Outer.Inner.Member     →  attr: Outer.Inner

A two-part RHS whose last component matches the assigned attribute name is
ambiguous (it could be a nested-class alias re-exported under its own name,
or an enum member re-exported under its own name). This is disambiguated by
checking whether the same RHS also occurs as a dotted prefix of some other
patch in the same file (e.g. ``Outer.Inner.Member``); if so, the two-part
form is itself a class alias, otherwise it is treated as an enum member.

Local import aliases of the form ``from qgis.core import Qgis as _Qgis`` are
resolved back to their fully-qualified ``_core.Qgis`` form, since the
local alias name is not available in the target stub.

Assignments whose LHS has three or more dotted parts (e.g.
``X.EnumClass.Member = ...``), whose attribute is a known metadata name
(``is_monkey_patched``, ``__doc__``, ``baseClass``), or whose RHS has four or
more parts (e.g. ``.value`` suffix) are silently skipped.

Classes not found as top-level definitions in the target stub are also skipped.

Any assignment line captured into a patch, as well as ``.is_monkey_patched =
True`` assignment lines, are stripped from the runtime __init__.py, since
they are now redundant (or, in the case of ``is_monkey_patched``, actively
trip up type checkers by assigning attributes to frozen enum members).
"""

import argparse
import ast
import pathlib
import re
from collections import defaultdict

# Matches exactly two-part LHS:  ClassName.attr = rhs
_ASSIGN_RE = re.compile(
    r'^([A-Za-z]\w+)\.([A-Za-z_]\w*)\s*=\s*([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)$'
)
_SKIP_ATTRS = frozenset({'is_monkey_patched', '__doc__', 'baseClass'})

# Identifies the native extension module (and thus its .pyi stub) an
# __init__.py wraps, e.g. "from qgis._core import *" -> "_core".
_NATIVE_IMPORT_RE = re.compile(r'^from qgis\.(_\w+) import \*', re.MULTILINE)

_IS_MONKEY_PATCHED_RE = re.compile(
    r'^[ \t]*[\w.]+\.is_monkey_patched[ \t]*=[ \t]*True[ \t]*$'
)

# Local aliases of qgis.core symbols, e.g. "from qgis.core import Qgis as _Qgis".
_ALIAS_IMPORT_RE = re.compile(r'^from qgis\.core import (\w+) as (\w+)$')


def parse_aliases(init_path: pathlib.Path) -> dict[str, str]:
    """Map local import aliases (e.g. "_Qgis") to their real name ("Qgis")."""
    aliases: dict[str, str] = {}
    for line in init_path.read_text('utf-8').splitlines():
        m = _ALIAS_IMPORT_RE.match(line.rstrip())
        if m:
            name, alias = m.groups()
            aliases[alias] = name
    return aliases


def resolve_rhs(rhs: str, aliases: dict[str, str]) -> str:
    """Replace a leading local import alias with its qualified _core.Name form."""
    head, sep, rest = rhs.partition('.')
    if head in aliases:
        return f'_core.{aliases[head]}{sep}{rest}'
    return rhs


def parse_patches(
    init_path: pathlib.Path,
) -> tuple[dict[str, list[tuple[str, str]]], set[str]]:
    """Parse monkey-patch assignments from a runtime module.

    Returns a tuple of:
      - ``{ClassName: [(attr_name, annotation), ...]}`` in source order,
        deduplicating by attribute name (first occurrence wins).
      - the set of raw source lines (rstripped) that were captured into a
        patch and can therefore be stripped from the runtime module.
    """
    aliases = parse_aliases(init_path)
    lines = init_path.read_text('utf-8').splitlines()

    # First pass: collect every candidate RHS, used to disambiguate two-part
    # aliases below (see module docstring).
    all_rhs: set[str] = set()
    for line in lines:
        m = _ASSIGN_RE.match(line.rstrip())
        if m:
            all_rhs.add(m.group(3))

    patches: dict[str, list[tuple[str, str]]] = defaultdict(list)
    seen: dict[str, set[str]] = defaultdict(set)
    consumed_lines: set[str] = set()

    for line in lines:
        stripped = line.rstrip()
        m = _ASSIGN_RE.match(stripped)
        if not m:
            continue
        class_name, attr, rhs = m.groups()

        if attr in _SKIP_ATTRS or attr.startswith('__'):
            continue

        parts = rhs.split('.')
        if len(parts) >= 4:
            # e.g. ending in .value — skip
            continue
        elif len(parts) == 3:
            # e.g. Qgis.LayerType.Vector  →  enum member; type is Qgis.LayerType
            annotation = resolve_rhs('.'.join(parts[:-1]), aliases)
        elif len(parts) == 2 and parts[-1] == attr:
            if any(other.startswith(rhs + '.') for other in all_rhs):
                # e.g. AltitudeClamping = Qgis.AltitudeClamping, with further
                # Qgis.AltitudeClamping.Member patches elsewhere  →  class alias
                annotation = f'typing.Type[{resolve_rhs(rhs, aliases)}]'
            else:
                # e.g. Triangles = SomeEnum.Triangles  →  enum member re-exported
                # under its own name; type is the owner
                annotation = resolve_rhs(parts[0], aliases)
        else:
            # e.g. Shape = Qgis.Point3DShape, or RenderingTechnique = SomeEnum
            annotation = f'typing.Type[{resolve_rhs(rhs, aliases)}]'

        consumed_lines.add(stripped)
        if attr not in seen[class_name]:
            seen[class_name].add(attr)
            patches[class_name].append((attr, annotation))

    return dict(patches), consumed_lines


def inject_into_stub(
    stub_path: pathlib.Path,
    patches: dict[str, list[tuple[str, str]]],
) -> int:
    """Append patch annotations to the end of matching class bodies in a stub.

    Processes classes in reverse line order so earlier insertions do not
    shift the indices of classes yet to be processed.

    Returns the number of classes modified.
    """
    source = stub_path.read_text('utf-8')
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)

    targets: list[tuple[int, str]] = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name in patches:
            targets.append((node.end_lineno, node.name))  # type: ignore

    # Descending order keeps already-computed end_lineno values valid.
    targets.sort(reverse=True)

    for end_lineno, class_name in targets:
        new_lines = [
            f'    {attr}: {annotation}\n'
            for attr, annotation in patches[class_name]
        ]
        # end_lineno is 1-based; inserting at that 0-based index places the
        # new lines immediately after the last line of the class body.
        lines[end_lineno:end_lineno] = new_lines

    stub_path.write_text(''.join(lines), encoding='utf-8')
    return len(targets)


def strip_patch_lines(init_path: pathlib.Path, consumed_lines: set[str]) -> int:
    """Remove captured setter lines and is_monkey_patched lines; return count."""
    lines = init_path.read_text('utf-8').splitlines(keepends=True)
    kept = [
        line
        for line in lines
        if line.rstrip() not in consumed_lines
        and not _IS_MONKEY_PATCHED_RE.match(line.rstrip())
    ]
    removed = len(lines) - len(kept)
    if removed:
        init_path.write_text(''.join(kept), encoding='utf-8')
    return removed


def iter_init_stub_pairs(
    root: pathlib.Path,
) -> list[tuple[pathlib.Path, pathlib.Path]]:
    """Find (__init__.py, .pyi) pairs by following the native module import."""
    pairs: list[tuple[pathlib.Path, pathlib.Path]] = []
    for init_path in sorted(root.rglob('__init__.py')):
        match = _NATIVE_IMPORT_RE.search(init_path.read_text('utf-8'))
        if match is None:
            continue
        stub_path = root / f'{match.group(1)}.pyi'
        if stub_path.is_file():
            pairs.append((init_path, stub_path))
    return pairs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'path',
        type=pathlib.Path,
        nargs='?',
        default=pathlib.Path('qgis-stubs'),
        help='Package root to scan for __init__.py/.pyi pairs (default: qgis-stubs)',
    )
    args = parser.parse_args()

    total = 0
    total_removed = 0
    for init_path, stub_path in iter_init_stub_pairs(args.path):
        patches, consumed_lines = parse_patches(init_path)
        count = inject_into_stub(stub_path, patches)
        if count:
            print(f'Injected annotations into {count} classes in {stub_path}.')
        total += count

        removed = strip_patch_lines(init_path, consumed_lines)
        if removed:
            print(f'Removed {removed} redundant assignments from {init_path}.')
        total_removed += removed
    print(f'Injected annotations into {total} classes total.')
    print(f'Removed {total_removed} redundant assignments total.')


if __name__ == '__main__':
    main()
