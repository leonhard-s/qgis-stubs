import typing

# https://github.com/leonhard-s/qgis-stubs/issues/10#issuecomment-5869049598
from qgis.core import NULL
from qgis.gui import QgisInterface
from qgis.utils import iface
typing.assert_type(NULL, None)
typing.assert_type(iface, QgisInterface)

# https://github.com/leonhard-s/qgis-stubs/issues/10#issuecomment-5887795387
from PyQt6.QtCore import QtMsgType as _PyQt6MsgType
from qgis.PyQt.QtCore import QtMsgType as _QgisPyQtMsgType
typing.assert_type(_PyQt6MsgType, _QgisPyQtMsgType)
