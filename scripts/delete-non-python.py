"""Deletes any non-Python files in the given directory."""

import argparse
import pathlib


def filter_recursive(dir_: pathlib.Path, *extensions: str) -> None:
    """Delete any files in `path` that do not match the extensions.

    This recursively searches any subdirectories as well.

    Args:
        dir_: The directory to search.
        *extensions: List of file extensions to keep.

    """
    if not dir_.is_dir():
        raise ValueError(f"{dir_} is not a directory")
    for path in dir_.iterdir():
        if path.is_dir():
            filter_recursive(path, *extensions)
            if not len(list(path.iterdir())):
                path.rmdir()
        elif path.suffix not in extensions:
            path.unlink()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dir", help="Directory to search")
    parser.add_argument(
        "-e", "--extensions", nargs="+", default=['.py', '.pyi'],
        help="File extensions to keep (default: .py .pyi)")
    args = parser.parse_args()

    filter_recursive(pathlib.Path(args.dir), *args.extensions)
