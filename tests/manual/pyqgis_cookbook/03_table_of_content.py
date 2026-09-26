# Adapted from:
# https://docs.qgis.org/4.2/en/docs/pyqgis_developer_cookbook/legend.html

from qgis.core import QgsProject, QgsVectorLayer


def list_layers() -> None:
    project = QgsProject.instance()
    assert project is not None
    # list of layer names using list comprehension
    layer_names: list[str] = [
        layer.name() for layer in project.mapLayers().values()]
    print(layer_names)
    # dictionary with key = layer name and value = layer object
    layers_list: dict[str, QgsVectorLayer] = {}
    l: QgsVectorLayer
    project = QgsProject.instance()
    assert project is not None
    for l in project.mapLayers().values():
        layers_list[l.name()] = l

    print(layers_list)


def move_layer_on_legend() -> None:
    project = QgsProject.instance()
    assert project is not None
    root = project.layerTreeRoot()
    assert root is not None
    # get a QgsVectorLayer
    vl = project.mapLayersByName("countries")[0]
    # create a QgsLayerTreeLayer object from vl by its id
    myvl = root.findLayer(vl.id())
    assert myvl is not None
    # clone the myvl QgsLayerTreeLayer object
    myvlclone = myvl.clone()
    # create a new group
    group1 = root.addGroup("Group1")
    assert group1 is not None
    # get the parent. If None (layer is not in group) returns ''
    parent = myvl.parent()
    assert parent is not None
    # move the cloned layer to the top (0)
    group1.insertChildNode(0, myvlclone)

    # remove the QgsLayerTreeLayer from its parent
    # TODO: This call is still referenced in the docs but no longer exposed in
    # the stubs, need to clarify if the docs or stubs are correct
    parent.removeChildNode(myvl)  # type: ignore
