import typing

# https://github.com/leonhard-s/qgis-stubs/issues/10#issuecomment-5869049598
from qgis.core import NULL
from qgis.gui import QgisInterface
from qgis.utils import iface
assert NULL is not None
assert NULL == None
typing.assert_type(iface, QgisInterface | None)

# https://github.com/leonhard-s/qgis-stubs/issues/10#issuecomment-5887795387
from qgis.PyQt.QtCore import QtMsgType
from PyQt6.QtCore import QtMsgType as _PyQt6MsgType
_msg_type = typing.cast(QtMsgType, QtMsgType.QtDebugMsg)
typing.assert_type(_msg_type, _PyQt6MsgType)
