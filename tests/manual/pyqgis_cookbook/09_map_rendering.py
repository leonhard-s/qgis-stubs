# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/composer.html

import os
from qgis.core import QgsProject, QgsMapRendererParallelJob, QgsMapSettings
from qgis.gui import QgisInterface
from PyQt5.QtCore import QEventLoop, QSize
from PyQt5.QtGui import QColor

iface = QgisInterface()

def simple_rendering() -> None:
    project = QgsProject.instance()
    assert project is not None
    image_location = os.path.join(project.homePath(), "render.png")

    vlayer = iface.activeLayer()
    assert vlayer is not None
    settings = QgsMapSettings()
    settings.setLayers([vlayer])
    settings.setBackgroundColor(QColor(255, 255, 255))
    settings.setOutputSize(QSize(800, 600))
    settings.setExtent(vlayer.extent())

    render = QgsMapRendererParallelJob(settings)

    def finished() -> None:
        img = render.renderedImage()
        # save the image; e.g. img.save("/Users/myuser/render.png","png")
        img.save(image_location, "png")

    render.finished.connect(finished)

    # Start the rendering
    render.start()

    # The following loop is not normally required, we
    # are using it here because this is a standalone example.
    loop = QEventLoop()
    render.finished.connect(loop.quit)
    loop.exec_()
