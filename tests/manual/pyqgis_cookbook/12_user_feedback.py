# Adapted from:
# https://docs.qgis.org/4.2/en/docs/pyqgis_developer_cookbook/communicating.html

import typing
from qgis.core import Qgis
from qgis.gui import QgsMessageBar
from PyQt6.QtWidgets import QDialog, QGridLayout, QSizePolicy, QDialogButtonBox


class MyDialog(QDialog):
    # pylint: disable=missing-class-docstring,disallowed-name

    def __init__(self) -> None:
        QDialog.__init__(self)
        self.bar = QgsMessageBar()
        self.bar.setSizePolicy( QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed )
        self.setLayout(QGridLayout())
        layout = typing.cast(QGridLayout | None, self.layout())
        assert layout is not None
        layout.setContentsMargins(0, 0, 0, 0)
        self.buttonbox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.buttonbox.accepted.connect(self.run)
        layout.addWidget(self.buttonbox, 0, 0, 2, 1)
        layout.addWidget(self.bar, 0, 0, 1, 1)

    def run(self) -> None:
        self.bar.pushMessage("Hello", "World", level=Qgis.MessageLevel.Info)

myDlg = MyDialog()
myDlg.show()
