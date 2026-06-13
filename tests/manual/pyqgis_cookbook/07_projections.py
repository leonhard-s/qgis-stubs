# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/crs.html

from qgis.core import (QgsCoordinateReferenceSystem, QgsCoordinateTransform,
                       QgsProject, QgsPointXY)

def crs_transformation() -> None:
    crsSrc = QgsCoordinateReferenceSystem("EPSG:4326")    # WGS 84
    crsDest = QgsCoordinateReferenceSystem("EPSG:32633")  # WGS 84 / UTM zone 33N
    transformContext = QgsProject.instance().transformContext()
    xform = QgsCoordinateTransform(crsSrc, crsDest, transformContext)

    # forward transformation: src -> dest
    pt1 = xform.transform(QgsPointXY(18,5))
    print("Transformed point:", pt1)

    # inverse transformation: dest -> src
    pt2 = xform.transform(pt1, QgsCoordinateTransform.ReverseTransform)  # type: ignore
    print("Transformed back:", pt2)
