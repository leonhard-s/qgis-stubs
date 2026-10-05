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

# https://github.com/leonhard-s/qgis-stubs/issues/10
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QAction, QDialog
from PyQt6.QtGui import QAction as _PyQt6QAction
typing.assert_type(QAction, type[_PyQt6QAction])
_FORM_CLASS: typing.Any
_FORM_CLASS, _ = uic.loadUiType('dialog.ui')
class _Dialog(QDialog, _FORM_CLASS):  # type: ignore[misc]  # generated form class is Any
    pass


_dialog = uic.loadUi('dialog.ui', QDialog())
typing.assert_type(_dialog, QDialog)
