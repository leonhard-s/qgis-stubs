# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/communicating.html

import typing
from qgis.core import Qgis
from qgis.gui import QgsMessageBar
from PyQt5.QtWidgets import QDialog, QGridLayout, QSizePolicy, QDialogButtonBox


class MyDialog(QDialog):
    # pylint: disable=missing-class-docstring,disallowed-name

    def __init__(self) -> None:
        QDialog.__init__(self)
        self.bar = QgsMessageBar()
        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.buttonbox = QDialogButtonBox(QDialogButtonBox.Ok)
        self.buttonbox.accepted.connect(self.run)

        layout = typing.cast(QGridLayout, self.layout())
        layout.addWidget(self.buttonbox, 0, 0, 2, 1)
        layout.addWidget(self.bar, 0, 0, 1, 1)

    def run(self) -> None:
        self.bar.pushMessage("Hello", "World", level=Qgis.MessageLevel.Info)

myDlg = MyDialog()
myDlg.show()
