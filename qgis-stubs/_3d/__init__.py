# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : May 2014
    Copyright            : (C) 2014 by Nathan Woodrow
    Email                : woodrow dot nathan at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Nathan Woodrow'
__date__ = 'May 2014'
__copyright__ = '(C) 2014, Nathan Woodrow'

from qgis.PyQt import QtCore
from qgis._3d_p import *

"""
This folder is completed using sipify.py script
It is not aimed to be manually edited
"""
# The following has been generated automatically from src/3d/qgs3d.h
try:
    Qgs3D.instance = staticmethod(Qgs3D.instance)
    Qgs3D.initialize = staticmethod(Qgs3D.initialize)
    Qgs3D.materialRegistry = staticmethod(Qgs3D.materialRegistry)
    Qgs3D.terrainRegistry = staticmethod(Qgs3D.terrainRegistry)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/processing/qgs3dalgorithms.h
try:
    Qgs3DAlgorithms.__overridden_methods__ = ['icon', 'svgIconPath', 'id', 'helpId', 'name', 'supportsNonFileBasedOutput', 'loadAlgorithms']
    Qgs3DAlgorithms.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/qgs3dmapcanvas.h
try:
    Qgs3DMapCanvas.__overridden_methods__ = ['showEvent', 'resizeEvent', 'eventFilter']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/qgs3dmapscene.h
