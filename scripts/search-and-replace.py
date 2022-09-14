"""Perform lazy search-and-replace on file or directory contents.

The files are first renamed to have a .bak extension, then the
replacements are made into new files with the original names. If
successful, the .bak files are then deleted.

Only single-line, non-RegEx replacements are supported.
"""

import argparse
import pathlib


def replace_to_file(in_: pathlib.Path, out: pathlib.Path,
                    old: str, new: str) -> None:
    """Replace all occurrences of `old` with `new`.

    The `in_` file is not altered but copied into `out` with the given
    changes.

    Args:
        in_: The file to read from.
        out: The file to write to.
        old: The string to replace.
        new: The string to replace with.

    """
    with in_.open('r', encoding='utf-8') as f_in:
        with out.open('w', encoding='utf-8') as f_out:
            for line in f_in:
                f_out.write(line.replace(old, new))


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


def search_and_replace(path: pathlib.Path, old: str, new: str) -> None:
    """Search and replace the given file.

    Args:
        path: The file to search and replace.
        old: The string to replace.
        new: The string to replace with.

    """
    backup = backup_file(path)
    replace_to_file(backup, path, old, new)
    backup.unlink()


def _search_and_replace_dir(dir_: pathlib.Path, old: str, new: str) -> None:
    """Search and replace the given directory.

    Args:
        dir_: The directory to search and replace.
        old: The string to replace.
        new: The string to replace with.

    """
    if not dir_.is_dir():
        raise ValueError(f"{dir_} is not a directory")
    for path in dir_.iterdir():
        if path.is_dir():
            _search_and_replace_dir(path, old, new)
        else:
            search_and_replace(path, old, new)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="File or directory to search")
    parser.add_argument("old", help="String to replace")
    parser.add_argument("new", help="String to replace with")
    args = parser.parse_args()

    path = pathlib.Path(args.path)
    if path.is_dir():
        _search_and_replace_dir(path, args.old, args.new)
    elif path.exists():
        search_and_replace(path, args.old, args.new)
    else:
        raise ValueError(f"{path} does not exist")
