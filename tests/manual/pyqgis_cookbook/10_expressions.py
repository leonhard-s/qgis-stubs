# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/expressions.html

import typing
from qgis.core import (
    QgsExpression, QgsExpressionContext, QgsExpressionContextUtils, QgsFeature,
    QgsField, QgsGeometry, QgsPointXY, QgsProject, QgsVectorLayer)
from PyQt5.QtCore import QMetaType, QVariant

# FIXME: this should come from qgis.core, but it's not in the stubs
def edit(_: QgsVectorLayer) -> typing.ContextManager[None]:
    return typing.cast(typing.ContextManager[None], None)
# pylint: disable=not-context-manager

def expressions_with_features() -> None:
    # create a vector layer
    vl = QgsVectorLayer("Point", "Companies", "memory")
    pr = vl.dataProvider()
    assert pr is not None
    raw_args = (("Name", QMetaType.Type.QString),
                ("Employees",  QMetaType.Type.Int),
                ("Revenue", QMetaType.Type.Double),
                ("Rev. per employee", QMetaType.Type.Double),
                ("Sum", QMetaType.Type.Double),
                ("Fun", QMetaType.Type.Double))
    pr.addAttributes([
        QgsField(n, typing.cast(QVariant.Type, t)) for n, t in raw_args])
    vl.updateFields()

    # add data to the first three fields
    my_data: list[dict[str, typing.Any]] = [
        {'x': 0, 'y': 0, 'name': 'ABC', 'emp': 10,  'rev': 100.1},
        {'x': 1, 'y': 1, 'name': 'DEF', 'emp': 2,   'rev': 50.5},
        {'x': 5, 'y': 5, 'name': 'GHI', 'emp': 100, 'rev': 725.9}]

    for rec in my_data:
        f = QgsFeature()
        pt = QgsPointXY(rec['x'], rec['y'])
        f.setGeometry(QgsGeometry.fromPointXY(pt))
        f.setAttributes([rec['name'], rec['emp'], rec['rev']])
        pr.addFeature(f)

    vl.updateExtents()
    project = QgsProject.instance()
    assert project is not None
    project.addMapLayer(vl)

    # The first expression computes the revenue per employee.
    # The second one computes the sum of all revenue values in the layer.
    # The final third expression doesn’t really make sense but illustrates
    # the fact that we can use a wide range of expression functions, such
    # as area and buffer in our expressions:
    expression1 = QgsExpression('"Revenue"/"Employees"')
    expression2 = QgsExpression('sum("Revenue")')
    expression3 = QgsExpression('area(buffer($geometry,"Employees"))')

    # QgsExpressionContextUtils.globalProjectLayerScopes() is a convenience
    # function that adds the global, project, and layer scopes all at once.
    # Alternatively, those scopes can also be added manually. In any case,
    # it is important to always go from “most generic” to “most specific”
    # scope, i.e. from global to project to layer
    context = QgsExpressionContext()
    context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(vl))

    with edit(vl):
        for f in vl.getFeatures():
            context.setFeature(f)
            f['Rev. per employee'] = expression1.evaluate(context)
            f['Sum'] = expression2.evaluate(context)
            f['Fun'] = expression3.evaluate(context)
            vl.updateFeature(f)

            print(f['Sum'])