try:
    Qgs3DMapScene.__attribute_docs__ = {'terrainEntityChanged': 'Emitted when the current terrain entity is replaced by a new one\n', 'totalPendingJobsCountChanged': 'Emitted when the total number of pending jobs changes\n\n.. versionadded:: 3.12\n', 'sceneStateChanged': "Emitted when the scene's state has changed\n", 'fpsCountChanged': 'Emitted when the FPS count changes\n', 'fpsCounterEnabledChanged': 'Emitted when the FPS counter is activated or deactivated\n', 'viewed2DExtentFrom3DChanged': 'Emitted when the viewed 2D extent seen by the 3D camera has changed\n\n.. versionadded:: 3.26\n', 'gpuMemoryLimitReached': "Emitted when one of the entities reaches its GPU memory limit and it is\nnot possible to lower the GPU memory use by unloading data that's not\ncurrently needed.\n"}
    Qgs3DMapScene.openScenes = staticmethod(Qgs3DMapScene.openScenes)
    Qgs3DMapScene.__signal_arguments__ = {'fpsCountChanged': ['fpsCount: float'], 'fpsCounterEnabledChanged': ['fpsCounterEnabled: bool'], 'viewed2DExtentFrom3DChanged': ['extent: List[QgsPointXY]']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/qgs3dmapsettings.h
try:
    Qgs3DMapSettings.__attribute_docs__ = {'settingsChanged': 'Emitted when one of the configuration settings has changed\n\n.. versionadded:: 3.24\n', 'backgroundColorChanged': 'Emitted when the background color has changed\n', 'selectionColorChanged': 'Emitted when the selection color has changed\n', 'layersChanged': 'Emitted when the list of map layers for 3d rendering has changed.\n\n.. seealso:: :py:func:`setLayers`\n\n.. seealso:: :py:func:`layers`\n', 'terrainGeneratorChanged': 'Emitted when the terrain generator has changed\n', 'terrainSettingsChanged': 'Emitted when the terrain settings are changed.\n\n.. versionadded:: 3.42\n', 'terrainVerticalScaleChanged': 'Emitted when the vertical scale of the terrain has changed\n\n.. deprecated:: 3.42\n\n   Use :py:func:`~Qgs3DMapSettings.terrainSettingsChanged` instead.\n', 'mapTileResolutionChanged': 'Emitted when the map tile resoulution has changed\n\n.. deprecated:: 3.42\n\n   Use :py:func:`~Qgs3DMapSettings.terrainSettingsChanged` instead.\n', 'maxTerrainScreenErrorChanged': 'Emitted when the maximum terrain screen error has changed\n\n.. deprecated:: 3.42\n\n   Use :py:func:`~Qgs3DMapSettings.terrainSettingsChanged` instead.\n', 'maxTerrainGroundErrorChanged': 'Emitted when the maximum terrain ground error has changed\n\n.. deprecated:: 3.42\n\n   Use :py:func:`~Qgs3DMapSettings.terrainSettingsChanged` instead.\n', 'terrainElevationOffsetChanged': 'Emitted when the terrain elevation offset is changed\n\n.. deprecated:: 3.42\n\n   Use :py:func:`~Qgs3DMapSettings.terrainSettingsChanged` instead.\n', 'terrainShadingChanged': 'Emitted when terrain shading enabled flag or terrain shading material\nhas changed\n\n.. versionadded:: 3.6\n', 'terrainMapThemeChanged': "Emitted when terrain's map theme has changed\n\n.. versionadded:: 3.6\n", 'renderersChanged': "Emitted when the list of map's extra renderers have been modified\n\n.. versionadded:: 3.10\n", 'showTerrainBoundingBoxesChanged': "Emitted when the flag whether terrain's bounding boxes are shown has\nchanged\n", 'showTerrainTilesInfoChanged': "Emitted when the flag whether terrain's tile info is shown has changed\n", 'showCameraViewCenterChanged': "Emitted when the flag whether camera's view center is shown has changed\n\n.. versionadded:: 3.4\n", 'showCameraRotationCenterChanged': "Emitted when the flag whether camera's rotation center is shown has\nchanged\n\n.. versionadded:: 3.24\n", 'showLightSourceOriginsChanged': 'Emitted when the flag whether light source origins are shown has\nchanged.\n\n.. versionadded:: 3.15\n', 'showLabelsChanged': 'Emitted when the flag whether labels are displayed on terrain tiles has\nchanged\n', 'stopUpdatesChanged': 'Emitted when the flag whether to keep updating scene has changed\n\n.. versionadded:: 3.42\n', 'eyeDomeLightingEnabledChanged': 'Emitted when the flag whether eye dome lighting is used has changed\n\n.. versionadded:: 3.18\n', 'eyeDomeLightingStrengthChanged': 'Emitted when the eye dome lighting strength has changed\n\n.. versionadded:: 3.18\n', 'eyeDomeLightingDistanceChanged': 'Emitted when the eye dome lighting distance has changed\n\n.. versionadded:: 3.18\n', 'debugShadowMapSettingsChanged': 'Emitted when shadow map debugging has changed\n\n.. versionadded:: 3.18\n', 'debugDepthMapSettingsChanged': 'Emitted when depth map debugging has changed\n\n.. versionadded:: 3.18\n', 'pointLightsChanged': 'Emitted when the list of point lights changes\n\n.. versionadded:: 3.6\n', 'lightSourcesChanged': 'Emitted when any of the light source settings in the map changes.\n\n.. versionadded:: 3.26\n', 'directionalLightsChanged': 'Emitted when the list of directional lights changes\n\n.. versionadded:: 3.16\n', 'fieldOfViewChanged': 'Emitted when the camera lens field of view changes\n\n.. versionadded:: 3.8\n', 'projectionTypeChanged': 'Emitted when the camera lens projection type changes\n\n.. versionadded:: 3.18\n', 'cameraNavigationModeChanged': 'Emitted when the camera navigation mode was changed\n\n.. versionadded:: 3.18\n', 'cameraMovementSpeedChanged': 'Emitted when the camera movement speed was changed\n\n.. versionadded:: 3.18\n', 'skyboxSettingsChanged': 'Emitted when skybox settings are changed\n\n.. versionadded:: 3.16\n', 'shadowSettingsChanged': 'Emitted when shadow rendering settings are changed\n\n.. versionadded:: 3.16\n', 'ambientOcclusionSettingsChanged': 'Emitted when ambient occlusion rendering settings are changed\n\n.. versionadded:: 3.28\n', 'fpsCounterEnabledChanged': 'Emitted when the FPS counter is enabled or disabled\n\n.. versionadded:: 3.18\n', 'viewFrustumVisualizationEnabledChanged': "Emitted when the camera's view frustum visualization on the main 2D map\ncanvas is enabled or disabled\n\n.. versionadded:: 3.26\n", 'axisSettingsChanged': 'Emitted when 3d axis rendering settings are changed\n\n.. versionadded:: 3.26\n', 'debugOverlayEnabledChanged': 'Emitted when the debug overaly is enabled or disabled\n\n.. versionadded:: 3.26\n', 'extentChanged': "Emitted when the 3d view's 2d extent has changed\n\n.. seealso:: :py:func:`setExtent`\n\n.. versionadded:: 3.30\n", 'showExtentIn2DViewChanged': "Emitted when the parameter to display 3d view's extent in the 2D canvas\nhas changed\n\n.. seealso:: :py:func:`setShowExtentIn2DView`\n\n.. versionadded:: 3.32\n", 'showDebugPanelChanged': 'Emitted when the Show debug panel checkbox changes value\n\n.. seealso:: :py:func:`setShowDebugPanel`\n\n.. versionadded:: 3.42\n', 'originChanged': "Emitted when the world's origin point has been shifted\n\n.. seealso:: :py:func:`setOrigin`\n\n.. versionadded:: 3.42\n"}
    Qgs3DMapSettings.__signal_arguments__ = {'fpsCounterEnabledChanged': ['fpsCounterEnabled: bool'], 'debugOverlayEnabledChanged': ['debugOverlayEnabled: bool'], 'showDebugPanelChanged': ['shown: bool']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/terrain/qgs3dterrainregistry.h
try:
    Qgs3DTerrainAbstractMetadata.__abstract_methods__ = ['createTerrainSettings']
    Qgs3DTerrainAbstractMetadata.__group__ = ['terrain']
except (NameError, AttributeError):
    pass
try:
    Qgs3DTerrainRegistry.__group__ = ['terrain']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/qgs3dtypes.h
try:
    Qgs3DTypes.__attribute_docs__ = {'PROP_NAME_3D_RENDERER_FLAG': 'Qt property name to hold the 3D geometry renderer flag'}
    Qgs3DTypes.__annotations__ = {'PROP_NAME_3D_RENDERER_FLAG': str}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/materials/qgsabstractmaterialsettings.h
QgsAbstractMaterialSettings.RenderingTechnique = QgsMaterialSettingsRenderingTechnique
# monkey patching scoped based enum
QgsAbstractMaterialSettings.Triangles = QgsMaterialSettingsRenderingTechnique.Triangles
QgsAbstractMaterialSettings.Triangles.is_monkey_patched = True
QgsAbstractMaterialSettings.Triangles.__doc__ = "Triangle based rendering (default)"
QgsAbstractMaterialSettings.Lines = QgsMaterialSettingsRenderingTechnique.Lines
QgsAbstractMaterialSettings.Lines.is_monkey_patched = True
QgsAbstractMaterialSettings.Lines.__doc__ = "Line based rendering, requires line data"
QgsAbstractMaterialSettings.InstancedPoints = QgsMaterialSettingsRenderingTechnique.InstancedPoints
QgsAbstractMaterialSettings.InstancedPoints.is_monkey_patched = True
QgsAbstractMaterialSettings.InstancedPoints.__doc__ = "Instanced based rendering, requiring triangles and point data"
QgsAbstractMaterialSettings.Points = QgsMaterialSettingsRenderingTechnique.Points
QgsAbstractMaterialSettings.Points.is_monkey_patched = True
QgsAbstractMaterialSettings.Points.__doc__ = "Point based rendering, requires point data"
QgsAbstractMaterialSettings.TrianglesWithFixedTexture = QgsMaterialSettingsRenderingTechnique.TrianglesWithFixedTexture
QgsAbstractMaterialSettings.TrianglesWithFixedTexture.is_monkey_patched = True
QgsAbstractMaterialSettings.TrianglesWithFixedTexture.__doc__ = "Triangle based rendering, using a fixed, non-user-configurable texture (e.g. for terrain rendering)"
QgsAbstractMaterialSettings.TrianglesFromModel = QgsMaterialSettingsRenderingTechnique.TrianglesFromModel
QgsAbstractMaterialSettings.TrianglesFromModel.is_monkey_patched = True
QgsAbstractMaterialSettings.TrianglesFromModel.__doc__ = "Triangle based rendering, using a model object source"
QgsAbstractMaterialSettings.TrianglesDataDefined = QgsMaterialSettingsRenderingTechnique.TrianglesDataDefined
QgsAbstractMaterialSettings.TrianglesDataDefined.is_monkey_patched = True
QgsAbstractMaterialSettings.TrianglesDataDefined.__doc__ = "Triangle based rendering with possibility of datadefined color \n.. versionadded:: 3.18"
QgsMaterialSettingsRenderingTechnique.__doc__ = """Material rendering techniques

.. versionadded:: 3.16

* ``Triangles``: Triangle based rendering (default)
* ``Lines``: Line based rendering, requires line data
* ``InstancedPoints``: Instanced based rendering, requiring triangles and point data
* ``Points``: Point based rendering, requires point data
* ``TrianglesWithFixedTexture``: Triangle based rendering, using a fixed, non-user-configurable texture (e.g. for terrain rendering)
* ``TrianglesFromModel``: Triangle based rendering, using a model object source
* ``TrianglesDataDefined``: Triangle based rendering with possibility of datadefined color

  .. versionadded:: 3.18


"""
# --
try:
    QgsAbstractMaterialSettings.__virtual_methods__ = ['readXml', 'writeXml']
    QgsAbstractMaterialSettings.__abstract_methods__ = ['type', 'clone', 'equals']
    QgsAbstractMaterialSettings.__group__ = ['materials']
except (NameError, AttributeError):
    pass
try:
    QgsMaterialContext.__group__ = ['materials']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/terrain/qgsabstractterrainsettings.h
try:
    QgsAbstractTerrainSettings.__virtual_methods__ = ['resolveReferences']
    QgsAbstractTerrainSettings.__abstract_methods__ = ['clone', 'type', 'equals', 'readXml', 'writeXml']
    QgsAbstractTerrainSettings.__group__ = ['terrain']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/qgsabstractvectorlayer3drenderer.h
try:
    QgsAbstractVectorLayer3DRenderer.__overridden_methods__ = ['resolveReferences']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/qgscameracontroller.h
try:
    QgsCameraController.__attribute_docs__ = {'cameraChanged': 'Emitted when camera has been updated\n', 'navigationModeChanged': 'Emitted when the navigation mode is changed using the hotkey ctrl + ~\n', 'cameraMovementSpeedChanged': 'Emitted whenever the camera movement speed is changed by the controller.\n', 'setCursorPosition': 'Emitted when the mouse cursor position should be moved to the specified\n``point`` on the map viewport.\n', 'requestDepthBufferCapture': 'Emitted to ask for the depth buffer image\n\n.. versionadded:: 3.24\n', 'cameraRotationCenterChanged': 'Emitted when the camera rotation center changes\n\n.. versionadded:: 3.24\n'}
    QgsCameraController.__signal_arguments__ = {'navigationModeChanged': ['mode: Qgis.NavigationMode'], 'cameraMovementSpeedChanged': ['speed: float'], 'setCursorPosition': ['point: QPoint'], 'cameraRotationCenterChanged': ['position: QVector3D']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/terrain/qgsdemterrainsettings.h
try:
    QgsDemTerrainSettings.create = staticmethod(QgsDemTerrainSettings.create)
    QgsDemTerrainSettings.__overridden_methods__ = ['clone', 'type', 'readXml', 'writeXml', 'resolveReferences', 'equals']
    QgsDemTerrainSettings.__group__ = ['terrain']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/lights/qgsdirectionallightsettings.h
try:
    QgsDirectionalLightSettings.__overridden_methods__ = ['type', 'clone', 'writeXml', 'readXml']
    QgsDirectionalLightSettings.__group__ = ['lights']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/terrain/qgsflatterrainsettings.h
try:
    QgsFlatTerrainSettings.create = staticmethod(QgsFlatTerrainSettings.create)
    QgsFlatTerrainSettings.__overridden_methods__ = ['clone', 'type', 'readXml', 'writeXml', 'equals']
    QgsFlatTerrainSettings.__group__ = ['terrain']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/materials/qgsgoochmaterialsettings.h
try:
    QgsGoochMaterialSettings.create = staticmethod(QgsGoochMaterialSettings.create)
    QgsGoochMaterialSettings.supportsTechnique = staticmethod(QgsGoochMaterialSettings.supportsTechnique)
    QgsGoochMaterialSettings.__overridden_methods__ = ['type', 'clone', 'equals', 'readXml', 'writeXml', 'toExportParameters']
    QgsGoochMaterialSettings.__group__ = ['materials']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/qgslayoutitem3dmap.h
try:
    QgsLayoutItem3DMap.create = staticmethod(QgsLayoutItem3DMap.create)
    QgsLayoutItem3DMap.__overridden_methods__ = ['type', 'icon', 'displayName', 'finalizeRestoreFromXml', 'refresh', 'draw', 'writePropertiesToElement', 'readPropertiesFromElement']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/lights/qgslightsource.h
try:
    QgsLightSource.createFromXml = staticmethod(QgsLightSource.createFromXml)
    QgsLightSource.__virtual_methods__ = ['resolveReferences']
    QgsLightSource.__abstract_methods__ = ['type', 'clone', 'writeXml', 'readXml']
    QgsLightSource.__group__ = ['lights']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/symbols/qgsline3dsymbol.h
try:
    QgsLine3DSymbol.create = staticmethod(QgsLine3DSymbol.create)
    QgsLine3DSymbol.__overridden_methods__ = ['type', 'clone', 'writeXml', 'readXml', 'compatibleGeometryTypes', 'setDefaultPropertiesFromLayer']
    QgsLine3DSymbol.__group__ = ['symbols']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/materials/qgsmaterialregistry.h
try:
    QgsMaterialSettingsAbstractMetadata.__abstract_methods__ = ['create', 'supportsTechnique']
    QgsMaterialSettingsAbstractMetadata.__group__ = ['materials']
except (NameError, AttributeError):
    pass
try:
    QgsMaterialRegistry.__group__ = ['materials']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/symbols/qgsmesh3dsymbol.h
# monkey patching scoped based enum
QgsMesh3DSymbol.RenderingStyle.SingleColor.__doc__ = "Render the mesh with a single color"
QgsMesh3DSymbol.RenderingStyle.ColorRamp.__doc__ = "Render the mesh with a color ramp"
QgsMesh3DSymbol.RenderingStyle.ColorRamp2DRendering.__doc__ = "Render the mesh with the color ramp shader of the 2D rendering"
QgsMesh3DSymbol.RenderingStyle.__doc__ = """How to render the color of the mesh

.. versionadded:: 3.12

* ``SingleColor``: Render the mesh with a single color
* ``ColorRamp``: Render the mesh with a color ramp
* ``ColorRamp2DRendering``: Render the mesh with the color ramp shader of the 2D rendering

"""
# --
# monkey patching scoped based enum
QgsMesh3DSymbol.ZValueType.VerticesZValue.__doc__ = "Use the Z value of the vertices"
QgsMesh3DSymbol.ZValueType.ScalarDatasetZvalue.__doc__ = "Use the value from a dataset (for example, water surface value)"
QgsMesh3DSymbol.ZValueType.__doc__ = """How to render the Z value of the mesh

.. versionadded:: 3.14

* ``VerticesZValue``: Use the Z value of the vertices
* ``ScalarDatasetZvalue``: Use the value from a dataset (for example, water surface value)

"""
# --
try:
    QgsMesh3DSymbol.__overridden_methods__ = ['type', 'clone', 'writeXml', 'readXml']
    QgsMesh3DSymbol.__group__ = ['symbols']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/terrain/qgsmeshterrainsettings.h
try:
    QgsMeshTerrainSettings.create = staticmethod(QgsMeshTerrainSettings.create)
    QgsMeshTerrainSettings.__overridden_methods__ = ['clone', 'type', 'readXml', 'writeXml', 'resolveReferences', 'equals']
    QgsMeshTerrainSettings.__group__ = ['terrain']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/materials/qgsmetalroughmaterialsettings.h
try:
    QgsMetalRoughMaterialSettings.supportsTechnique = staticmethod(QgsMetalRoughMaterialSettings.supportsTechnique)
    QgsMetalRoughMaterialSettings.create = staticmethod(QgsMetalRoughMaterialSettings.create)
    QgsMetalRoughMaterialSettings.__overridden_methods__ = ['type', 'clone', 'equals', 'toExportParameters', 'readXml', 'writeXml']
    QgsMetalRoughMaterialSettings.__group__ = ['materials']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/materials/qgsnullmaterialsettings.h
try:
    QgsNullMaterialSettings.supportsTechnique = staticmethod(QgsNullMaterialSettings.supportsTechnique)
    QgsNullMaterialSettings.create = staticmethod(QgsNullMaterialSettings.create)
    QgsNullMaterialSettings.__overridden_methods__ = ['type', 'clone', 'equals', 'toExportParameters']
    QgsNullMaterialSettings.__group__ = ['materials']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/terrain/qgsonlinedemterrainsettings.h
try:
    QgsOnlineDemTerrainSettings.create = staticmethod(QgsOnlineDemTerrainSettings.create)
    QgsOnlineDemTerrainSettings.__overridden_methods__ = ['clone', 'type', 'readXml', 'writeXml', 'equals']
    QgsOnlineDemTerrainSettings.__group__ = ['terrain']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/materials/qgsphongmaterialsettings.h
try:
    QgsPhongMaterialSettings.supportsTechnique = staticmethod(QgsPhongMaterialSettings.supportsTechnique)
    QgsPhongMaterialSettings.create = staticmethod(QgsPhongMaterialSettings.create)
    QgsPhongMaterialSettings.__overridden_methods__ = ['type', 'clone', 'equals', 'toExportParameters', 'readXml', 'writeXml']
    QgsPhongMaterialSettings.__group__ = ['materials']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/materials/qgsphongtexturedmaterialsettings.h
try:
    QgsPhongTexturedMaterialSettings.supportsTechnique = staticmethod(QgsPhongTexturedMaterialSettings.supportsTechnique)
    QgsPhongTexturedMaterialSettings.create = staticmethod(QgsPhongTexturedMaterialSettings.create)
    QgsPhongTexturedMaterialSettings.__overridden_methods__ = ['type', 'clone', 'equals', 'toExportParameters', 'readXml', 'writeXml']
    QgsPhongTexturedMaterialSettings.__group__ = ['materials']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/symbols/qgspoint3dsymbol.h
try:
    QgsPoint3DSymbol.create = staticmethod(QgsPoint3DSymbol.create)
    QgsPoint3DSymbol.shapeFromString = staticmethod(QgsPoint3DSymbol.shapeFromString)
    QgsPoint3DSymbol.shapeToString = staticmethod(QgsPoint3DSymbol.shapeToString)
    QgsPoint3DSymbol.__overridden_methods__ = ['type', 'clone', 'writeXml', 'readXml', 'compatibleGeometryTypes', 'setDefaultPropertiesFromLayer']
    QgsPoint3DSymbol.__group__ = ['symbols']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/symbols/qgspointcloud3dsymbol.h
try:
    QgsPointCloud3DSymbol.__abstract_methods__ = ['clone', 'symbolType', 'byteStride']
    QgsPointCloud3DSymbol.__overridden_methods__ = ['type', 'clone', 'copyBaseSettings']
    QgsPointCloud3DSymbol.__group__ = ['symbols']
except (NameError, AttributeError):
    pass
try:
    QgsSingleColorPointCloud3DSymbol.__overridden_methods__ = ['symbolType', 'clone', 'writeXml', 'readXml', 'byteStride']
    QgsSingleColorPointCloud3DSymbol.__group__ = ['symbols']
except (NameError, AttributeError):
    pass
try:
    QgsColorRampPointCloud3DSymbol.__overridden_methods__ = ['clone', 'symbolType', 'writeXml', 'readXml', 'byteStride']
    QgsColorRampPointCloud3DSymbol.__group__ = ['symbols']
except (NameError, AttributeError):
    pass
try:
    QgsRgbPointCloud3DSymbol.__overridden_methods__ = ['symbolType', 'clone', 'writeXml', 'readXml', 'byteStride']
    QgsRgbPointCloud3DSymbol.__group__ = ['symbols']
except (NameError, AttributeError):
    pass
try:
    QgsClassificationPointCloud3DSymbol.__overridden_methods__ = ['clone', 'symbolType', 'writeXml', 'readXml', 'byteStride']
    QgsClassificationPointCloud3DSymbol.__group__ = ['symbols']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/qgspointcloudlayer3drenderer.h
try:
    QgsPointCloudLayer3DRenderer.__overridden_methods__ = ['type', 'clone', 'writeXml', 'readXml', 'resolveReferences', 'convertFrom2DRenderer']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/lights/qgspointlightsettings.h
try:
    QgsPointLightSettings.__overridden_methods__ = ['type', 'clone', 'writeXml', 'readXml']
    QgsPointLightSettings.__group__ = ['lights']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/symbols/qgspolygon3dsymbol.h
try:
    QgsPolygon3DSymbol.create = staticmethod(QgsPolygon3DSymbol.create)
    QgsPolygon3DSymbol.__overridden_methods__ = ['type', 'clone', 'writeXml', 'readXml', 'compatibleGeometryTypes', 'setDefaultPropertiesFromLayer']
    QgsPolygon3DSymbol.__group__ = ['symbols']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/terrain/qgsquantizedmeshterrainsettings.h
try:
    QgsQuantizedMeshTerrainSettings.create = staticmethod(QgsQuantizedMeshTerrainSettings.create)
    QgsQuantizedMeshTerrainSettings.__overridden_methods__ = ['clone', 'type', 'readXml', 'writeXml', 'resolveReferences', 'equals']
    QgsQuantizedMeshTerrainSettings.__group__ = ['terrain']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/qgsrulebased3drenderer.h
try:
    QgsRuleBased3DRenderer.Rule.create = staticmethod(QgsRuleBased3DRenderer.Rule.create)
except (NameError, AttributeError):
    pass
try:
    QgsRuleBased3DRendererMetadata.__overridden_methods__ = ['createRenderer']
except (NameError, AttributeError):
    pass
try:
    QgsRuleBased3DRenderer.__overridden_methods__ = ['type', 'clone', 'writeXml', 'readXml']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/materials/qgssimplelinematerialsettings.h
try:
    QgsSimpleLineMaterialSettings.supportsTechnique = staticmethod(QgsSimpleLineMaterialSettings.supportsTechnique)
    QgsSimpleLineMaterialSettings.create = staticmethod(QgsSimpleLineMaterialSettings.create)
    QgsSimpleLineMaterialSettings.__overridden_methods__ = ['type', 'clone', 'equals', 'toExportParameters', 'readXml', 'writeXml']
    QgsSimpleLineMaterialSettings.__group__ = ['materials']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/qgstiledscenelayer3drenderer.h
try:
    QgsTiledSceneLayer3DRendererMetadata.__overridden_methods__ = ['createRenderer']
except (NameError, AttributeError):
    pass
try:
    QgsTiledSceneLayer3DRenderer.__overridden_methods__ = ['type', 'clone', 'writeXml', 'readXml', 'resolveReferences']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/3d/qgsvectorlayer3drenderer.h
try:
    QgsVectorLayer3DRendererMetadata.__overridden_methods__ = ['createRenderer']
except (NameError, AttributeError):
    pass
try:
    QgsVectorLayer3DRenderer.__overridden_methods__ = ['type', 'clone', 'writeXml', 'readXml']
except (NameError, AttributeError):
    pass


from qgis.core import Qgis as _Qgis

# manual monkey patching for old enum values
Qgs3DTypes.AltitudeClamping = _Qgis.AltitudeClamping
Qgs3DTypes.AltClampAbsolute = _Qgis.AltitudeClamping.Absolute
Qgs3DTypes.AltClampAbsolute.is_monkey_patched = True
Qgs3DTypes.AltClampRelative = _Qgis.AltitudeClamping.Relative
Qgs3DTypes.AltClampRelative.is_monkey_patched = True
Qgs3DTypes.AltClampTerrain = _Qgis.AltitudeClamping.Terrain
Qgs3DTypes.AltClampTerrain.is_monkey_patched = True

Qgs3DTypes.AltitudeBinding = _Qgis.AltitudeBinding
Qgs3DTypes.AltBindVertex = _Qgis.AltitudeBinding.Vertex
Qgs3DTypes.AltBindVertex.is_monkey_patched = True
Qgs3DTypes.AltBindCentroid = _Qgis.AltitudeBinding.Centroid
Qgs3DTypes.AltBindCentroid.is_monkey_patched = True

QgsPoint3DSymbol.Shape = _Qgis.Point3DShape
QgsPoint3DSymbol.Cylinder = _Qgis.Point3DShape.Cylinder
QgsPoint3DSymbol.Cylinder.is_monkey_patched = True
QgsPoint3DSymbol.Sphere = _Qgis.Point3DShape.Sphere
QgsPoint3DSymbol.Sphere.is_monkey_patched = True
QgsPoint3DSymbol.Cone = _Qgis.Point3DShape.Cone
QgsPoint3DSymbol.Cone.is_monkey_patched = True
QgsPoint3DSymbol.Cube = _Qgis.Point3DShape.Cube
QgsPoint3DSymbol.Cube.is_monkey_patched = True
QgsPoint3DSymbol.Torus = _Qgis.Point3DShape.Torus
QgsPoint3DSymbol.Torus.is_monkey_patched = True
QgsPoint3DSymbol.Plane = _Qgis.Point3DShape.Plane
QgsPoint3DSymbol.Plane.is_monkey_patched = True
QgsPoint3DSymbol.ExtrudedText = _Qgis.Point3DShape.ExtrudedText
QgsPoint3DSymbol.ExtrudedText.is_monkey_patched = True
QgsPoint3DSymbol.Model = _Qgis.Point3DShape.Model
QgsPoint3DSymbol.Model.is_monkey_patched = True
QgsPoint3DSymbol.Billboard = _Qgis.Point3DShape.Billboard
QgsPoint3DSymbol.Billboard.is_monkey_patched = True
