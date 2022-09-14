"""Convert all invalid sip-style enums to standard Python class hints.

sip generates enum type hints like this:

    class MyEnum(int): ...
    MyEnum.Field1 = ...  # type: MyEnum
    MyEnum.Field2 = ...  # type: MyEnum

Unforunately, this is not how classes are typed as the annotated
members are being defined outside their class body. This script
therefore converts them to the following, standard syntax:

    class MyEnum(int):
        Field1: MyEnum
        Field2: MyEnum

"""

import argparse
import pathlib
import re

_CLS_PATTERN = re.compile(r'^( *)class (\w+(?:\(int\))?): \.\.\. *\n')
_FIELD_PATTERN = re.compile(r'^( *)(\w+) = \.\.\. +# type: +(\'?[\w\.]+\'?) *\n')


def convert_enum_to_file(in_: pathlib.Path, out: pathlib.Path) -> None:
    """Replace any sip-style enums to sensible Python type hints.

    sip generates enum type hints like this:

        class MyEnum(int): ...
        MyEnum.Field1 = ...  # type: MyEnum
        MyEnum.Field2 = ...  # type: MyEnum

    This function converts these to the following:

        class MyEnum(int):
            Field1: MyEnum
            Field2: MyEnum

    Args:
        in_: The file to read from.
        out: The file to write to.

    """
    with in_.open('r', encoding='utf-8') as f_in:
        with out.open('w', encoding='utf-8') as f_out:
            iterator = iter(f_in)
            for line in iterator:

                # Check if the line is an enum-like class definition
                match = _CLS_PATTERN.match(line)
                if match is not None:
                    indent, enum_name = match.groups()

                    # Write class definition
                    f_out.writelines([indent, 'class ', enum_name, ':\n'])
                    # Keep consuming lines until one does not match
                    line = next(iterator)
                    match = _FIELD_PATTERN.match(line)
                    while match is not None:
                        indent, field_name, qualified_type = match.groups()
                        f_out.writelines(
                            [indent, '    ', field_name, ': \'',
                            qualified_type.replace('\'', ''), '\'\n'])
                        # Consume next line
                        line = next(iterator)
                        match = _FIELD_PATTERN.match(line)

                    # Write last non-matching line unchanged
                    f_out.write(line)

                # Line not an enum class definition, copy it unchanged
                else:
                    f_out.write(line)


def backup_file(path: pathlib.Path) -> pathlib.Path:
    """Rename the given file to ``<file>.bak`` and return that path.

    Args:
        path: The file to rename.

    Returns:
        The new path of the file.

    """
    new_path = path.with_suffix(path.suffix + ".bak")
    path.rename(new_path)
    return new_path


def convert_enum(path: pathlib.Path) -> None:
    """Convert the given file to use sensible Python type hints.

    Args:
        path: The file to convert.

    """
    backup = backup_file(path)
    convert_enum_to_file(backup, path)
    backup.unlink()


def _convert_enum_dir(dir_: pathlib.Path) -> None:
    """Recursive scanner for directory-wide enum conversions.

    Args:
        dir_: The directory to scan.

    """
    if not dir_.is_dir():
        raise ValueError(f"{dir_} is not a directory")
    for path in dir_.iterdir():
        if path.is_dir():
            _convert_enum_dir(path)
        elif path.suffix in ('.py', '.pyi'):
            convert_enum(path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="File or directory to search")
    args = parser.parse_args()

    path = pathlib.Path(args.path)
    if path.is_dir():
        _convert_enum_dir(path)
    else:
        convert_enum(path)
