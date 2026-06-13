"""Inject monkey-patch alias annotations from a runtime __init__.py into a .pyi stub.

Handles the following assignment patterns found in QGIS's generated __init__.py:

    ClassName.attr = Name                   →  attr: type[Name]
    ClassName.attr = Outer.Inner            →  attr: type[Outer.Inner]
    ClassName.attr = Outer.Inner.Member     →  attr: Outer.Inner

Assignments whose LHS has three or more dotted parts (e.g.
``X.EnumClass.Member = ...``), whose attribute is a known metadata name
(``is_monkey_patched``, ``__doc__``, ``baseClass``), or whose RHS has four or
more parts (e.g. ``.value`` suffix) are silently skipped.

Classes not found as top-level definitions in the target stub are also skipped.
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


def parse_patches(
    init_path: pathlib.Path,
) -> dict[str, list[tuple[str, str]]]:
    """Parse monkey-patch assignments from a runtime module.

    Returns ``{ClassName: [(attr_name, annotation), ...]}`` in source order,
    deduplicating by attribute name (first occurrence wins).
    """
    patches: dict[str, list[tuple[str, str]]] = defaultdict(list)
    seen: dict[str, set[str]] = defaultdict(set)

    for line in init_path.read_text('utf-8').splitlines():
        m = _ASSIGN_RE.match(line.rstrip())
        if not m:
            continue
        class_name, attr, rhs = m.groups()

        if attr in _SKIP_ATTRS or attr.startswith('__'):
            continue

        parts = rhs.split('.')
        if len(parts) == 1:
            # e.g. _LinePlacementFlags  →  class alias
            annotation = f'typing.Type[{rhs}]'
        elif len(parts) == 2:
            # e.g. Qgis.GeometryType  →  class alias (whole enum)
            annotation = f'typing.Type[{rhs}]'
        elif len(parts) == 3:
            # e.g. Qgis.LayerType.Vector  →  enum member; type is Qgis.LayerType
            annotation = f'{parts[0]}.{parts[1]}'
        else:
            # 4+ parts (e.g. ending in .value) — skip
            continue

        if attr not in seen[class_name]:
            seen[class_name].add(attr)
            patches[class_name].append((attr, annotation))

    return dict(patches)


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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'init',
        type=pathlib.Path,
        help='Runtime module with monkey-patch assignments (e.g. qgis/core/__init__.py)',
    )
    parser.add_argument(
        'stub',
        type=pathlib.Path,
        help='.pyi stub file to inject annotations into (e.g. qgis/_core.pyi)',
    )
    args = parser.parse_args()

    patches = parse_patches(args.init)
    print(f'Parsed patches for {len(patches)} classes.')

    count = inject_into_stub(args.stub, patches)
    print(f'Injected annotations into {count} classes in {args.stub}.')


if __name__ == '__main__':
    main()
