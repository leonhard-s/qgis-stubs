# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/raster.html

import typing
from qgis.core import (
    Qgis, QgsColorRampShader, QgsProject, QgsRasterLayer, QgsRasterShader,
    QgsSingleBandPseudoColorRenderer)
from PyQt5.QtGui import QColor


def get_layer() -> None:
    project = QgsProject.instance()
    assert project is not None
    rlayer = typing.cast(
        QgsRasterLayer, project.mapLayersByName('srtm')[0])
    # get the resolution of the raster in layer unit
    print(rlayer.width(), rlayer.height())
    # get the extent of the layer as QgsRectangle
    print(rlayer.extent())
    # get the extent of the layer as Strings
    print(rlayer.extent().toString())
    # get the raster type:
    # 0 = GrayOrUndefined (single band), 1 = Palette (single band), 2 = Multiband
    print(rlayer.rasterType())
    # get the total band count of the raster
    print(rlayer.bandCount())
    # get the first band name of the raster
    print(rlayer.bandName(1))
    # get all the available metadata as a QgsLayerMetadata object
    print(rlayer.metadata())


def set_single_band_renderer() -> None:
    fcn = QgsColorRampShader()
    fcn.setColorRampType(Qgis.ShaderInterpolationMethod.Linear)
    lst = [ QgsColorRampShader.ColorRampItem(0, QColor(0,255,0)),
        QgsColorRampShader.ColorRampItem(255, QColor(255,255,0)) ]
    fcn.setColorRampItemList(lst)
    shader = QgsRasterShader()
    shader.setRasterShaderFunction(fcn)

    project = QgsProject.instance()
    assert project is not None
    rlayer = typing.cast(
        QgsRasterLayer, project.mapLayersByName('srtm')[0])
    renderer = QgsSingleBandPseudoColorRenderer(rlayer.dataProvider(), 1, shader)
    rlayer.setRenderer(renderer)
    rlayer.triggerRepaint()
