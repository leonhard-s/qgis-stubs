# -*- coding: utf-8 -*-

"""
***************************************************************************
    utils.py
    ---------------------
    Date                 : November 2009
    Copyright            : (C) 2009 by Martin Dobias
    Email                : wonder dot sk at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Martin Dobias'
__date__ = 'November 2009'
__copyright__ = '(C) 2009, Martin Dobias'

import configparser
import datetime
import sqlite3
from types import TracebackType
from typing import Any, Dict, List, Optional, Type, Union

from .core import Qgis
from .gui import QgisInterface
from .server import QgsServerInterface


def showWarning(message: Union[Warning, str], category: Type[Warning], filename: str, lineno: int, file: Any = ..., line: Optional[str] = ...) -> None: ...
def showException(type: Optional[Type[BaseException]], value: Optional[BaseException], tb: Optional[TracebackType], msg: Optional[str], messagebar: bool = ..., level: Qgis.MessageLevel = ...) -> None: ...
def show_message_log(pop_error: bool = ...) -> None: ...
def open_stack_dialog(type: Optional[Type[BaseException]], value: Optional[BaseException], tb: Optional[TracebackType], msg: Optional[str], pop_error: bool = ...) -> None: ...
def qgis_excepthook(type: Optional[Type[BaseException]], value: Optional[BaseException], tb: Optional[TracebackType]) -> None: ...


def installErrorHook() -> None:
    """
    Installs the QGIS application error/warning hook. This causes Python exceptions
    to be intercepted by the QGIS application and shown in the main window message bar
    and in custom dialogs.

    Generally you shouldn't call this method - it's automatically called by
    the QGIS app on startup, and has no use in standalone applications and scripts.
    """


def uninstallErrorHook() -> None: ...


iface: Optional[QgisInterface] = None


def initInterface(pointer: Any) -> None: ...


plugin_paths: List[str]
plugins: Dict[str, str]
plugin_times: Dict[str, datetime.datetime]
active_plugins: List[str]
available_plugins: List[str]
plugins_metadata_parser: Dict[str, configparser.ConfigParser]


def metadataParser() -> Dict[str, configparser.ConfigParser]:
    """Used by other modules to access the local parser object"""


def updateAvailablePlugins() -> None:
    """ Go through the plugin_paths list and find out what plugins are available. """


def pluginMetadata(packageName: str, fct: str) -> str:
    """ fetch metadata from a plugin - use values from metadata.txt """


def loadPlugin(packageName: str) -> bool:
    """ load plugin's package """


def startPlugin(packageName: str) -> bool:
    """ initialize the plugin """


def startProcessingPlugin(packageName: str) -> bool:
    """ initialize only the Processing components of a plugin """


def canUninstallPlugin(packageName: str) -> bool:
    """ confirm that the plugin can be uninstalled """


def unloadPlugin(packageName: str) -> bool:
    """ unload and delete plugin! """


def isPluginLoaded(packageName: str) -> bool:
    """ find out whether a plugin is active (i.e. has been started) """


def reloadPlugin(packageName: str) -> None:
    """ unload and start again a plugin """


def showPluginHelp(packageName: Optional[str] = ..., filename: str = ..., section: str = ...) -> None:
    """Open help in the user's html browser. The help file should be named index-ll_CC.html or index-ll.html or index.html.

    :param str packageName: name of package folder, if None it's using the current file package. Defaults to None. Optional.
    :param str filename: name of file to open. It can be a path like 'doc/index' for example. Defaults to 'index'.
    :param str section: URL path to open. Defaults to empty string.
    """


def pluginDirectory(packageName: str) -> str:
    """ return directory where the plugin resides. Plugin must be loaded already """


def reloadProjectMacros() -> None: ...
def unloadProjectMacros() -> None: ...
def openProjectMacro() -> None: ...
def saveProjectMacro() -> None: ...
def closeProjectMacro() -> None: ...


server_plugin_paths: List[str]
server_plugins: Dict[str, str]
server_active_plugins: List[str]
serverIface: Optional[QgsServerInterface] = None


def initServerInterface(pointer: Any) -> None: ...


def startServerPlugin(packageName: str) -> None:
    """ initialize the plugin """


def spatialite_connect(*args: Any, **kwargs: Any) -> sqlite3.Connection:
    """returns a dbapi2.Connection to a SpatiaLite db
using the "mod_spatialite" extension (python3)"""


class OverrideCursor():
    """
    Executes a code block with a different cursor set and makes sure the cursor
    is restored even if exceptions are raised or an intermediate ``return``
    statement is hit.

    Example:
    ```
    with OverrideCursor(Qt.WaitCursor):
        do_a_slow(operation)
    ```
    """

    def __init__(self, cursor: sqlite3.Cursor) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]) -> bool: ...


def run_script_from_file(filepath: str) -> None:
    """
    Runs a Python script from a given file. Supports loading processing scripts.
    :param filepath: The .py file to load.
    """
