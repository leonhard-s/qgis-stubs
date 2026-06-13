# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/plugins/snippets.html

from qgis.gui import QgisInterface, QgsOptionsPageWidget, QgsOptionsWidgetFactory
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout

# pylint: disable=missing-class-docstring


class ConfigOptionsPage(QgsOptionsPageWidget):

    def __init__(self, parent: QWidget | None) -> None:
        super().__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)


class MyPluginOptionsFactory(QgsOptionsWidgetFactory):

    # pylint: disable=useless-super-delegation
    def __init__(self) -> None:
        super().__init__()

    def icon(self) -> QIcon:
        return QIcon('icons/my_plugin_icon.svg')

    def createWidget(self, parent: QWidget | None = None) -> QgsOptionsPageWidget:
        return ConfigOptionsPage(parent)


class MyPlugin:
    """QGIS Plugin Implementation."""

    def __init__(self, iface: QgisInterface) -> None:
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        self.options_factory: MyPluginOptionsFactory

    def initGui(self) -> None:
        self.options_factory = MyPluginOptionsFactory()
        self.options_factory.setTitle('My Plugin')
        self.iface.registerOptionsWidgetFactory(self.options_factory)

    def unload(self) -> None:
        self.iface.unregisterOptionsWidgetFactory(self.options_factory)
