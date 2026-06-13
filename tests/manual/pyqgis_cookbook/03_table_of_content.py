# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/legend.html

from qgis.core import QgsProject, QgsLayerTreeGroup, QgsVectorLayer


def list_layers() -> None:
    project = QgsProject.instance()
    assert project is not None
    # list of layer names using list comprehension
    layer_names: list[QgsVectorLayer] = [
        layer.name() for layer in project.mapLayers().values()]
    print(layer_names)
    # dictionary with key = layer name and value = layer object
    layers_list: dict[str, QgsVectorLayer] = {}
    l: QgsVectorLayer
    for l in QgsProject.instance().mapLayers().values():
        layers_list[l.name()] = l

    print(layers_list)


def move_layer_on_legend() -> None:
    project = QgsProject.instance()
    assert project is not None
    root = project.layerTreeRoot()
    # get a QgsVectorLayer
    vl = project.mapLayersByName("countries")[0]
    # create a QgsLayerTreeLayer object from vl by its id
    myvl = root.findLayer(vl.id())
    # clone the myvl QgsLayerTreeLayer object
    myvlclone = myvl.clone()
    # get the parent. If None (layer is not in group) returns ''
    parent: QgsLayerTreeGroup = myvl.parent()  # type: ignore
    # move the cloned layer to the top (0)
    parent.insertChildNode(0, myvlclone)
    # remove the original myvl
    root.removeChildNode(myvl)
