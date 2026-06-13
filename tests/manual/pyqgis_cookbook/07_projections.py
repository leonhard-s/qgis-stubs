# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/crs.html

from qgis.core import (QgsCoordinateReferenceSystem, QgsCoordinateTransform,
                       QgsProject, QgsPointXY)

def crs_transformation() -> None:
    crsSrc = QgsCoordinateReferenceSystem("EPSG:4326")    # WGS 84
    crsDest = QgsCoordinateReferenceSystem("EPSG:32633")  # WGS 84 / UTM zone 33N
    project = QgsProject.instance()
    assert project is not None
    transformContext = project.transformContext()
    xform = QgsCoordinateTransform(crsSrc, crsDest, transformContext)

    # forward transformation: src -> dest
    pt1 = xform.transform(QgsPointXY(18,5))
    print("Transformed point:", pt1)

    # inverse transformation: dest -> src
    pt2 = xform.transform(pt1, QgsCoordinateTransform.ReverseTransform)
    print("Transformed back:", pt2)
