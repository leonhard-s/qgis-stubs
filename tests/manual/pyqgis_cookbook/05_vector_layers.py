# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/vector.html

import typing
from qgis.core import (
    QgsFeature, QgsField, QgsFields, QgsGeometry, QgsPointXY, QgsProject,
    QgsVectorDataProvider, QgsVectorFileWriter, QgsVectorLayer,
    QgsWkbTypes)
from qgis.gui import QgisInterface
from PyQt5.QtCore import QMetaType, QVariant


def get_layer_info() -> None:
    vlayer = QgsVectorLayer(
        "testdata/data/data.gpkg|layername=airports", "Airports layer", "ogr")
    field: QgsField
    for field in vlayer.fields().toList():
        print(field.name(), field.typeName())


def iterate_vector_layer() -> None:
    iface = QgisInterface()

    # "layer" is a QgsVectorLayer instance
    layer = typing.cast(QgsVectorLayer, iface.activeLayer())
    features = layer.getFeatures()

    for feature in features:
        # retrieve every feature with its geometry and attributes
        print("Feature ID: ", feature.id())
        # fetch geometry
        # show some information about the feature geometry
        geom = feature.geometry()
        geomSingleType = QgsWkbTypes.isSingleType(geom.wkbType())
        if geom.type() == QgsWkbTypes.PointGeometry:
            x: typing.Any
            # the geometry type can be of single or multi type
            if geomSingleType:
                x = geom.asPoint()
                print("Point: ", x)
            else:
                x = geom.asMultiPoint()
                print("MultiPoint: ", x)
        elif geom.type() == QgsWkbTypes.LineGeometry:
            if geomSingleType:
                x = geom.asPolyline()
                print("Line: ", x, "length: ", geom.length())
            else:
                x = geom.asMultiPolyline()
                print("MultiLine: ", x, "length: ", geom.length())
        elif geom.type() == QgsWkbTypes.PolygonGeometry:
            if geomSingleType:
                x = geom.asPolygon()
                print("Polygon: ", x, "Area: ", geom.area())
            else:
                x = geom.asMultiPolygon()
                print("MultiPolygon: ", x, "Area: ", geom.area())
        else:
            print("Unknown or invalid geometry")
        # fetch attributes
        attrs = feature.attributes()
        # attrs is a list. It contains all the attribute values of this feature
        print(attrs)
        # for this test only print the first feature
        break


def get_capabilities() -> None:
    layer = QgsVectorLayer()
    provider = layer.dataProvider()
    assert provider is not None
    caps = provider.capabilities()
    # Check if a particular capability is supported:
    if caps & QgsVectorDataProvider.Capability.DeleteFeatures:
        print('The layer supports DeleteFeatures')


def add_features() -> None:
    layer = QgsVectorLayer()
    provider = layer.dataProvider()
    assert provider is not None
    caps = provider.capabilities()
    if caps & QgsVectorDataProvider.Capability.AddFeatures:
        feat = QgsFeature(layer.fields())
        feat.setAttributes([0, 'hello'])
        # Or set a single attribute by key or by index:
        feat.setAttribute('name', 'hello')
        feat.setAttribute(0, 'hello')
        feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(123, 456)))
        (res, outFeats) = provider.addFeatures([feat])

        _ = (res, outFeats)


def editing_buffer() -> None:
    layer = QgsVectorLayer()

    feat1 = feat2 = QgsFeature(layer.fields())
    fid = 99
    feat1.setId(fid)

    # add two features (QgsFeature instances)
    layer.addFeatures([feat1,feat2])
    # delete a feature with specified ID
    layer.deleteFeature(fid)

    # set new geometry (QgsGeometry instance) for a feature
    geometry = QgsGeometry.fromWkt("POINT(7 45)")
    layer.changeGeometry(fid, geometry)
    # update an attribute with given field index (int) to a given value
    fieldIndex =1
    value = 'My new name'
    layer.changeAttributeValue(fid, fieldIndex, value)

    # add new field
    type_ = typing.cast(QVariant.Type, QMetaType.Type.QString)
    layer.addAttribute(QgsField("mytext", type_))
    # remove a field
    layer.deleteAttribute(fieldIndex)


def create_from_file_writer() -> None:
    # SaveVectorOptions contains many settings for the writer process
    save_options = QgsVectorFileWriter.SaveVectorOptions()
    project = QgsProject.instance()
    assert project is not None
    transform_context = project.transformContext()
    # Write to a GeoPackage (default)
    layer = QgsVectorLayer()
    error = QgsVectorFileWriter.writeAsVectorFormatV3(layer,
                                                    "testdata/my_new_file.gpkg",
                                                    transform_context,
                                                    save_options)
    if error[0] == QgsVectorFileWriter.WriterError.NoError:
        print("success!")
    else:
        print(error)


def create_from_features() -> None:
    # define fields for feature attributes. A QgsFields object is needed
    fields = QgsFields()
    type_ = typing.cast(QVariant.Type, QMetaType.Type.Int)
    fields.append(QgsField("first", type_))
    type_ = typing.cast(QVariant.Type, QMetaType.Type.QString)
    fields.append(QgsField("second", type_))

    # pylint: disable=pointless-string-statement
    """ create an instance of vector file writer, which will create the vector file.
    Arguments:
    1. path to new file (will fail if exists already)
    2. field map
    3. geometry type - from WKBTYPE enum
    4. layer's spatial reference (instance of
    QgsCoordinateReferenceSystem)
    5. coordinate transform context
    6. save options (driver name for the output file, encoding etc.)
    """

    project = QgsProject.instance()
    assert project is not None
    crs = project.crs()
    transform_context = project.transformContext()
    save_options = QgsVectorFileWriter.SaveVectorOptions()
    save_options.driverName = "ESRI Shapefile"
    save_options.fileEncoding = "UTF-8"

    writer = QgsVectorFileWriter.create(
    "testdata/my_new_shapefile.shp",
    fields,
    QgsWkbTypes.Type.Point,
    crs,
    transform_context,
    save_options
    )
    assert writer is not None

    if writer.hasError() != QgsVectorFileWriter.WriterError.NoError:
        print("Error when creating shapefile: ",  writer.errorMessage())

    # add a feature
    fet = QgsFeature()

    fet.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(10,10)))
    fet.setAttributes([1, "text"])
    writer.addFeature(fet)

    # delete the writer to flush features to disk
    del writer
