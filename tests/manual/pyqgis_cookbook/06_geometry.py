# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/geometry.html

import typing
from qgis.core import (
    QgsDistanceArea, QgsGeometry, QgsFeatureRequest, QgsPoint, QgsPointXY,
    QgsProject, QgsUnitTypes,  QgsVectorLayer)


def geometry_from_coordinates() -> None:
    gPnt = QgsGeometry.fromPointXY(QgsPointXY(1,1))
    print(gPnt)
    gLine = QgsGeometry.fromPolyline([QgsPoint(1, 1), QgsPoint(2, 2)])
    print(gLine)
    gPolygon = QgsGeometry.fromPolygonXY([[QgsPointXY(1, 1),
    QgsPointXY(2, 2), QgsPointXY(2, 1)]])
    print(gPolygon)


def calculate_area() -> None:
    d = QgsDistanceArea()
    d.setEllipsoid('WGS84')

    instance = QgsProject.instance()
    assert instance is not None
    layer = typing.cast(
        QgsVectorLayer, instance.mapLayersByName('countries')[0])

    # let's filter for countries that begin with Z, then get their features
    query = '"name" LIKE \'Z%\''
    features = layer.getFeatures(QgsFeatureRequest().setFilterExpression(query))

    for f in features:
        geom = f.geometry()
        name = f.attribute('NAME')
        print(name)
        print("Perimeter (m):", d.measurePerimeter(geom))
        print("Area (m2):", d.measureArea(geom))

        # let's calculate and print the area again, but this time in square
        # kilometers
        print("Area (km2):", d.convertAreaMeasurement(
            d.measureArea(geom), QgsUnitTypes.AreaUnit.AreaSquareKilometers))
