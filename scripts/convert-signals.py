"""SIP generates methods for all signals, which is not how types work.

To remedy this, the following script steps through each class, looks it
up in the C++ API, and retrieves the list of signals from there. It
then replaces the names of the corresponding methods in the stub files
with `QtCore.pyqtSignal` types instead.
"""

import argparse
import pathlib
import re
import typing

import requests
from bs4 import BeautifulSoup, Tag

_RE_CLASSNAME = re.compile(r'class (\w+)\(')
_SIGNAL_TYPE = 'typing.ClassVar[QtCore.pyqtSignal]'


class _Soup:
    """Namespace for hiding hideous HTML-specific scrapery."""

    @staticmethod
    def get_signals_table(soup: BeautifulSoup) -> typing.Optional[Tag]:
        """Get the table listing the signals for this class.

        This only includes direct public signals, not inherited ones.
        """
        for table in soup.find_all('table', class_='memberdecls'):
            if table.find('a', id='signals') is not None:
                return table

    @classmethod
    def get_signal_rows(cls, table: Tag) -> typing.Iterator[Tag]:
        """Grab the type/name rows from the given signals table."""
        row: Tag
        for row in table.find_all('tr'):

            # Stop parsing once we reach inherited members
            if cls._is_inheritance_header(row):
                break
        
            if cls._is_signal_row(row):
                yield cls._table_cell_by_class(row, 'memItemRight')

    @staticmethod
    def _is_signal_row(row: Tag) -> bool:
        """Check if the given row is a signal row."""
        return any(c.startswith('memitem') for c in row['class'])

    @staticmethod
    def _is_inheritance_header(row: Tag) -> bool:
        return 'inherit_header' in row['class']

    @staticmethod
    def _table_cell_by_class(row: Tag, class_: str) -> Tag:
        """Get the first cell in the given row with the given class."""
        cell = typing.cast(typing.Optional[Tag], row.find('td', class_=class_))
        if cell is None:
            raise ValueError(f'Unable to find table cell with class {class_}')
        return cell


def _generate_cpp_api_url(classname: str) -> typing.List[str] :
    """Generate the URL for the C++ API docs for a given class."""
    return [f'https://api.qgis.org/api/{k}{classname}.html'
            for k in ('class', 'struct')]


def _get_signals_for_class(classname: str) -> typing.List[str]:
    """Get the list of signals for a given class from the C++ API.

    This makes a request to the QGIS C++ API docs and scrapes the
    resulting web page.
    """

    # NOTE: Using requests because making this work reliably with
    # aiohttp sounds like a bad time.

    # Try multiple URLs since some Python classes may be based on C++ structs,
    # which use a different URL
    for url in _generate_cpp_api_url(classname):
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            continue
        else:
            break
    else:
        print(f'ERROR: Class not found: {classname}')
        return []

    # Get the signals table from the page
    soup = BeautifulSoup(response.text, 'html.parser')
    table = _Soup.get_signals_table(soup)
    if table is None:
        return []

    # Find the signal names for this class
    signals: typing.List[str] = []
    for cell in _Soup.get_signal_rows(table):
    
        # NOTE: Since PyQt5-stubs's "QtCore.pyqtSignal" does not support
        # argument annotation, we don't need to worry about arguments (yet).
        # But if we did, this is where we'd do it.
    
        name_link = cell.find('a')
        if name_link is None:
            raise ValueError(f'Unable to find signal name in {cell}')
        
        signals.append(name_link.text)

    return signals


def _replace_signals_in_class(
        in_: typing.Iterator[str], out_f: typing.IO[str], classname: str,
) -> typing.Tuple[typing.Optional[str], int]:
    """Replace signal methods in the given class.

    Returns the number of replacements made.
    """
    signals = _get_signals_for_class(classname)
    total = len(signals)

    # Generate a RegEx for all signals in this class
    signals_re = re.compile(r'^( +)(def )(' + '|'.join(signals) + r')\(')

    line: typing.Optional[str] = next(in_)
    while True:

        # Find a method matching a known signal
        signal_match = signals_re.match(line)
        if signal_match is not None:

            # Get indentation
            indent = signal_match.group(1)
            # Get signal name
            signal = signal_match.group(3)

            # Remove signal (some signals are overloaded)
            if signal in signals:
                signals.remove(signal)
            else:
                print(f'WARNING: Overloaded signal: {classname}.{signal}')

            # Replace the method with pyqtsignal typehint
            out_f.write(f'{indent}{signal}: {_SIGNAL_TYPE}\n')

        # Not a signal
        else:
            out_f.write(line)

        # If we found the next class, break and let the next call handle it
        if line.startswith('class'):
            break

        # End of the file
        try:
            line = next(in_)
        except StopIteration:
            line = None
            break

    if signals:
        print(f'    WARNING: {len(signals)} signals were found but not '
              f'replaced class {classname}: {", ".join(signals)}')

    return line, total - len(signals)


def _replace_signals_in_file(
        in_: pathlib.Path, out: pathlib.Path) -> typing.Tuple[int, int]:
    """Replace signal methods with pyqtSignal types in the given file.

    Returns a tuple of the number of classes found and number of
    replacements made.
    """
    classes = 0
    replacements = 0
    with in_.open('r', encoding='utf-8') as in_f:
        with out.open('w', encoding='utf-8') as out_f:

            # NOTE: This does not support nested classes, but I am not aware of
            # any that use signals (yet)

            in_iter = iter(in_f)
            line = next(in_iter)
            while True:
                out_f.write(line)

                # Find a class, consuming additional lines as needed
                if line.startswith('class'):
                    classes += 1
                    classname = _RE_CLASSNAME.match(line).group(1)
                    line, new_replacements = _replace_signals_in_class(
                        in_iter, out_f, classname)

                    replacements += new_replacements
                    if line is None:
                        break

                else:
                    try:
                        line = next(in_iter)
                    except StopIteration:
                        break

    return classes, replacements


if __name__ == '__main__':
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument(
        'path', type=pathlib.Path, help='File or folder to process')
    args = parser.parse_args()

    files: typing.List[pathlib.Path]
    if args.path.is_dir():
        files = args.path.glob('*.pyi')
    else:
        files = [args.path]

    for filename in files:
        print(f'\nProcessing file: {filename}')
    
        in_path = filename.rename(filename.with_suffix('.pyi.bak'))
        out_path = filename
        classes, replacements = _replace_signals_in_file(in_path, out_path)

        print(f'  {classes} classes processed\n'
            f'  {replacements} signals replaced')

    print('done \\o/')
