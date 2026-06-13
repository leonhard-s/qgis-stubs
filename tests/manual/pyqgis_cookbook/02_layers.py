# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/loadlayer.html

from qgis.core import (
    QgsDataSourceUri, QgsProject, QgsRasterLayer,
    QgsRelationManager, QgsVectorLayer)
from qgis.gui import QgisInterface


def add_vector_layer() -> None:
    path_to_gpkg = "testdata/data/data.gpkg"
    gpkg_airports_layer = path_to_gpkg + "|layername=airports"
    vlayer = QgsVectorLayer(gpkg_airports_layer, "Airports layer", "ogr")
    if not vlayer.isValid():
        print("Layer failed to load!")
    else:
        project = QgsProject.instance()
        assert project is not None
        project.addMapLayer(vlayer)


def add_vector_layer_via_interface() -> None:
    path_to_gpkg = "testdata/data/data.gpkg"
    gpkg_airports_layer = path_to_gpkg + "|layername=airports"
    iface = QgisInterface()
    vlayer = iface.addVectorLayer(gpkg_airports_layer, "Airports layer", "ogr")
    if not vlayer:
        print("Layer failed to load!")


def add_vector_layer_from_shapefile() -> None:
    uri = "testdata/airports.shp"
    vlayer = QgsVectorLayer(uri, "layer_name_you_like", "ogr")
    project = QgsProject.instance()
    assert project is not None
    project.addMapLayer(vlayer)


def discover_layer_relations() -> None:
    project = QgsProject.instance()
    assert project is not None
    relation_manager = project.relationManager()
    existing_relations = list(relation_manager.relations().values())

    layers = [
        layer for layer in project.mapLayers().values() if layer.type() == layer.VectorLayer
    ]

    discovered_relations = QgsRelationManager.discoverRelations(existing_relations, layers)
    for relation in discovered_relations:
        relation_manager.addRelation(relation)


def add_vector_layer_from_postgis() -> None:
    uri = QgsDataSourceUri()
    # set host name, port, database name, username and password
    uri.setConnection("localhost", "5432", "dbname", "johny", "xxx")
    # set database schema, table name, geometry column and optionally
    # subset (WHERE clause)
    uri.setDataSource("public", "roads", "the_geom", "cityid = 2643", "primary_key_field")

    vlayer = QgsVectorLayer(uri.uri(False), "layer name you like", "postgres")
    _ = vlayer


def add_raster_layer() -> None:
    # get the path to a tif file  e.g. /home/project/data/srtm.tif
    path_to_tif = "qgis-projects/python_cookbook/data/srtm.tif"
    rlayer = QgsRasterLayer(path_to_tif, "SRTM layer name")
    if not rlayer.isValid():
        print("Layer failed to load!")
