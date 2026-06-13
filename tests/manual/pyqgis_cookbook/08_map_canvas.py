# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/canvas.html

# pylint: disable=missing-class-docstring

from qgis.core import QgsMapLayer
from qgis.gui import QgsMapCanvas, QgsMapToolPan, QgsMapToolZoom
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QMainWindow


class MyWnd(QMainWindow):
    def __init__(self, layer: QgsMapLayer) -> None:
        QMainWindow.__init__(self)

        self.canvas = QgsMapCanvas()
        self.canvas.setCanvasColor(Qt.white)

        self.canvas.setExtent(layer.extent())
        self.canvas.setLayers([layer])

        self.setCentralWidget(self.canvas)

        self.actionZoomIn = QAction("Zoom in", self)
        self.actionZoomOut = QAction("Zoom out", self)
        self.actionPan = QAction("Pan", self)

        self.actionZoomIn.setCheckable(True)
        self.actionZoomOut.setCheckable(True)
        self.actionPan.setCheckable(True)

        self.actionZoomIn.triggered.connect(self.zoomIn)
        self.actionZoomOut.triggered.connect(self.zoomOut)
        self.actionPan.triggered.connect(self.pan)

        self.toolbar = self.addToolBar("Canvas actions")
        self.toolbar.addAction(self.actionZoomIn)
        self.toolbar.addAction(self.actionZoomOut)
        self.toolbar.addAction(self.actionPan)

        # create the map tools
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(self.actionPan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
        self.toolZoomIn.setAction(self.actionZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
        self.toolZoomOut.setAction(self.actionZoomOut)

        self.pan()

    def zoomIn(self) -> None:
        self.canvas.setMapTool(self.toolZoomIn)

    def zoomOut(self) -> None:
        self.canvas.setMapTool(self.toolZoomOut)

    def pan(self) -> None:
        self.canvas.setMapTool(self.toolPan)
