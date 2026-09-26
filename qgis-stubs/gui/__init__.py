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
from qgis._gui import *
from qgis.core import Qgis as _Qgis
from .additions.qgssettingsenumflageditorwrapper import PyQgsSettingsEnumEditorWidgetWrapper

"""
This folder is completed using sipify.py script
It is not aimed to be manually edited
"""
# The following has been generated automatically from src/gui/symbology/characterwidget.h
try:
    CharacterWidget.__attribute_docs__ = {'characterSelected': 'Emitted when a character is selected in the widget.\n'}
    CharacterWidget.__overridden_methods__ = ['sizeHint', 'keyPressEvent', 'mouseMoveEvent', 'mousePressEvent', 'paintEvent', 'resizeEvent']
    CharacterWidget.__signal_arguments__ = {'characterSelected': ['character: QChar']}
    CharacterWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgisinterface.h
try:
    QgisInterface.__attribute_docs__ = {'currentLayerChanged': 'Emitted whenever current (selected) layer changes. The pointer to layer\ncan be ``None`` if no layer is selected.\n', 'currentThemeChanged': 'Emitted when the current ``theme`` is changed so plugins can change\ntheir tool button icons.\n', 'layoutDesignerOpened': 'Emitted when a new layout ``designer`` has been opened.\n\n.. seealso:: :py:func:`layoutDesignerWillBeClosed`\n', 'layoutDesignerWillBeClosed': 'Emitted before a layout ``designer`` is going to be closed and deleted.\n\n.. seealso:: :py:func:`layoutDesignerClosed`\n\n.. seealso:: :py:func:`layoutDesignerOpened`\n', 'layoutDesignerClosed': 'Emitted after a layout designer window is closed.\n\n.. seealso:: :py:func:`layoutDesignerWillBeClosed`\n\n.. seealso:: :py:func:`layoutDesignerOpened`\n', 'initializationCompleted': 'Emitted when the initialization is complete.\n', 'projectRead': 'Emitted when a project file is successfully read.\n\n.. note::\n\n   This is useful for plugins that store properties with project files.\n   A plugin can connect to this signal. When it is emitted the plugin\n   knows to then check the project properties for any relevant state.\n', 'newProjectCreated': "Emitted when starting an entirely new project.\n\n.. note::\n\n   This is similar to :py:func:`~QgisInterface.projectRead`; plugins might want to be notified\n   that they're in a new project. Yes, :py:func:`~QgisInterface.projectRead` could have been\n   overloaded to be used in the case of new projects instead. However,\n   it's probably more semantically correct to have an entirely separate\n   signal for when this happens.\n", 'layerSavedAs': 'Emitted when a layer has been saved using save as.\n'}
    QgisInterface.__virtual_methods__ = ['actionCircle2Points', 'actionCircle3Points', 'actionCircle3Tangents', 'actionCircle2TangentsPoint', 'actionCircleCenterPoint', 'actionEllipseCenter2Points', 'actionEllipseCenterPoint', 'actionEllipseExtent', 'actionEllipseFoci', 'actionRectangleCenterPoint', 'actionRectangleExtent', 'actionRectangle3PointsDistance', 'actionRectangle3PointsProjected', 'actionRegularPolygon2Points', 'actionRegularPolygonCenterPoint', 'actionRegularPolygonCenterCorner', 'takeAppScreenShots']
    QgisInterface.__abstract_methods__ = ['pluginManagerInterface', 'layerTreeView', 'gpsTools', 'addCustomActionForLayerType', 'addCustomActionForLayer', 'removeCustomActionForLayerType', 'mapCanvases', 'createNewMapCanvas', 'closeMapCanvas', 'mapCanvases3D', 'createNewMapCanvas3D', 'closeMapCanvas3D', 'iconSize', 'editableLayers', 'activeLayer', 'mapCanvas', 'activeDecorations', 'layerTreeCanvasBridge', 'mainWindow', 'messageBar', 'openLayoutDesigners', 'defaultStyleSheetOptions', 'defaultStyleSheetFont', 'cadDockWidget', 'projectMenu', 'projectImportExportMenu', 'addProjectImportAction', 'removeProjectImportAction', 'addProjectExportAction', 'removeProjectExportAction', 'projectModelsMenu', 'createProjectModelSubMenu', 'editMenu', 'viewMenu', 'layerMenu', 'newLayerMenu', 'addLayerMenu', 'settingsMenu', 'pluginMenu', 'pluginHelpMenu', 'rasterMenu', 'databaseMenu', 'vectorMenu', 'webMenu', 'meshMenu', 'firstRightStandardMenu', 'windowMenu', 'helpMenu', 'fileToolBar', 'layerToolBar', 'dataSourceManagerToolBar', 'openDataSourceManagerPage', 'mapNavToolToolBar', 'digitizeToolBar', 'advancedDigitizeToolBar', 'shapeDigitizeToolBar', 'attributesToolBar', 'selectionToolBar', 'pluginToolBar', 'helpToolBar', 'rasterToolBar', 'vectorToolBar', 'databaseToolBar', 'webToolBar', 'actionNewProject', 'actionOpenProject', 'actionSaveProject', 'actionSaveProjectAs', 'actionSaveMapAsImage', 'actionProjectProperties', 'actionCreatePrintLayout', 'actionShowLayoutManager', 'actionExit', 'actionCutFeatures', 'actionCopyFeatures', 'actionPasteFeatures', 'actionAddFeature', 'actionDeleteSelected', 'actionMoveFeature', 'actionSplitFeatures', 'actionSplitParts', 'actionAddRing', 'actionAddPart', 'actionSimplifyFeature', 'actionDeleteRing', 'actionDeletePart', 'actionVertexTool', 'actionVertexToolActiveLayer', 'mapToolActionGroup', 'actionPan', 'actionPanToSelected', 'actionZoomIn', 'actionZoomOut', 'actionSelect', 'actionSelectRectangle', 'actionSelectPolygon', 'actionSelectFreehand', 'actionSelectRadius', 'actionIdentify', 'actionFeatureAction', 'actionMeasure', 'actionMeasureArea', 'actionZoomFullExtent', 'actionZoomToLayer', 'actionZoomToLayers', 'actionZoomToSelected', 'actionZoomLast', 'actionZoomNext', 'actionZoomActualSize', 'actionMapTips', 'actionNewBookmark', 'actionShowBookmarks', 'actionDraw', 'actionNewVectorLayer', 'actionAddOgrLayer', 'actionAddRasterLayer', 'actionAddPgLayer', 'actionAddWmsLayer', 'actionAddXyzLayer', 'actionAddVectorTileLayer', 'actionAddPointCloudLayer', 'actionAddAfsLayer', 'actionAddAmsLayer', 'actionCopyLayerStyle', 'actionPasteLayerStyle', 'actionOpenTable', 'actionOpenFieldCalculator', 'actionOpenStatisticalSummary', 'actionToggleEditing', 'actionSaveActiveLayerEdits', 'actionAllEdits', 'actionSaveEdits', 'actionSaveAllEdits', 'actionRollbackEdits', 'actionRollbackAllEdits', 'actionCancelEdits', 'actionCancelAllEdits', 'actionLayerSaveAs', 'actionDuplicateLayer', 'actionLayerProperties', 'actionAddToOverview', 'actionAddAllToOverview', 'actionRemoveAllFromOverview', 'actionHideAllLayers', 'actionShowAllLayers', 'actionHideSelectedLayers', 'actionToggleSelectedLayers', 'actionToggleSelectedLayersIndependently', 'actionHideDeselectedLayers', 'actionShowSelectedLayers', 'actionManagePlugins', 'actionPluginListSeparator', 'actionShowPythonDialog', 'actionToggleFullScreen', 'actionOptions', 'actionCustomProjection', 'actionHelpContents', 'actionQgisHomePage', 'actionCheckQgisVersion', 'actionAbout', 'vectorLayerTools', 'messageTimeout', 'statusBarIface', 'layerTreeInsertionPoint', 'userProfileManager', 'zoomFull', 'zoomToPrevious', 'zoomToNext', 'zoomToActiveLayer', 'addVectorLayer', 'addRasterLayer', 'addMeshLayer', 'addVectorTileLayer', 'addPointCloudLayer', 'addTiledSceneLayer', 'addProject', 'newProject', 'reloadConnections', 'setActiveLayer', 'copySelectionToClipboard', 'pasteFromClipboard', 'addToolBarIcon', 'addToolBarWidget', 'removeToolBarIcon', 'addRasterToolBarWidget', 'addRasterToolBarIcon', 'removeRasterToolBarIcon', 'addVectorToolBarIcon', 'addVectorToolBarWidget', 'removeVectorToolBarIcon', 'addDatabaseToolBarIcon', 'addDatabaseToolBarWidget', 'removeDatabaseToolBarIcon', 'addWebToolBarIcon', 'addWebToolBarWidget', 'removeWebToolBarIcon', 'addToolBar', 'openMessageLog', 'addUserInputWidget', 'showLayoutManager', 'openLayoutDesigner', 'showOptionsDialog', 'showProjectPropertiesDialog', 'buildStyleSheet', 'saveStyleSheetOptions', 'addPluginToMenu', 'removePluginMenu', 'insertAddLayerAction', 'removeAddLayerAction', 'addPluginToDatabaseMenu', 'removePluginDatabaseMenu', 'addPluginToRasterMenu', 'removePluginRasterMenu', 'addPluginToVectorMenu', 'removePluginVectorMenu', 'addPluginToWebMenu', 'removePluginWebMenu', 'addPluginToMeshMenu', 'removePluginMeshMenu', 'addDockWidget', 'addTabifiedDockWidget', 'removeDockWidget', 'showLayerProperties', 'showAttributeTable', 'addWindow', 'removeWindow', 'registerMainWindowAction', 'unregisterMainWindowAction', 'registerMapLayerConfigWidgetFactory', 'unregisterMapLayerConfigWidgetFactory', 'registerOptionsWidgetFactory', 'unregisterOptionsWidgetFactory', 'registerProjectPropertiesWidgetFactory', 'unregisterProjectPropertiesWidgetFactory', 'registerDevToolWidgetFactory', 'unregisterDevToolWidgetFactory', 'showApiDocumentation', 'registerApplicationExitBlocker', 'unregisterApplicationExitBlocker', 'registerMapToolHandler', 'unregisterMapToolHandler', 'registerCustomDropHandler', 'unregisterCustomDropHandler', 'registerCustomProjectOpenHandler', 'unregisterCustomProjectOpenHandler', 'registerCustomLayoutDropHandler', 'unregisterCustomLayoutDropHandler', 'openURL', 'openFeatureForm', 'getFeatureForm', 'preloadForm', 'locatorSearch', 'registerLocatorFilter', 'deregisterLocatorFilter', 'invalidateLocatorResults', 'askForDatumTransform', 'browserModel', 'setGpsPanelConnection', 'blockActiveLayerChanges']
    QgisInterface.__signal_arguments__ = {'currentLayerChanged': ['layer: QgsMapLayer'], 'currentThemeChanged': ['theme: str'], 'layoutDesignerOpened': ['designer: QgsLayoutDesignerInterface'], 'layoutDesignerWillBeClosed': ['designer: QgsLayoutDesignerInterface'], 'layerSavedAs': ['l: QgsMapLayer', 'path: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgs25drendererwidget.h
try:
    Qgs25DRendererWidget.create = staticmethod(Qgs25DRendererWidget.create)
    Qgs25DRendererWidget.__overridden_methods__ = ['renderer', 'apply']
    Qgs25DRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/inputcontroller/qgs2dgamepadcontroller.h
try:
    QgsGamepad2DMapController.__attribute_docs__ = {'connectedChanged': 'Emitted when the connection state of the gamepad is changed.\n', 'axisLeftXChanged': "Emitted when the value of the left thumbstick's X axis is changed.\n\n.. seealso:: :py:func:`axisLeftX`\n", 'axisLeftYChanged': "Emitted when the value of the left thumbstick's Y axis is changed.\n\n.. seealso:: :py:func:`axisLeftY`\n", 'axisRightXChanged': "Emitted when the value of the right thumbstick's X axis is changed.\n\n.. seealso:: :py:func:`axisRightX`\n", 'axisRightYChanged': "Emitted when the value of the right thumbstick's Y axis is changed.\n\n.. seealso:: :py:func:`axisRightY`\n", 'buttonAChanged': 'Emitted when the state of the A button is changed.\n\n.. seealso:: :py:func:`buttonA`\n', 'buttonBChanged': 'Emitted when the state of the B button is changed.\n\n.. seealso:: :py:func:`buttonB`\n', 'buttonXChanged': 'Emitted when the state of the X button is changed.\n\n.. seealso:: :py:func:`buttonX`\n', 'buttonYChanged': 'Emitted when the state of the Y button is changed.\n\n.. seealso:: :py:func:`buttonY`\n', 'buttonL1Changed': 'Emitted when the state of the left shoulder button is changed.\n\n.. seealso:: :py:func:`buttonL1`\n', 'buttonR1Changed': 'Emitted when the state of the right shoulder button is changed.\n\n.. seealso:: :py:func:`buttonR1`\n', 'buttonL2Changed': 'Emitted when the state of the left trigger button is changed.\n\n.. seealso:: :py:func:`buttonL2`\n', 'buttonR2Changed': 'Emitted when the state of the right trigger button is changed.\n\n.. seealso:: :py:func:`buttonR2`\n', 'buttonSelectChanged': 'Emitted when the state of the select button is changed.\n\n.. seealso:: :py:func:`buttonSelect`\n', 'buttonStartChanged': 'Emitted when the state of the start button is changed.\n\n.. seealso:: :py:func:`buttonStart`\n', 'buttonL3Changed': 'Emitted when the state of the left stick button is changed.\n\n.. seealso:: :py:func:`buttonL3`\n', 'buttonR3Changed': 'Emitted when the state of the right stick button is changed.\n\n.. seealso:: :py:func:`buttonR3`\n', 'buttonUpChanged': 'Emitted when the state of the direction pad up button is changed.\n\n.. seealso:: :py:func:`buttonUp`\n', 'buttonDownChanged': 'Emitted when the state of the direction pad down button is changed.\n\n.. seealso:: :py:func:`buttonDown`\n', 'buttonLeftChanged': 'Emitted when the state of the direction pad left button is changed.\n\n.. seealso:: :py:func:`buttonLeft`\n', 'buttonRightChanged': 'Emitted when the state of the direction pad right button is changed.\n\n.. seealso:: :py:func:`buttonRight`\n', 'buttonCenterChanged': 'Emitted when the state of the center button is changed.\n\n.. seealso:: :py:func:`buttonCenter`\n', 'buttonGuideChanged': 'Emitted when the state of the guide button is changed.\n\n.. seealso:: :py:func:`buttonCenter`\n'}
    QgsGamepad2DMapController.__overridden_methods__ = ['clone', 'deviceId']
    QgsGamepad2DMapController.__signal_arguments__ = {'connectedChanged': ['value: bool'], 'axisLeftXChanged': ['value: float'], 'axisLeftYChanged': ['value: float'], 'axisRightXChanged': ['value: float'], 'axisRightYChanged': ['value: float'], 'buttonAChanged': ['value: bool'], 'buttonBChanged': ['value: bool'], 'buttonXChanged': ['value: bool'], 'buttonYChanged': ['value: bool'], 'buttonL1Changed': ['value: bool'], 'buttonR1Changed': ['value: bool'], 'buttonL2Changed': ['value: float'], 'buttonR2Changed': ['value: float'], 'buttonSelectChanged': ['value: bool'], 'buttonStartChanged': ['value: bool'], 'buttonL3Changed': ['value: bool'], 'buttonR3Changed': ['value: bool'], 'buttonUpChanged': ['value: bool'], 'buttonDownChanged': ['value: bool'], 'buttonLeftChanged': ['value: bool'], 'buttonRightChanged': ['value: bool'], 'buttonCenterChanged': ['value: bool'], 'buttonGuideChanged': ['value: bool']}
    QgsGamepad2DMapController.__group__ = ['inputcontroller']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/inputcontroller/qgs2dmapcontroller.h
try:
    QgsAbstract2DMapController.__overridden_methods__ = ['type']
    QgsAbstract2DMapController.__group__ = ['inputcontroller']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/inputcontroller/qgs3dgamepadcontroller.h
try:
    QgsGamepad3DMapController.__attribute_docs__ = {'connectedChanged': 'Emitted when the connection state of the gamepad is changed.\n', 'axisLeftXChanged': "Emitted when the value of the left thumbstick's X axis is changed.\n\n.. seealso:: :py:func:`axisLeftX`\n", 'axisLeftYChanged': "Emitted when the value of the left thumbstick's Y axis is changed.\n\n.. seealso:: :py:func:`axisLeftY`\n", 'axisRightXChanged': "Emitted when the value of the right thumbstick's X axis is changed.\n\n.. seealso:: :py:func:`axisRightX`\n", 'axisRightYChanged': "Emitted when the value of the right thumbstick's Y axis is changed.\n\n.. seealso:: :py:func:`axisRightY`\n", 'buttonAChanged': 'Emitted when the state of the A button is changed.\n\n.. seealso:: :py:func:`buttonA`\n', 'buttonBChanged': 'Emitted when the state of the B button is changed.\n\n.. seealso:: :py:func:`buttonB`\n', 'buttonXChanged': 'Emitted when the state of the X button is changed.\n\n.. seealso:: :py:func:`buttonX`\n', 'buttonYChanged': 'Emitted when the state of the Y button is changed.\n\n.. seealso:: :py:func:`buttonY`\n', 'buttonL1Changed': 'Emitted when the state of the left shoulder button is changed.\n\n.. seealso:: :py:func:`buttonL1`\n', 'buttonR1Changed': 'Emitted when the state of the right shoulder button is changed.\n\n.. seealso:: :py:func:`buttonR1`\n', 'buttonL2Changed': 'Emitted when the state of the left trigger button is changed.\n\n.. seealso:: :py:func:`buttonL2`\n', 'buttonR2Changed': 'Emitted when the state of the right trigger button is changed.\n\n.. seealso:: :py:func:`buttonR2`\n', 'buttonSelectChanged': 'Emitted when the state of the select button is changed.\n\n.. seealso:: :py:func:`buttonSelect`\n', 'buttonStartChanged': 'Emitted when the state of the start button is changed.\n\n.. seealso:: :py:func:`buttonStart`\n', 'buttonL3Changed': 'Emitted when the state of the left stick button is changed.\n\n.. seealso:: :py:func:`buttonL3`\n', 'buttonR3Changed': 'Emitted when the state of the right stick button is changed.\n\n.. seealso:: :py:func:`buttonR3`\n', 'buttonUpChanged': 'Emitted when the state of the direction pad up button is changed.\n\n.. seealso:: :py:func:`buttonUp`\n', 'buttonDownChanged': 'Emitted when the state of the direction pad down button is changed.\n\n.. seealso:: :py:func:`buttonDown`\n', 'buttonLeftChanged': 'Emitted when the state of the direction pad left button is changed.\n\n.. seealso:: :py:func:`buttonLeft`\n', 'buttonRightChanged': 'Emitted when the state of the direction pad right button is changed.\n\n.. seealso:: :py:func:`buttonRight`\n', 'buttonCenterChanged': 'Emitted when the state of the center button is changed.\n\n.. seealso:: :py:func:`buttonCenter`\n', 'buttonGuideChanged': 'Emitted when the state of the guide button is changed.\n\n.. seealso:: :py:func:`buttonCenter`\n'}
    QgsGamepad3DMapController.__overridden_methods__ = ['clone', 'deviceId']
    QgsGamepad3DMapController.__signal_arguments__ = {'connectedChanged': ['value: bool'], 'axisLeftXChanged': ['value: float'], 'axisLeftYChanged': ['value: float'], 'axisRightXChanged': ['value: float'], 'axisRightYChanged': ['value: float'], 'buttonAChanged': ['value: bool'], 'buttonBChanged': ['value: bool'], 'buttonXChanged': ['value: bool'], 'buttonYChanged': ['value: bool'], 'buttonL1Changed': ['value: bool'], 'buttonR1Changed': ['value: bool'], 'buttonL2Changed': ['value: float'], 'buttonR2Changed': ['value: float'], 'buttonSelectChanged': ['value: bool'], 'buttonStartChanged': ['value: bool'], 'buttonL3Changed': ['value: bool'], 'buttonR3Changed': ['value: bool'], 'buttonUpChanged': ['value: bool'], 'buttonDownChanged': ['value: bool'], 'buttonLeftChanged': ['value: bool'], 'buttonRightChanged': ['value: bool'], 'buttonCenterChanged': ['value: bool'], 'buttonGuideChanged': ['value: bool']}
    QgsGamepad3DMapController.__group__ = ['inputcontroller']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/inputcontroller/qgs3dmapcontroller.h
try:
    QgsAbstract3DMapController.__overridden_methods__ = ['type']
    QgsAbstract3DMapController.__group__ = ['inputcontroller']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgs3dsymbolwidget.h
try:
    Qgs3DSymbolWidget.__attribute_docs__ = {'changed': 'Emitted when the symbol is changed.\n'}
    Qgs3DSymbolWidget.__abstract_methods__ = ['setSymbol', 'symbol', 'symbolType']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsabstractdatasourcewidget.h
try:
    QgsAbstractDataSourceWidget.__attribute_docs__ = {'connectionsChanged': "Emitted when the provider's connections have changed This signal is\nnormally forwarded the app and used to refresh browser items\n", 'addDatabaseLayers': 'Emitted when a DB layer has been selected for addition\n', 'addRasterLayer': 'Emitted when a raster layer has been selected for addition\n\n.. deprecated:: 3.40\n\n   Use :py:func:`~QgsAbstractDataSourceWidget.addLayer` instead.\n', 'addRasterLayers': 'Emitted when one or more GDAL supported layers are selected for addition\n\n:param layersList: list of layers protocol URIs\n\n.. versionadded:: 3.20\n', 'addVectorLayer': 'Emitted when a vector layer has been selected for addition.\n\nIf ``providerKey`` is not specified, the default provider key associated\nwith the source will be used.\n\n.. deprecated:: 3.40\n\n   Use :py:func:`~QgsAbstractDataSourceWidget.addLayer` instead.\n', 'addMeshLayer': 'Emitted when a mesh layer has been selected for addition.\n\n.. deprecated:: 3.40\n\n   Use :py:func:`~QgsAbstractDataSourceWidget.addLayer` instead.\n', 'addVectorTileLayer': 'Emitted when a vector tile layer has been selected for addition.\n\n.. deprecated:: 3.40\n\n   Use :py:func:`~QgsAbstractDataSourceWidget.addLayer` instead.\n', 'addPointCloudLayer': 'Emitted when a point cloud layer has been selected for addition.\n\n.. deprecated:: 3.40\n\n   Use :py:func:`~QgsAbstractDataSourceWidget.addLayer` instead.\n', 'addLayer': 'Emitted when a layer has been selected for addition.\n\nThis is a generic method, intended for replacing the specific layer type\nsignals implemented above.\n\n.. warning::\n\n   For QGIS versions < 4.x, the specific layer type added signals must be emitted for vector, raster,\n   mesh, vector tile and point cloud layers in addition to this signal.\n\n.. versionadded:: 3.34\n', 'addVectorLayers': 'Emitted when one or more OGR supported layers are selected for addition\n\n:param layerList: list of layers protocol URIs\n:param encoding: encoding\n:param dataSourceType: string (can be "file" or "database")\n', 'replaceVectorLayer': 'Emitted when a layer needs to be replaced\n\n:param oldId: old layer ID\n:param source: URI of the layer\n:param name: of the layer\n:param provider: key\n', 'progress': 'Emitted when a progress dialog is shown by the provider dialog.\n\n.. deprecated:: 3.4\n\n   This signal is no longer used. Use :py:class:`QgsProxyProgressTask` instead to show progress reports.\n', 'progressMessage': 'Emitted when a progress dialog is shown by the provider dialog\n', 'enableButtons': 'Emitted when the ok/add buttons should be enabled/disabled\n', 'pushMessage': 'Emitted when a ``message`` with ``title`` and ``level`` must be shown to\nthe user using the parent visible message bar\n\n.. versionadded:: 3.14\n'}
    QgsAbstractDataSourceWidget.__virtual_methods__ = ['setBrowserModel', 'mapCanvas', 'setMapCanvas', 'refresh', 'addButtonClicked', 'reset', 'configureFromUri']
    QgsAbstractDataSourceWidget.__signal_arguments__ = {'addDatabaseLayers': ['paths: List[str]', 'providerKey: str'], 'addRasterLayers': ['layersList: List[str]'], 'addLayer': ['type: Qgis.LayerType', 'url: str', 'baseName: str', 'providerKey: str'], 'addVectorLayers': ['layerList: List[str]', 'encoding: str', 'dataSourceType: str'], 'replaceVectorLayer': ['oldId: str', 'source: str', 'name: str', 'provider: str'], 'progressMessage': ['message: str'], 'enableButtons': ['enable: bool'], 'pushMessage': ['title: str', 'message: str', 'level: Qgis.MessageLevel = Qgis.MessageLevel.Info']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/providers/qgsabstractdbsourceselect.h
try:
    QgsAbstractDbSourceSelect.__virtual_methods__ = ['settingPath', 'treeviewClicked', 'treeviewDoubleClicked']
    QgsAbstractDbSourceSelect.__abstract_methods__ = ['setSql']
    QgsAbstractDbSourceSelect.__group__ = ['providers']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/inputcontroller/qgsabstractinputcontroller.h
try:
    QgsAbstractInputController.__abstract_methods__ = ['clone', 'deviceId', 'type']
    QgsAbstractInputController.__group__ = ['inputcontroller']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsabstractmaptoolhandler.h
try:
    QgsAbstractMapToolHandler.Context.__attribute_docs__ = {'dummy': 'Placeholder only'}
    QgsAbstractMapToolHandler.Context.__annotations__ = {'dummy': bool}
    QgsAbstractMapToolHandler.Context.__doc__ = """Context of a QgsAbstractMapToolHandler call.

.. versionadded:: 3.16"""
except (NameError, AttributeError):
    pass
try:
    QgsAbstractMapToolHandler.__virtual_methods__ = ['setLayerForTool']
    QgsAbstractMapToolHandler.__abstract_methods__ = ['isCompatibleWithLayer']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsabstractrelationeditorwidget.h
try:
    QgsAbstractRelationEditorWidget.__attribute_docs__ = {'relatedFeaturesChanged': 'Emit this signal, whenever the related features changed. This happens\nfor example when related features are added, removed, linked or\nunlinked.\n\n.. versionadded:: 3.22\n'}
    QgsAbstractRelationEditorWidget.__virtual_methods__ = ['setEditorContext', 'updateUi', 'setTitle', 'beforeSetRelationFeature', 'afterSetRelationFeature', 'beforeSetRelations', 'afterSetRelations']
    QgsAbstractRelationEditorWidget.__abstract_methods__ = ['config', 'setConfig', 'parentFormValueChanged']
except (NameError, AttributeError):
    pass
try:
    QgsAbstractRelationEditorConfigWidget.__virtual_methods__ = ['setNmRelation', 'nmRelation']
    QgsAbstractRelationEditorConfigWidget.__abstract_methods__ = ['config', 'setConfig']
except (NameError, AttributeError):
    pass
try:
    QgsAbstractRelationEditorWidgetFactory.__abstract_methods__ = ['type', 'name', 'create', 'configWidget']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/actions/qgsactionmenu.h
try:
    QgsActionMenu.__attribute_docs__ = {'reinit': 'Emitted after actions have been reloaded.\n'}
    QgsActionMenu.__group__ = ['actions']
except (NameError, AttributeError):
    pass
try:
    QgsActionMenu.ActionData.__group__ = ['actions']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsactionwidgetwrapper.h
try:
    QgsActionWidgetWrapper.__overridden_methods__ = ['valid', 'createWidget', 'initWidget', 'setFeature', 'setEnabled']
    QgsActionWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsadvanceddigitizingcanvasitem.h
try:
    QgsAdvancedDigitizingCanvasItem.__overridden_methods__ = ['paint', 'updatePosition']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsadvanceddigitizingdockwidget.h
QgsAdvancedDigitizingDockWidget.CadCapacities.baseClass = QgsAdvancedDigitizingDockWidget
CadCapacities = QgsAdvancedDigitizingDockWidget  # dirty hack since SIP seems to introduce the flags in module
try:
    QgsAdvancedDigitizingDockWidget.__attribute_docs__ = {'pushWarning': 'Push a warning\n\n:param message: An informative message\n', 'popWarning': 'Remove any previously emitted warnings (if any)\n', 'pointChangedV2': 'Sometimes a constraint may change the current point out of a mouse\nevent. This happens normally when a constraint is toggled.\n\n:param point: The last known digitizing point. Can be used to emulate a\n              mouse event.\n\n.. versionadded:: 3.22\n', 'pointChanged': 'Sometimes a constraint may change the current point out of a mouse\nevent. This happens normally when a constraint is toggled.\n\n:param point: The last known digitizing point. Can be used to emulate a\n              mouse event.\n\n.. deprecated:: 3.22\n\n   No longer used, will be removed in QGIS 4.0. Use :py:func:`~QgsAdvancedDigitizingDockWidget.pointChangedV2` instead.\n', 'cadEnabledChanged': 'Emitted whenever CAD is enabled or disabled\n\n:param enabled: Whether CAD is enabled or not\n\n.. note::\n\n   unstable API (will likely change).\n\n.. versionadded:: 3.8\n', 'valueXChanged': 'Emitted whenever the X ``value`` changes (either the mouse moved, or the\nuser changed the input). Could be used by widgets that must reflect the\ncurrent advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'valueYChanged': 'Emitted whenever the Y ``value`` changes (either the mouse moved, or the\nuser changed the input). Could be used by widgets that must reflect the\ncurrent advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'valueZChanged': 'Emitted whenever the Z ``value`` changes (either the mouse moved, or the\nuser changed the input). Could be used by widgets that must reflect the\ncurrent advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.22\n', 'valueMChanged': 'Emitted whenever the M ``value`` changes (either the mouse moved, or the\nuser changed the input). Could be used by widgets that must reflect the\ncurrent advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.22\n', 'valueAngleChanged': 'Emitted whenever the angle ``value`` changes (either the mouse moved, or\nthe user changed the input). Could be used by widgets that must reflect\nthe current advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'valueDistanceChanged': 'Emitted whenever the distance ``value`` changes (either the mouse moved,\nor the user changed the input). Could be used by widgets that must\nreflect the current advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'valueBearingChanged': 'Emitted whenever the bearing ``value`` changes. Could be used by widgets\nthat must reflect the current advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.32\n', 'lockXChanged': 'Emitted whenever the X parameter is ``locked``. Could be used by widgets\nthat must reflect the current advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'lockYChanged': 'Emitted whenever the Y parameter is ``locked``. Could be used by widgets\nthat must reflect the current advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'lockZChanged': 'Emitted whenever the Z parameter is ``locked``. Could be used by widgets\nthat must reflect the current advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.22\n', 'lockMChanged': 'Emitted whenever the M parameter is ``locked``. Could be used by widgets\nthat must reflect the current advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.22\n', 'lockAngleChanged': 'Emitted whenever the angle parameter is ``locked``. Could be used by\nwidgets that must reflect the current advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'lockDistanceChanged': 'Emitted whenever the distance parameter is ``locked``. Could be used by\nwidgets that must reflect the current advanced digitizing state.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'relativeXChanged': 'Emitted whenever the X parameter is toggled between absolute and\nrelative. Could be used by widgets that must reflect the current\nadvanced digitizing state.\n\n:param relative: Whether the X parameter is relative or not.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'relativeYChanged': 'Emitted whenever the Y parameter is toggled between absolute and\nrelative. Could be used by widgets that must reflect the current\nadvanced digitizing state.\n\n:param relative: Whether the Y parameter is relative or not.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'relativeZChanged': 'Emitted whenever the Z parameter is toggled between absolute and\nrelative. Could be used by widgets that must reflect the current\nadvanced digitizing state.\n\n:param relative: Whether the Z parameter is relative or not.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.22\n', 'relativeMChanged': 'Emitted whenever the M parameter is toggled between absolute and\nrelative. Could be used by widgets that must reflect the current\nadvanced digitizing state.\n\n:param relative: Whether the M parameter is relative or not.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.22\n', 'relativeAngleChanged': 'Emitted whenever the angleX parameter is toggled between absolute and\nrelative. Could be used by widgets that must reflect the current\nadvanced digitizing state.\n\n:param relative: Whether the angle parameter is relative or not.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'softLockLineExtensionChanged': 'Emitted whenever the soft line extension parameter is ``locked``. Could\nbe used by widgets that must reflect the current advanced digitizing\nstate.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.26\n', 'softLockXyChanged': 'Emitted whenever the soft x/y extension parameter is ``locked``. Could\nbe used by widgets that must reflect the current advanced digitizing\nstate.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.26\n', 'enabledChangedX': 'Emitted whenever the X field is enabled or disabled. Depending on the\ncontext, some parameters do not make sense (e.g. you need a previous\npoint to define a distance). Could be used by widgets that must reflect\nthe current advanced digitizing state.\n\n:param enabled: Whether the X parameter is enabled or not.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'enabledChangedY': 'Emitted whenever the Y field is enabled or disabled. Depending on the\ncontext, some parameters do not make sense (e.g. you need a previous\npoint to define a distance). Could be used by widgets that must reflect\nthe current advanced digitizing state.\n\n:param enabled: Whether the Y parameter is enabled or not.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'enabledChangedZ': 'Emitted whenever the Z field is enabled or disabled. Depending on the\ncontext, some parameters do not make sense (e.g. you need a previous\npoint to define a distance). Could be used by widgets that must reflect\nthe current advanced digitizing state.\n\n:param enabled: Whether the Z parameter is enabled or not.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.22\n', 'enabledChangedM': 'Emitted whenever the M field is enabled or disabled. Depending on the\ncontext, some parameters do not make sense (e.g. you need a previous\npoint to define a distance). Could be used by widgets that must reflect\nthe current advanced digitizing state.\n\n:param enabled: Whether the M parameter is enabled or not.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.22\n', 'enabledChangedAngle': 'Emitted whenever the angle field is enabled or disabled. Depending on\nthe context, some parameters do not make sense (e.g. you need a previous\npoint to define a distance). Could be used by widgets that must reflect\nthe current advanced digitizing state.\n\n:param enabled: Whether the angle parameter is enabled or not.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'enabledChangedDistance': 'Emitted whenever the distance field is enabled or disabled. Depending on\nthe context, some parameters do not make sense (e.g. you need a previous\npoint to define a distance). Could be used by widgets that must reflect\nthe current advanced digitizing state.\n\n:param enabled: Whether the distance parameter is enabled or not.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'focusOnXRequested': 'Emitted whenever the X field should get the focus using the shortcuts\n(X). Could be used by widgets to capture the focus when a field is being\nedited.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'focusOnYRequested': 'Emitted whenever the Y field should get the focus using the shortcuts\n(Y). Could be used by widgets to capture the focus when a field is being\nedited.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'focusOnZRequested': 'Emitted whenever the Z field should get the focus using the shortcuts\n(Z). Could be used by widgets to capture the focus when a field is being\nedited.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.22\n', 'focusOnMRequested': 'Emitted whenever the M field should get the focus using the shortcuts\n(M). Could be used by widgets to capture the focus when a field is being\nedited.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.22\n', 'focusOnAngleRequested': 'Emitted whenever the angle field should get the focus using the\nshortcuts (A). Could be used by widgets to capture the focus when a\nfield is being edited.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'focusOnDistanceRequested': 'Emitted whenever the distance field should get the focus using the\nshortcuts (D). Could be used by widgets to capture the focus when a\nfield is being edited.\n\n.. note::\n\n   unstable API (will likely change)\n\n.. versionadded:: 3.8\n', 'valueCommonAngleSnappingChanged': 'Emitted whenever the snapping to common angle option changes, angle = 0\nmeans that the functionality is disabled.\n\n.. versionadded:: 3.32\n'}
    QgsAdvancedDigitizingDockWidget.__overridden_methods__ = ['keyPressEvent']
    QgsAdvancedDigitizingDockWidget.__signal_arguments__ = {'pushWarning': ['message: str'], 'pointChangedV2': ['point: QgsPoint'], 'cadEnabledChanged': ['enabled: bool'], 'valueXChanged': ['value: str'], 'valueYChanged': ['value: str'], 'valueZChanged': ['value: str'], 'valueMChanged': ['value: str'], 'valueAngleChanged': ['value: str'], 'valueDistanceChanged': ['value: str'], 'valueBearingChanged': ['value: str'], 'lockXChanged': ['locked: bool'], 'lockYChanged': ['locked: bool'], 'lockZChanged': ['locked: bool'], 'lockMChanged': ['locked: bool'], 'lockAngleChanged': ['locked: bool'], 'lockDistanceChanged': ['locked: bool'], 'relativeXChanged': ['relative: bool'], 'relativeYChanged': ['relative: bool'], 'relativeZChanged': ['relative: bool'], 'relativeMChanged': ['relative: bool'], 'relativeAngleChanged': ['relative: bool'], 'softLockLineExtensionChanged': ['locked: bool'], 'softLockXyChanged': ['locked: bool'], 'enabledChangedX': ['enabled: bool'], 'enabledChangedY': ['enabled: bool'], 'enabledChangedZ': ['enabled: bool'], 'enabledChangedM': ['enabled: bool'], 'enabledChangedAngle': ['enabled: bool'], 'enabledChangedDistance': ['enabled: bool'], 'valueCommonAngleSnappingChanged': ['angle: float']}
except (NameError, AttributeError):
    pass
try:
    QgsAdvancedDigitizingDockWidget.CadConstraint.removeSuffix = staticmethod(QgsAdvancedDigitizingDockWidget.CadConstraint.removeSuffix)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsadvanceddigitizingfloater.h
# monkey patching scoped based enum
QgsAdvancedDigitizingFloater.FloaterItem.XCoordinate.__doc__ = ""
QgsAdvancedDigitizingFloater.FloaterItem.YCoordinate.__doc__ = ""
QgsAdvancedDigitizingFloater.FloaterItem.MCoordinate.__doc__ = ""
QgsAdvancedDigitizingFloater.FloaterItem.ZCoordinate.__doc__ = ""
QgsAdvancedDigitizingFloater.FloaterItem.Angle.__doc__ = ""
QgsAdvancedDigitizingFloater.FloaterItem.CommonAngleSnapping.__doc__ = ""
QgsAdvancedDigitizingFloater.FloaterItem.Distance.__doc__ = ""
QgsAdvancedDigitizingFloater.FloaterItem.Bearing.__doc__ = ""
QgsAdvancedDigitizingFloater.FloaterItem.__doc__ = """Available floater items

* ``XCoordinate``: 
* ``YCoordinate``: 
* ``MCoordinate``: 
* ``ZCoordinate``: 
* ``Angle``: 
* ``CommonAngleSnapping``: 
* ``Distance``: 
* ``Bearing``: 

"""
# --
QgsAdvancedDigitizingFloater.FloaterItem.baseClass = QgsAdvancedDigitizingFloater
FloaterItem = QgsAdvancedDigitizingFloater  # dirty hack since SIP seems to introduce the flags in module
try:
    QgsAdvancedDigitizingFloater.__overridden_methods__ = ['eventFilter']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsadvanceddigitizingtools.h
try:
    QgsAdvancedDigitizingTool.__attribute_docs__ = {'paintRequested': 'Requests a new painting event to the advanced digitizing canvas item.\n'}
    QgsAdvancedDigitizingTool.__virtual_methods__ = ['createWidget', 'paint', 'canvasPressEvent', 'canvasMoveEvent', 'canvasReleaseEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsadvanceddigitizingtoolsregistry.h
try:
    QgsAdvancedDigitizingToolAbstractMetadata.__virtual_methods__ = ['createTool']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsaggregatetoolbutton.h
try:
    QgsAggregateToolButton.__attribute_docs__ = {'aggregateChanged': 'The function name of the selected aggregate has changed.\n', 'activeChanged': 'A function has been selected or deselected.\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsalignmentcombobox.h
try:
    QgsAlignmentComboBox.__attribute_docs__ = {'changed': 'Emitted when the alignment is changed.\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/annotations/qgsannotationitemcommonpropertieswidget.h
try:
    QgsAnnotationItemCommonPropertiesWidget.__attribute_docs__ = {'itemChanged': 'Emitted when the annotation item definition in the widget is changed by\nthe user.\n'}
    QgsAnnotationItemCommonPropertiesWidget.__group__ = ['annotations']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/annotations/qgsannotationitemguiregistry.h
try:
    QgsAnnotationItemGuiGroup.__attribute_docs__ = {'id': 'Unique (untranslated) group ID string.', 'name': 'Translated group name.', 'icon': 'Icon for group.'}
    QgsAnnotationItemGuiGroup.__annotations__ = {'id': str, 'name': str, 'icon': 'QIcon'}
    QgsAnnotationItemGuiGroup.__group__ = ['annotations']
except (NameError, AttributeError):
    pass
try:
    QgsAnnotationItemGuiRegistry.__attribute_docs__ = {'typeAdded': 'Emitted whenever a new item type is added to the registry, with the\nspecified ``metadataId``.\n'}
    QgsAnnotationItemGuiRegistry.__signal_arguments__ = {'typeAdded': ['metadataId: int']}
    QgsAnnotationItemGuiRegistry.__group__ = ['annotations']
except (NameError, AttributeError):
    pass
try:
    QgsAnnotationItemAbstractGuiMetadata.__virtual_methods__ = ['creationIcon', 'createItemWidget', 'createMapTool', 'createItem', 'newItemAddedToLayer']
    QgsAnnotationItemAbstractGuiMetadata.__group__ = ['annotations']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/annotations/qgsannotationitemwidget.h
try:
    QgsAnnotationItemBaseWidget.__attribute_docs__ = {'itemChanged': 'Emitted when the annotation item definition in the widget is changed by\nthe user.\n'}
    QgsAnnotationItemBaseWidget.__virtual_methods__ = ['setLayer', 'setContext', 'focusDefaultWidget', 'setNewItem']
    QgsAnnotationItemBaseWidget.__abstract_methods__ = ['createItem', 'updateItem']
    QgsAnnotationItemBaseWidget.__group__ = ['annotations']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsapplicationexitblockerinterface.h
try:
    QgsApplicationExitBlockerInterface.__abstract_methods__ = ['allowExit']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsarrowsymbollayerwidget.h
try:
    QgsArrowSymbolLayerWidget.create = staticmethod(QgsArrowSymbolLayerWidget.create)
    QgsArrowSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsArrowSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsattributedialog.h
try:
    QgsAttributeDialog.__overridden_methods__ = ['event', 'showEvent', 'createActionContext', 'accept', 'reject']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsattributeeditorcontext.h
QgsAttributeEditorContext.Mode.baseClass = QgsAttributeEditorContext
# The following has been generated automatically from src/gui/qgsattributeform.h
try:
    QgsAttributeForm.__attribute_docs__ = {'attributeChanged': 'Notifies about changes of attributes, this signal is not emitted when\nthe value is set back to the original one.\n\n:param attribute: The name of the attribute that changed.\n:param value: The new value of the attribute.\n\n.. deprecated:: 3.0\n', 'widgetValueChanged': 'Notifies about changes of attributes\n\n:param attribute: The name of the attribute that changed.\n:param value: The new value of the attribute.\n:param attributeChanged: If ``True``, it corresponds to an actual change\n                         of the feature attribute\n', 'featureSaved': 'Emitted when a feature is changed or added\n', 'filterExpressionSet': 'Emitted when a filter expression is set using the form.\n\n:param expression: filter expression\n:param type: filter type\n', 'modeChanged': 'Emitted when the form changes mode.\n\n:param mode: new mode\n', 'closed': "Emitted when the user selects the close option from the form's button\nbar.\n", 'zoomToFeatures': 'Emitted when the user chooses to zoom to a filtered set of features.\n', 'flashFeatures': 'Emitted when the user chooses to flash a filtered set of features.\n', 'openFilteredFeaturesAttributeTable': 'Emitted when the user chooses to open the attribute table dialog with a\nfiltered set of features.\n\n.. versionadded:: 3.24\n'}
    QgsAttributeForm.__overridden_methods__ = ['eventFilter']
    QgsAttributeForm.__signal_arguments__ = {'widgetValueChanged': ['attribute: str', 'value: object', 'attributeChanged: bool'], 'featureSaved': ['feature: QgsFeature'], 'filterExpressionSet': ['expression: str', 'type: QgsAttributeForm.FilterType'], 'modeChanged': ['mode: QgsAttributeEditorContext.Mode'], 'zoomToFeatures': ['filter: str'], 'flashFeatures': ['filter: str'], 'openFilteredFeaturesAttributeTable': ['filter: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsattributeformeditorwidget.h
try:
    QgsAttributeFormEditorWidget.__attribute_docs__ = {'valueChanged': "Emitted when the widget's value changes\n\n:param value: new widget value\n\n.. deprecated:: 3.10\n\n   Use :py:func:`~QgsAttributeFormEditorWidget.valuesChanged` instead.\n", 'valuesChanged': "Emitted when the widget's value changes\n\n:param value: new widget value\n:param additionalFieldValues: of the potential additional fields\n\n.. versionadded:: 3.10\n"}
    QgsAttributeFormEditorWidget.__overridden_methods__ = ['createSearchWidgetWrappers']
    QgsAttributeFormEditorWidget.__signal_arguments__ = {'valueChanged': ['value: object'], 'valuesChanged': ['value: object', 'additionalFieldValues: List[object]']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsattributeforminterface.h
try:
    QgsAttributeFormInterface.__virtual_methods__ = ['acceptChanges', 'initForm', 'featureChanged']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsattributeformrelationeditorwidget.h
try:
    QgsAttributeFormRelationEditorWidget.__overridden_methods__ = ['createSearchWidgetWrappers', 'currentFilterExpression']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsattributeformwidget.h
try:
    QgsAttributeFormWidget.__virtual_methods__ = ['currentFilterExpression']
    QgsAttributeFormWidget.__abstract_methods__ = ['createSearchWidgetWrappers']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsattributetabledelegate.h
try:
    QgsAttributeTableDelegate.__attribute_docs__ = {'actionColumnItemPainted': 'Emitted when an action column item is painted. The consumer of this\nsignal can initialize the index widget.\n\n.. note::\n\n   This signal is emitted repeatedly whenever the item is being painted.\n   It is the consumers responsibility to check if initialization has already\n   happened before.\n'}
    QgsAttributeTableDelegate.__overridden_methods__ = ['createEditor', 'paint', 'setModelData', 'setEditorData']
    QgsAttributeTableDelegate.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsattributetablefiltermodel.h
QgsAttributeTableFilterModel.FilterMode.baseClass = QgsAttributeTableFilterModel
QgsAttributeTableFilterModel.ColumnType.baseClass = QgsAttributeTableFilterModel
QgsAttributeTableFilterModel.Role = QgsAttributeTableFilterModel.CustomRole
# monkey patching scoped based enum
QgsAttributeTableFilterModel.TypeRole = QgsAttributeTableFilterModel.CustomRole.Type
QgsAttributeTableFilterModel.Role.TypeRole = QgsAttributeTableFilterModel.CustomRole.Type
QgsAttributeTableFilterModel.TypeRole.is_monkey_patched = True
QgsAttributeTableFilterModel.TypeRole.__doc__ = ""
QgsAttributeTableFilterModel.CustomRole.__doc__ = """The additional roles defined by this filter model.
The values of these roles start just after the roles defined by
:py:class:`QgsAttributeTableModel` so they do not conflict.

.. note::

   Prior to QGIS 3.36 this was available as QgsAttributeTableFilterModel.Role

.. versionadded:: 3.36

* ``Type``: 

  Available as ``QgsAttributeTableFilterModel.TypeRole`` in older QGIS releases.


"""
# --
QgsAttributeTableFilterModel.CustomRole.baseClass = QgsAttributeTableFilterModel
try:
    QgsAttributeTableFilterModel.__attribute_docs__ = {'sortColumnChanged': 'Emitted whenever the sort column is changed\n\n:param column: The sort column\n:param order: The sort order\n', 'featuresFiltered': 'Emitted when the filtering of the features has been done\n', 'visibleReloaded': 'Emitted when the the visible features on extend are reloaded (the list\nis created)\n', 'filterError': 'Emitted when an error occurred while filtering features\n\n.. versionadded:: 3.18\n'}
    QgsAttributeTableFilterModel.__virtual_methods__ = ['setFilteredFeatures']
    QgsAttributeTableFilterModel.__overridden_methods__ = ['fidToIndex', 'mapToSource', 'mapFromSource', 'flags', 'sort', 'data', 'headerData', 'columnCount', 'filterAcceptsRow', 'lessThan']
    QgsAttributeTableFilterModel.__signal_arguments__ = {'sortColumnChanged': ['column: int', 'order: Qt.SortOrder'], 'filterError': ['errorMessage: str']}
    QgsAttributeTableFilterModel.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsattributetablemodel.h
QgsAttributeTableModel.Role = QgsAttributeTableModel.CustomRole
# monkey patching scoped based enum
QgsAttributeTableModel.FeatureIdRole = QgsAttributeTableModel.CustomRole.FeatureId
QgsAttributeTableModel.Role.FeatureIdRole = QgsAttributeTableModel.CustomRole.FeatureId
QgsAttributeTableModel.FeatureIdRole.is_monkey_patched = True
QgsAttributeTableModel.FeatureIdRole.__doc__ = "Get the feature id of the feature in this row"
QgsAttributeTableModel.FieldIndexRole = QgsAttributeTableModel.CustomRole.FieldIndex
QgsAttributeTableModel.Role.FieldIndexRole = QgsAttributeTableModel.CustomRole.FieldIndex
QgsAttributeTableModel.FieldIndexRole.is_monkey_patched = True
QgsAttributeTableModel.FieldIndexRole.__doc__ = "Get the field index of this column"
QgsAttributeTableModel.UserRole = QgsAttributeTableModel.CustomRole.User
QgsAttributeTableModel.Role.UserRole = QgsAttributeTableModel.CustomRole.User
QgsAttributeTableModel.UserRole.is_monkey_patched = True
QgsAttributeTableModel.UserRole.__doc__ = "Start further roles starting from this role"
QgsAttributeTableModel.SortRole = QgsAttributeTableModel.CustomRole.Sort
QgsAttributeTableModel.Role.SortRole = QgsAttributeTableModel.CustomRole.Sort
QgsAttributeTableModel.SortRole.is_monkey_patched = True
QgsAttributeTableModel.SortRole.__doc__ = "Role used for sorting start here"
QgsAttributeTableModel.CustomRole.__doc__ = """Custom model roles.

.. note::

   Prior to QGIS 3.36 this was available as QgsAttributeTableModel.Role

.. versionadded:: 3.36

* ``FeatureId``: Get the feature id of the feature in this row

  Available as ``QgsAttributeTableModel.FeatureIdRole`` in older QGIS releases.

* ``FieldIndex``: Get the field index of this column

  Available as ``QgsAttributeTableModel.FieldIndexRole`` in older QGIS releases.

* ``User``: Start further roles starting from this role

  Available as ``QgsAttributeTableModel.UserRole`` in older QGIS releases.

* ``Sort``: Role used for sorting start here

  Available as ``QgsAttributeTableModel.SortRole`` in older QGIS releases.


"""
# --
QgsAttributeTableModel.CustomRole.baseClass = QgsAttributeTableModel
try:
    QgsAttributeTableModel.__attribute_docs__ = {'modelChanged': 'Emitted when the model has been changed.\n', 'finished': 'Emitted when the model has completely loaded all features.\n'}
    QgsAttributeTableModel.__virtual_methods__ = ['loadLayer']
    QgsAttributeTableModel.__overridden_methods__ = ['rowCount', 'columnCount', 'headerData', 'data', 'setData', 'flags', 'removeRows']
    QgsAttributeTableModel.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsattributetableview.h
try:
    QgsAttributeTableView.__attribute_docs__ = {'willShowContextMenu': 'Emitted in order to provide a hook to add additional* menu entries to\nthe context menu.\n\n:param menu: If additional QMenuItems are added, they will show up in\n             the context menu.\n:param atIndex: The QModelIndex, to which the context menu belongs.\n                Relative to the source model. In most cases, this will\n                be a :py:class:`QgsAttributeTableFilterModel`\n', 'columnResized': 'Emitted when a column in the view has been resized.\n\n:param column: column index (starts at 0)\n:param width: new width in pixel\n', 'finished': '.. deprecated:: 3.40\n\n   No longer used.\n'}
    QgsAttributeTableView.__virtual_methods__ = ['setModel', 'selectRow', '_q_selectRow']
    QgsAttributeTableView.__overridden_methods__ = ['eventFilter', 'mousePressEvent', 'mouseReleaseEvent', 'mouseMoveEvent', 'keyPressEvent', 'contextMenuEvent', 'closeEvent', 'selectAll']
    QgsAttributeTableView.__signal_arguments__ = {'willShowContextMenu': ['menu: QMenu', 'atIndex: QModelIndex'], 'columnResized': ['column: int', 'width: int']}
    QgsAttributeTableView.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsattributetypeloaddialog.h
try:
    QgsAttributeTypeLoadDialog.__overridden_methods__ = ['accept']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthauthoritieseditor.h
try:
    QgsAuthAuthoritiesEditor.__overridden_methods__ = ['showEvent']
    QgsAuthAuthoritiesEditor.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthcertificateinfo.h
try:
    QgsAuthCertInfo.__group__ = ['auth']
except (NameError, AttributeError):
    pass
try:
    QgsAuthCertInfoDialog.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthcertificatemanager.h
try:
    QgsAuthCertEditors.__group__ = ['auth']
except (NameError, AttributeError):
    pass
try:
    QgsAuthCertManager.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthcerttrustpolicycombobox.h
try:
    QgsAuthCertTrustPolicyComboBox.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthconfigeditor.h
try:
    QgsAuthConfigEditor.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthconfigselect.h
try:
    QgsAuthConfigSelect.__attribute_docs__ = {'selectedConfigIdChanged': 'Emitted when authentication config is changed or missing\n', 'selectedConfigIdRemoved': 'Emitted when authentication config is removed\n'}
    QgsAuthConfigSelect.__signal_arguments__ = {'selectedConfigIdChanged': ['authcfg: str'], 'selectedConfigIdRemoved': ['authcfg: str']}
    QgsAuthConfigSelect.__group__ = ['auth']
except (NameError, AttributeError):
    pass
try:
    QgsAuthConfigUriEdit.hasConfigId = staticmethod(QgsAuthConfigUriEdit.hasConfigId)
    QgsAuthConfigUriEdit.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsautheditorwidgets.h
try:
    QgsAuthMethodPlugins.__group__ = ['auth']
except (NameError, AttributeError):
    pass
try:
    QgsAuthEditorWidgets.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthidentitieseditor.h
try:
    QgsAuthIdentitiesEditor.__overridden_methods__ = ['showEvent']
    QgsAuthIdentitiesEditor.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthimportcertdialog.h
try:
    QgsAuthImportCertDialog.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthimportidentitydialog.h
try:
    QgsAuthImportIdentityDialog.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthmethodedit.h
try:
    QgsAuthMethodEdit.__attribute_docs__ = {'validityChanged': 'Emitted when the configuration validatity changes\n'}
    QgsAuthMethodEdit.__abstract_methods__ = ['validateConfig', 'configMap', 'loadConfig', 'resetConfig', 'clearConfig']
    QgsAuthMethodEdit.__signal_arguments__ = {'validityChanged': ['valid: bool']}
    QgsAuthMethodEdit.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthserverseditor.h
try:
    QgsAuthServersEditor.__overridden_methods__ = ['showEvent']
    QgsAuthServersEditor.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthsettingswidget.h
QgsAuthSettingsWidget.WarningType.baseClass = QgsAuthSettingsWidget
try:
    QgsAuthSettingsWidget.__attribute_docs__ = {'usernameChanged': 'Emitted when the plain text username defined in the dialog is changed.\n\n.. versionadded:: 3.22\n', 'passwordChanged': 'Emitted when the plain text password defined in the dialog is changed.\n\n.. versionadded:: 3.22\n', 'configIdChanged': 'Emitted when the auth configuration ID selected in the dialog is\nchanged.\n\n.. versionadded:: 3.22\n'}
    QgsAuthSettingsWidget.formattedWarning = staticmethod(QgsAuthSettingsWidget.formattedWarning)
    QgsAuthSettingsWidget.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthsslconfigwidget.h
try:
    QgsAuthSslConfigWidget.__attribute_docs__ = {'configEnabledChanged': 'Emitted when the enabled state of the configuration changes\n', 'certFoundInAuthDatabase': 'Emitted when an certificate of same SHA hash is found in authentication\ndatabase\n', 'hostPortValidityChanged': 'Emitted when the validity of the host:port changes\n', 'readyToSaveChanged': 'Emitted when the configuration can be saved changes\n'}
    QgsAuthSslConfigWidget.__signal_arguments__ = {'configEnabledChanged': ['enabled: bool'], 'certFoundInAuthDatabase': ['found: bool'], 'hostPortValidityChanged': ['valid: bool'], 'readyToSaveChanged': ['cansave: bool']}
    QgsAuthSslConfigWidget.__group__ = ['auth']
except (NameError, AttributeError):
    pass
try:
    QgsAuthSslConfigDialog.__overridden_methods__ = ['accept']
    QgsAuthSslConfigDialog.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthsslerrorsdialog.h
try:
    QgsAuthSslErrorsDialog.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthsslimportdialog.h
try:
    QgsAuthSslImportDialog.__overridden_methods__ = ['accept']
    QgsAuthSslImportDialog.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/auth/qgsauthtrustedcasdialog.h
try:
    QgsAuthTrustedCAsDialog.__overridden_methods__ = ['showEvent']
    QgsAuthTrustedCAsDialog.__group__ = ['auth']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsbrowserdockwidget.h
try:
    QgsBrowserDockWidget.__attribute_docs__ = {'openFile': 'Emitted when a file needs to be opened\n', 'handleDropUriList': 'Emitted when drop uri list needs to be handled\n', 'connectionsChanged': 'Connections changed in the browser\n'}
    QgsBrowserDockWidget.__signal_arguments__ = {'openFile': ['fileName: str', 'fileTypeHint: Optional[str] = None'], 'handleDropUriList': ['uris: QgsMimeDataUtils.UriList']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsbrowserguimodel.h
try:
    QgsBrowserGuiModel.__overridden_methods__ = ['flags', 'dropMimeData', 'setData']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsbrowsertreeview.h
try:
    QgsBrowserTreeView.__overridden_methods__ = ['setModel', 'showEvent', 'hideEvent', 'keyPressEvent', 'rowsInserted']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsbrowserwidget.h
try:
    QgsBrowserWidget.__overridden_methods__ = ['showEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsbrushstylecombobox.h
try:
    QgsBrushStyleComboBox.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/callouts/qgscalloutpanelwidget.h
try:
    QgsCalloutPanelWidget.__attribute_docs__ = {'calloutChanged': 'Emitted when the callout defined by the widget changes\n'}
    QgsCalloutPanelWidget.__group__ = ['callouts']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/callouts/qgscalloutwidget.h
try:
    QgsCalloutWidget.__attribute_docs__ = {'changed': 'Should be emitted whenever configuration changes happened on this symbol\nlayer configuration. If the subsymbol is changed,\n:py:func:`~QgsCalloutWidget.symbolChanged` should be emitted instead.\n'}
    QgsCalloutWidget.__virtual_methods__ = ['setContext']
    QgsCalloutWidget.__abstract_methods__ = ['setCallout', 'callout', 'setGeometryType']
    QgsCalloutWidget.__overridden_methods__ = ['createExpressionContext']
    QgsCalloutWidget.__group__ = ['callouts']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgscategorizedsymbolrendererwidget.h
QgsCategorizedSymbolRendererWidget.CustomRoles = QgsCategorizedSymbolRendererWidget.CustomRole
# monkey patching scoped based enum
QgsCategorizedSymbolRendererWidget.ValueRole = QgsCategorizedSymbolRendererWidget.CustomRole.Value
QgsCategorizedSymbolRendererWidget.CustomRoles.ValueRole = QgsCategorizedSymbolRendererWidget.CustomRole.Value
QgsCategorizedSymbolRendererWidget.ValueRole.is_monkey_patched = True
QgsCategorizedSymbolRendererWidget.ValueRole.__doc__ = "Category value"
QgsCategorizedSymbolRendererWidget.CustomRole.__doc__ = """Custom model roles.

.. note::

   Prior to QGIS 3.36 this was available as QgsCategorizedSymbolRendererWidget.CustomRoles

.. versionadded:: 3.36

* ``Value``: Category value

  Available as ``QgsCategorizedSymbolRendererWidget.ValueRole`` in older QGIS releases.


"""
# --
QgsCategorizedSymbolRendererWidget.CustomRole.baseClass = QgsCategorizedSymbolRendererWidget
try:
    QgsCategorizedSymbolRendererWidget.create = staticmethod(QgsCategorizedSymbolRendererWidget.create)
    QgsCategorizedSymbolRendererWidget.__overridden_methods__ = ['renderer', 'setContext', 'createExpressionContext', 'setSymbolLevels', 'pasteSymbolToSelection', 'selectedSymbols', 'refreshSymbolView', 'keyPressEvent']
    QgsCategorizedSymbolRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscheckablecombobox.h
try:
    QgsCheckableComboBox.__attribute_docs__ = {'checkedItemsChanged': 'Emitted whenever the checked items list changed.\n'}
    QgsCheckableComboBox.__overridden_methods__ = ['hidePopup', 'eventFilter', 'resizeEvent']
    QgsCheckableComboBox.__signal_arguments__ = {'checkedItemsChanged': ['items: List[str]']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgscheckboxsearchwidgetwrapper.h
try:
    QgsCheckboxSearchWidgetWrapper.__overridden_methods__ = ['applyDirectly', 'expression', 'valid', 'supportedFlags', 'defaultFlags', 'createExpression', 'clearWidget', 'setEnabled', 'createWidget', 'initWidget', 'setExpression']
    QgsCheckboxSearchWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditor.h
# monkey patching scoped based enum
QgsCodeEditor.Mode.ScriptEditor.__doc__ = "Standard mode, allows for display and edit of entire scripts"
QgsCodeEditor.Mode.OutputDisplay.__doc__ = "Read only mode for display of command outputs"
QgsCodeEditor.Mode.CommandInput.__doc__ = "Command input mode"
QgsCodeEditor.Mode.__doc__ = """Code editor modes.

.. versionadded:: 3.30

* ``ScriptEditor``: Standard mode, allows for display and edit of entire scripts
* ``OutputDisplay``: Read only mode for display of command outputs
* ``CommandInput``: Command input mode

"""
# --
QgsCodeEditor.Mode.baseClass = QgsCodeEditor
# monkey patching scoped based enum
QgsCodeEditor.LineNumbers = QgsCodeEditor.MarginRole.LineNumbers
QgsCodeEditor.LineNumbers.is_monkey_patched = True
QgsCodeEditor.LineNumbers.__doc__ = "Line numbers"
QgsCodeEditor.ErrorIndicators = QgsCodeEditor.MarginRole.ErrorIndicators
QgsCodeEditor.ErrorIndicators.is_monkey_patched = True
QgsCodeEditor.ErrorIndicators.__doc__ = "Error indicators"
QgsCodeEditor.FoldingControls = QgsCodeEditor.MarginRole.FoldingControls
QgsCodeEditor.FoldingControls.is_monkey_patched = True
QgsCodeEditor.FoldingControls.__doc__ = "Folding controls"
QgsCodeEditor.MarginRole.__doc__ = """Margin roles.

This enum contains the roles which the different numbered margins are used for.

.. versionadded:: 3.16

* ``LineNumbers``: Line numbers
* ``ErrorIndicators``: Error indicators
* ``FoldingControls``: Folding controls

"""
# --
QgsCodeEditor.MarginRole.baseClass = QgsCodeEditor
# monkey patching scoped based enum
QgsCodeEditor.Flag.CodeFolding.__doc__ = "Indicates that code folding should be enabled for the editor"
QgsCodeEditor.Flag.ImmediatelyUpdateHistory.__doc__ = "Indicates that the history file should be immediately updated whenever a command is executed, instead of the default behavior of only writing the history on widget close \n.. versionadded:: 3.32"
QgsCodeEditor.Flag.__doc__ = """Flags controlling behavior of code editor

.. versionadded:: 3.28

* ``CodeFolding``: Indicates that code folding should be enabled for the editor
* ``ImmediatelyUpdateHistory``: Indicates that the history file should be immediately updated whenever a command is executed, instead of the default behavior of only writing the history on widget close

  .. versionadded:: 3.32


"""
# --
QgsCodeEditor.Flag.baseClass = QgsCodeEditor
QgsCodeEditor.Flags.baseClass = QgsCodeEditor
Flags = QgsCodeEditor  # dirty hack since SIP seems to introduce the flags in module
try:
    QgsCodeEditor.__attribute_docs__ = {'SEARCH_RESULT_INDICATOR': 'Indicator index for search results', 'sessionHistoryCleared': 'Emitted when the history of commands run in the current session is\ncleared.\n\n.. versionadded:: 3.30\n', 'persistentHistoryCleared': 'Emitted when the persistent history of commands run in the editor is\ncleared.\n\n.. versionadded:: 3.30\n', 'helpRequested': 'Emitted when documentation was requested for the specified ``word``.\n\n.. versionadded:: 3.42\n', 'editingTimeout': 'Emitted when either:\n\n1. 1 second has elapsed since the last text change in the widget\n2. or, immediately after the widget has lost focus after its text was changed.\n\n.. seealso:: :py:func:`editingTimeoutInterval`\n\n.. versionadded:: 3.42\n'}
    QgsCodeEditor.__annotations__ = {'SEARCH_RESULT_INDICATOR': int}
    QgsCodeEditor.languageToString = staticmethod(QgsCodeEditor.languageToString)
    QgsCodeEditor.defaultColor = staticmethod(QgsCodeEditor.defaultColor)
    QgsCodeEditor.color = staticmethod(QgsCodeEditor.color)
    QgsCodeEditor.setColor = staticmethod(QgsCodeEditor.setColor)
    QgsCodeEditor.getMonospaceFont = staticmethod(QgsCodeEditor.getMonospaceFont)
    QgsCodeEditor.isFixedPitch = staticmethod(QgsCodeEditor.isFixedPitch)
    QgsCodeEditor.__virtual_methods__ = ['language', 'languageCapabilities', 'moveCursorToStart', 'moveCursorToEnd', 'checkSyntax', 'toggleComment', 'initializeLexer', 'populateContextMenu', 'reformatCodeString', 'showMessage']
    QgsCodeEditor.__overridden_methods__ = ['callTip', 'setText', 'focusOutEvent', 'keyPressEvent', 'contextMenuEvent', 'eventFilter']
    QgsCodeEditor.__signal_arguments__ = {'helpRequested': ['word: str']}
    QgsCodeEditor.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
try:
    QgsCodeInterpreter.__virtual_methods__ = ['currentState']
    QgsCodeInterpreter.__abstract_methods__ = ['promptForState', 'execCommandImpl']
    QgsCodeInterpreter.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorcolorscheme.h
# monkey patching scoped based enum
QgsCodeEditorColorScheme.ColorRole.Default.__doc__ = "Default text color"
QgsCodeEditorColorScheme.ColorRole.Keyword.__doc__ = "Keyword color"
QgsCodeEditorColorScheme.ColorRole.Class.__doc__ = "Class color"
QgsCodeEditorColorScheme.ColorRole.Method.__doc__ = "Method color"
QgsCodeEditorColorScheme.ColorRole.Decoration.__doc__ = "Decoration color"
QgsCodeEditorColorScheme.ColorRole.Number.__doc__ = "Number color"
QgsCodeEditorColorScheme.ColorRole.Comment.__doc__ = "Comment color"
QgsCodeEditorColorScheme.ColorRole.CommentLine.__doc__ = "Line comment color"
QgsCodeEditorColorScheme.ColorRole.CommentBlock.__doc__ = "Comment block color"
QgsCodeEditorColorScheme.ColorRole.Background.__doc__ = "Background color"
QgsCodeEditorColorScheme.ColorRole.Cursor.__doc__ = "Cursor color"
QgsCodeEditorColorScheme.ColorRole.CaretLine.__doc__ = "Caret line color"
QgsCodeEditorColorScheme.ColorRole.SingleQuote.__doc__ = "Single quote color"
QgsCodeEditorColorScheme.ColorRole.DoubleQuote.__doc__ = "Double quote color"
QgsCodeEditorColorScheme.ColorRole.TripleSingleQuote.__doc__ = "Triple single quote color"
QgsCodeEditorColorScheme.ColorRole.TripleDoubleQuote.__doc__ = "Triple double quote color"
QgsCodeEditorColorScheme.ColorRole.Operator.__doc__ = "Operator color"
QgsCodeEditorColorScheme.ColorRole.QuotedOperator.__doc__ = "Quoted operator color"
QgsCodeEditorColorScheme.ColorRole.Identifier.__doc__ = "Identifier color"
QgsCodeEditorColorScheme.ColorRole.QuotedIdentifier.__doc__ = "Quoted identifier color"
QgsCodeEditorColorScheme.ColorRole.Tag.__doc__ = "Tag color"
QgsCodeEditorColorScheme.ColorRole.UnknownTag.__doc__ = "Unknown tag"
QgsCodeEditorColorScheme.ColorRole.MarginBackground.__doc__ = "Margin background color"
QgsCodeEditorColorScheme.ColorRole.MarginForeground.__doc__ = "Margin foreground color"
QgsCodeEditorColorScheme.ColorRole.SelectionBackground.__doc__ = "Selection background color"
QgsCodeEditorColorScheme.ColorRole.SelectionForeground.__doc__ = "Selection foreground color"
QgsCodeEditorColorScheme.ColorRole.MatchedBraceBackground.__doc__ = "Matched brace background color"
QgsCodeEditorColorScheme.ColorRole.MatchedBraceForeground.__doc__ = "Matched brace foreground color"
QgsCodeEditorColorScheme.ColorRole.Edge.__doc__ = "Edge color"
QgsCodeEditorColorScheme.ColorRole.Fold.__doc__ = "Fold color"
QgsCodeEditorColorScheme.ColorRole.Error.__doc__ = "Error color"
QgsCodeEditorColorScheme.ColorRole.ErrorBackground.__doc__ = "Error background color"
QgsCodeEditorColorScheme.ColorRole.FoldIconForeground.__doc__ = "Fold icon foreground color"
QgsCodeEditorColorScheme.ColorRole.FoldIconHalo.__doc__ = "Fold icon halo color"
QgsCodeEditorColorScheme.ColorRole.IndentationGuide.__doc__ = "Indentation guide line"
QgsCodeEditorColorScheme.ColorRole.SearchMatchBackground.__doc__ = "Background color for search matches \n.. versionadded:: 3.38"
QgsCodeEditorColorScheme.ColorRole.__doc__ = """Color roles.

* ``Default``: Default text color
* ``Keyword``: Keyword color
* ``Class``: Class color
* ``Method``: Method color
* ``Decoration``: Decoration color
* ``Number``: Number color
* ``Comment``: Comment color
* ``CommentLine``: Line comment color
* ``CommentBlock``: Comment block color
* ``Background``: Background color
* ``Cursor``: Cursor color
* ``CaretLine``: Caret line color
* ``SingleQuote``: Single quote color
* ``DoubleQuote``: Double quote color
* ``TripleSingleQuote``: Triple single quote color
* ``TripleDoubleQuote``: Triple double quote color
* ``Operator``: Operator color
* ``QuotedOperator``: Quoted operator color
* ``Identifier``: Identifier color
* ``QuotedIdentifier``: Quoted identifier color
* ``Tag``: Tag color
* ``UnknownTag``: Unknown tag
* ``MarginBackground``: Margin background color
* ``MarginForeground``: Margin foreground color
* ``SelectionBackground``: Selection background color
* ``SelectionForeground``: Selection foreground color
* ``MatchedBraceBackground``: Matched brace background color
* ``MatchedBraceForeground``: Matched brace foreground color
* ``Edge``: Edge color
* ``Fold``: Fold color
* ``Error``: Error color
* ``ErrorBackground``: Error background color
* ``FoldIconForeground``: Fold icon foreground color
* ``FoldIconHalo``: Fold icon halo color
* ``IndentationGuide``: Indentation guide line
* ``SearchMatchBackground``: Background color for search matches

  .. versionadded:: 3.38


"""
# --
try:
    QgsCodeEditorColorScheme.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorcolorschemeregistry.h
try:
    QgsCodeEditorColorSchemeRegistry.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorcss.h
try:
    QgsCodeEditorCSS.__overridden_methods__ = ['language', 'initializeLexer']
    QgsCodeEditorCSS.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditordockwidget.h
try:
    QgsCodeEditorDockWidget.__attribute_docs__ = {'visibilityChanged': "Emitted when the editor's visibility is changed.\n"}
    QgsCodeEditorDockWidget.__signal_arguments__ = {'visibilityChanged': ['isVisible: bool']}
    QgsCodeEditorDockWidget.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorexpression.h
try:
    QgsCodeEditorExpression.__overridden_methods__ = ['language', 'languageCapabilities', 'toggleComment', 'initializeLexer']
    QgsCodeEditorExpression.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorhtml.h
try:
    QgsCodeEditorHTML.__overridden_methods__ = ['language', 'languageCapabilities', 'toggleComment', 'initializeLexer', 'reformatCodeString']
    QgsCodeEditorHTML.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorjs.h
try:
    QgsCodeEditorJavascript.__overridden_methods__ = ['language', 'initializeLexer']
    QgsCodeEditorJavascript.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorjson.h
try:
    QgsCodeEditorJson.__overridden_methods__ = ['language', 'initializeLexer']
    QgsCodeEditorJson.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorpython.h
try:
    QgsCodeEditorPython.__virtual_methods__ = ['showApiDocumentation']
    QgsCodeEditorPython.__overridden_methods__ = ['language', 'languageCapabilities', 'checkSyntax', 'toggleComment', 'initializeLexer', 'keyPressEvent', 'reformatCodeString', 'populateContextMenu']
    QgsCodeEditorPython.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorr.h
try:
    QgsCodeEditorR.__overridden_methods__ = ['language', 'initializeLexer']
    QgsCodeEditorR.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorshell.h
try:
    QgsCodeEditorShell.__overridden_methods__ = ['language', 'initializeLexer']
    QgsCodeEditorShell.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorsql.h
try:
    QgsCodeEditorSQL.__overridden_methods__ = ['language', 'initializeLexer']
    QgsCodeEditorSQL.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/codeeditors/qgscodeeditorwidget.h
try:
    QgsCodeEditorWidget.__attribute_docs__ = {'searchBarToggled': 'Emitted when the visibility of the search bar is changed.\n', 'filePathChanged': "Emitted when the widget's associated file path is changed.\n\n.. seealso:: :py:func:`setFilePath`\n\n.. seealso:: :py:func:`filePath`\n", 'loadedExternalChanges': 'Emitted when the widget loads in text from the associated file to bring\nin changes made externally to the file.\n'}
    QgsCodeEditorWidget.__overridden_methods__ = ['resizeEvent', 'showEvent', 'eventFilter']
    QgsCodeEditorWidget.__signal_arguments__ = {'searchBarToggled': ['visible: bool'], 'filePathChanged': ['path: str']}
    QgsCodeEditorWidget.__group__ = ['codeeditors']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscollapsiblegroupbox.h
try:
    QgsCollapsibleGroupBoxBasic.__attribute_docs__ = {'collapsedStateChanged': 'Signal emitted when groupbox collapsed/expanded state is changed, and\nwhen first shown\n'}
    QgsCollapsibleGroupBoxBasic.__overridden_methods__ = ['showEvent', 'mousePressEvent', 'mouseReleaseEvent', 'changeEvent']
    QgsCollapsibleGroupBoxBasic.__signal_arguments__ = {'collapsedStateChanged': ['collapsed: bool']}
except (NameError, AttributeError):
    pass
try:
    QgsGroupBoxCollapseButton.__overridden_methods__ = ['mouseReleaseEvent']
except (NameError, AttributeError):
    pass
try:
    QgsCollapsibleGroupBox.__overridden_methods__ = ['showEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscolorbrewercolorrampdialog.h
try:
    QgsColorBrewerColorRampWidget.__attribute_docs__ = {'changed': 'Emitted when the dialog settings change\n'}
except (NameError, AttributeError):
    pass
try:
    QgsColorBrewerColorRampDialog.__attribute_docs__ = {'changed': 'Emitted when the dialog settings change\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscolorbutton.h
QgsColorButton.Behavior.baseClass = QgsColorButton
try:
    QgsColorButton.__attribute_docs__ = {'colorChanged': 'Emitted whenever a new color is set for the button. The color is always\nvalid. In case the new color is the same no signal is emitted, to avoid\ninfinite loops.\n\n:param color: New color\n', 'colorClicked': "Emitted when the button is clicked, if the button's behavior is set to\nSignalOnly\n\n:param color: button color\n\n.. seealso:: :py:func:`setBehavior`\n\n.. seealso:: :py:func:`behavior`\n", 'cleared': 'Emitted when the color is cleared (set to null).\n\n.. seealso:: :py:func:`setToNull`\n\n.. versionadded:: 3.12\n', 'unlinked': 'Emitted when the color is unlinked, e.g. when it was previously set to\nlink to a project color and is now no longer linked.\n\n.. seealso:: :py:func:`unlink`\n\n.. seealso:: :py:func:`linkToProjectColor`\n\n.. versionadded:: 3.6\n'}
    QgsColorButton.createMenuIcon = staticmethod(QgsColorButton.createMenuIcon)
    QgsColorButton.__overridden_methods__ = ['minimumSizeHint', 'sizeHint', 'event', 'changeEvent', 'showEvent', 'resizeEvent', 'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent', 'keyPressEvent', 'dragEnterEvent', 'dragLeaveEvent', 'dropEvent', 'wheelEvent']
    QgsColorButton.__signal_arguments__ = {'colorChanged': ['color: QColor'], 'colorClicked': ['color: QColor']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscolordialog.h
try:
    QgsColorDialog.__attribute_docs__ = {'currentColorChanged': "Emitted when the dialog's color changes\n\n:param color: current color\n"}
    QgsColorDialog.getColor = staticmethod(QgsColorDialog.getColor)
    QgsColorDialog.__overridden_methods__ = ['closeEvent']
    QgsColorDialog.__signal_arguments__ = {'currentColorChanged': ['color: QColor']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscolorrampbutton.h
try:
    QgsColorRampButton.__attribute_docs__ = {'colorRampChanged': 'Emitted whenever a new color ramp is set for the button. The color ramp\nis always valid. In case the new color ramp is the same, no signal is\nemitted to avoid infinite loops.\n'}
    QgsColorRampButton.__overridden_methods__ = ['sizeHint', 'event', 'changeEvent', 'showEvent', 'resizeEvent', 'mousePressEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscolorramplegendnodewidget.h
# monkey patching scoped based enum
QgsColorRampLegendNodeWidget.Capability.Prefix.__doc__ = "Allow editing legend prefix"
QgsColorRampLegendNodeWidget.Capability.Suffix.__doc__ = "Allow editing legend suffix"
QgsColorRampLegendNodeWidget.Capability.NumberFormat.__doc__ = "Allow editing number format"
QgsColorRampLegendNodeWidget.Capability.DefaultMinimum.__doc__ = "Allow resetting minimum label to default"
QgsColorRampLegendNodeWidget.Capability.DefaultMaximum.__doc__ = "Allow resetting maximum label to default"
QgsColorRampLegendNodeWidget.Capability.AllCapabilities.__doc__ = "All capabilities"
QgsColorRampLegendNodeWidget.Capability.__doc__ = """Capabilities to expose in the widget.

.. versionadded:: 3.38

* ``Prefix``: Allow editing legend prefix
* ``Suffix``: Allow editing legend suffix
* ``NumberFormat``: Allow editing number format
* ``DefaultMinimum``: Allow resetting minimum label to default
* ``DefaultMaximum``: Allow resetting maximum label to default
* ``AllCapabilities``: All capabilities

"""
# --
QgsColorRampLegendNodeWidget.Capability.baseClass = QgsColorRampLegendNodeWidget
QgsColorRampLegendNodeWidget.Capabilities.baseClass = QgsColorRampLegendNodeWidget
Capabilities = QgsColorRampLegendNodeWidget  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/gui/raster/qgscolorrampshaderwidget.h
try:
    QgsColorRampShaderWidget.__attribute_docs__ = {'minimumMaximumChangedFromTree': 'Color ramp tree has changed\n', 'widgetChanged': 'Widget changed\n', 'classificationModeChanged': 'Classification mode changed\n'}
    QgsColorRampShaderWidget.__signal_arguments__ = {'minimumMaximumChangedFromTree': ['minimum: float', 'maximum: float'], 'classificationModeChanged': ['mode: Qgis.ShaderClassificationMethod']}
    QgsColorRampShaderWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscolorschemelist.h
try:
    QgsColorSchemeList.__attribute_docs__ = {'colorSelected': 'Emitted when a color is selected from the list\n\n:param color: color selected\n'}
    QgsColorSchemeList.__overridden_methods__ = ['keyPressEvent', 'mousePressEvent', 'mouseReleaseEvent']
    QgsColorSchemeList.__signal_arguments__ = {'colorSelected': ['color: QColor']}
except (NameError, AttributeError):
    pass
try:
    QgsColorSwatchDelegate.__overridden_methods__ = ['paint', 'sizeHint', 'editorEvent']
except (NameError, AttributeError):
    pass
try:
    QgsColorSchemeModel.__overridden_methods__ = ['index', 'parent', 'rowCount', 'columnCount', 'data', 'flags', 'setData', 'headerData', 'supportedDropActions', 'mimeTypes', 'removeRows', 'insertRows', 'mimeData', 'dropMimeData']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscolorswatchgrid.h
try:
    QgsColorSwatchGrid.__attribute_docs__ = {'colorChanged': 'Emitted when a color has been selected from the widget\n\n:param color: selected color\n', 'hovered': 'Emitted when mouse hovers over widget\n'}
    QgsColorSwatchGrid.__overridden_methods__ = ['minimumSizeHint', 'sizeHint', 'paintEvent', 'mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent', 'keyPressEvent', 'focusInEvent', 'focusOutEvent']
    QgsColorSwatchGrid.__signal_arguments__ = {'colorChanged': ['color: QColor']}
except (NameError, AttributeError):
    pass
try:
    QgsColorSwatchGridAction.__attribute_docs__ = {'colorChanged': 'Emitted when a color has been selected from the widget\n\n:param color: selected color\n'}
    QgsColorSwatchGridAction.__signal_arguments__ = {'colorChanged': ['color: QColor']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscolorwidgets.h
# monkey patching scoped based enum
QgsColorWidget.ComponentUnit.Scaled0to255.__doc__ = "Values in the range 0-255"
QgsColorWidget.ComponentUnit.Percent.__doc__ = "Percent values in the range 0-100"
QgsColorWidget.ComponentUnit.Degree.__doc__ = "Degree values in the range 0-359"
QgsColorWidget.ComponentUnit.__doc__ = """Specified the color component unit

* ``Scaled0to255``: Values in the range 0-255
* ``Percent``: Percent values in the range 0-100
* ``Degree``: Degree values in the range 0-359

"""
# --
QgsColorWidget.ComponentUnit.baseClass = QgsColorWidget
QgsColorTextWidget.ColorTextFormat.baseClass = QgsColorTextWidget
try:
    QgsColorWidget.__attribute_docs__ = {'colorChanged': "Emitted when the widget's color changes\n\n:param color: new widget color\n", 'hovered': 'Emitted when mouse hovers over widget.\n'}
    QgsColorWidget.createDragIcon = staticmethod(QgsColorWidget.createDragIcon)
    QgsColorWidget.componentUnit = staticmethod(QgsColorWidget.componentUnit)
    QgsColorWidget.alterColor = staticmethod(QgsColorWidget.alterColor)
    QgsColorWidget.alterColorF = staticmethod(QgsColorWidget.alterColorF)
    QgsColorWidget.__virtual_methods__ = ['setColor', 'setComponent', 'setComponentValue', 'setComponentValueF']
    QgsColorWidget.__overridden_methods__ = ['dragEnterEvent', 'dropEvent', 'mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent']
    QgsColorWidget.__signal_arguments__ = {'colorChanged': ['color: QColor']}
except (NameError, AttributeError):
    pass
try:
    QgsColorWidgetAction.__attribute_docs__ = {'colorChanged': 'Emitted when a color has been selected from the widget\n\n:param color: selected color\n'}
    QgsColorWidgetAction.__signal_arguments__ = {'colorChanged': ['color: QColor']}
except (NameError, AttributeError):
    pass
try:
    QgsColorRampWidget.__attribute_docs__ = {'valueChanged': "Emitted when the widget's color component value changes\n\n:param value: new value of color component in the range between 0 and\n              the value returned by\n              :py:func:`~QgsColorRampWidget.componentRange`\n\n.. deprecated:: 3.40\n\n   Use :py:func:`~QgsColorRampWidget.valueChangedF` instead.\n", 'valueChangedF': "Emitted when the widget's color component value changes\n\n:param value: new value of color component in the range 0.0-1.0\n\n.. versionadded:: 3.40\n"}
    QgsColorRampWidget.__overridden_methods__ = ['sizeHint', 'paintEvent', 'mouseMoveEvent', 'wheelEvent', 'mousePressEvent', 'mouseReleaseEvent', 'keyPressEvent']
    QgsColorRampWidget.__signal_arguments__ = {'valueChangedF': ['value: float']}
except (NameError, AttributeError):
    pass
try:
    QgsColorPreviewWidget.__virtual_methods__ = ['setColor2']
    QgsColorPreviewWidget.__overridden_methods__ = ['paintEvent', 'sizeHint', 'mousePressEvent', 'mouseReleaseEvent', 'mouseMoveEvent']
except (NameError, AttributeError):
    pass
try:
    QgsColorWheel.__overridden_methods__ = ['sizeHint', 'paintEvent', 'setColor', 'resizeEvent', 'mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent']
except (NameError, AttributeError):
    pass
try:
    QgsColorBox.__overridden_methods__ = ['sizeHint', 'paintEvent', 'setComponent', 'setColor', 'resizeEvent', 'mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent']
except (NameError, AttributeError):
    pass
try:
    QgsColorSliderWidget.__overridden_methods__ = ['setComponent', 'setComponentValueF', 'setColor']
except (NameError, AttributeError):
    pass
try:
    QgsColorTextWidget.__overridden_methods__ = ['setColor', 'resizeEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscompoundcolorwidget.h
try:
    QgsCompoundColorWidget.__attribute_docs__ = {'currentColorChanged': "Emitted when the dialog's color changes\n\n:param color: current color\n"}
    QgsCompoundColorWidget.importUserPaletteFromFile = staticmethod(QgsCompoundColorWidget.importUserPaletteFromFile)
    QgsCompoundColorWidget.createNewUserPalette = staticmethod(QgsCompoundColorWidget.createNewUserPalette)
    QgsCompoundColorWidget.removeUserPalette = staticmethod(QgsCompoundColorWidget.removeUserPalette)
    QgsCompoundColorWidget.__overridden_methods__ = ['hideEvent', 'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent', 'keyPressEvent']
    QgsCompoundColorWidget.__signal_arguments__ = {'currentColorChanged': ['color: QColor']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsconfigureshortcutsdialog.h
try:
    QgsConfigureShortcutsDialog.__overridden_methods__ = ['keyPressEvent', 'keyReleaseEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/proj/qgscoordinateboundspreviewmapwidget.h
try:
    QgsCoordinateBoundsPreviewMapWidget.__group__ = ['proj']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/proj/qgscoordinateoperationwidget.h
try:
    QgsCoordinateOperationWidget.OperationDetails.__attribute_docs__ = {'sourceTransformId': 'Source transform ID', 'destinationTransformId': 'Destination transform ID', 'proj': 'Proj coordinate operation description, for Proj >= 6.0 builds only', 'isAvailable': '``True`` if operation is available', 'allowFallback': '``True`` if fallback transforms can be used'}
    QgsCoordinateOperationWidget.OperationDetails.__annotations__ = {'sourceTransformId': int, 'destinationTransformId': int, 'proj': str, 'isAvailable': bool, 'allowFallback': bool}
    QgsCoordinateOperationWidget.OperationDetails.__doc__ = """Coordinate operation details"""
    QgsCoordinateOperationWidget.OperationDetails.__group__ = ['proj']
except (NameError, AttributeError):
    pass
try:
    QgsCoordinateOperationWidget.__attribute_docs__ = {'operationChanged': 'Emitted when the operation selected in the dialog is changed.\n', 'operationDoubleClicked': 'Emitted when an operation is double-clicked in the widget.\n'}
    QgsCoordinateOperationWidget.__group__ = ['proj']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/proj/qgscoordinatereferencesystemmodel.h
QgsCoordinateReferenceSystemModel.Roles = QgsCoordinateReferenceSystemModel.CustomRole
# monkey patching scoped based enum
QgsCoordinateReferenceSystemModel.RoleNodeType = QgsCoordinateReferenceSystemModel.CustomRole.NodeType
QgsCoordinateReferenceSystemModel.Roles.RoleNodeType = QgsCoordinateReferenceSystemModel.CustomRole.NodeType
QgsCoordinateReferenceSystemModel.RoleNodeType.is_monkey_patched = True
QgsCoordinateReferenceSystemModel.RoleNodeType.__doc__ = "Corresponds to the node's type"
QgsCoordinateReferenceSystemModel.RoleName = QgsCoordinateReferenceSystemModel.CustomRole.Name
QgsCoordinateReferenceSystemModel.Roles.RoleName = QgsCoordinateReferenceSystemModel.CustomRole.Name
QgsCoordinateReferenceSystemModel.RoleName.is_monkey_patched = True
QgsCoordinateReferenceSystemModel.RoleName.__doc__ = "The coordinate reference system name"
QgsCoordinateReferenceSystemModel.RoleAuthId = QgsCoordinateReferenceSystemModel.CustomRole.AuthId
QgsCoordinateReferenceSystemModel.Roles.RoleAuthId = QgsCoordinateReferenceSystemModel.CustomRole.AuthId
QgsCoordinateReferenceSystemModel.RoleAuthId.is_monkey_patched = True
QgsCoordinateReferenceSystemModel.RoleAuthId.__doc__ = "The coordinate reference system authority name and id"
QgsCoordinateReferenceSystemModel.RoleDeprecated = QgsCoordinateReferenceSystemModel.CustomRole.Deprecated
QgsCoordinateReferenceSystemModel.Roles.RoleDeprecated = QgsCoordinateReferenceSystemModel.CustomRole.Deprecated
QgsCoordinateReferenceSystemModel.RoleDeprecated.is_monkey_patched = True
QgsCoordinateReferenceSystemModel.RoleDeprecated.__doc__ = "``True`` if the CRS is deprecated"
QgsCoordinateReferenceSystemModel.RoleType = QgsCoordinateReferenceSystemModel.CustomRole.Type
QgsCoordinateReferenceSystemModel.Roles.RoleType = QgsCoordinateReferenceSystemModel.CustomRole.Type
QgsCoordinateReferenceSystemModel.RoleType.is_monkey_patched = True
QgsCoordinateReferenceSystemModel.RoleType.__doc__ = "The coordinate reference system type"
QgsCoordinateReferenceSystemModel.RoleGroupId = QgsCoordinateReferenceSystemModel.CustomRole.GroupId
QgsCoordinateReferenceSystemModel.Roles.RoleGroupId = QgsCoordinateReferenceSystemModel.CustomRole.GroupId
QgsCoordinateReferenceSystemModel.RoleGroupId.is_monkey_patched = True
QgsCoordinateReferenceSystemModel.RoleGroupId.__doc__ = "The node ID (for group nodes)"
QgsCoordinateReferenceSystemModel.RoleWkt = QgsCoordinateReferenceSystemModel.CustomRole.Wkt
QgsCoordinateReferenceSystemModel.Roles.RoleWkt = QgsCoordinateReferenceSystemModel.CustomRole.Wkt
QgsCoordinateReferenceSystemModel.RoleWkt.is_monkey_patched = True
QgsCoordinateReferenceSystemModel.RoleWkt.__doc__ = "The coordinate reference system's WKT representation. This is only used for non-standard CRS (i.e. those not present in the database)."
QgsCoordinateReferenceSystemModel.RoleProj = QgsCoordinateReferenceSystemModel.CustomRole.Proj
QgsCoordinateReferenceSystemModel.Roles.RoleProj = QgsCoordinateReferenceSystemModel.CustomRole.Proj
QgsCoordinateReferenceSystemModel.RoleProj.is_monkey_patched = True
QgsCoordinateReferenceSystemModel.RoleProj.__doc__ = "The coordinate reference system's PROJ representation. This is only used for non-standard CRS (i.e. those not present in the database)."
QgsCoordinateReferenceSystemModel.Group = QgsCoordinateReferenceSystemModel.CustomRole.Group
QgsCoordinateReferenceSystemModel.Group.is_monkey_patched = True
QgsCoordinateReferenceSystemModel.Group.__doc__ = "Group name. \n.. versionadded:: 3.42"
QgsCoordinateReferenceSystemModel.Projection = QgsCoordinateReferenceSystemModel.CustomRole.Projection
QgsCoordinateReferenceSystemModel.Projection.is_monkey_patched = True
QgsCoordinateReferenceSystemModel.Projection.__doc__ = "Projection name. \n.. versionadded:: 3.42"
QgsCoordinateReferenceSystemModel.CustomRole.__doc__ = """Custom model roles.

.. note::

   Prior to QGIS 3.36 this was available as QgsCoordinateReferenceSystemModel.Roles

.. versionadded:: 3.36

* ``NodeType``: Corresponds to the node's type

  Available as ``QgsCoordinateReferenceSystemModel.RoleNodeType`` in older QGIS releases.

* ``Name``: The coordinate reference system name

  Available as ``QgsCoordinateReferenceSystemModel.RoleName`` in older QGIS releases.

* ``AuthId``: The coordinate reference system authority name and id

  Available as ``QgsCoordinateReferenceSystemModel.RoleAuthId`` in older QGIS releases.

* ``Deprecated``: ``True`` if the CRS is deprecated

  Available as ``QgsCoordinateReferenceSystemModel.RoleDeprecated`` in older QGIS releases.

* ``Type``: The coordinate reference system type

  Available as ``QgsCoordinateReferenceSystemModel.RoleType`` in older QGIS releases.

* ``GroupId``: The node ID (for group nodes)

  Available as ``QgsCoordinateReferenceSystemModel.RoleGroupId`` in older QGIS releases.

* ``Wkt``: The coordinate reference system's WKT representation. This is only used for non-standard CRS (i.e. those not present in the database).

  Available as ``QgsCoordinateReferenceSystemModel.RoleWkt`` in older QGIS releases.

* ``Proj``: The coordinate reference system's PROJ representation. This is only used for non-standard CRS (i.e. those not present in the database).

  Available as ``QgsCoordinateReferenceSystemModel.RoleProj`` in older QGIS releases.

* ``Group``: Group name.

  .. versionadded:: 3.42

* ``Projection``: Projection name.

  .. versionadded:: 3.42


"""
# --
QgsCoordinateReferenceSystemModel.CustomRole.baseClass = QgsCoordinateReferenceSystemModel
QgsCoordinateReferenceSystemProxyModel.Filters.baseClass = QgsCoordinateReferenceSystemProxyModel
Filters = QgsCoordinateReferenceSystemProxyModel  # dirty hack since SIP seems to introduce the flags in module
try:
    QgsCoordinateReferenceSystemModel.__overridden_methods__ = ['flags', 'data', 'headerData', 'rowCount', 'columnCount', 'index', 'parent']
    QgsCoordinateReferenceSystemModel.__group__ = ['proj']
except (NameError, AttributeError):
    pass
try:
    QgsCoordinateReferenceSystemProxyModel.__overridden_methods__ = ['filterAcceptsRow', 'lessThan']
    QgsCoordinateReferenceSystemProxyModel.__group__ = ['proj']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgscptcitycolorrampdialog.h
try:
    QgsCptCityColorRampDialog.__attribute_docs__ = {'changed': 'Emitted when the dialog settings change\n'}
    QgsCptCityColorRampDialog.__overridden_methods__ = ['eventFilter']
    QgsCptCityColorRampDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/annotations/qgscreateannotationitemmaptool.h
try:
    QgsCreateAnnotationItemMapToolHandler.__attribute_docs__ = {'itemCreated': 'Emitted by the tool when a new annotation item has been created.\n\nClients should connect to this signal and call\n:py:func:`~QgsCreateAnnotationItemMapToolHandler.takeCreatedItem` to\ntake the newly created item from the map tool.\n'}
    QgsCreateAnnotationItemMapToolHandler.__group__ = ['annotations']
except (NameError, AttributeError):
    pass
try:
    QgsCreateAnnotationItemMapToolInterface.__abstract_methods__ = ['handler', 'mapTool']
    QgsCreateAnnotationItemMapToolInterface.__group__ = ['annotations']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscredentialdialog.h
try:
    QgsCredentialDialog.__overridden_methods__ = ['request', 'requestMasterPassword']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/proj/qgscrsdefinitionwidget.h
try:
    QgsCrsDefinitionWidget.__attribute_docs__ = {'crsChanged': 'Emitted when the CRS defined in the widget is changed.\n'}
    QgsCrsDefinitionWidget.__group__ = ['proj']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscurveeditorwidget.h
try:
    QgsCurveEditorWidget.__attribute_docs__ = {'changed': 'Emitted when the widget curve changes\n'}
    QgsCurveEditorWidget.__overridden_methods__ = ['keyPressEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscustomdrophandler.h
try:
    QgsCustomDropHandler.__virtual_methods__ = ['customUriProviderKey', 'handleCustomUriDrop', 'canHandleMimeData', 'handleMimeData', 'handleMimeDataV2', 'handleFileDrop', 'canHandleCustomUriCanvasDrop', 'handleCustomUriCanvasDrop']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layertree/qgscustomlayerorderwidget.h
try:
    QgsCustomLayerOrderWidget.__group__ = ['layertree']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgscustomprojectopenhandler.h
try:
    QgsCustomProjectOpenHandler.__virtual_methods__ = ['createDocumentThumbnailAfterOpen', 'icon']
    QgsCustomProjectOpenHandler.__abstract_methods__ = ['handleProjectOpen', 'filters']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsdashspacedialog.h
try:
    QgsDashSpaceWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsDashSpaceDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsdatabaseschemacombobox.h
try:
    QgsDatabaseSchemaComboBox.__attribute_docs__ = {'schemaChanged': 'Emitted whenever the currently selected schema changes.\n'}
    QgsDatabaseSchemaComboBox.__signal_arguments__ = {'schemaChanged': ['schema: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsdatabasetablecombobox.h
try:
    QgsDatabaseTableComboBox.__attribute_docs__ = {'tableChanged': 'Emitted whenever the currently selected table changes.\n'}
    QgsDatabaseTableComboBox.__signal_arguments__ = {'tableChanged': ['table: str', 'schema: Optional[str] = None']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsdatadefinedsizelegendwidget.h
try:
    QgsDataDefinedSizeLegendWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsdataitemguiprovider.h
try:
    QgsDataItemGuiProvider.notify = staticmethod(QgsDataItemGuiProvider.notify)
    QgsDataItemGuiProvider.__virtual_methods__ = ['populateContextMenu', 'precedenceWhenPopulatingMenus', 'rename', 'deleteLayer', 'handleDoubleClick', 'acceptDrop', 'handleDrop', 'createParamWidget']
    QgsDataItemGuiProvider.__abstract_methods__ = ['name']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsdatasourceselectdialog.h
try:
    QgsDataSourceSelectWidget.__attribute_docs__ = {'validationChanged': 'This signal is emitted whenever the validation status of the widget\nchanges.\n\n:param isValid: ``True`` if the current status of the widget is valid\n', 'selectionChanged': 'Emitted when the current selection changes in the widget.\n', 'itemTriggered': 'Emitted when an item is triggered, e.g. via a double-click.\n'}
    QgsDataSourceSelectWidget.__overridden_methods__ = ['showEvent', 'dragEnterEvent', 'dropEvent']
    QgsDataSourceSelectWidget.__signal_arguments__ = {'validationChanged': ['isValid: bool'], 'itemTriggered': ['uri: QgsMimeDataUtils.Uri']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsdatetimeedit.h
try:
    QgsDateTimeEdit.__attribute_docs__ = {'valueChanged': 'Signal emitted whenever the value changes.\n\n:param date: The new date/time value.\n'}
    QgsDateTimeEdit.__virtual_methods__ = ['emitValueChanged']
    QgsDateTimeEdit.__overridden_methods__ = ['clear', 'event', 'mousePressEvent', 'focusOutEvent', 'focusInEvent', 'wheelEvent', 'showEvent']
    QgsDateTimeEdit.__signal_arguments__ = {'valueChanged': ['date: QDateTime']}
    QgsDateTimeEdit.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
try:
    QgsTimeEdit.__attribute_docs__ = {'timeValueChanged': 'Signal emitted whenever the time changes.\n'}
    QgsTimeEdit.__overridden_methods__ = ['emitValueChanged']
    QgsTimeEdit.__signal_arguments__ = {'timeValueChanged': ['time: QTime']}
    QgsTimeEdit.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
try:
    QgsDateEdit.__attribute_docs__ = {'dateValueChanged': 'Signal emitted whenever the date changes.\n'}
    QgsDateEdit.__overridden_methods__ = ['emitValueChanged']
    QgsDateEdit.__signal_arguments__ = {'dateValueChanged': ['date: QDate']}
    QgsDateEdit.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsdatetimesearchwidgetwrapper.h
try:
    QgsDateTimeSearchWidgetWrapper.__overridden_methods__ = ['applyDirectly', 'expression', 'valid', 'supportedFlags', 'defaultFlags', 'createExpression', 'clearWidget', 'setEnabled', 'createWidget', 'initWidget', 'setExpression']
    QgsDateTimeSearchWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsdbrelationshipwidget.h
try:
    QgsDbRelationWidget.__attribute_docs__ = {'validityChanged': 'Emitted whenever the validity of the relationship configuration in the\nwidget changes.\n\n.. seealso:: :py:func:`isValid`\n'}
    QgsDbRelationWidget.__signal_arguments__ = {'validityChanged': ['isValid: bool']}
except (NameError, AttributeError):
    pass
try:
    QgsDbRelationDialog.__overridden_methods__ = ['accept']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsdecoratedscrollbar.h
# monkey patching scoped based enum
QgsScrollBarHighlight.Priority.Invalid.__doc__ = "Invalid"
QgsScrollBarHighlight.Priority.LowPriority.__doc__ = "Low priority, rendered below all other highlights"
QgsScrollBarHighlight.Priority.NormalPriority.__doc__ = "Normal priority"
QgsScrollBarHighlight.Priority.HighPriority.__doc__ = "High priority"
QgsScrollBarHighlight.Priority.HighestPriority.__doc__ = "Highest priority, rendered above all other highlights"
QgsScrollBarHighlight.Priority.__doc__ = """Priority, which dictates how overlapping highlights are rendered

* ``Invalid``: Invalid
* ``LowPriority``: Low priority, rendered below all other highlights
* ``NormalPriority``: Normal priority
* ``HighPriority``: High priority
* ``HighestPriority``: Highest priority, rendered above all other highlights

"""
# --
try:
    QgsScrollBarHighlight.__attribute_docs__ = {'category': 'Category ID', 'position': 'Position in scroll bar', 'color': 'Highlight color', 'priority': 'Priority, which dictates how overlapping highlights are rendered'}
    QgsScrollBarHighlight.__annotations__ = {'category': int, 'position': int, 'color': 'QColor', 'priority': 'QgsScrollBarHighlight.Priority'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsdefaultsearchwidgetwrapper.h
try:
    QgsDefaultSearchWidgetWrapper.__overridden_methods__ = ['expression', 'applyDirectly', 'supportedFlags', 'defaultFlags', 'createExpression', 'clearWidget', 'setEnabled', 'setExpression', 'createWidget', 'initWidget', 'valid']
    QgsDefaultSearchWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsdetaileditemdelegate.h
try:
    QgsDetailedItemDelegate.__overridden_methods__ = ['paint', 'sizeHint']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/devtools/qgsdevtoolwidget.h
try:
    QgsDevToolWidget.__group__ = ['devtools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/devtools/qgsdevtoolwidgetfactory.h
try:
    QgsDevToolWidgetFactory.__virtual_methods__ = ['icon', 'title']
    QgsDevToolWidgetFactory.__abstract_methods__ = ['createWidget']
    QgsDevToolWidgetFactory.__group__ = ['devtools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsdial.h
try:
    QgsDial.__overridden_methods__ = ['paintEvent']
    QgsDial.__signal_arguments__ = {'valueChanged': [': object']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsdirectionallightwidget.h
try:
    QgsDirectionalLightWidget.__attribute_docs__ = {'directionChanged': 'Emitted when the direction is changed\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsdockwidget.h
try:
    QgsDockWidget.__attribute_docs__ = {'closed': 'Emitted when dock widget is closed.\n\n.. seealso:: :py:func:`closedStateChanged`\n\n.. seealso:: :py:func:`opened`\n', 'closedStateChanged': 'Emitted when dock widget is closed (or opened).\n\n:param wasClosed: will be ``True`` if dock widget was closed, or\n                  ``False`` if dock widget was opened\n\n.. seealso:: :py:func:`closed`\n\n.. seealso:: :py:func:`openedStateChanged`\n', 'opened': 'Emitted when dock widget is opened.\n\n.. seealso:: :py:func:`openedStateChanged`\n\n.. seealso:: :py:func:`closed`\n', 'openedStateChanged': 'Emitted when dock widget is opened (or closed).\n\n:param wasOpened: will be ``True`` if dock widget was opened, or\n                  ``False`` if dock widget was closed\n\n.. seealso:: :py:func:`closedStateChanged`\n\n.. seealso:: :py:func:`opened`\n'}
    QgsDockWidget.__overridden_methods__ = ['closeEvent', 'showEvent']
    QgsDockWidget.__signal_arguments__ = {'closedStateChanged': ['wasClosed: bool'], 'openedStateChanged': ['wasOpened: bool']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsdoublespinbox.h
try:
    QgsDoubleSpinBox.__attribute_docs__ = {'returnPressed': 'Emitted when the Return or Enter key is used in the line edit.\n\n.. versionadded:: 3.40\n', 'textEdited': 'Emitted when the the value has been manually edited via line edit.\n\n.. versionadded:: 3.40\n', 'editingTimeout': 'Emitted when either:\n\n1. 1 second has elapsed since the last value change in the widget (eg last key press or scroll wheel event)\n2. or, immediately after the widget has lost focus after its value was changed.\n\nThis signal can be used to respond semi-instantly to changes in the spin\nbox, without responding too quickly while the user in the middle of\nsetting the value.\n\n.. seealso:: :py:func:`editingTimeoutInterval`\n\n.. versionadded:: 3.42\n'}
    QgsDoubleSpinBox.__overridden_methods__ = ['clear', 'valueFromText', 'validate', 'paintEvent', 'stepBy', 'changeEvent', 'wheelEvent', 'focusOutEvent', 'timerEvent']
    QgsDoubleSpinBox.__signal_arguments__ = {'textEdited': ['text: str'], 'editingTimeout': ['value: float']}
    QgsDoubleSpinBox.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsdoublevalidator.h
try:
    QgsDoubleValidator.toDouble = staticmethod(QgsDoubleValidator.toDouble)
    QgsDoubleValidator.__virtual_methods__ = ['setRange']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsdualview.h
QgsDualView.ViewMode.baseClass = QgsDualView
QgsDualView.FeatureListBrowsingAction.baseClass = QgsDualView
try:
    QgsDualView.__attribute_docs__ = {'displayExpressionChanged': 'Emitted whenever the display expression is successfully changed\n\n:param expression: The expression that was applied\n', 'filterChanged': 'Emitted whenever the filter changes\n', 'filterExpressionSet': 'Emitted when a filter expression is set using the view.\n\n:param expression: filter expression\n:param type: filter type\n', 'formModeChanged': 'Emitted when the form changes mode.\n\n:param mode: new mode\n', 'showContextMenuExternally': 'Emitted when selecting context menu on the feature list to create the\ncontext menu individually\n\n:param menu: context menu\n:param fid: feature id of the selected feature\n'}
    QgsDualView.requiredAttributes = staticmethod(QgsDualView.requiredAttributes)
    QgsDualView.__overridden_methods__ = ['hideEvent']
    QgsDualView.__signal_arguments__ = {'displayExpressionChanged': ['expression: str'], 'filterExpressionSet': ['expression: str', 'type: QgsAttributeForm.FilterType'], 'formModeChanged': ['mode: QgsAttributeEditorContext.Mode'], 'showContextMenuExternally': ['menu: QgsActionMenu', 'fid: QgsFeatureId']}
    QgsDualView.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
try:
    QgsAttributeTableAction.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
try:
    QgsAttributeTableMapLayerAction.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/core/qgseditorconfigwidget.h
try:
    QgsEditorConfigWidget.__attribute_docs__ = {'changed': 'Emitted when the configuration of the widget is changed.\n'}
    QgsEditorConfigWidget.__abstract_methods__ = ['config', 'setConfig']
    QgsEditorConfigWidget.__overridden_methods__ = ['createExpressionContext']
    QgsEditorConfigWidget.__group__ = ['editorwidgets', 'core']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/core/qgseditorwidgetautoconf.h
try:
    QgsEditorWidgetAutoConfPlugin.__abstract_methods__ = ['editorWidgetSetup']
    QgsEditorWidgetAutoConfPlugin.__group__ = ['editorwidgets', 'core']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/core/qgseditorwidgetfactory.h
try:
    QgsEditorWidgetFactory.__virtual_methods__ = ['createSearchWidget', 'isReadOnly', 'fieldScore']
    QgsEditorWidgetFactory.__abstract_methods__ = ['create', 'configWidget']
    QgsEditorWidgetFactory.__group__ = ['editorwidgets', 'core']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/core/qgseditorwidgetregistry.h
try:
    QgsEditorWidgetRegistry.__group__ = ['editorwidgets', 'core']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/core/qgseditorwidgetwrapper.h
try:
    QgsEditorWidgetWrapper.__attribute_docs__ = {'valueChanged': 'Emit this signal, whenever the value changed.\n\n:param value: The new value\n\n.. deprecated:: 3.10\n\n   Use valuesChanged signal instead.\n', 'valuesChanged': 'Emit this signal, whenever the value changed. It will also return the\nvalues for the additional fields handled by the widget\n\n:param value: The new value\n:param additionalFieldValues: A map of additional field names with their\n                              corresponding values\n\n.. versionadded:: 3.10\n', 'constraintStatusChanged': 'Emit this signal when the constraint status changed.\nconstraintStatusChanged\n\n:param constraint: represented as a string\n:param desc: is the constraint description\n:param err: the error represented as a string. Empty if none.\n:param status: \n', 'constraintResultVisibleChanged': 'Emit this signal when the constraint result visibility changed.\n'}
    QgsEditorWidgetWrapper.fromWidget = staticmethod(QgsEditorWidgetWrapper.fromWidget)
    QgsEditorWidgetWrapper.isInTable = staticmethod(QgsEditorWidgetWrapper.isInTable)
    QgsEditorWidgetWrapper.__virtual_methods__ = ['additionalFields', 'additionalFieldValues', 'showIndeterminateState', 'setHint', 'setValue', 'parentFormValueChanged', 'updateConstraintWidgetStatus']
    QgsEditorWidgetWrapper.__abstract_methods__ = ['value']
    QgsEditorWidgetWrapper.__overridden_methods__ = ['setEnabled', 'setFeature']
    QgsEditorWidgetWrapper.__signal_arguments__ = {'valueChanged': ['value: object'], 'valuesChanged': ['value: object', 'additionalFieldValues: List[object] = []'], 'constraintStatusChanged': ['constraint: str', 'desc: str', 'err: str', 'status: QgsEditorWidgetWrapper.ConstraintResult'], 'constraintResultVisibleChanged': ['visible: bool']}
    QgsEditorWidgetWrapper.__group__ = ['editorwidgets', 'core']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/effects/qgseffectdrawmodecombobox.h
try:
    QgsEffectDrawModeComboBox.__group__ = ['effects']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/effects/qgseffectstackpropertieswidget.h
try:
    QgsEffectStackCompactWidget.__attribute_docs__ = {'changed': 'Emitted when the paint effect properties change\n'}
    QgsEffectStackCompactWidget.__group__ = ['effects']
except (NameError, AttributeError):
    pass
try:
    QgsEffectStackPropertiesWidget.__group__ = ['effects']
except (NameError, AttributeError):
    pass
try:
    QgsEffectStackPropertiesDialog.__group__ = ['effects']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/elevation/qgselevationcontrollerwidget.h
try:
    QgsElevationControllerWidget.__attribute_docs__ = {'rangeChanged': 'Emitted when the visible range from the widget is changed.\n\n.. seealso:: :py:func:`setRange`\n\n.. seealso:: :py:func:`range`\n', 'fixedRangeSizeChanged': 'Emitted when the fixed range size is changed from the widget.\n\n.. seealso:: :py:func:`fixedRangeSize`\n\n.. seealso:: :py:func:`setFixedRangeSize`\n', 'invertedChanged': 'Emitted when the elevation filter slider is inverted.\n\n.. seealso:: :py:func:`setInverted`\n'}
    QgsElevationControllerWidget.__overridden_methods__ = ['resizeEvent']
    QgsElevationControllerWidget.__signal_arguments__ = {'rangeChanged': ['range: QgsDoubleRange'], 'fixedRangeSizeChanged': ['size: float'], 'invertedChanged': ['inverted: bool']}
    QgsElevationControllerWidget.__group__ = ['elevation']
except (NameError, AttributeError):
    pass
try:
    QgsElevationControllerSettingsAction.__group__ = ['elevation']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/elevation/qgselevationprofilecanvas.h
try:
    QgsElevationProfileCanvas.__attribute_docs__ = {'activeJobCountChanged': 'Emitted when the number of active background jobs changes.\n', 'canvasPointHovered': 'Emitted when the mouse hovers over the specified point (in canvas\ncoordinates).\n\nThe ``profilePoint`` argument gives the hovered profile point, which may\nbe snapped.\n'}
    QgsElevationProfileCanvas.__overridden_methods__ = ['crs', 'toMapCoordinates', 'toCanvasCoordinates', 'resizeEvent', 'paintEvent', 'panContentsBy', 'centerPlotOn', 'scalePlot', 'snapToPlot', 'zoomToRect', 'wheelZoom', 'mouseMoveEvent', 'refresh']
    QgsElevationProfileCanvas.__signal_arguments__ = {'activeJobCountChanged': ['count: int'], 'canvasPointHovered': ['point: QgsPointXY', 'profilePoint: QgsProfilePoint']}
    QgsElevationProfileCanvas.__group__ = ['elevation']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsellipsesymbollayerwidget.h
try:
    QgsEllipseSymbolLayerWidget.create = staticmethod(QgsEllipseSymbolLayerWidget.create)
    QgsEllipseSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsEllipseSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsembeddedsymbolrendererwidget.h
try:
    QgsEmbeddedSymbolRendererWidget.create = staticmethod(QgsEmbeddedSymbolRendererWidget.create)
    QgsEmbeddedSymbolRendererWidget.__overridden_methods__ = ['renderer', 'setContext', 'createExpressionContext']
    QgsEmbeddedSymbolRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgserrordialog.h
try:
    QgsErrorDialog.show = staticmethod(QgsErrorDialog.show)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsexpressionbuilderdialog.h
try:
    QgsExpressionBuilderDialog.__attribute_docs__ = {'allowEvalErrorsChanged': "Allow accepting expressions with evaluation errors. This can be useful\nwhen we are not able to provide an expression context of which we are\nsure it's completely populated.\n"}
    QgsExpressionBuilderDialog.__overridden_methods__ = ['done', 'accept', 'reject']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsexpressionbuilderwidget.h
QgsExpressionBuilderWidget.Flag.baseClass = QgsExpressionBuilderWidget
Flag = QgsExpressionBuilderWidget  # dirty hack since SIP seems to introduce the flags in module
try:
    QgsExpressionBuilderWidget.__attribute_docs__ = {'expressionParsed': 'Emitted when the user changes the expression in the widget. Users of\nthis widget should connect to this signal to decide if to let the user\ncontinue.\n\n:param isValid: Is ``True`` if the expression the user has typed is\n                valid.\n', 'evalErrorChanged': 'Will be set to ``True`` if the current expression text reported an eval\nerror with the context.\n', 'parserErrorChanged': 'Will be set to ``True`` if the current expression text reported a parser\nerror with the context.\n'}
    QgsExpressionBuilderWidget.__overridden_methods__ = ['showEvent']
    QgsExpressionBuilderWidget.__signal_arguments__ = {'expressionParsed': ['isValid: bool']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsexpressionhighlighter.h
try:
    QgsExpressionHighlighter.__overridden_methods__ = ['highlightBlock']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsexpressionlineedit.h
try:
    QgsExpressionLineEdit.__attribute_docs__ = {'expressionChanged': 'Emitted when the expression is changed.\n\n:param expression: new expression\n'}
    QgsExpressionLineEdit.__overridden_methods__ = ['changeEvent']
    QgsExpressionLineEdit.__signal_arguments__ = {'expressionChanged': ['expression: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsexpressionpreviewwidget.h
try:
    QgsExpressionPreviewWidget.__attribute_docs__ = {'expressionParsed': 'Emitted when the user changes the expression in the widget. Users of\nthis widget should connect to this signal to decide if to let the user\ncontinue.\n\n:param isValid: Is ``True`` if the expression the user has typed is\n                valid.\n', 'evalErrorChanged': 'Will be set to ``True`` if the current expression text reported an eval\nerror with the context.\n', 'parserErrorChanged': 'Will be set to ``True`` if the current expression text reported a parser\nerror with the context.\n', 'toolTipChanged': 'Emitted whenever the tool tip changed\n'}
    QgsExpressionPreviewWidget.__signal_arguments__ = {'expressionParsed': ['isValid: bool'], 'toolTipChanged': ['toolTip: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsexpressionselectiondialog.h
try:
    QgsExpressionSelectionDialog.__overridden_methods__ = ['closeEvent', 'done']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsexpressiontreeview.h
try:
    QgsExpressionItem.__attribute_docs__ = {'CUSTOM_SORT_ROLE': 'Custom sort order role', 'ITEM_TYPE_ROLE': 'Item type role', 'SEARCH_TAGS_ROLE': 'Search tags role', 'ITEM_NAME_ROLE': 'Item name role', 'LAYER_ID_ROLE': '\n.. versionadded:: 3.24'}
    QgsExpressionItem.__annotations__ = {'CUSTOM_SORT_ROLE': int, 'ITEM_TYPE_ROLE': int, 'SEARCH_TAGS_ROLE': int, 'ITEM_NAME_ROLE': int, 'LAYER_ID_ROLE': int}
except (NameError, AttributeError):
    pass
try:
    QgsExpressionTreeView.__attribute_docs__ = {'expressionItemDoubleClicked': 'Emitted when a expression item is double clicked\n', 'currentExpressionItemChanged': 'Emitter when the current expression item changed\n'}
    QgsExpressionTreeView.__signal_arguments__ = {'expressionItemDoubleClicked': ['text: str'], 'currentExpressionItemChanged': ['item: QgsExpressionItem']}
except (NameError, AttributeError):
    pass
try:
    QgsExpressionTreeView.MenuProvider.__virtual_methods__ = ['createContextMenu']
except (NameError, AttributeError):
    pass
try:
    QgsExpressionItemSearchProxy.__overridden_methods__ = ['filterAcceptsRow', 'lessThan']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsextentgroupbox.h
try:
    QgsExtentGroupBox.__attribute_docs__ = {'extentChanged': "Emitted when the widget's extent is changed.\n", 'extentLayerChanged': 'Emitted when the extent layer is changed.\n\n.. versionadded:: 3.44\n'}
    QgsExtentGroupBox.__signal_arguments__ = {'extentChanged': ['r: QgsRectangle'], 'extentLayerChanged': ['layer: QgsMapLayer']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsextentwidget.h
try:
    QgsExtentWidget.__attribute_docs__ = {'extentChanged': "Emitted when the widget's extent is changed.\n", 'validationChanged': "Emitted when the widget's validation state changes.\n", 'toggleDialogVisibility': 'Emitted when the parent dialog visibility must be changed (e.g. to\npermit access to the map canvas)\n', 'extentLayerChanged': 'Emitted when the extent layer is changed.\n\n.. versionadded:: 3.44\n'}
    QgsExtentWidget.__overridden_methods__ = ['dragEnterEvent', 'dragLeaveEvent', 'dropEvent', 'showEvent']
    QgsExtentWidget.__signal_arguments__ = {'extentChanged': ['r: QgsRectangle'], 'validationChanged': ['valid: bool'], 'toggleDialogVisibility': ['visible: bool'], 'extentLayerChanged': ['layer: QgsMapLayer']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsexternalresourcewidget.h
try:
    QgsExternalResourceWidget.__attribute_docs__ = {'valueChanged': 'Emitted as soon as the current document changes\n'}
    QgsExternalResourceWidget.__signal_arguments__ = {'valueChanged': ['value: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsexternalstoragefilewidget.h
try:
    QgsExternalStorageFileWidget.createFileWidgetScope = staticmethod(QgsExternalStorageFileWidget.createFileWidgetScope)
    QgsExternalStorageFileWidget.__overridden_methods__ = ['setReadOnly', 'updateLayout', 'setSelectedFileNames', 'dragEnterEvent', 'dropEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfeaturelistcombobox.h
try:
    QgsFeatureListComboBox.__attribute_docs__ = {'modelUpdated': 'The underlying model has been updated.\n\n.. versionadded:: 3.2\n', 'sourceLayerChanged': 'The layer from which features should be listed.\n', 'displayExpressionChanged': 'The display expression will be used to display features as well as the\nthe value to match the typed text against.\n', 'filterExpressionChanged': 'An additional expression to further restrict the available features.\nThis can be used to integrate additional spatial or other constraints.\n', 'formFeatureChanged': 'An attribute form feature to be used alongside the filter expression.\n\n.. versionadded:: 3.42.2\n', 'parentFormFeatureChanged': 'A parent attribute form feature to be used alongside the filter\nexpression.\n\n.. versionadded:: 3.42.2\n', 'identifierValueChanged': 'The identifier value of the currently selected feature. A value from the\nidentifierField.\n', 'identifierFieldChanged': 'Field name that will be used to uniquely identify the current feature.\nNormally the primary key of the layer.\n', 'allowNullChanged': 'Determines if a NULL value should be available in the list.\n', 'currentFeatureChanged': 'Emitted when the current feature changes\n\n.. versionadded:: 3.16.5\n', 'currentFeatureFoundChanged': 'Emitted when the feature picker model changes its feature ``found``\nstate\n\n.. versionadded:: 3.38\n'}
    QgsFeatureListComboBox.__overridden_methods__ = ['focusOutEvent', 'keyPressEvent']
    QgsFeatureListComboBox.__signal_arguments__ = {'currentFeatureFoundChanged': ['found: bool']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsfeaturelistmodel.h
try:
    QgsFeatureListModel.FeatureInfo.__attribute_docs__ = {'isNew': 'True if feature is a newly added feature.', 'isEdited': 'True if feature has been edited.'}
    QgsFeatureListModel.FeatureInfo.__annotations__ = {'isNew': bool, 'isEdited': bool}
    QgsFeatureListModel.FeatureInfo.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
try:
    QgsFeatureListModel.__virtual_methods__ = ['setSourceModel', 'mapToMaster', 'mapFromMaster', 'mapSelectionFromMaster', 'mapSelectionToMaster']
    QgsFeatureListModel.__overridden_methods__ = ['data', 'flags', 'mapToSource', 'mapFromSource', 'parent', 'columnCount', 'rowCount', 'fidToIndex']
    QgsFeatureListModel.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsfeaturelistview.h
try:
    QgsFeatureListView.__attribute_docs__ = {'currentEditSelectionChanged': 'Emitted whenever the current edit selection has been changed.\n\n:param feat: the feature, which will be edited.\n', 'currentEditSelectionProgressChanged': 'Emitted whenever the current edit selection has been changed.\n\n:param progress: the position of the feature in the list\n:param count: the number of features in the list\n\n.. versionadded:: 3.8\n', 'displayExpressionChanged': 'Emitted whenever the display expression is successfully changed\n\n:param expression: The expression that was applied\n', 'willShowContextMenu': 'Emitted when the context menu is created to add the specific actions to\nit\n\n:param menu: is the already created context menu\n:param atIndex: is the position of the current feature in the model\n'}
    QgsFeatureListView.__virtual_methods__ = ['setModel']
    QgsFeatureListView.__overridden_methods__ = ['mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent', 'keyPressEvent', 'contextMenuEvent', 'selectAll']
    QgsFeatureListView.__signal_arguments__ = {'currentEditSelectionChanged': ['feat: QgsFeature'], 'currentEditSelectionProgressChanged': ['progress: int', 'count: int'], 'displayExpressionChanged': ['expression: str'], 'willShowContextMenu': ['menu: QgsActionMenu', 'atIndex: QModelIndex']}
    QgsFeatureListView.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsfeaturelistviewdelegate.h
try:
    QgsFeatureListViewDelegate.__attribute_docs__ = {'editButtonClicked': 'Emitted when the edit button is clicked for the feature with matching\n``index``.\n'}
    QgsFeatureListViewDelegate.__overridden_methods__ = ['sizeHint', 'paint']
    QgsFeatureListViewDelegate.__signal_arguments__ = {'editButtonClicked': ['index: QModelIndex']}
    QgsFeatureListViewDelegate.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsfeaturemodel.h
try:
    QgsFeatureModel.__abstract_methods__ = ['fidToIndex']
    QgsFeatureModel.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfeaturepickerwidget.h
try:
    QgsFeaturePickerWidget.__attribute_docs__ = {'modelUpdated': 'The underlying model has been updated.\n', 'layerChanged': 'The layer from which features should be listed.\n', 'displayExpressionChanged': 'The display expression will be used to display features as well as the\nthe value to match the typed text against.\n', 'filterExpressionChanged': 'An additional expression to further restrict the available features.\nThis can be used to integrate additional spatial or other constraints.\n', 'featureChanged': 'Sends the feature as soon as it is chosen\n', 'allowNullChanged': 'Determines if a NULL value should be available in the list.\n', 'fetchGeometryChanged': 'Emitted when the fetching of the geometry changes\n', 'fetchLimitChanged': 'Emitted when the fetching limit for the feature request changes\n', 'showBrowserButtonsChanged': 'Emitted when showing the browser buttons changes\n'}
    QgsFeaturePickerWidget.__overridden_methods__ = ['focusOutEvent', 'keyPressEvent']
    QgsFeaturePickerWidget.__signal_arguments__ = {'featureChanged': ['feature: QgsFeature']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfeatureselectiondlg.h
try:
    QgsFeatureSelectionDlg.__overridden_methods__ = ['keyPressEvent', 'showEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsfeatureselectionmodel.h
try:
    QgsFeatureSelectionModel.__attribute_docs__ = {'requestRepaint': 'Request a repaint of the visible items of connected views. Views using\nthis model should connect to and properly process this signal.\n'}
    QgsFeatureSelectionModel.__virtual_methods__ = ['isSelected', 'selectFeatures', 'setFeatureSelectionManager']
    QgsFeatureSelectionModel.__overridden_methods__ = ['select']
    QgsFeatureSelectionModel.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/vector/qgsfieldcalculator.h
try:
    QgsFieldCalculator.__overridden_methods__ = ['accept']
    QgsFieldCalculator.__group__ = ['vector']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfieldcombobox.h
try:
    QgsFieldComboBox.__attribute_docs__ = {'fieldChanged': 'Emitted when the currently selected field changes.\n'}
    QgsFieldComboBox.__signal_arguments__ = {'fieldChanged': ['fieldName: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsfieldconditionalformatwidget.h
try:
    QgsFieldConditionalFormatWidget.__attribute_docs__ = {'rulesUpdated': 'Emitted when the conditional styling rules are updated.\n\nThe ``fieldName`` argument indicates the name of the field whose rules\nhave been modified, or an empty ``fieldName`` indicates that a row-based\nrule was updated.\n'}
    QgsFieldConditionalFormatWidget.defaultPresets = staticmethod(QgsFieldConditionalFormatWidget.defaultPresets)
    QgsFieldConditionalFormatWidget.__signal_arguments__ = {'rulesUpdated': ['fieldName: str']}
    QgsFieldConditionalFormatWidget.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
try:
    QgsEditConditionalFormatRuleWidget.__attribute_docs__ = {'ruleSaved': 'Emitted when a user has opted to save the current rule.\n', 'ruleDeleted': 'Emitted when a user has opted to deleted the current rule.\n', 'canceled': 'Emitted when a user has opted to cancel the rule modification.\n'}
    QgsEditConditionalFormatRuleWidget.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfielddomainwidget.h
try:
    QgsFieldDomainWidget.__attribute_docs__ = {'validityChanged': 'Emitted whenever the validity of the field domain configuration in the\nwidget changes.\n\n.. seealso:: :py:func:`isValid`\n'}
    QgsFieldDomainWidget.__signal_arguments__ = {'validityChanged': ['isValid: bool']}
except (NameError, AttributeError):
    pass
try:
    QgsFieldDomainDialog.__overridden_methods__ = ['accept']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfieldexpressionwidget.h
try:
    QgsFieldExpressionWidget.__attribute_docs__ = {'fieldChanged': 'fieldChanged signal with indication of the validity of the expression\n', 'allowEvalErrorsChanged': "Allow accepting expressions with evaluation errors. This can be useful\nwhen we are not able to provide an expression context of which we are\nsure it's completely populated.\n", 'buttonVisibleChanged': 'Emitted when the button visibility changes\n\n.. versionadded:: 3.36\n'}
    QgsFieldExpressionWidget.__overridden_methods__ = ['changeEvent', 'eventFilter']
    QgsFieldExpressionWidget.__signal_arguments__ = {'fieldChanged': ['fieldName: str', 'isValid: bool']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfieldmappingmodel.h
# monkey patching scoped based enum
QgsFieldMappingModel.ColumnDataIndex.SourceExpression.__doc__ = "Expression"
QgsFieldMappingModel.ColumnDataIndex.DestinationName.__doc__ = "Destination field name"
QgsFieldMappingModel.ColumnDataIndex.DestinationType.__doc__ = "Destination field type string"
QgsFieldMappingModel.ColumnDataIndex.DestinationLength.__doc__ = "Destination field length"
QgsFieldMappingModel.ColumnDataIndex.DestinationPrecision.__doc__ = "Destination field precision"
QgsFieldMappingModel.ColumnDataIndex.DestinationConstraints.__doc__ = "Destination field constraints"
QgsFieldMappingModel.ColumnDataIndex.DestinationAlias.__doc__ = "Destination alias"
QgsFieldMappingModel.ColumnDataIndex.DestinationComment.__doc__ = "Destination comment"
QgsFieldMappingModel.ColumnDataIndex.__doc__ = """The ColumnDataIndex enum represents the column index for the view

* ``SourceExpression``: Expression
* ``DestinationName``: Destination field name
* ``DestinationType``: Destination field type string
* ``DestinationLength``: Destination field length
* ``DestinationPrecision``: Destination field precision
* ``DestinationConstraints``: Destination field constraints
* ``DestinationAlias``: Destination alias
* ``DestinationComment``: Destination comment

"""
# --
QgsFieldMappingModel.ColumnDataIndex.baseClass = QgsFieldMappingModel
try:
    QgsFieldMappingModel.Field.__attribute_docs__ = {'originalName': 'The original name of the field', 'field': 'The field in its current status (it might have been renamed)', 'expression': 'The expression for the mapped field from the source fields'}
    QgsFieldMappingModel.Field.__annotations__ = {'originalName': str, 'field': 'QgsField', 'expression': str}
    QgsFieldMappingModel.Field.__doc__ = """The Field struct holds information about a mapped field"""
except (NameError, AttributeError):
    pass
try:
    QgsFieldMappingModel.__overridden_methods__ = ['rowCount', 'columnCount', 'data', 'headerData', 'flags', 'setData']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfieldmappingwidget.h
try:
    QgsFieldMappingWidget.__attribute_docs__ = {'changed': 'Emitted when the fields defined in the widget are changed.\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfieldvalidator.h
try:
    QgsFieldValidator.__overridden_methods__ = ['validate', 'fixup']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfieldvalueslineedit.h
try:
    QgsFieldValuesLineEdit.__attribute_docs__ = {'layerChanged': 'Emitted when the layer associated with the widget changes.\n\n:param layer: vector layer\n', 'attributeIndexChanged': 'Emitted when the field associated with the widget changes.\n\n:param index: new attribute index for field\n'}
    QgsFieldValuesLineEdit.__signal_arguments__ = {'layerChanged': ['layer: QgsVectorLayer'], 'attributeIndexChanged': ['index: int']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfilecontentsourcelineedit.h
try:
    QgsAbstractFileContentSourceLineEdit.__attribute_docs__ = {'sourceChanged': 'Emitted whenever the file source is changed in the widget.\n'}
    QgsAbstractFileContentSourceLineEdit.__signal_arguments__ = {'sourceChanged': ['source: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfiledownloaderdialog.h
try:
    QgsFileDownloaderDialog.__attribute_docs__ = {'downloadCompleted': 'Emitted when the download has completed successfully\n', 'downloadExited': 'Emitted always when the downloader exits\n', 'downloadCanceled': 'Emitted when the download was canceled by the user\n', 'downloadError': 'Emitted when an error makes the download fail\n', 'downloadProgress': 'Emitted when data are ready to be processed\n'}
    QgsFileDownloaderDialog.__signal_arguments__ = {'downloadError': ['errorMessages: List[str]'], 'downloadProgress': ['bytesReceived: int', 'bytesTotal: int']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfilewidget.h
QgsFileWidget.StorageMode.baseClass = QgsFileWidget
QgsFileWidget.RelativeStorage.baseClass = QgsFileWidget
try:
    QgsFileWidget.__attribute_docs__ = {'fileChanged': 'Emitted whenever the current file or directory ``path`` is changed.\n'}
    QgsFileWidget.splitFilePaths = staticmethod(QgsFileWidget.splitFilePaths)
    QgsFileWidget.isMultiFiles = staticmethod(QgsFileWidget.isMultiFiles)
    QgsFileWidget.__virtual_methods__ = ['setReadOnly', 'updateLayout', 'setSelectedFileNames']
    QgsFileWidget.__overridden_methods__ = ['minimumSizeHint']
    QgsFileWidget.__signal_arguments__ = {'fileChanged': ['path: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfilterlineedit.h
QgsFilterLineEdit.ClearMode.baseClass = QgsFilterLineEdit
try:
    QgsFilterLineEdit.__attribute_docs__ = {'cleared': 'Emitted when the widget is cleared\n\n.. seealso:: :py:func:`clearValue`\n', 'valueChanged': 'Same as :py:func:`~QgsFilterLineEdit.textChanged` but with support for\nnull values.\n\n:param value: The current text or null string if it matches the\n              :py:func:`~QgsFilterLineEdit.nullValue` property.\n', 'showSpinnerChanged': 'Show a spinner icon. This can be used for search boxes to indicate that\nsomething is going on in the background.\n', 'selectOnFocusChanged': 'Will select all text when this widget receives the focus.\n'}
    QgsFilterLineEdit.__virtual_methods__ = ['clearValue']
    QgsFilterLineEdit.__overridden_methods__ = ['event', 'focusInEvent', 'mouseReleaseEvent']
    QgsFilterLineEdit.__signal_arguments__ = {'valueChanged': ['value: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfindfilesbypatternwidget.h
try:
    QgsFindFilesByPatternWidget.__attribute_docs__ = {'findComplete': 'Emitted after files are found in the dialog.\n\nThe ``files`` argument contains a list of all matching files found. This\nmay be empty if no matching files were found.\n\n.. seealso:: :py:func:`files`\n'}
    QgsFindFilesByPatternWidget.__signal_arguments__ = {'findComplete': ['files: List[str]']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfloatingwidget.h
QgsFloatingWidget.AnchorPoint.baseClass = QgsFloatingWidget
try:
    QgsFloatingWidget.__attribute_docs__ = {'anchorWidgetChanged': 'Emitted when the anchor widget changes\n', 'anchorPointChanged': 'Emitted when the anchor point changes\n', 'anchorWidgetPointChanged': 'Emitted when the anchor widget point changes\n'}
    QgsFloatingWidget.__overridden_methods__ = ['showEvent', 'paintEvent', 'resizeEvent']
    QgsFloatingWidget.__signal_arguments__ = {'anchorWidgetChanged': ['widget: QWidget'], 'anchorPointChanged': ['point: QgsFloatingWidget.AnchorPoint'], 'anchorWidgetPointChanged': ['point: QgsFloatingWidget.AnchorPoint']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfocuswatcher.h
try:
    QgsFocusWatcher.__attribute_docs__ = {'focusChanged': "Emitted when parent object's focus changes.\n\n:param focused: ``True`` if object gained focus, ``False`` if object\n                lost focus\n", 'focusIn': 'Emitted when parent object gains focus.\n', 'focusOut': 'Emitted when parent object loses focus.\n'}
    QgsFocusWatcher.__overridden_methods__ = ['eventFilter']
    QgsFocusWatcher.__signal_arguments__ = {'focusChanged': ['focused: bool']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsfontbutton.h
QgsFontButton.Mode.baseClass = QgsFontButton
try:
    QgsFontButton.__attribute_docs__ = {'changed': "Emitted when the widget's text format settings are changed.\n"}
    QgsFontButton.__overridden_methods__ = ['minimumSizeHint', 'sizeHint', 'event', 'changeEvent', 'showEvent', 'resizeEvent', 'mousePressEvent', 'mouseMoveEvent', 'dragEnterEvent', 'dragLeaveEvent', 'dropEvent', 'wheelEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsformannotation.h
try:
    QgsFormAnnotation.create = staticmethod(QgsFormAnnotation.create)
    QgsFormAnnotation.__overridden_methods__ = ['clone', 'minimumFrameSize', 'writeXml', 'readXml', 'setAssociatedFeature', 'renderAnnotation']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/providers/gdal/qgsgdalcredentialoptionswidget.h
try:
    QgsGdalCredentialOptionsWidget.__attribute_docs__ = {'optionsChanged': 'Emitted when the credential options are changed in the widget.\n'}
    QgsGdalCredentialOptionsWidget.__group__ = ['providers', 'gdal']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsgeocoderlocatorfilter.h
try:
    QgsGeocoderLocatorFilter.__overridden_methods__ = ['clone']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsgeometryrubberband.h
try:
    QgsGeometryRubberBand.__virtual_methods__ = ['setGeometry']
    QgsGeometryRubberBand.__overridden_methods__ = ['updatePosition', 'paint']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsgeometrywidget.h
try:
    QgsGeometryWidget.__attribute_docs__ = {'geometryValueChanged': 'Emitted whenever the geometry value of the widget is changed.\n\n.. seealso:: :py:func:`geometryValue`\n\n.. seealso:: :py:func:`setGeometryValue`\n'}
    QgsGeometryWidget.__signal_arguments__ = {'geometryValueChanged': ['value: QgsReferencedGeometry']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsgpstoolsinterface.h
try:
    QgsGpsToolsInterface.__abstract_methods__ = ['setGpsPanelConnection', 'createFeatureFromGpsTrack', 'setGpsTrackLineSymbol']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsgradientcolorrampdialog.h
try:
    QgsGradientColorRampDialog.__attribute_docs__ = {'changed': 'Emitted when the dialog settings change\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsgradientstopeditor.h
try:
    QgsGradientStopEditor.__attribute_docs__ = {'changed': 'Emitted when the gradient ramp is changed by a user\n', 'selectedStopChanged': 'Emitted when the current selected stop changes.\n\n:param stop: details about newly selected stop\n'}
    QgsGradientStopEditor.__overridden_methods__ = ['sizeHint', 'paintEvent', 'mouseMoveEvent', 'mousePressEvent', 'mouseDoubleClickEvent', 'keyPressEvent', 'dragEnterEvent', 'dropEvent']
    QgsGradientStopEditor.__signal_arguments__ = {'selectedStopChanged': ['stop: QgsGradientStop']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsgraduatedhistogramwidget.h
try:
    QgsGraduatedHistogramWidget.__attribute_docs__ = {'rangesModified': 'Emitted when the user modifies the graduated ranges using the histogram\nwidget.\n\n:param rangesAdded: ``True`` if the user has added ranges, ``False`` if\n                    the user has just modified existing range breaks\n'}
    QgsGraduatedHistogramWidget.__overridden_methods__ = ['drawHistogram']
    QgsGraduatedHistogramWidget.__signal_arguments__ = {'rangesModified': ['rangesAdded: bool']}
    QgsGraduatedHistogramWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsgraduatedsymbolrendererwidget.h
try:
    QgsGraduatedSymbolRendererWidget.create = staticmethod(QgsGraduatedSymbolRendererWidget.create)
    QgsGraduatedSymbolRendererWidget.__overridden_methods__ = ['renderer', 'setContext', 'createExpressionContext', 'setSymbolLevels', 'pasteSymbolToSelection', 'selectedSymbols', 'refreshSymbolView', 'keyPressEvent']
    QgsGraduatedSymbolRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsgroupwmsdatadialog.h
try:
    QgsGroupWmsDataDialog.__overridden_methods__ = ['accept']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsgui.h
QgsGui.ProjectCrsBehavior.baseClass = QgsGui
try:
    QgsGui.__attribute_docs__ = {'optionsChanged': 'This signal is emitted whenever the application options have been\nchanged.\n\nThis signal is a "blanket" signal, and will be emitted whenever the\noptions dialog has been accepted regardless of whether or not individual\nsettings are changed. It is designed as a "last resort" fallback only,\nallowing widgets to respond to possible settings changes.\n\n.. versionadded:: 3.16\n'}
    QgsGui.instance = staticmethod(QgsGui.instance)
    QgsGui.settingsRegistryGui = staticmethod(QgsGui.settingsRegistryGui)
    QgsGui.editorWidgetRegistry = staticmethod(QgsGui.editorWidgetRegistry)
    QgsGui.sourceSelectProviderRegistry = staticmethod(QgsGui.sourceSelectProviderRegistry)
    QgsGui.shortcutsManager = staticmethod(QgsGui.shortcutsManager)
    QgsGui.layerTreeEmbeddedWidgetRegistry = staticmethod(QgsGui.layerTreeEmbeddedWidgetRegistry)
    QgsGui.mapLayerActionRegistry = staticmethod(QgsGui.mapLayerActionRegistry)
    QgsGui.layoutItemGuiRegistry = staticmethod(QgsGui.layoutItemGuiRegistry)
    QgsGui.annotationItemGuiRegistry = staticmethod(QgsGui.annotationItemGuiRegistry)
    QgsGui.advancedDigitizingToolsRegistry = staticmethod(QgsGui.advancedDigitizingToolsRegistry)
    QgsGui.processingGuiRegistry = staticmethod(QgsGui.processingGuiRegistry)
    QgsGui.numericFormatGuiRegistry = staticmethod(QgsGui.numericFormatGuiRegistry)
    QgsGui.codeEditorColorSchemeRegistry = staticmethod(QgsGui.codeEditorColorSchemeRegistry)
    QgsGui.processingRecentAlgorithmLog = staticmethod(QgsGui.processingRecentAlgorithmLog)
    QgsGui.processingFavoriteAlgorithmManager = staticmethod(QgsGui.processingFavoriteAlgorithmManager)
    QgsGui.dataItemGuiProviderRegistry = staticmethod(QgsGui.dataItemGuiProviderRegistry)
    QgsGui.projectStorageGuiRegistry = staticmethod(QgsGui.projectStorageGuiRegistry)
    QgsGui.providerGuiRegistry = staticmethod(QgsGui.providerGuiRegistry)
    QgsGui.sensorGuiRegistry = staticmethod(QgsGui.sensorGuiRegistry)
    QgsGui.subsetStringEditorProviderRegistry = staticmethod(QgsGui.subsetStringEditorProviderRegistry)
    QgsGui.sourceWidgetProviderRegistry = staticmethod(QgsGui.sourceWidgetProviderRegistry)
    QgsGui.relationWidgetRegistry = staticmethod(QgsGui.relationWidgetRegistry)
    QgsGui.historyProviderRegistry = staticmethod(QgsGui.historyProviderRegistry)
    QgsGui.settingsEditorWidgetRegistry = staticmethod(QgsGui.settingsEditorWidgetRegistry)
    QgsGui.enableAutoGeometryRestore = staticmethod(QgsGui.enableAutoGeometryRestore)
    QgsGui.windowManager = staticmethod(QgsGui.windowManager)
    QgsGui.setWindowManager = staticmethod(QgsGui.setWindowManager)
    QgsGui.inputControllerManager = staticmethod(QgsGui.inputControllerManager)
    QgsGui.storedQueryManager = staticmethod(QgsGui.storedQueryManager)
    QgsGui.higFlags = staticmethod(QgsGui.higFlags)
    QgsGui.sampleColor = staticmethod(QgsGui.sampleColor)
    QgsGui.findScreenAt = staticmethod(QgsGui.findScreenAt)
    QgsGui.hasWebEngine = staticmethod(QgsGui.hasWebEngine)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsheatmaprendererwidget.h
try:
    QgsHeatmapRendererWidget.create = staticmethod(QgsHeatmapRendererWidget.create)
    QgsHeatmapRendererWidget.__overridden_methods__ = ['renderer', 'setContext', 'createExpressionContext']
    QgsHeatmapRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgshelp.h
try:
    QgsHelp.openHelp = staticmethod(QgsHelp.openHelp)
    QgsHelp.helpUrl = staticmethod(QgsHelp.helpUrl)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgshighlight.h
try:
    QgsHighlight.__overridden_methods__ = ['updatePosition', 'paint']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgshighlightablelineedit.h
try:
    QgsHighlightableLineEdit.__overridden_methods__ = ['paintEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgshillshaderendererwidget.h
try:
    QgsHillshadeRendererWidget.create = staticmethod(QgsHillshadeRendererWidget.create)
    QgsHillshadeRendererWidget.__overridden_methods__ = ['renderer']
    QgsHillshadeRendererWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgshistogramwidget.h
try:
    QgsHistogramWidget.__virtual_methods__ = ['drawHistogram']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/history/qgshistoryentry.h
try:
    QgsHistoryEntry.__attribute_docs__ = {'id': 'Entry ID.\n\n.. versionadded:: 3.32', 'timestamp': 'Entry timestamp', 'providerId': 'Associated history provider ID', 'entry': 'Entry details.\n\nEntries details are stored as a free-form map. Interpretation of this map is the responsibility of the\nassociated history provider.'}
    QgsHistoryEntry.__annotations__ = {'id': int, 'timestamp': 'QDateTime', 'providerId': str, 'entry': 'Dict[str, object]'}
    QgsHistoryEntry.__group__ = ['history']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/history/qgshistoryentrymodel.h
try:
    QgsHistoryEntryModel.__overridden_methods__ = ['rowCount', 'columnCount', 'index', 'parent', 'data', 'flags']
    QgsHistoryEntryModel.__group__ = ['history']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/history/qgshistoryentrynode.h
try:
    QgsHistoryEntryNode.__virtual_methods__ = ['childCount', 'html', 'createWidget', 'doubleClicked', 'populateContextMenu', 'matchesString']
    QgsHistoryEntryNode.__abstract_methods__ = ['data']
    QgsHistoryEntryNode.__group__ = ['history']
except (NameError, AttributeError):
    pass
try:
    QgsHistoryEntryGroup.__virtual_methods__ = ['childCount']
    QgsHistoryEntryGroup.__group__ = ['history']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/history/qgshistoryprovider.h
try:
    QgsAbstractHistoryProvider.__virtual_methods__ = ['createNodeForEntry', 'updateNodeForEntry']
    QgsAbstractHistoryProvider.__abstract_methods__ = ['id']
    QgsAbstractHistoryProvider.__group__ = ['history']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/history/qgshistoryproviderregistry.h
try:
    QgsHistoryProviderRegistry.HistoryEntryOptions.__attribute_docs__ = {'storageBackends': 'Target storage backends'}
    QgsHistoryProviderRegistry.HistoryEntryOptions.__annotations__ = {'storageBackends': 'Qgis.HistoryProviderBackends'}
    QgsHistoryProviderRegistry.HistoryEntryOptions.__group__ = ['history']
except (NameError, AttributeError):
    pass
try:
    QgsHistoryProviderRegistry.__attribute_docs__ = {'entryAdded': 'Emitted when an ``entry`` is added.\n\n.. versionadded:: 3.32\n', 'entryUpdated': 'Emitted when an ``entry`` is updated.\n\n.. versionadded:: 3.32\n', 'historyCleared': 'Emitted when the history is cleared for a ``backend``.\n\nIf ``providerId`` is non-empty then the history has only been cleared\nfor the specified provider.\n\n.. versionadded:: 3.32\n'}
    QgsHistoryProviderRegistry.userHistoryDbPath = staticmethod(QgsHistoryProviderRegistry.userHistoryDbPath)
    QgsHistoryProviderRegistry.__signal_arguments__ = {'entryAdded': ['id: int', 'entry: QgsHistoryEntry', 'backend: Qgis.HistoryProviderBackend'], 'entryUpdated': ['id: int', 'entry: Dict[str, object]', 'backend: Qgis.HistoryProviderBackend'], 'historyCleared': ['backend: Qgis.HistoryProviderBackend', 'providerId: str']}
    QgsHistoryProviderRegistry.__group__ = ['history']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/history/qgshistorywidget.h
try:
    QgsHistoryWidget.__group__ = ['history']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/history/qgshistorywidgetcontext.h
try:
    QgsHistoryWidgetContext.__group__ = ['history']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgshtmlwidgetwrapper.h
try:
    QgsHtmlWidgetWrapper.__overridden_methods__ = ['valid', 'createWidget', 'initWidget', 'setFeature']
    QgsHtmlWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsidentifymenu.h
try:
    QgsIdentifyMenu.findFeaturesOnCanvas = staticmethod(QgsIdentifyMenu.findFeaturesOnCanvas)
    QgsIdentifyMenu.styleHighlight = staticmethod(QgsIdentifyMenu.styleHighlight)
    QgsIdentifyMenu.__overridden_methods__ = ['closeEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsifeatureselectionmanager.h
try:
    QgsIFeatureSelectionManager.__attribute_docs__ = {'selectionChanged': 'Emitted when selection was changed.\n\n:param selected: Newly selected feature ids\n:param deselected: Ids of all features which have previously been\n                   selected but are not any more\n:param clearAndSelect: In case this is set to ``True``, the old\n                       selection was dismissed and the new selection\n                       corresponds to selected\n'}
    QgsIFeatureSelectionManager.__abstract_methods__ = ['selectedFeatureCount', 'select', 'deselect', 'setSelectedFeatures']
    QgsIFeatureSelectionManager.__signal_arguments__ = {'selectionChanged': ['selected: QgsFeatureIds', 'deselected: QgsFeatureIds', 'clearAndSelect: bool']}
    QgsIFeatureSelectionManager.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/inputcontroller/qgsinputcontrollermanager.h
try:
    QgsInputControllerManager.__group__ = ['inputcontroller']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsinterpolatedlinesymbollayerwidget.h
try:
    QgsInterpolatedLineSymbolLayerWidget.create = staticmethod(QgsInterpolatedLineSymbolLayerWidget.create)
    QgsInterpolatedLineSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsInterpolatedLineSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsinvertedpolygonrendererwidget.h
try:
    QgsInvertedPolygonRendererWidget.create = staticmethod(QgsInvertedPolygonRendererWidget.create)
    QgsInvertedPolygonRendererWidget.__overridden_methods__ = ['renderer', 'setContext', 'setDockMode']
    QgsInvertedPolygonRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsjsoneditwidget.h
# monkey patching scoped based enum
QgsJsonEditWidget.View.Text.__doc__ = "JSON data displayed as text."
QgsJsonEditWidget.View.Tree.__doc__ = "JSON data displayed as tree. Tree view is disabled for invalid JSON data."
QgsJsonEditWidget.View.__doc__ = """View mode, text or tree.

* ``Text``: JSON data displayed as text.
* ``Tree``: JSON data displayed as tree. Tree view is disabled for invalid JSON data.

"""
# --
# monkey patching scoped based enum
QgsJsonEditWidget.FormatJson.Indented.__doc__ = "JSON data formatted with regular indentation"
QgsJsonEditWidget.FormatJson.Compact.__doc__ = "JSON data formatted as a compact one line string"
QgsJsonEditWidget.FormatJson.Disabled.__doc__ = "JSON data is not formatted"
QgsJsonEditWidget.FormatJson.__doc__ = """Format mode in the text view

* ``Indented``: JSON data formatted with regular indentation
* ``Compact``: JSON data formatted as a compact one line string
* ``Disabled``: JSON data is not formatted

"""
# --
try:
    QgsJsonEditWidget.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgskeyvaluewidget.h
try:
    QgsKeyValueWidget.__overridden_methods__ = ['setReadOnly']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/labeling/qgslabelingengineruleswidget.h
try:
    QgsLabelingEngineRulesWidget.__attribute_docs__ = {'changed': 'Emitted when the rules configured in the widget are changed.\n'}
    QgsLabelingEngineRulesWidget.__group__ = ['labeling']
except (NameError, AttributeError):
    pass
try:
    QgsLabelingEngineRulesDialog.__group__ = ['labeling']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/labeling/qgslabelingenginerulewidget.h
try:
    QgsLabelingEngineRuleWidget.__attribute_docs__ = {'changed': 'Emitted whenever the configuration of the rule is changed.\n'}
    QgsLabelingEngineRuleWidget.__abstract_methods__ = ['setRule', 'rule']
    QgsLabelingEngineRuleWidget.__group__ = ['labeling']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/labeling/qgslabellineanchorwidget.h
try:
    QgsLabelLineAnchorWidget.__overridden_methods__ = ['updateDataDefinedProperties']
    QgsLabelLineAnchorWidget.__group__ = ['labeling']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/labeling/qgslabelobstaclesettingswidget.h
try:
    QgsLabelObstacleSettingsWidget.__overridden_methods__ = ['setGeometryType', 'updateDataDefinedProperties']
    QgsLabelObstacleSettingsWidget.__group__ = ['labeling']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/labeling/qgslabelremoveduplicatesettingswidget.h
try:
    QgsLabelRemoveDuplicatesSettingsWidget.__overridden_methods__ = ['setGeometryType', 'updateDataDefinedProperties']
    QgsLabelRemoveDuplicatesSettingsWidget.__group__ = ['labeling']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/labeling/qgslabelsettingswidgetbase.h
try:
    QgsLabelSettingsWidgetBase.__attribute_docs__ = {'changed': 'Emitted when any of the settings described by the widget are changed.\n', 'auxiliaryFieldCreated': 'Emitted when an auxiliary field is created in the widget.\n'}
    QgsLabelSettingsWidgetBase.__virtual_methods__ = ['setContext', 'setGeometryType', 'updateDataDefinedProperties']
    QgsLabelSettingsWidgetBase.__overridden_methods__ = ['createExpressionContext']
    QgsLabelSettingsWidgetBase.__group__ = ['labeling']
except (NameError, AttributeError):
    pass
try:
    QgsLabelSettingsWidgetDialog.__group__ = ['labeling']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgslayermetadataresultsmodel.h
QgsLayerMetadataResultsModel.Roles = QgsLayerMetadataResultsModel.CustomRole
# monkey patching scoped based enum
QgsLayerMetadataResultsModel.Metadata = QgsLayerMetadataResultsModel.CustomRole.Metadata
QgsLayerMetadataResultsModel.Metadata.is_monkey_patched = True
QgsLayerMetadataResultsModel.Metadata.__doc__ = "Layer metadata role"
QgsLayerMetadataResultsModel.CustomRole.__doc__ = """The Roles enum represents the user roles for the model.

.. note::

   Prior to QGIS 3.36 this was available as QgsLayerMetadataResultsModel.Roles

.. versionadded:: 3.36

* ``Metadata``: Layer metadata role

"""
# --
QgsLayerMetadataResultsModel.CustomRole.baseClass = QgsLayerMetadataResultsModel
try:
    QgsLayerMetadataResultsModel.__attribute_docs__ = {'progressChanged': 'Emitted when the progress changed to ``progress``.\n'}
    QgsLayerMetadataResultsModel.__overridden_methods__ = ['rowCount', 'columnCount', 'data', 'headerData']
    QgsLayerMetadataResultsModel.__signal_arguments__ = {'progressChanged': ['progress: int']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgslayermetadataresultsproxymodel.h
try:
    QgsLayerMetadataResultsProxyModel.__overridden_methods__ = ['filterAcceptsRow']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgslayermetadatasearchwidget.h
try:
    QgsLayerMetadataSearchWidget.__overridden_methods__ = ['setMapCanvas', 'refresh', 'addButtonClicked', 'reset', 'showEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgslayerpropertiesdialog.h
try:
    QgsLayerPropertiesDialog.__virtual_methods__ = ['addPropertiesPageFactory', 'rollback']
    QgsLayerPropertiesDialog.__overridden_methods__ = ['optionsStackedWidget_CurrentChanged']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgslayerpropertieswidget.h
try:
    QgsLayerPropertiesWidget.__attribute_docs__ = {'changed': 'Emitted when the symbol layer configuration is changed in the widget.\n', 'changeLayer': 'Emitted when the symbol ``layer`` is changed in the widget.\n'}
    QgsLayerPropertiesWidget.__overridden_methods__ = ['setDockMode', 'createExpressionContext']
    QgsLayerPropertiesWidget.__signal_arguments__ = {'changeLayer': ['layer: QgsSymbolLayer']}
    QgsLayerPropertiesWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layertree/qgslayertreeembeddedconfigwidget.h
try:
    QgsLayerTreeEmbeddedConfigWidget.__group__ = ['layertree']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layertree/qgslayertreeembeddedwidgetregistry.h
try:
    QgsLayerTreeEmbeddedWidgetProvider.__abstract_methods__ = ['id', 'name', 'createWidget', 'supportsLayer']
    QgsLayerTreeEmbeddedWidgetProvider.__group__ = ['layertree']
except (NameError, AttributeError):
    pass
try:
    QgsLayerTreeEmbeddedWidgetRegistry.__group__ = ['layertree']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layertree/qgslayertreemapcanvasbridge.h
try:
    QgsLayerTreeMapCanvasBridge.__attribute_docs__ = {'canvasLayersChanged': 'Emitted when the set of layers (or order of layers) visible in the\ncanvas changes.\n'}
    QgsLayerTreeMapCanvasBridge.__signal_arguments__ = {'canvasLayersChanged': ['layers: List[QgsMapLayer]']}
    QgsLayerTreeMapCanvasBridge.__group__ = ['layertree']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layertree/qgslayertreeview.h
try:
    QgsLayerTreeView.__attribute_docs__ = {'currentLayerChanged': 'Emitted when a current layer is changed\n', 'datasetsDropped': 'Emitted when datasets are dropped onto the layer tree view\n', 'contextMenuAboutToShow': 'Emitted when the context menu is about to show.\n\nAllows customization of the menu.\n\n.. versionadded:: 3.32\n'}
    QgsLayerTreeView.__overridden_methods__ = ['setModel', 'contextMenuEvent', 'mouseDoubleClickEvent', 'mouseReleaseEvent', 'keyPressEvent', 'dragEnterEvent', 'dragMoveEvent', 'dropEvent', 'resizeEvent']
    QgsLayerTreeView.__signal_arguments__ = {'currentLayerChanged': ['layer: QgsMapLayer'], 'datasetsDropped': ['event: QDropEvent'], 'contextMenuAboutToShow': ['menu: QMenu']}
    QgsLayerTreeView.__group__ = ['layertree']
except (NameError, AttributeError):
    pass
try:
    QgsLayerTreeViewMenuProvider.__abstract_methods__ = ['createContextMenu']
    QgsLayerTreeViewMenuProvider.__group__ = ['layertree']
except (NameError, AttributeError):
    pass
try:
    QgsLayerTreeProxyModel.__overridden_methods__ = ['filterAcceptsRow']
    QgsLayerTreeProxyModel.__group__ = ['layertree']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layertree/qgslayertreeviewdefaultactions.h
try:
    QgsLayerTreeViewDefaultActions.__group__ = ['layertree']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layertree/qgslayertreeviewindicator.h
try:
    QgsLayerTreeViewIndicator.__attribute_docs__ = {'clicked': 'Emitted when user clicks on the indicator\n', 'changed': 'Emitted when the indicator changes state (e.g. icon).\n\n.. versionadded:: 3.10\n'}
    QgsLayerTreeViewIndicator.__signal_arguments__ = {'clicked': ['index: QModelIndex']}
    QgsLayerTreeViewIndicator.__group__ = ['layertree']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutcombobox.h
try:
    QgsLayoutComboBox.__attribute_docs__ = {'layoutChanged': 'Emitted whenever the currently selected layout changes\n'}
    QgsLayoutComboBox.__signal_arguments__ = {'layoutChanged': ['layout: QgsMasterLayoutInterface']}
    QgsLayoutComboBox.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutcustomdrophandler.h
try:
    QgsLayoutCustomDropHandler.__virtual_methods__ = ['handleFileDrop', 'handlePaste']
    QgsLayoutCustomDropHandler.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutdesignerinterface.h
try:
    QgsLayoutDesignerInterface.ExportResults.__attribute_docs__ = {'result': 'Result/error code of export.', 'labelingResults': 'Returns the labeling results for all map items included in the export. Map keys are the item UUIDs (see :py:func:`QgsLayoutItem.uuid()`).\n\nOwnership of the results remains with the layout designer.'}
    QgsLayoutDesignerInterface.ExportResults.__annotations__ = {'result': 'QgsLayoutExporter.ExportResult', 'labelingResults': 'Dict[str, QgsLabelingResults]'}
    QgsLayoutDesignerInterface.ExportResults.__group__ = ['layout']
except (NameError, AttributeError):
    pass
try:
    QgsLayoutDesignerInterface.__attribute_docs__ = {'layoutExported': 'Emitted whenever a layout is exported from the layout designer.\n\nThe results of the export can be retrieved by calling\n:py:func:`~QgsLayoutDesignerInterface.lastExportResults`.\n\n.. versionadded:: 3.20\n', 'mapPreviewRefreshed': "Emitted when a ``map`` item's preview has been refreshed.\n\n.. versionadded:: 3.20\n"}
    QgsLayoutDesignerInterface.__abstract_methods__ = ['layout', 'masterLayout', 'window', 'view', 'messageBar', 'selectItems', 'setAtlasPreviewEnabled', 'atlasPreviewEnabled', 'setAtlasFeature', 'showItemOptions', 'layoutMenu', 'editMenu', 'viewMenu', 'itemsMenu', 'atlasMenu', 'reportMenu', 'settingsMenu', 'layoutToolbar', 'navigationToolbar', 'actionsToolbar', 'atlasToolbar', 'addDockWidget', 'removeDockWidget', 'activateTool', 'lastExportResults', 'close', 'showRulers']
    QgsLayoutDesignerInterface.__signal_arguments__ = {'mapPreviewRefreshed': ['map: QgsLayoutItemMap']}
    QgsLayoutDesignerInterface.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutitemcombobox.h
try:
    QgsLayoutItemComboBox.__attribute_docs__ = {'itemChanged': 'Emitted whenever the currently selected item changes\n'}
    QgsLayoutItemComboBox.__signal_arguments__ = {'itemChanged': ['item: QgsLayoutItem']}
    QgsLayoutItemComboBox.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutitemguiregistry.h
try:
    QgsLayoutItemGuiGroup.__attribute_docs__ = {'id': 'Unique (untranslated) group ID string.', 'name': 'Translated group name.', 'icon': 'Icon for group.'}
    QgsLayoutItemGuiGroup.__annotations__ = {'id': str, 'name': str, 'icon': 'QIcon'}
    QgsLayoutItemGuiGroup.__group__ = ['layout']
except (NameError, AttributeError):
    pass
try:
    QgsLayoutItemGuiRegistry.__attribute_docs__ = {'typeAdded': 'Emitted whenever a new item type is added to the registry, with the\nspecified ``metadataId``.\n'}
    QgsLayoutItemGuiRegistry.__signal_arguments__ = {'typeAdded': ['metadataId: int']}
    QgsLayoutItemGuiRegistry.__group__ = ['layout']
except (NameError, AttributeError):
    pass
try:
    QgsLayoutItemAbstractGuiMetadata.__virtual_methods__ = ['creationIcon', 'createItemWidget', 'createRubberBand', 'createNodeRubberBand', 'createItem', 'newItemAddedToLayout', 'handleDoubleClick']
    QgsLayoutItemAbstractGuiMetadata.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutitemwidget.h
try:
    QgsLayoutItemBaseWidget.__virtual_methods__ = ['setReportTypeString', 'setDesignerInterface', 'setMasterLayout', 'setNewItem']
    QgsLayoutItemBaseWidget.__group__ = ['layout']
except (NameError, AttributeError):
    pass
try:
    QgsLayoutConfigObject.__group__ = ['layout']
except (NameError, AttributeError):
    pass
try:
    QgsLayoutItemPropertiesWidget.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutnewitempropertiesdialog.h
try:
    QgsLayoutItemPropertiesDialog.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutruler.h
try:
    QgsLayoutRuler.__attribute_docs__ = {'cursorPosChanged': 'Emitted when mouse cursor coordinates change\n'}
    QgsLayoutRuler.__overridden_methods__ = ['minimumSizeHint', 'paintEvent', 'mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent']
    QgsLayoutRuler.__signal_arguments__ = {'cursorPosChanged': ['position: QPointF']}
    QgsLayoutRuler.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutunitscombobox.h
try:
    QgsLayoutUnitsComboBox.__attribute_docs__ = {'changed': 'Emitted when the ``unit`` is changed.\n'}
    QgsLayoutUnitsComboBox.__signal_arguments__ = {'changed': ['unit: int']}
    QgsLayoutUnitsComboBox.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutview.h
try:
    QgsLayoutView.__attribute_docs__ = {'layoutSet': 'Emitted when a ``layout`` is set for the view.\n\n.. seealso:: :py:func:`currentLayout`\n\n.. seealso:: :py:func:`setCurrentLayout`\n', 'toolSet': 'Emitted when the current ``tool`` is changed.\n\n.. seealso:: :py:func:`setTool`\n', 'zoomLevelChanged': 'Emitted whenever the zoom level of the view is changed.\n', 'cursorPosChanged': 'Emitted when the mouse cursor coordinates change within the view. The\n``layoutPoint`` argument indicates the cursor position within the layout\ncoordinate system.\n', 'pageChanged': 'Emitted when the page visible in the view is changed. This signal\nconsiders the page at the center of the view as the current visible\npage.\n\n.. seealso:: :py:func:`currentPage`\n', 'statusMessage': "Emitted when the view has a ``message`` for display in a parent window's\nstatus bar.\n\n.. seealso:: :py:func:`pushStatusMessage`\n", 'itemFocused': 'Emitted when an ``item`` is "focused" in the view, i.e. it becomes the\nactive item and should have its properties displayed in any designer\nwindows.\n', 'willBeDeleted': 'Emitted in the destructor when the view is about to be deleted, but is\nstill in a perfectly valid state.\n'}
    QgsLayoutView.__overridden_methods__ = ['mousePressEvent', 'mouseReleaseEvent', 'mouseMoveEvent', 'mouseDoubleClickEvent', 'wheelEvent', 'keyPressEvent', 'keyReleaseEvent', 'resizeEvent', 'scrollContentsBy', 'dragEnterEvent', 'paintEvent']
    QgsLayoutView.__signal_arguments__ = {'layoutSet': ['layout: QgsLayout'], 'toolSet': ['tool: QgsLayoutViewTool'], 'cursorPosChanged': ['layoutPoint: QPointF'], 'pageChanged': ['page: int'], 'statusMessage': ['message: str'], 'itemFocused': ['item: QgsLayoutItem']}
    QgsLayoutView.__group__ = ['layout']
except (NameError, AttributeError):
    pass
try:
    QgsLayoutViewMenuProvider.__abstract_methods__ = ['createContextMenu']
    QgsLayoutViewMenuProvider.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewmouseevent.h
try:
    QgsLayoutViewMouseEvent.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewrubberband.h
try:
    QgsLayoutViewRubberBand.__attribute_docs__ = {'sizeChanged': 'Emitted when the size of the rubber band is changed. The ``size``\nargument gives a translated string describing the new rubber band size,\nwith a format which differs per subclass (e.g. rectangles may describe a\nsize using width and height, while circles may describe a size by\nradius).\n'}
    QgsLayoutViewRubberBand.__abstract_methods__ = ['create', 'start', 'update', 'finish']
    QgsLayoutViewRubberBand.__signal_arguments__ = {'sizeChanged': ['size: str']}
    QgsLayoutViewRubberBand.__group__ = ['layout']
except (NameError, AttributeError):
    pass
try:
    QgsLayoutViewRectangularRubberBand.__overridden_methods__ = ['create', 'start', 'update', 'finish']
    QgsLayoutViewRectangularRubberBand.__group__ = ['layout']
except (NameError, AttributeError):
    pass
try:
    QgsLayoutViewEllipticalRubberBand.__overridden_methods__ = ['create', 'start', 'update', 'finish']
    QgsLayoutViewEllipticalRubberBand.__group__ = ['layout']
except (NameError, AttributeError):
    pass
try:
    QgsLayoutViewTriangleRubberBand.__overridden_methods__ = ['create', 'start', 'update', 'finish']
    QgsLayoutViewTriangleRubberBand.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewtool.h
try:
    QgsLayoutViewTool.__attribute_docs__ = {'activated': 'Emitted when the tool is activated.\n', 'deactivated': 'Emitted when the tool is deactivated.\n', 'itemFocused': 'Emitted when an ``item`` is "focused" by the tool, i.e. it should become\nthe active item and should have its properties displayed in any designer\nwindows.\n'}
    QgsLayoutViewTool.__virtual_methods__ = ['layoutMoveEvent', 'layoutDoubleClickEvent', 'layoutPressEvent', 'layoutReleaseEvent', 'wheelEvent', 'keyPressEvent', 'keyReleaseEvent', 'activate', 'deactivate', 'ignoredSnapItems']
    QgsLayoutViewTool.__signal_arguments__ = {'itemFocused': ['item: QgsLayoutItem']}
    QgsLayoutViewTool.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewtooladditem.h
try:
    QgsLayoutViewToolAddItem.__attribute_docs__ = {'createdItem': 'Emitted when an item has been created using the tool.\n'}
    QgsLayoutViewToolAddItem.__overridden_methods__ = ['layoutPressEvent', 'layoutMoveEvent', 'layoutReleaseEvent', 'activate', 'deactivate']
    QgsLayoutViewToolAddItem.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewtooladdnodeitem.h
try:
    QgsLayoutViewToolAddNodeItem.__attribute_docs__ = {'createdItem': 'Emitted when an item has been created using the tool.\n'}
    QgsLayoutViewToolAddNodeItem.__overridden_methods__ = ['layoutPressEvent', 'layoutMoveEvent', 'layoutReleaseEvent', 'keyPressEvent', 'deactivate']
    QgsLayoutViewToolAddNodeItem.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewtooleditnodes.h
try:
    QgsLayoutViewToolEditNodes.__overridden_methods__ = ['activate', 'layoutPressEvent', 'layoutMoveEvent', 'layoutReleaseEvent', 'layoutDoubleClickEvent', 'keyPressEvent', 'deactivate', 'ignoredSnapItems']
    QgsLayoutViewToolEditNodes.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewtoolmoveitemcontent.h
try:
    QgsLayoutViewToolMoveItemContent.__overridden_methods__ = ['layoutPressEvent', 'layoutMoveEvent', 'layoutReleaseEvent', 'wheelEvent']
    QgsLayoutViewToolMoveItemContent.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewtoolpan.h
try:
    QgsLayoutViewToolPan.__overridden_methods__ = ['layoutPressEvent', 'layoutMoveEvent', 'layoutReleaseEvent', 'deactivate']
    QgsLayoutViewToolPan.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewtoolselect.h
try:
    QgsLayoutViewToolSelect.__overridden_methods__ = ['layoutPressEvent', 'layoutMoveEvent', 'layoutReleaseEvent', 'wheelEvent', 'keyPressEvent', 'deactivate']
    QgsLayoutViewToolSelect.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewtooltemporarykeypan.h
try:
    QgsLayoutViewToolTemporaryKeyPan.__overridden_methods__ = ['layoutMoveEvent', 'keyReleaseEvent', 'activate']
    QgsLayoutViewToolTemporaryKeyPan.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewtooltemporarykeyzoom.h
try:
    QgsLayoutViewToolTemporaryKeyZoom.__overridden_methods__ = ['layoutReleaseEvent', 'keyPressEvent', 'keyReleaseEvent', 'activate']
    QgsLayoutViewToolTemporaryKeyZoom.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewtooltemporarymousepan.h
try:
    QgsLayoutViewToolTemporaryMousePan.__overridden_methods__ = ['layoutMoveEvent', 'layoutReleaseEvent', 'activate']
    QgsLayoutViewToolTemporaryMousePan.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/layout/qgslayoutviewtoolzoom.h
try:
    QgsLayoutViewToolZoom.__overridden_methods__ = ['layoutPressEvent', 'layoutMoveEvent', 'layoutReleaseEvent', 'keyPressEvent', 'keyReleaseEvent', 'deactivate']
    QgsLayoutViewToolZoom.__group__ = ['layout']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgslegendfilterbutton.h
try:
    QgsLegendFilterButton.__attribute_docs__ = {'expressionTextChanged': 'Emitted when the expression text changes\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgslegendpatchshapebutton.h
try:
    QgsLegendPatchShapeButton.__attribute_docs__ = {'changed': "Emitted when the shape's settings are changed.\n\n.. seealso:: :py:func:`shape`\n\n.. seealso:: :py:func:`setShape`\n"}
    QgsLegendPatchShapeButton.__overridden_methods__ = ['minimumSizeHint', 'sizeHint', 'changeEvent', 'showEvent', 'resizeEvent', 'mousePressEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgslegendpatchshapewidget.h
try:
    QgsLegendPatchShapeWidget.__attribute_docs__ = {'changed': 'Emitted whenever the patch shape defined by the widget is changed.\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgslimitedrandomcolorrampdialog.h
try:
    QgsLimitedRandomColorRampWidget.__attribute_docs__ = {'changed': 'Emitted when the dialog settings change\n'}
except (NameError, AttributeError):
    pass
try:
    QgsLimitedRandomColorRampDialog.__attribute_docs__ = {'changed': 'Emitted when the dialog settings change\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgslistwidget.h
try:
    QgsListWidget.__overridden_methods__ = ['setReadOnly']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/locator/qgslocatorwidget.h
try:
    QgsLocatorWidget.__attribute_docs__ = {'configTriggered': 'Emitted when the configure option is triggered in the widget.\n'}
    QgsLocatorWidget.__overridden_methods__ = ['eventFilter']
    QgsLocatorWidget.__group__ = ['locator']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgslonglongvalidator.h
try:
    QgsLongLongValidator.__virtual_methods__ = ['setRange']
    QgsLongLongValidator.__overridden_methods__ = ['validate']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmapcanvas.h
try:
    QgsMapCanvas.__attribute_docs__ = {'xyCoordinates': 'Emits current mouse position\n\n.. note::\n\n   changed in 1.3\n', 'scaleChanged': 'Emitted when the scale of the map changes\n', 'scaleLockChanged': 'Emitted when the scale locked state of the map changes\n\n:param locked: true if the scale is locked\n\n.. seealso:: :py:func:`setScaleLocked`\n\n.. versionadded:: 3.18\n', 'extentsChanged': 'Emitted when the extents of the map change\n', 'rotationChanged': 'Emitted when the rotation of the map changes\n', 'magnificationChanged': 'Emitted when the scale of the map changes\n', 'canvasColorChanged': 'Emitted when canvas background color changes\n', 'renderComplete': 'Emitted when the canvas has rendered. Passes a pointer to the painter on\nwhich the map was drawn. This is useful for plugins that wish to draw on\nthe map after it has been rendered. Passing the painter allows plugins\nto work when the map is being rendered onto a pixmap other than the\nmapCanvas own pixmap member.\n\n- anything related to rendering progress is not visible outside of map canvas\n- additional drawing shall be done directly within the renderer job or independently as a map canvas item\n', 'mapCanvasRefreshed': 'Emitted when canvas finished a refresh request.\n', 'renderStarting': 'Emitted when the canvas is about to be rendered.\n', 'mapRefreshCanceled': 'Emitted when the pending map refresh has been canceled\n\n.. versionadded:: 3.18\n', 'layersChanged': 'Emitted when a new set of layers has been received\n', 'keyPressed': 'Emit key press event\n', 'keyReleased': 'Emit key release event\n', 'mapToolSet': 'Emit map tool changed with the old tool\n', 'selectionChanged': 'Emitted when selection in any ``layer`` gets changed.\n\n.. note::\n\n   Since QGIS 3.28 this signal is emitted for multiple layer types, including :py:class:`QgsVectorLayer` and :py:class:`QgsVectorTileLayer`\n', 'zoomLastStatusChanged': 'Emitted when zoom last status changed\n', 'zoomNextStatusChanged': 'Emitted when zoom next status changed\n', 'destinationCrsChanged': 'Emitted when map CRS has changed\n', 'transformContextChanged': 'Emitted when the canvas transform context is changed.\n', 'currentLayerChanged': 'Emitted when the current layer is changed\n', 'layerStyleOverridesChanged': 'Emitted when the configuration of overridden layer styles changes\n', 'themeChanged': 'Emitted when the canvas has been assigned a different map theme.\n\n.. seealso:: :py:func:`setTheme`\n', 'messageEmitted': 'emit a message (usually to be displayed in a message bar)\n', 'renderErrorOccurred': 'Emitted whenever an error is encountered during a map render operation.\n\nThe ``layer`` argument indicates the associated map layer, if available.\n\n.. versionadded:: 3.10.0\n', 'panDistanceBearingChanged': 'Emitted whenever the distance or bearing of an in-progress panning\noperation is changed.\n\nThis signal will be emitted during a pan operation as the user moves the\nmap, giving the total distance and bearing between the map position at\nthe start of the pan and the current pan position.\n\n.. versionadded:: 3.12\n', 'tapAndHoldGestureOccurred': 'Emitted whenever a tap and hold ``gesture`` occurs at the specified map\npoint.\n\n.. versionadded:: 3.12\n', 'temporalRangeChanged': 'Emitted when the map canvas temporal range changes.\n\n.. versionadded:: 3.14\n', 'zRangeChanged': 'Emitted when the map canvas z (elevation) range changes.\n\n.. seealso:: :py:func:`zRange`\n\n.. seealso:: :py:func:`setZRange`\n\n.. versionadded:: 3.18\n', 'contextMenuAboutToShow': 'Emitted before the map canvas context menu will be shown. Can be used to\nextend the context menu.\n\n.. versionadded:: 3.16\n'}
    QgsMapCanvas.__overridden_methods__ = ['createExpressionContext', 'event', 'keyPressEvent', 'keyReleaseEvent', 'mouseDoubleClickEvent', 'mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent', 'wheelEvent', 'resizeEvent', 'paintEvent', 'dragEnterEvent', 'viewportEvent', 'dropEvent', 'showEvent']
    QgsMapCanvas.__signal_arguments__ = {'xyCoordinates': ['p: QgsPointXY'], 'scaleChanged': ['scale: float'], 'scaleLockChanged': ['locked: bool'], 'rotationChanged': ['rotation: float'], 'magnificationChanged': ['magnification: float'], 'renderComplete': ['painter: QPainter'], 'keyPressed': ['e: QKeyEvent'], 'keyReleased': ['e: QKeyEvent'], 'mapToolSet': ['newTool: QgsMapTool', 'oldTool: QgsMapTool'], 'selectionChanged': ['layer: QgsMapLayer'], 'zoomLastStatusChanged': ['available: bool'], 'zoomNextStatusChanged': ['available: bool'], 'currentLayerChanged': ['layer: QgsMapLayer'], 'themeChanged': ['theme: str'], 'messageEmitted': ['title: str', 'message: str', 'level: Qgis.MessageLevel = Qgis.MessageLevel.Info'], 'renderErrorOccurred': ['error: str', 'layer: QgsMapLayer'], 'panDistanceBearingChanged': ['distance: float', 'unit: Qgis.DistanceUnit', 'bearing: float'], 'tapAndHoldGestureOccurred': ['mapPoint: QgsPointXY', 'gesture: QTapAndHoldGesture'], 'contextMenuAboutToShow': ['menu: QMenu', 'event: QgsMapMouseEvent']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmapcanvasannotationitem.h
try:
    QgsMapCanvasAnnotationItem.__overridden_methods__ = ['updatePosition', 'boundingRect', 'paint']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmapcanvasinteractionblocker.h
# monkey patching scoped based enum
QgsMapCanvasInteractionBlocker.Interaction.MapPanOnSingleClick.__doc__ = "A map pan interaction caused by a single click and release on the map canvas"
QgsMapCanvasInteractionBlocker.Interaction.__doc__ = """Available interactions to block.

* ``MapPanOnSingleClick``: A map pan interaction caused by a single click and release on the map canvas

"""
# --
try:
    QgsMapCanvasInteractionBlocker.__abstract_methods__ = ['blockCanvasInteraction']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmapcanvasitem.h
try:
    QgsMapCanvasItem.__virtual_methods__ = ['updatePosition']
    QgsMapCanvasItem.__abstract_methods__ = ['paint']
    QgsMapCanvasItem.__overridden_methods__ = ['paint', 'boundingRect']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmapcanvassnappingutils.h
try:
    QgsMapCanvasSnappingUtils.__overridden_methods__ = ['prepareIndexStarting', 'prepareIndexProgress']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmapcanvastracer.h
try:
    QgsMapCanvasTracer.tracerForCanvas = staticmethod(QgsMapCanvasTracer.tracerForCanvas)
    QgsMapCanvasTracer.__overridden_methods__ = ['configure']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmapcanvasutils.h
try:
    QgsMapCanvasUtils.zoomToMatchingFeatures = staticmethod(QgsMapCanvasUtils.zoomToMatchingFeatures)
    QgsMapCanvasUtils.flashMatchingFeatures = staticmethod(QgsMapCanvasUtils.flashMatchingFeatures)
    QgsMapCanvasUtils.filterForLayer = staticmethod(QgsMapCanvasUtils.filterForLayer)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/actions/qgsmaplayeraction.h
try:
    QgsMapLayerAction.__attribute_docs__ = {'triggeredForFeatures': 'Triggered when action has been run for a specific list of features\n\n.. deprecated:: 3.40\n\n   Use the version with :py:class:`QgsMapLayerActionContext` instead.\n', 'triggeredForFeature': 'Triggered when action has been run for a specific feature\n\n.. deprecated:: 3.40\n\n   Use the version with :py:class:`QgsMapLayerActionContext` instead.\n', 'triggeredForLayer': 'Triggered when action has been run for a specific layer\n\n.. deprecated:: 3.40\n\n   Use the version with :py:class:`QgsMapLayerActionContext` instead.\n', 'triggeredForFeaturesV2': 'Triggered when action has been run for a specific list of features\n\n.. versionadded:: 3.30\n', 'triggeredForFeatureV2': 'Triggered when action has been run for a specific feature.\n\n.. versionadded:: 3.30\n', 'triggeredForLayerV2': 'Triggered when action has been run for a specific layer.\n\n.. versionadded:: 3.30\n'}
    QgsMapLayerAction.__virtual_methods__ = ['canRunUsingLayer', 'triggerForFeatures', 'triggerForFeature', 'triggerForLayer']
    QgsMapLayerAction.__signal_arguments__ = {'triggeredForFeaturesV2': ['layer: QgsMapLayer', 'featureList: List[QgsFeature]', 'context: QgsMapLayerActionContext'], 'triggeredForFeatureV2': ['layer: QgsMapLayer', 'feature: QgsFeature', 'context: QgsMapLayerActionContext'], 'triggeredForLayerV2': ['layer: QgsMapLayer', 'context: QgsMapLayerActionContext']}
    QgsMapLayerAction.__group__ = ['actions']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/actions/qgsmaplayeractioncontext.h
try:
    QgsMapLayerActionContext.__group__ = ['actions']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/actions/qgsmaplayeractioncontextgenerator.h
try:
    QgsMapLayerActionContextGenerator.__abstract_methods__ = ['createActionContext']
    QgsMapLayerActionContextGenerator.__group__ = ['actions']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/actions/qgsmaplayeractionregistry.h
try:
    QgsMapLayerActionRegistry.__attribute_docs__ = {'changed': 'Triggered when an action is added or removed from the registry\n'}
    QgsMapLayerActionRegistry.__group__ = ['actions']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmaplayercombobox.h
try:
    QgsMapLayerComboBox.__attribute_docs__ = {'layerChanged': 'Emitted whenever the currently selected layer changes.\n'}
    QgsMapLayerComboBox.__overridden_methods__ = ['dragEnterEvent', 'dragLeaveEvent', 'dropEvent', 'paintEvent']
    QgsMapLayerComboBox.__signal_arguments__ = {'layerChanged': ['layer: QgsMapLayer']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmaplayerconfigwidget.h
try:
    QgsMapLayerConfigWidget.__virtual_methods__ = ['shouldTriggerLayerRepaint', 'syncToLayer', 'setMapLayerConfigWidgetContext', 'focusDefaultWidget']
    QgsMapLayerConfigWidget.__abstract_methods__ = ['apply']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmaplayerconfigwidgetfactory.h
# monkey patching scoped based enum
QgsMapLayerConfigWidgetFactory.ParentPage.NoParent.__doc__ = "Factory creates pages itself, not sub-components"
QgsMapLayerConfigWidgetFactory.ParentPage.Temporal.__doc__ = "Factory creates sub-components of the temporal properties page (only supported for raster layer temporal properties)"
QgsMapLayerConfigWidgetFactory.ParentPage.__doc__ = """Available parent pages, for factories which create a widget which is a sub-component
of a standard page.

.. versionadded:: 3.20

* ``NoParent``: Factory creates pages itself, not sub-components
* ``Temporal``: Factory creates sub-components of the temporal properties page (only supported for raster layer temporal properties)

"""
# --
try:
    QgsMapLayerConfigWidgetFactory.__virtual_methods__ = ['icon', 'title', 'supportsStyleDock', 'supportLayerPropertiesDialog', 'layerPropertiesPagePositionHint', 'supportsLayer', 'supportsLayerTreeGroup', 'parentPage']
    QgsMapLayerConfigWidgetFactory.__abstract_methods__ = ['createWidget']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmaplayerstylecategoriesmodel.h
# monkey patching scoped based enum
QgsMapLayerStyleCategoriesModel.Role.NameRole.__doc__ = ""
QgsMapLayerStyleCategoriesModel.Role.__doc__ = """Custom model roles

* ``NameRole``: 

"""
# --
try:
    QgsMapLayerStyleCategoriesModel.__overridden_methods__ = ['rowCount', 'columnCount', 'data', 'setData', 'flags']
except (NameError, AttributeError):
    pass
try:
    QgsCategoryDisplayLabelDelegate.__overridden_methods__ = ['drawDisplay', 'sizeHint']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmaplayerstylemanagerwidget.h
try:
    QgsMapLayerStyleManagerWidget.__overridden_methods__ = ['apply']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmapoverviewcanvas.h
try:
    QgsMapOverviewCanvas.__overridden_methods__ = ['paintEvent', 'showEvent', 'resizeEvent', 'mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent', 'wheelEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmaptip.h
try:
    QgsMapTip.vectorMapTipPreviewText = staticmethod(QgsMapTip.vectorMapTipPreviewText)
    QgsMapTip.rasterMapTipPreviewText = staticmethod(QgsMapTip.rasterMapTipPreviewText)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/maptools/qgsmaptool.h
try:
    QgsMapTool.__attribute_docs__ = {'messageEmitted': 'Emitted when a ``message`` should be shown to the user in the\napplication message bar.\n\n.. seealso:: :py:func:`messageDiscarded`\n', 'messageDiscarded': 'Emitted when the previous message from the tool should be cleared from\nthe application message bar.\n\n.. seealso:: :py:func:`messageEmitted`\n', 'activated': 'Emitted when the map tool is activated.\n\n.. seealso:: :py:func:`deactivated`\n', 'deactivated': 'Emitted when the map tool is deactivated.\n\n.. seealso:: :py:func:`activated`\n', 'reactivated': 'Emitted when the map tool is activated, while it is already active.\n\n.. versionadded:: 3.32\n'}
    QgsMapTool.searchRadiusMM = staticmethod(QgsMapTool.searchRadiusMM)
    QgsMapTool.searchRadiusMU = staticmethod(QgsMapTool.searchRadiusMU)
    QgsMapTool.__virtual_methods__ = ['flags', 'canvasMoveEvent', 'canvasDoubleClickEvent', 'canvasPressEvent', 'canvasReleaseEvent', 'wheelEvent', 'keyPressEvent', 'keyReleaseEvent', 'gestureEvent', 'canvasToolTipEvent', 'setCursor', 'activate', 'deactivate', 'reactivate', 'clean', 'populateContextMenu', 'populateContextMenuWithEvent']
    QgsMapTool.__signal_arguments__ = {'messageEmitted': ['message: str', 'level: Qgis.MessageLevel = Qgis.MessageLevel.Info']}
    QgsMapTool.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/maptools/qgsmaptooladvanceddigitizing.h
try:
    QgsMapToolAdvancedDigitizing.__virtual_methods__ = ['layer', 'cadCanvasPressEvent', 'cadCanvasReleaseEvent', 'cadCanvasMoveEvent']
    QgsMapToolAdvancedDigitizing.__overridden_methods__ = ['canvasPressEvent', 'canvasReleaseEvent', 'canvasMoveEvent', 'activate', 'deactivate']
    QgsMapToolAdvancedDigitizing.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/maptools/qgsmaptoolcapture.h
try:
    QgsMapToolCapture.__virtual_methods__ = ['capabilities', 'supportsTechnique', 'geometryCaptured', 'pointCaptured', 'lineCaptured', 'polygonCaptured']
    QgsMapToolCapture.__overridden_methods__ = ['activate', 'deactivate', 'cadCanvasMoveEvent', 'cadCanvasReleaseEvent', 'keyPressEvent', 'clean']
    QgsMapToolCapture.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/maptools/qgsmaptoolcapturelayergeometry.h
try:
    QgsMapToolCaptureLayerGeometry.__virtual_methods__ = ['layerGeometryCaptured', 'layerPointCaptured', 'layerLineCaptured', 'layerPolygonCaptured']
    QgsMapToolCaptureLayerGeometry.__overridden_methods__ = ['geometryCaptured']
    QgsMapToolCaptureLayerGeometry.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/maptools/qgsmaptooldigitizefeature.h
try:
    QgsMapToolDigitizeFeature.__attribute_docs__ = {'digitizingCompleted': 'Emitted whenever the digitizing has been successfully completed\n\n:param feature: the new digitized feature\n', 'digitizingFinished': 'Emitted whenever the digitizing has been ended without digitizing any\nfeature\n', 'digitizingCanceled': 'Emitted when the digitizing process was interrupted by the user.\n\n.. versionadded:: 3.28\n'}
    QgsMapToolDigitizeFeature.__virtual_methods__ = ['layerGeometryCaptured', 'featureDigitized']
    QgsMapToolDigitizeFeature.__overridden_methods__ = ['capabilities', 'supportsTechnique', 'cadCanvasReleaseEvent', 'activate', 'deactivate', 'reactivate', 'keyPressEvent']
    QgsMapToolDigitizeFeature.__signal_arguments__ = {'digitizingCompleted': ['feature: QgsFeature']}
    QgsMapToolDigitizeFeature.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/maptools/qgsmaptooledit.h
try:
    QgsMapToolEdit.defaultZValue = staticmethod(QgsMapToolEdit.defaultZValue)
    QgsMapToolEdit.defaultMValue = staticmethod(QgsMapToolEdit.defaultMValue)
    QgsMapToolEdit.digitizingStrokeColor = staticmethod(QgsMapToolEdit.digitizingStrokeColor)
    QgsMapToolEdit.digitizingStrokeWidth = staticmethod(QgsMapToolEdit.digitizingStrokeWidth)
    QgsMapToolEdit.digitizingFillColor = staticmethod(QgsMapToolEdit.digitizingFillColor)
    QgsMapToolEdit.__overridden_methods__ = ['flags']
    QgsMapToolEdit.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/maptools/qgsmaptoolemitpoint.h
try:
    QgsMapToolEmitPoint.__attribute_docs__ = {'canvasClicked': 'signal emitted on canvas click\n'}
    QgsMapToolEmitPoint.__overridden_methods__ = ['flags', 'canvasMoveEvent', 'canvasPressEvent', 'canvasReleaseEvent']
    QgsMapToolEmitPoint.__signal_arguments__ = {'canvasClicked': ['point: QgsPointXY', 'button: Qt.MouseButton']}
    QgsMapToolEmitPoint.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/maptools/qgsmaptoolextent.h
try:
    QgsMapToolExtent.__attribute_docs__ = {'extentChanged': 'signal emitted on extent change\n'}
    QgsMapToolExtent.__overridden_methods__ = ['flags', 'canvasMoveEvent', 'canvasPressEvent', 'canvasReleaseEvent', 'activate', 'deactivate']
    QgsMapToolExtent.__signal_arguments__ = {'extentChanged': ['extent: QgsRectangle']}
    QgsMapToolExtent.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/maptools/qgsmaptoolidentify.h
QgsMapToolIdentify.IdentifyMode.baseClass = QgsMapToolIdentify
QgsMapToolIdentify.LayerType.baseClass = QgsMapToolIdentify
LayerType = QgsMapToolIdentify  # dirty hack since SIP seems to introduce the flags in module
try:
    QgsMapToolIdentify.IdentifyProperties.__attribute_docs__ = {'searchRadiusMapUnits': 'Identify search radius is map units. Use negative value to ignore', 'skip3DLayers': 'Skip identify results from layers that have a 3d renderer set'}
    QgsMapToolIdentify.IdentifyProperties.__annotations__ = {'searchRadiusMapUnits': float, 'skip3DLayers': bool}
    QgsMapToolIdentify.IdentifyProperties.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
try:
    QgsMapToolIdentify.__attribute_docs__ = {'identifyProgress': 'Emitted when the identify action progresses.\n\n:param processed: number of objects processed so far\n:param total: total number of objects to process\n', 'identifyMessage': 'Emitted when the identify operation needs to show a user-facing message\n\n:param message: Message to show to the user\n', 'changedRasterResults': 'Emitted when the format of raster ``results`` is changed and need to be\nupdated in user-facing displays.\n'}
    QgsMapToolIdentify.__overridden_methods__ = ['flags', 'canvasMoveEvent', 'canvasPressEvent', 'canvasReleaseEvent', 'activate', 'deactivate']
    QgsMapToolIdentify.__signal_arguments__ = {'identifyProgress': ['processed: int', 'total: int'], 'identifyMessage': ['message: str'], 'changedRasterResults': ['results: List[QgsMapToolIdentify.IdentifyResult]']}
    QgsMapToolIdentify.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
try:
    QgsMapToolIdentify.IdentifyResult.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/maptools/qgsmaptoolidentifyfeature.h
try:
    QgsMapToolIdentifyFeature.__attribute_docs__ = {'featureIdentified': 'Emitted when a feature has been identified by its ``id``.\n\n.. deprecated:: 3.40\n\n   Use the signal with a :py:class:`QgsFeature` argument instead.\n'}
    QgsMapToolIdentifyFeature.__overridden_methods__ = ['canvasReleaseEvent', 'keyPressEvent']
    QgsMapToolIdentifyFeature.__signal_arguments__ = {'featureIdentified': ['feature: QgsFeature']}
    QgsMapToolIdentifyFeature.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/maptools/qgsmaptoolpan.h
try:
    QgsMapToolPan.__attribute_docs__ = {'panDistanceBearingChanged': 'Emitted whenever the distance or bearing of an in-progress panning\noperation is changed.\n\nThis signal will be emitted during a pan operation as the user moves the\nmap, giving the total distance and bearing between the map position at\nthe start of the pan and the current pan position.\n\n.. versionadded:: 3.12\n'}
    QgsMapToolPan.__overridden_methods__ = ['activate', 'deactivate', 'flags', 'canvasPressEvent', 'canvasMoveEvent', 'canvasReleaseEvent', 'canvasDoubleClickEvent', 'gestureEvent']
    QgsMapToolPan.__signal_arguments__ = {'panDistanceBearingChanged': ['distance: float', 'unit: Qgis.DistanceUnit', 'bearing: float']}
    QgsMapToolPan.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/maptools/qgsmaptoolzoom.h
try:
    QgsMapToolZoom.__overridden_methods__ = ['flags', 'canvasMoveEvent', 'canvasPressEvent', 'canvasReleaseEvent', 'keyPressEvent', 'keyReleaseEvent', 'deactivate']
    QgsMapToolZoom.__group__ = ['maptools']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsmasksymbollayerwidget.h
try:
    QgsMaskMarkerSymbolLayerWidget.create = staticmethod(QgsMaskMarkerSymbolLayerWidget.create)
    QgsMaskMarkerSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsMaskMarkerSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmediawidget.h
QgsMediaWidget.Mode.baseClass = QgsMediaWidget
# The following has been generated automatically from src/gui/qgsmenuheader.h
try:
    QgsMenuHeader.__overridden_methods__ = ['minimumSizeHint', 'sizeHint', 'paintEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsmergedfeaturerendererwidget.h
try:
    QgsMergedFeatureRendererWidget.create = staticmethod(QgsMergedFeatureRendererWidget.create)
    QgsMergedFeatureRendererWidget.__overridden_methods__ = ['renderer', 'setContext', 'setDockMode']
    QgsMergedFeatureRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/mesh/qgsmeshlayerproperties.h
try:
    QgsMeshLayerProperties.__virtual_methods__ = ['syncToLayer', 'apply', 'rollback']
    QgsMeshLayerProperties.__group__ = ['mesh']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmessagebar.h
try:
    QgsMessageBar.__attribute_docs__ = {'widgetAdded': 'Emitted whenever an ``item`` is added to the bar.\n', 'widgetRemoved': 'Emitted whenever an ``item`` was removed from the bar.\n'}
    QgsMessageBar.createMessage = staticmethod(QgsMessageBar.createMessage)
    QgsMessageBar.defaultMessageTimeout = staticmethod(QgsMessageBar.defaultMessageTimeout)
    QgsMessageBar.__overridden_methods__ = ['mousePressEvent']
    QgsMessageBar.__signal_arguments__ = {'widgetAdded': ['item: QgsMessageBarItem'], 'widgetRemoved': ['item: QgsMessageBarItem']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmessagebaritem.h
try:
    QgsMessageBarItem.__attribute_docs__ = {'styleChanged': "Emitted when the item's message level has changed and the message bar\nstyle will need to be updated as a result.\n"}
    QgsMessageBarItem.__signal_arguments__ = {'styleChanged': ['styleSheet: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmessagelogviewer.h
try:
    QgsMessageLogViewer.__overridden_methods__ = ['closeEvent', 'reject', 'eventFilter']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmessageviewer.h
try:
    QgsMessageViewer.__overridden_methods__ = ['setMessage', 'appendMessage', 'showMessage', 'setTitle']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsmetadatawidget.h
try:
    QgsMetadataWidget.__attribute_docs__ = {'titleChanged': 'Emitted when the ``title`` field is changed.\n\n.. seealso:: :py:func:`title`\n\n.. seealso:: :py:func:`setTitle`\n\n.. versionadded:: 3.2\n'}
    QgsMetadataWidget.parseLanguages = staticmethod(QgsMetadataWidget.parseLanguages)
    QgsMetadataWidget.parseLicenses = staticmethod(QgsMetadataWidget.parseLicenses)
    QgsMetadataWidget.parseLinkTypes = staticmethod(QgsMetadataWidget.parseLinkTypes)
    QgsMetadataWidget.parseMimeTypes = staticmethod(QgsMetadataWidget.parseMimeTypes)
    QgsMetadataWidget.parseTypes = staticmethod(QgsMetadataWidget.parseTypes)
    QgsMetadataWidget.__signal_arguments__ = {'titleChanged': ['title: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/models/qgsmodelarrowitem.h
try:
    QgsModelArrowItem.__overridden_methods__ = ['paint']
    QgsModelArrowItem.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/models/qgsmodelcomponentgraphicitem.h
try:
    QgsModelComponentGraphicItem.__attribute_docs__ = {'requestModelRepaint': 'Emitted by the item to request a repaint of the parent model scene.\n', 'aboutToChange': 'Emitted when the definition of the associated component is about to be\nchanged by the item.\n\nThe ``text`` argument gives the translated text describing the change\nabout to occur, and the optional ``id`` can be used to group the\nassociated undo commands.\n', 'changed': 'Emitted when the definition of the associated component is changed by\nthe item.\n', 'repaintArrows': 'Emitted when item requests that all connected arrows are repainted.\n', 'updateArrowPaths': 'Emitted when item requires that all connected arrow paths are\nrecalculated.\n', 'sizePositionChanged': "Emitted when the item's size or position changes.\n"}
    QgsModelComponentGraphicItem.__virtual_methods__ = ['flags', 'linkPointCount', 'linkPointText', 'editComment', 'canDeleteComponent', 'deleteComponent', 'editComponent', 'strokeStyle', 'titleAlignment', 'iconPicture', 'iconPixmap']
    QgsModelComponentGraphicItem.__abstract_methods__ = ['fillColor', 'strokeColor', 'textColor', 'updateStoredComponentPosition']
    QgsModelComponentGraphicItem.__overridden_methods__ = ['mouseDoubleClickEvent', 'hoverEnterEvent', 'hoverMoveEvent', 'hoverLeaveEvent', 'itemChange', 'boundingRect', 'contains', 'paint']
    QgsModelComponentGraphicItem.__signal_arguments__ = {'aboutToChange': ['text: str', 'id: int = 0']}
    QgsModelComponentGraphicItem.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
try:
    QgsModelChildAlgorithmGraphicItem.__attribute_docs__ = {'runFromHere': 'Emitted when the user opts to run the model from this child algorithm.\n\n.. versionadded:: 3.38\n', 'runSelected': 'Emitted when the user opts to run selected steps from the model.\n\n.. versionadded:: 3.38\n', 'showPreviousResults': 'Emitted when the user opts to view previous results from this child\nalgorithm.\n\n.. versionadded:: 3.38\n', 'showLog': 'Emitted when the user opts to view the previous log from this child\nalgorithm.\n\n.. versionadded:: 3.38\n'}
    QgsModelChildAlgorithmGraphicItem.__overridden_methods__ = ['contextMenuEvent', 'canDeleteComponent', 'fillColor', 'strokeColor', 'textColor', 'iconPixmap', 'iconPicture', 'linkPointCount', 'linkPointText', 'updateStoredComponentPosition', 'deleteComponent']
    QgsModelChildAlgorithmGraphicItem.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
try:
    QgsModelParameterGraphicItem.__overridden_methods__ = ['contextMenuEvent', 'canDeleteComponent', 'fillColor', 'strokeColor', 'textColor', 'iconPicture', 'linkPointCount', 'linkPointText', 'updateStoredComponentPosition', 'deleteComponent']
    QgsModelParameterGraphicItem.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
try:
    QgsModelOutputGraphicItem.__overridden_methods__ = ['canDeleteComponent', 'fillColor', 'strokeColor', 'textColor', 'iconPicture', 'updateStoredComponentPosition', 'deleteComponent']
    QgsModelOutputGraphicItem.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
try:
    QgsModelCommentGraphicItem.__overridden_methods__ = ['contextMenuEvent', 'canDeleteComponent', 'fillColor', 'strokeColor', 'textColor', 'strokeStyle', 'updateStoredComponentPosition', 'deleteComponent', 'editComponent']
    QgsModelCommentGraphicItem.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
try:
    QgsModelGroupBoxGraphicItem.__overridden_methods__ = ['contextMenuEvent', 'canDeleteComponent', 'fillColor', 'strokeColor', 'textColor', 'strokeStyle', 'titleAlignment', 'updateStoredComponentPosition', 'deleteComponent', 'editComponent']
    QgsModelGroupBoxGraphicItem.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/models/qgsmodeldesignerdialog.h
# monkey patching scoped based enum
QgsModelDesignerDialog.SaveAction.SaveAsFile.__doc__ = "Save model as a file"
QgsModelDesignerDialog.SaveAction.SaveInProject.__doc__ = "Save model into project"
QgsModelDesignerDialog.SaveAction.__doc__ = """Save action.

.. versionadded:: 3.24

* ``SaveAsFile``: Save model as a file
* ``SaveInProject``: Save model into project

"""
# --
try:
    QgsModelDesignerDialog.__abstract_methods__ = ['repaintModel', 'addAlgorithm', 'addInput', 'exportAsScriptAlgorithm', 'saveModel', 'createExecutionDialog']
    QgsModelDesignerDialog.__overridden_methods__ = ['closeEvent']
    QgsModelDesignerDialog.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
try:
    QgsModelChildDependenciesWidget.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/models/qgsmodelgraphicitem.h
try:
    QgsModelDesignerFlatButtonGraphicItem.__attribute_docs__ = {'clicked': 'Emitted when the button is clicked.\n'}
    QgsModelDesignerFlatButtonGraphicItem.__overridden_methods__ = ['paint', 'boundingRect', 'hoverEnterEvent', 'hoverLeaveEvent', 'mousePressEvent']
    QgsModelDesignerFlatButtonGraphicItem.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
try:
    QgsModelDesignerFoldButtonGraphicItem.__attribute_docs__ = {'folded': 'Emitted when the button ``folded`` state changes.\n\nIf ``folded`` is ``True``, the button represents the collapsed state for\nthe item.\n'}
    QgsModelDesignerFoldButtonGraphicItem.__overridden_methods__ = ['mousePressEvent']
    QgsModelDesignerFoldButtonGraphicItem.__signal_arguments__ = {'folded': ['folded: bool']}
    QgsModelDesignerFoldButtonGraphicItem.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
try:
    QgsModelDesignerSocketGraphicItem.__overridden_methods__ = ['paint']
    QgsModelDesignerSocketGraphicItem.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/models/qgsmodelgraphicsscene.h
try:
    QgsModelGraphicsScene.__attribute_docs__ = {'rebuildRequired': 'Emitted when a change in the model requires a full rebuild of the scene.\n', 'componentAboutToChange': 'Emitted whenever a component of the model is about to be changed.\n\nThe ``text`` argument gives the translated text describing the change\nabout to occur, and the optional ``id`` can be used to group the\nassociated undo commands.\n', 'componentChanged': 'Emitted whenever a component of the model is changed.\n', 'selectedItemChanged': 'Emitted whenever the selected item changes. If ``None``, no item is\nselected.\n', 'runSelected': 'Emitted when the user opts to run selected steps from the model.\n\n.. versionadded:: 3.38\n', 'runFromChild': 'Emitted when the user opts to run the part of the model starting from\nthe specified child algorithm.\n\n.. versionadded:: 3.38\n', 'showChildAlgorithmOutputs': 'Emitted when the user opts to view previous results from the child\nalgorithm with matching ID.\n\n.. versionadded:: 3.38\n', 'showChildAlgorithmLog': 'Emitted when the user opts to view the previous log from the child\nalgorithm with matching ID.\n\n.. versionadded:: 3.38\n'}
    QgsModelGraphicsScene.__virtual_methods__ = ['createParameterGraphicItem', 'createChildAlgGraphicItem', 'createOutputGraphicItem', 'createCommentGraphicItem']
    QgsModelGraphicsScene.__overridden_methods__ = ['mousePressEvent']
    QgsModelGraphicsScene.__signal_arguments__ = {'componentAboutToChange': ['text: str', 'id: int = 0'], 'selectedItemChanged': ['selected: QgsModelComponentGraphicItem'], 'runFromChild': ['childId: str'], 'showChildAlgorithmOutputs': ['childId: str'], 'showChildAlgorithmLog': ['childId: str']}
    QgsModelGraphicsScene.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/models/qgsmodelgraphicsview.h
try:
    QgsModelGraphicsView.__attribute_docs__ = {'algorithmDropped': 'Emitted when an algorithm is dropped onto the view.\n', 'inputDropped': 'Emitted when an input parameter is dropped onto the view.\n', 'itemFocused': 'Emitted when an ``item`` is "focused" in the view, i.e. it becomes the\nactive item and should have its properties displayed in any designer\nwindows.\n', 'willBeDeleted': 'Emitted in the destructor when the view is about to be deleted, but is\nstill in a perfectly valid state.\n', 'macroCommandStarted': 'Emitted when a macro command containing a group of interactions is\nstarted in the view.\n', 'macroCommandEnded': 'Emitted when a macro command containing a group of interactions in the\nview has ended.\n', 'commandBegun': 'Emitted when an undo command is started in the view.\n', 'commandEnded': 'Emitted when an undo command in the view has ended.\n', 'deleteSelectedItems': 'Emitted when the selected items should be deleted;\n'}
    QgsModelGraphicsView.__overridden_methods__ = ['dragEnterEvent', 'dropEvent', 'dragMoveEvent', 'wheelEvent', 'mousePressEvent', 'mouseReleaseEvent', 'mouseMoveEvent', 'mouseDoubleClickEvent', 'keyPressEvent', 'keyReleaseEvent']
    QgsModelGraphicsView.__signal_arguments__ = {'algorithmDropped': ['algorithmId: str', 'pos: QPointF'], 'inputDropped': ['inputId: str', 'pos: QPointF'], 'itemFocused': ['item: QgsModelComponentGraphicItem'], 'macroCommandStarted': ['text: str'], 'commandBegun': ['text: str']}
    QgsModelGraphicsView.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
try:
    QgsModelViewSnapMarker.__overridden_methods__ = ['paint']
    QgsModelViewSnapMarker.__group__ = ['processing', 'models']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsmultibandcolorrendererwidget.h
try:
    QgsMultiBandColorRendererWidget.create = staticmethod(QgsMultiBandColorRendererWidget.create)
    QgsMultiBandColorRendererWidget.__overridden_methods__ = ['renderer', 'setMapCanvas', 'min', 'max', 'setMin', 'setMax', 'selectedBand', 'contrastEnhancementAlgorithm', 'setContrastEnhancementAlgorithm', 'doComputations', 'minMaxWidget']
    QgsMultiBandColorRendererWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsmultiedittoolbutton.h
try:
    QgsMultiEditToolButton.__attribute_docs__ = {'setFieldValueTriggered': 'Emitted when the "set field value for all features" option is selected.\n', 'resetFieldValueTriggered': 'Emitted when the "reset to original values" option is selected.\n'}
    QgsMultiEditToolButton.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsnewauxiliaryfielddialog.h
try:
    QgsNewAuxiliaryFieldDialog.__overridden_methods__ = ['accept']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsnewauxiliarylayerdialog.h
try:
    QgsNewAuxiliaryLayerDialog.__overridden_methods__ = ['accept']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsnewdatabasetablenamewidget.h
try:
    QgsNewDatabaseTableNameWidget.__attribute_docs__ = {'validationChanged': 'This signal is emitted whenever the validation status of the widget\nchanges.\n\n:param isValid: ``True`` if the current status of the widget is valid\n', 'schemaNameChanged': 'This signal is emitted when the user selects a schema (or file path for\nfilesystem-based DBs like spatialite or GPKG).\n\n:param schemaName: the name of the selected schema\n', 'tableNameChanged': 'This signal is emitted when the user enters a table name\n\n:param tableName: the name of the new table\n', 'providerKeyChanged': 'This signal is emitted when the selects a data provider or a schema name\nthat has a different data provider than the previously selected one.\n\n:param providerKey: the data provider key of the selected schema\n', 'uriChanged': 'This signal is emitted when the URI of the new table changes, whether or\nnot it is a valid one.\n\n:param uri: URI string representation\n', 'accepted': 'Emitted when the OK/accept button is clicked.\n'}
    QgsNewDatabaseTableNameWidget.__overridden_methods__ = ['showEvent']
    QgsNewDatabaseTableNameWidget.__signal_arguments__ = {'validationChanged': ['isValid: bool'], 'schemaNameChanged': ['schemaName: str'], 'tableNameChanged': ['tableName: str'], 'providerKeyChanged': ['providerKey: str'], 'uriChanged': ['uri: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsnewhttpconnection.h
try:
    QgsNewHttpConnection.__virtual_methods__ = ['validate', 'wfsSettingsKey', 'wmsSettingsKey']
    QgsNewHttpConnection.__overridden_methods__ = ['accept', 'showEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsnewmemorylayerdialog.h
try:
    QgsNewMemoryLayerDialog.runAndCreateLayer = staticmethod(QgsNewMemoryLayerDialog.runAndCreateLayer)
    QgsNewMemoryLayerDialog.__overridden_methods__ = ['accept']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsnewnamedialog.h
try:
    QgsNewNameDialog.__attribute_docs__ = {'newNameChanged': 'Emitted when the name is changed in the dialog.\n\n.. versionadded:: 3.2\n'}
    QgsNewNameDialog.exists = staticmethod(QgsNewNameDialog.exists)
    QgsNewNameDialog.fullNames = staticmethod(QgsNewNameDialog.fullNames)
    QgsNewNameDialog.matching = staticmethod(QgsNewNameDialog.matching)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsnewvectorlayerdialog.h
try:
    QgsNewVectorLayerDialog.runAndCreateLayer = staticmethod(QgsNewVectorLayerDialog.runAndCreateLayer)
    QgsNewVectorLayerDialog.execAndCreateLayer = staticmethod(QgsNewVectorLayerDialog.execAndCreateLayer)
    QgsNewVectorLayerDialog.__overridden_methods__ = ['accept']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsnewvectortabledialog.h
try:
    QgsNewVectorTableDialog.__overridden_methods__ = ['showEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsnullsymbolrendererwidget.h
try:
    QgsNullSymbolRendererWidget.create = staticmethod(QgsNullSymbolRendererWidget.create)
    QgsNullSymbolRendererWidget.__overridden_methods__ = ['renderer']
    QgsNullSymbolRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/numericformats/qgsnumericformatguiregistry.h
try:
    QgsNumericFormatConfigurationWidgetFactory.__abstract_methods__ = ['create']
    QgsNumericFormatConfigurationWidgetFactory.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
try:
    QgsNumericFormatGuiRegistry.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/numericformats/qgsnumericformatselectorwidget.h
try:
    QgsNumericFormatSelectorWidget.__attribute_docs__ = {'changed': 'Emitted whenever the format configured55 in the widget is changed.\n'}
    QgsNumericFormatSelectorWidget.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
try:
    QgsNumericFormatSelectorDialog.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/numericformats/qgsnumericformatwidget.h
try:
    QgsNumericFormatWidget.__attribute_docs__ = {'changed': 'Emitted whenever the configuration of the numeric format is changed.\n'}
    QgsNumericFormatWidget.__abstract_methods__ = ['setFormat', 'format']
    QgsNumericFormatWidget.__overridden_methods__ = ['createExpressionContext']
    QgsNumericFormatWidget.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
try:
    QgsBasicNumericFormatWidget.__overridden_methods__ = ['setFormat', 'format']
    QgsBasicNumericFormatWidget.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
try:
    QgsBearingNumericFormatWidget.__overridden_methods__ = ['setFormat', 'format']
    QgsBearingNumericFormatWidget.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
try:
    QgsGeographicCoordinateNumericFormatWidget.__overridden_methods__ = ['setFormat', 'format']
    QgsGeographicCoordinateNumericFormatWidget.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
try:
    QgsCurrencyNumericFormatWidget.__overridden_methods__ = ['setFormat', 'format']
    QgsCurrencyNumericFormatWidget.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
try:
    QgsPercentageNumericFormatWidget.__overridden_methods__ = ['setFormat', 'format']
    QgsPercentageNumericFormatWidget.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
try:
    QgsScientificNumericFormatWidget.__overridden_methods__ = ['setFormat', 'format']
    QgsScientificNumericFormatWidget.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
try:
    QgsFractionNumericFormatWidget.__overridden_methods__ = ['setFormat', 'format']
    QgsFractionNumericFormatWidget.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
try:
    QgsExpressionBasedNumericFormatWidget.__overridden_methods__ = ['createExpressionContext', 'setFormat', 'format']
    QgsExpressionBasedNumericFormatWidget.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
try:
    QgsBearingNumericFormatDialog.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
try:
    QgsGeographicCoordinateNumericFormatDialog.__group__ = ['numericformats']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsopacitywidget.h
try:
    QgsOpacityWidget.__attribute_docs__ = {'opacityChanged': 'Emitted when the ``opacity`` is changed in the widget, where ``opacity``\nranges from 0.0 (transparent) to 1.0 (opaque).\n\n.. seealso:: :py:func:`setOpacity`\n\n.. seealso:: :py:func:`opacity`\n'}
    QgsOpacityWidget.__signal_arguments__ = {'opacityChanged': ['opacity: float']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsoptionsdialogbase.h
try:
    QgsOptionsDialogBase.__virtual_methods__ = ['updateOptionsListVerticalTabs', 'optionsStackedWidget_CurrentChanged', 'optionsStackedWidget_WidgetRemoved', 'updateWindowTitle']
    QgsOptionsDialogBase.__overridden_methods__ = ['showEvent', 'paintEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsoptionsdialoghighlightwidget.h
try:
    QgsOptionsDialogHighlightWidget.createWidget = staticmethod(QgsOptionsDialogHighlightWidget.createWidget)
    QgsOptionsDialogHighlightWidget.__abstract_methods__ = ['searchText', 'highlightText', 'reset']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsoptionsdialoghighlightwidgetsimpl.h
try:
    QgsOptionsDialogHighlightLabel.__overridden_methods__ = ['searchText', 'highlightText', 'reset']
except (NameError, AttributeError):
    pass
try:
    QgsOptionsDialogHighlightCheckBox.__overridden_methods__ = ['searchText', 'highlightText', 'reset']
except (NameError, AttributeError):
    pass
try:
    QgsOptionsDialogHighlightButton.__overridden_methods__ = ['searchText', 'highlightText', 'reset']
except (NameError, AttributeError):
    pass
try:
    QgsOptionsDialogHighlightGroupBox.__overridden_methods__ = ['searchText', 'highlightText', 'reset']
except (NameError, AttributeError):
    pass
try:
    QgsOptionsDialogHighlightTree.__overridden_methods__ = ['searchText', 'highlightText', 'reset']
except (NameError, AttributeError):
    pass
try:
    QgsOptionsDialogHighlightTable.__overridden_methods__ = ['searchText', 'highlightText', 'reset']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsoptionswidgetfactory.h
try:
    QgsOptionsPageWidget.__virtual_methods__ = ['helpKey', 'isValid', 'cancel']
    QgsOptionsPageWidget.__abstract_methods__ = ['apply']
except (NameError, AttributeError):
    pass
try:
    QgsOptionsWidgetFactory.__virtual_methods__ = ['icon', 'title', 'key', 'pagePositionHint', 'path']
    QgsOptionsWidgetFactory.__abstract_methods__ = ['createWidget']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsorderbydialog.h
try:
    QgsOrderByDialog.__overridden_methods__ = ['eventFilter']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/attributetable/qgsorganizetablecolumnsdialog.h
try:
    QgsOrganizeTableColumnsDialog.__group__ = ['attributetable']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsoverlaywidgetlayout.h
try:
    QgsOverlayWidgetLayout.__overridden_methods__ = ['count', 'addItem', 'itemAt', 'takeAt', 'sizeHint', 'minimumSize', 'setGeometry']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsowssourceselect.h
try:
    QgsOWSSourceSelect.__virtual_methods__ = ['providerFormats', 'selectedLayersFormats', 'selectedLayersCrses', 'selectedLayersTimes', 'populateLayerList', 'enableLayersForCrs']
    QgsOWSSourceSelect.__overridden_methods__ = ['refresh', 'reset', 'setMapCanvas']
except (NameError, AttributeError):
    pass
try:
    QgsOWSSourceSelect.SupportedFormat.__doc__ = """Formats supported by provider"""
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/effects/qgspainteffectpropertieswidget.h
try:
    QgsPaintEffectPropertiesWidget.__attribute_docs__ = {'changed': 'Emitted when paint effect properties changes\n', 'changeEffect': 'Emitted when paint effect type changes\n'}
    QgsPaintEffectPropertiesWidget.__signal_arguments__ = {'changeEffect': ['effect: QgsPaintEffect']}
    QgsPaintEffectPropertiesWidget.__group__ = ['effects']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/effects/qgspainteffectwidget.h
try:
    QgsPaintEffectWidget.__attribute_docs__ = {'changed': 'Emitted when properties of the effect are changed through the widget\n'}
    QgsPaintEffectWidget.__abstract_methods__ = ['setPaintEffect']
    QgsPaintEffectWidget.__group__ = ['effects']
except (NameError, AttributeError):
    pass
try:
    QgsDrawSourceWidget.create = staticmethod(QgsDrawSourceWidget.create)
    QgsDrawSourceWidget.__overridden_methods__ = ['setPaintEffect']
    QgsDrawSourceWidget.__group__ = ['effects']
except (NameError, AttributeError):
    pass
try:
    QgsBlurWidget.create = staticmethod(QgsBlurWidget.create)
    QgsBlurWidget.__overridden_methods__ = ['setPaintEffect']
    QgsBlurWidget.__group__ = ['effects']
except (NameError, AttributeError):
    pass
try:
    QgsShadowEffectWidget.create = staticmethod(QgsShadowEffectWidget.create)
    QgsShadowEffectWidget.__overridden_methods__ = ['setPaintEffect']
    QgsShadowEffectWidget.__group__ = ['effects']
except (NameError, AttributeError):
    pass
try:
    QgsGlowWidget.create = staticmethod(QgsGlowWidget.create)
    QgsGlowWidget.__overridden_methods__ = ['setPaintEffect']
    QgsGlowWidget.__group__ = ['effects']
except (NameError, AttributeError):
    pass
try:
    QgsTransformWidget.create = staticmethod(QgsTransformWidget.create)
    QgsTransformWidget.__overridden_methods__ = ['setPaintEffect']
    QgsTransformWidget.__group__ = ['effects']
except (NameError, AttributeError):
    pass
try:
    QgsColorEffectWidget.create = staticmethod(QgsColorEffectWidget.create)
    QgsColorEffectWidget.__overridden_methods__ = ['setPaintEffect']
    QgsColorEffectWidget.__group__ = ['effects']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgspalettedrendererwidget.h
try:
    QgsPalettedRendererWidget.create = staticmethod(QgsPalettedRendererWidget.create)
    QgsPalettedRendererWidget.__overridden_methods__ = ['renderer']
    QgsPalettedRendererWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgspanelwidget.h
try:
    QgsPanelWidget.__attribute_docs__ = {'panelAccepted': 'Emitted when the panel is accepted by the user.\n\n:param panel: The panel widget that was accepted.\n\n.. note::\n\n   This argument is normally raised with emit panelAccepted(this)\n   so that callers can retrieve the widget easier in calling code.\n\n.. note::\n\n   this is emitted only when this panel is accepted, and is not emitted for\n   child panels. For example, if this panel opens a second stacked panel, then this panel\n   will not emit panelAccepted when the second panel is accepted.\n', 'showPanel': 'Emit when you require a panel to be show in the interface.\n\n:param panel: The panel widget to show.\n\n.. note::\n\n   If you are connected to this signal you should also connect\n   given panels showPanel signal as they can be nested.\n', 'widgetChanged': 'Emitted when the widget state changes. Connect to this to pull any\nchanges off the widget when needed. As panels are non blocking "dialogs"\nyou should listen to this signal to give the user feedback when\nsomething changes.\n'}
    QgsPanelWidget.findParentPanel = staticmethod(QgsPanelWidget.findParentPanel)
    QgsPanelWidget.__virtual_methods__ = ['setDockMode', 'applySizeConstraintsToStack', 'menuButtonTooltip', 'menuButtonMenu']
    QgsPanelWidget.__overridden_methods__ = ['keyPressEvent']
    QgsPanelWidget.__signal_arguments__ = {'panelAccepted': ['panel: QgsPanelWidget'], 'showPanel': ['panel: QgsPanelWidget']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgspanelwidgetstack.h
try:
    QgsPanelWidgetStack.__overridden_methods__ = ['sizeHint', 'minimumSizeHint', 'mouseReleaseEvent', 'keyPressEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgspenstylecombobox.h
try:
    QgsPenStyleComboBox.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsPenJoinStyleComboBox.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsPenCapStyleComboBox.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgspercentagewidget.h
try:
    QgsPercentageWidget.__attribute_docs__ = {'valueChanged': 'Emitted when the ``value`` is changed in the widget, where ``value`` is\na factor which ranges from 0.0 to 1.0.\n\n.. seealso:: :py:func:`setValue`\n\n.. seealso:: :py:func:`value`\n'}
    QgsPercentageWidget.__signal_arguments__ = {'valueChanged': ['value: float']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgspixmaplabel.h
try:
    QgsPixmapLabel.__overridden_methods__ = ['heightForWidth', 'sizeHint', 'resizeEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsplaybackcontrollerwidget.h
try:
    QgsPlaybackControllerWidget.__attribute_docs__ = {'operationTriggered': 'Emitted when a playback operation is triggered.\n'}
    QgsPlaybackControllerWidget.__signal_arguments__ = {'operationTriggered': ['operation: Qgis.PlaybackOperation']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/plot/qgsplotcanvas.h
try:
    QgsPlotCanvas.__attribute_docs__ = {'toolChanged': 'Emitted when the plot tool is changed.\n', 'plotAreaChanged': 'Emitted whenever the visible area of the plot is changed.\n', 'contextMenuAboutToShow': 'Emitted before the canvas context menu will be shown. Can be used to\nextend the context menu.\n', 'willBeDeleted': 'Emitted in the destructor when the canvas is about to be deleted, but is\nstill in a perfectly valid state.\n'}
    QgsPlotCanvas.__virtual_methods__ = ['crs', 'toMapCoordinates', 'toCanvasCoordinates', 'panContentsBy', 'centerPlotOn', 'scalePlot', 'zoomToRect', 'snapToPlot', 'refresh', 'wheelZoom']
    QgsPlotCanvas.__overridden_methods__ = ['event', 'keyPressEvent', 'keyReleaseEvent', 'mouseDoubleClickEvent', 'mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent', 'wheelEvent', 'resizeEvent', 'viewportEvent']
    QgsPlotCanvas.__signal_arguments__ = {'toolChanged': ['newTool: QgsPlotTool'], 'contextMenuAboutToShow': ['menu: QMenu', 'event: QgsPlotMouseEvent']}
    QgsPlotCanvas.__group__ = ['plot']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/plot/qgsplotcanvasitem.h
try:
    QgsPlotCanvasItem.__abstract_methods__ = ['paint']
    QgsPlotCanvasItem.__overridden_methods__ = ['paint']
    QgsPlotCanvasItem.__group__ = ['plot']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/plot/qgsplotmouseevent.h
try:
    QgsPlotMouseEvent.__group__ = ['plot']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/plot/qgsplotrubberband.h
try:
    QgsPlotRubberBand.__abstract_methods__ = ['start', 'update', 'finish']
    QgsPlotRubberBand.__group__ = ['plot']
except (NameError, AttributeError):
    pass
try:
    QgsPlotRectangularRubberBand.__overridden_methods__ = ['start', 'update', 'finish']
    QgsPlotRectangularRubberBand.__group__ = ['plot']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/plot/qgsplottool.h
try:
    QgsPlotTool.__attribute_docs__ = {'activated': 'Emitted when the tool is activated.\n', 'deactivated': 'Emitted when the tool is deactivated\n'}
    QgsPlotTool.constrainPointToRect = staticmethod(QgsPlotTool.constrainPointToRect)
    QgsPlotTool.__virtual_methods__ = ['flags', 'plotMoveEvent', 'plotDoubleClickEvent', 'plotPressEvent', 'plotReleaseEvent', 'wheelEvent', 'keyPressEvent', 'keyReleaseEvent', 'gestureEvent', 'canvasToolTipEvent', 'activate', 'deactivate', 'populateContextMenuWithEvent']
    QgsPlotTool.__group__ = ['plot']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/plot/qgsplottoolpan.h
try:
    QgsPlotToolPan.__overridden_methods__ = ['flags', 'plotMoveEvent', 'plotPressEvent', 'plotReleaseEvent', 'deactivate']
    QgsPlotToolPan.__group__ = ['plot']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/plot/qgsplottoolzoom.h
try:
    QgsPlotToolZoom.__overridden_methods__ = ['plotPressEvent', 'plotMoveEvent', 'plotReleaseEvent', 'keyPressEvent', 'keyReleaseEvent', 'deactivate']
    QgsPlotToolZoom.__group__ = ['plot']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/plot/qgsplottransienttools.h
try:
    QgsPlotToolTemporaryKeyPan.__overridden_methods__ = ['plotMoveEvent', 'keyReleaseEvent', 'activate']
    QgsPlotToolTemporaryKeyPan.__group__ = ['plot']
except (NameError, AttributeError):
    pass
try:
    QgsPlotToolTemporaryMousePan.__overridden_methods__ = ['plotMoveEvent', 'plotReleaseEvent', 'activate']
    QgsPlotToolTemporaryMousePan.__group__ = ['plot']
except (NameError, AttributeError):
    pass
try:
    QgsPlotToolTemporaryKeyZoom.__overridden_methods__ = ['plotReleaseEvent', 'keyPressEvent', 'keyReleaseEvent', 'activate']
    QgsPlotToolTemporaryKeyZoom.__group__ = ['plot']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgspluginmanagerinterface.h
try:
    QgsPluginManagerInterface.__abstract_methods__ = ['clearPythonPluginMetadata', 'addPluginMetadata', 'reloadModel', 'clearRepositoryList', 'addToRepositoryList', 'showPluginManager', 'pushMessage']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgspointcloudattributecombobox.h
try:
    QgsPointCloudAttributeComboBox.__attribute_docs__ = {'attributeChanged': 'Emitted when the currently selected attribute changes.\n'}
    QgsPointCloudAttributeComboBox.__signal_arguments__ = {'attributeChanged': ['name: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgspointcloudquerybuilder.h
try:
    QgsPointCloudQueryBuilder.__overridden_methods__ = ['showEvent', 'subsetString', 'setSubsetString', 'accept', 'reject']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/pointcloud/qgspointcloudrendererpropertieswidget.h
try:
    QgsPointCloudRendererPropertiesWidget.__overridden_methods__ = ['syncToLayer', 'setDockMode', 'apply']
    QgsPointCloudRendererPropertiesWidget.__group__ = ['pointcloud']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/pointcloud/qgspointcloudrendererwidget.h
try:
    QgsPointCloudRendererWidget.__virtual_methods__ = ['setContext']
    QgsPointCloudRendererWidget.__abstract_methods__ = ['renderer']
    QgsPointCloudRendererWidget.__group__ = ['pointcloud']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgspointclusterrendererwidget.h
try:
    QgsPointClusterRendererWidget.create = staticmethod(QgsPointClusterRendererWidget.create)
    QgsPointClusterRendererWidget.__overridden_methods__ = ['renderer', 'setContext', 'createExpressionContext']
    QgsPointClusterRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgspointdisplacementrendererwidget.h
try:
    QgsPointDisplacementRendererWidget.create = staticmethod(QgsPointDisplacementRendererWidget.create)
    QgsPointDisplacementRendererWidget.__overridden_methods__ = ['renderer', 'setContext', 'createExpressionContext']
    QgsPointDisplacementRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgspresetcolorrampdialog.h
try:
    QgsPresetColorRampWidget.__attribute_docs__ = {'changed': 'Emitted when the dialog settings change\n'}
except (NameError, AttributeError):
    pass
try:
    QgsPresetColorRampDialog.__attribute_docs__ = {'changed': 'Emitted when the dialog settings change\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsprevieweffect.h
try:
    QgsPreviewEffect.__overridden_methods__ = ['draw']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingaggregatewidgets.h
# monkey patching scoped based enum
QgsAggregateMappingModel.ColumnDataIndex.SourceExpression.__doc__ = "Expression"
QgsAggregateMappingModel.ColumnDataIndex.Aggregate.__doc__ = "Aggregate name"
QgsAggregateMappingModel.ColumnDataIndex.Delimiter.__doc__ = "Delimiter"
QgsAggregateMappingModel.ColumnDataIndex.DestinationName.__doc__ = "Destination field name"
QgsAggregateMappingModel.ColumnDataIndex.DestinationType.__doc__ = "Destination field type string"
QgsAggregateMappingModel.ColumnDataIndex.DestinationLength.__doc__ = "Destination field length"
QgsAggregateMappingModel.ColumnDataIndex.DestinationPrecision.__doc__ = "Destination field precision"
QgsAggregateMappingModel.ColumnDataIndex.__doc__ = """The ColumnDataIndex enum represents the column index for the view

* ``SourceExpression``: Expression
* ``Aggregate``: Aggregate name
* ``Delimiter``: Delimiter
* ``DestinationName``: Destination field name
* ``DestinationType``: Destination field type string
* ``DestinationLength``: Destination field length
* ``DestinationPrecision``: Destination field precision

"""
# --
QgsAggregateMappingModel.ColumnDataIndex.baseClass = QgsAggregateMappingModel
try:
    QgsAggregateMappingModel.Aggregate.__attribute_docs__ = {'source': 'The source expression used as the input for the aggregate calculation', 'aggregate': 'Aggregate name', 'delimiter': 'Delimiter string', 'field': 'The field in its current status (it might have been renamed)'}
    QgsAggregateMappingModel.Aggregate.__annotations__ = {'source': str, 'aggregate': str, 'delimiter': str, 'field': 'QgsField'}
    QgsAggregateMappingModel.Aggregate.__doc__ = """The Aggregate struct holds information about an aggregate column"""
    QgsAggregateMappingModel.Aggregate.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsAggregateMappingWidget.__attribute_docs__ = {'changed': 'Emitted when the aggregates defined in the widget are changed.\n'}
    QgsAggregateMappingWidget.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsAggregateMappingModel.__overridden_methods__ = ['rowCount', 'columnCount', 'data', 'headerData', 'flags', 'setData']
    QgsAggregateMappingModel.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingalgorithmconfigurationwidget.h
try:
    QgsProcessingAlgorithmConfigurationWidget.__virtual_methods__ = ['setWidgetContext']
    QgsProcessingAlgorithmConfigurationWidget.__abstract_methods__ = ['configuration', 'setConfiguration']
    QgsProcessingAlgorithmConfigurationWidget.__overridden_methods__ = ['createExpressionContext']
    QgsProcessingAlgorithmConfigurationWidget.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingAlgorithmConfigurationWidgetFactory.__abstract_methods__ = ['create', 'canCreateFor']
    QgsProcessingAlgorithmConfigurationWidgetFactory.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingalgorithmdialogbase.h
# monkey patching scoped based enum
QgsProcessingAlgorithmDialogBase.DialogMode.Single.__doc__ = "Single algorithm execution mode"
QgsProcessingAlgorithmDialogBase.DialogMode.Batch.__doc__ = "Batch processing mode"
QgsProcessingAlgorithmDialogBase.DialogMode.__doc__ = """Dialog modes.

.. versionadded:: 3.24

* ``Single``: Single algorithm execution mode
* ``Batch``: Batch processing mode

"""
# --
try:
    QgsProcessingAlgorithmDialogBase.__attribute_docs__ = {'algorithmAboutToRun': 'Emitted when the algorithm is about to run in the specified ``context``.\n\nThis signal can be used to tweak the ``context`` prior to the algorithm\nexecution.\n\n.. versionadded:: 3.38\n', 'algorithmFinished': 'Emitted whenever an algorithm has finished executing in the dialog.\n\n.. versionadded:: 3.14\n'}
    QgsProcessingAlgorithmDialogBase.formatStringForLog = staticmethod(QgsProcessingAlgorithmDialogBase.formatStringForLog)
    QgsProcessingAlgorithmDialogBase.__virtual_methods__ = ['setParameters', 'resetAdditionalGui', 'blockAdditionalControlsWhileRunning', 'isFinalized', 'finished', 'runAlgorithm', 'algExecuted']
    QgsProcessingAlgorithmDialogBase.__overridden_methods__ = ['reject', 'closeEvent']
    QgsProcessingAlgorithmDialogBase.__signal_arguments__ = {'algorithmAboutToRun': ['context: QgsProcessingContext'], 'algorithmFinished': ['successful: bool', 'result: Dict[str, object]']}
    QgsProcessingAlgorithmDialogBase.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingbatchalgorithmdialogbase.h
try:
    QgsProcessingBatchAlgorithmDialogBase.__abstract_methods__ = ['runAsSingle', 'createContext', 'handleAlgorithmResults', 'loadHtmlResults', 'createSummaryTable']
    QgsProcessingBatchAlgorithmDialogBase.__overridden_methods__ = ['resetAdditionalGui', 'blockAdditionalControlsWhileRunning', 'algExecuted', 'isFinalized']
    QgsProcessingBatchAlgorithmDialogBase.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingfavoritealgorithmmanager.h
try:
    QgsProcessingFavoriteAlgorithmManager.__attribute_docs__ = {'changed': 'Emitted when the list of favorite algorithms is changed, e.g. when a new\nalgorithm ID is added to the list or an existing algorithm ID is removed\nfrom the list.\n'}
    QgsProcessingFavoriteAlgorithmManager.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingguiregistry.h
try:
    QgsProcessingGuiRegistry.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingguiutils.h
try:
    QgsProcessingGuiUtils.ResultLayerDetails.__attribute_docs__ = {'layer': 'Associated map layer.', 'targetLayerTreeGroup': 'Optional target layer tree group, where the layer should be placed.', 'sortKey': 'Sort order key for ordering output layers in the layer tree.', 'destinationProject': 'Destination QGIS project.'}
    QgsProcessingGuiUtils.ResultLayerDetails.__annotations__ = {'layer': 'QgsMapLayer', 'targetLayerTreeGroup': 'QgsLayerTreeGroup', 'sortKey': int, 'destinationProject': 'QgsProject'}
    QgsProcessingGuiUtils.ResultLayerDetails.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingGuiUtils.configureResultLayerTreeLayer = staticmethod(QgsProcessingGuiUtils.configureResultLayerTreeLayer)
    QgsProcessingGuiUtils.layerTreeResultsGroup = staticmethod(QgsProcessingGuiUtils.layerTreeResultsGroup)
    QgsProcessingGuiUtils.addResultLayers = staticmethod(QgsProcessingGuiUtils.addResultLayers)
    QgsProcessingGuiUtils.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessinghistoryprovider.h
try:
    QgsProcessingHistoryProvider.__attribute_docs__ = {'executePython': 'Emitted when the provider needs to execute python ``commands`` in the\nProcessing context.\n\n.. versionadded:: 3.32\n', 'createTest': 'Emitted when the provider needs to create a Processing test with the\ngiven python ``command``.\n\n.. versionadded:: 3.32\n'}
    QgsProcessingHistoryProvider.__overridden_methods__ = ['id', 'createNodeForEntry', 'updateNodeForEntry']
    QgsProcessingHistoryProvider.__signal_arguments__ = {'executePython': ['commands: str'], 'createTest': ['command: str']}
    QgsProcessingHistoryProvider.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessinghistorywidget.h
try:
    QgsProcessingHistoryWidget.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingHistoryDialog.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingmaplayercombobox.h
try:
    QgsProcessingMapLayerComboBox.__attribute_docs__ = {'valueChanged': 'Emitted whenever the value is changed in the widget.\n'}
    QgsProcessingMapLayerComboBox.__overridden_methods__ = ['dragEnterEvent', 'dragLeaveEvent', 'dropEvent']
    QgsProcessingMapLayerComboBox.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingmodelerparameterwidget.h
try:
    QgsProcessingModelerParameterWidget.__virtual_methods__ = ['value']
    QgsProcessingModelerParameterWidget.__overridden_methods__ = ['createExpressionContext']
    QgsProcessingModelerParameterWidget.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingmultipleselectiondialog.h
try:
    QgsProcessingMultipleSelectionPanelWidget.__attribute_docs__ = {'acceptClicked': 'Emitted when the accept button is clicked.\n', 'selectionChanged': 'Emitted when the selection changes in the widget.\n'}
    QgsProcessingMultipleSelectionPanelWidget.__overridden_methods__ = ['dragEnterEvent', 'dropEvent']
    QgsProcessingMultipleSelectionPanelWidget.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingMultipleInputPanelWidget.__overridden_methods__ = ['dragEnterEvent', 'dropEvent']
    QgsProcessingMultipleInputPanelWidget.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingMultipleSelectionDialog.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingMultipleInputDialog.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingoutputdestinationwidget.h
try:
    QgsProcessingLayerOutputDestinationWidget.__attribute_docs__ = {'skipOutputChanged': 'Emitted whenever the "skip output" option is toggled in the widget.\n', 'destinationChanged': 'Emitted whenever the destination value is changed in the widget.\n'}
    QgsProcessingLayerOutputDestinationWidget.__overridden_methods__ = ['dragEnterEvent', 'dragLeaveEvent', 'dropEvent']
    QgsProcessingLayerOutputDestinationWidget.__signal_arguments__ = {'skipOutputChanged': ['skipped: bool']}
    QgsProcessingLayerOutputDestinationWidget.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingparameterdefinitionwidget.h
try:
    QgsProcessingAbstractParameterDefinitionWidget.__virtual_methods__ = ['setWidgetContext']
    QgsProcessingAbstractParameterDefinitionWidget.__abstract_methods__ = ['createParameter']
    QgsProcessingAbstractParameterDefinitionWidget.__overridden_methods__ = ['createExpressionContext']
    QgsProcessingAbstractParameterDefinitionWidget.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingParameterDefinitionDialog.__overridden_methods__ = ['accept']
    QgsProcessingParameterDefinitionDialog.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingParameterDefinitionWidget.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingparameterswidget.h
try:
    QgsProcessingParametersWidget.__virtual_methods__ = ['initWidgets']
    QgsProcessingParametersWidget.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingrecentalgorithmlog.h
try:
    QgsProcessingRecentAlgorithmLog.__attribute_docs__ = {'changed': 'Emitted when the list of recently used algorithms is changed, e.g. when\na new algorithm ID is pushed to the list (see\n:py:func:`~QgsProcessingRecentAlgorithmLog.push`).\n'}
    QgsProcessingRecentAlgorithmLog.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingtoolboxmodel.h
# monkey patching scoped based enum
QgsProcessingToolboxModelNode.NodeProvider = QgsProcessingToolboxModelNode.NodeType.Provider
QgsProcessingToolboxModelNode.NodeType.NodeProvider = QgsProcessingToolboxModelNode.NodeType.Provider
QgsProcessingToolboxModelNode.NodeProvider.is_monkey_patched = True
QgsProcessingToolboxModelNode.NodeProvider.__doc__ = "Provider node"
QgsProcessingToolboxModelNode.NodeGroup = QgsProcessingToolboxModelNode.NodeType.Group
QgsProcessingToolboxModelNode.NodeType.NodeGroup = QgsProcessingToolboxModelNode.NodeType.Group
QgsProcessingToolboxModelNode.NodeGroup.is_monkey_patched = True
QgsProcessingToolboxModelNode.NodeGroup.__doc__ = "Group node"
QgsProcessingToolboxModelNode.NodeAlgorithm = QgsProcessingToolboxModelNode.NodeType.Algorithm
QgsProcessingToolboxModelNode.NodeType.NodeAlgorithm = QgsProcessingToolboxModelNode.NodeType.Algorithm
QgsProcessingToolboxModelNode.NodeAlgorithm.is_monkey_patched = True
QgsProcessingToolboxModelNode.NodeAlgorithm.__doc__ = "Algorithm node"
QgsProcessingToolboxModelNode.NodeRecent = QgsProcessingToolboxModelNode.NodeType.Recent
QgsProcessingToolboxModelNode.NodeType.NodeRecent = QgsProcessingToolboxModelNode.NodeType.Recent
QgsProcessingToolboxModelNode.NodeRecent.is_monkey_patched = True
QgsProcessingToolboxModelNode.NodeRecent.__doc__ = "Recent algorithms node"
QgsProcessingToolboxModelNode.Parameter = QgsProcessingToolboxModelNode.NodeType.Parameter
QgsProcessingToolboxModelNode.Parameter.is_monkey_patched = True
QgsProcessingToolboxModelNode.Parameter.__doc__ = "Parameter node, \n.. versionadded:: 3.44"
QgsProcessingToolboxModelNode.ParameterGroup = QgsProcessingToolboxModelNode.NodeType.ParameterGroup
QgsProcessingToolboxModelNode.ParameterGroup.is_monkey_patched = True
QgsProcessingToolboxModelNode.ParameterGroup.__doc__ = "Parameter group node \n.. versionadded:: 3.44"
QgsProcessingToolboxModelNode.Favorite = QgsProcessingToolboxModelNode.NodeType.Favorite
QgsProcessingToolboxModelNode.Favorite.is_monkey_patched = True
QgsProcessingToolboxModelNode.Favorite.__doc__ = "Favorites algorithms node, \n.. versionadded:: 3.40"
QgsProcessingToolboxModelNode.NodeType.__doc__ = """Enumeration of possible model node types

* ``Provider``: Provider node

  Available as ``QgsProcessingToolboxModelNode.NodeProvider`` in older QGIS releases.

* ``Group``: Group node

  Available as ``QgsProcessingToolboxModelNode.NodeGroup`` in older QGIS releases.

* ``Algorithm``: Algorithm node

  Available as ``QgsProcessingToolboxModelNode.NodeAlgorithm`` in older QGIS releases.

* ``Recent``: Recent algorithms node

  Available as ``QgsProcessingToolboxModelNode.NodeRecent`` in older QGIS releases.

* ``Parameter``: Parameter node,

  .. versionadded:: 3.44

* ``ParameterGroup``: Parameter group node

  .. versionadded:: 3.44

* ``Favorite``: Favorites algorithms node,

  .. versionadded:: 3.40


"""
# --
QgsProcessingToolboxModelNode.NodeType.baseClass = QgsProcessingToolboxModelNode
QgsProcessingToolboxModel.Roles = QgsProcessingToolboxModel.CustomRole
# monkey patching scoped based enum
QgsProcessingToolboxModel.RoleNodeType = QgsProcessingToolboxModel.CustomRole.NodeType
QgsProcessingToolboxModel.Roles.RoleNodeType = QgsProcessingToolboxModel.CustomRole.NodeType
QgsProcessingToolboxModel.RoleNodeType.is_monkey_patched = True
QgsProcessingToolboxModel.RoleNodeType.__doc__ = "Corresponds to the node's type"
QgsProcessingToolboxModel.RoleAlgorithmFlags = QgsProcessingToolboxModel.CustomRole.AlgorithmFlags
QgsProcessingToolboxModel.Roles.RoleAlgorithmFlags = QgsProcessingToolboxModel.CustomRole.AlgorithmFlags
QgsProcessingToolboxModel.RoleAlgorithmFlags.is_monkey_patched = True
QgsProcessingToolboxModel.RoleAlgorithmFlags.__doc__ = "Returns the node's algorithm flags, for algorithm nodes"
QgsProcessingToolboxModel.RoleAlgorithmId = QgsProcessingToolboxModel.CustomRole.AlgorithmId
QgsProcessingToolboxModel.Roles.RoleAlgorithmId = QgsProcessingToolboxModel.CustomRole.AlgorithmId
QgsProcessingToolboxModel.RoleAlgorithmId.is_monkey_patched = True
QgsProcessingToolboxModel.RoleAlgorithmId.__doc__ = "Algorithm ID, for algorithm nodes"
QgsProcessingToolboxModel.RoleAlgorithmName = QgsProcessingToolboxModel.CustomRole.AlgorithmName
QgsProcessingToolboxModel.Roles.RoleAlgorithmName = QgsProcessingToolboxModel.CustomRole.AlgorithmName
QgsProcessingToolboxModel.RoleAlgorithmName.is_monkey_patched = True
QgsProcessingToolboxModel.RoleAlgorithmName.__doc__ = "Untranslated algorithm name, for algorithm nodes"
QgsProcessingToolboxModel.RoleAlgorithmShortDescription = QgsProcessingToolboxModel.CustomRole.AlgorithmShortDescription
QgsProcessingToolboxModel.Roles.RoleAlgorithmShortDescription = QgsProcessingToolboxModel.CustomRole.AlgorithmShortDescription
QgsProcessingToolboxModel.RoleAlgorithmShortDescription.is_monkey_patched = True
QgsProcessingToolboxModel.RoleAlgorithmShortDescription.__doc__ = "Short algorithm description, for algorithm nodes"
QgsProcessingToolboxModel.RoleAlgorithmTags = QgsProcessingToolboxModel.CustomRole.AlgorithmTags
QgsProcessingToolboxModel.Roles.RoleAlgorithmTags = QgsProcessingToolboxModel.CustomRole.AlgorithmTags
QgsProcessingToolboxModel.RoleAlgorithmTags.is_monkey_patched = True
QgsProcessingToolboxModel.RoleAlgorithmTags.__doc__ = "List of algorithm tags, for algorithm nodes"
QgsProcessingToolboxModel.RoleProviderFlags = QgsProcessingToolboxModel.CustomRole.ProviderFlags
QgsProcessingToolboxModel.Roles.RoleProviderFlags = QgsProcessingToolboxModel.CustomRole.ProviderFlags
QgsProcessingToolboxModel.RoleProviderFlags.is_monkey_patched = True
QgsProcessingToolboxModel.RoleProviderFlags.__doc__ = "Returns the node's provider flags"
QgsProcessingToolboxModel.ParameterTypeId = QgsProcessingToolboxModel.CustomRole.ParameterTypeId
QgsProcessingToolboxModel.ParameterTypeId.is_monkey_patched = True
QgsProcessingToolboxModel.ParameterTypeId.__doc__ = "Untranslated parameter type unique identifier for parameter nodes \n.. versionadded:: 3.44"
QgsProcessingToolboxModel.CustomRole.__doc__ = """Custom model roles.

.. note::

   Prior to QGIS 3.36 this was available as QgsProcessingToolboxModel.Roles

.. versionadded:: 3.36

* ``NodeType``: Corresponds to the node's type

  Available as ``QgsProcessingToolboxModel.RoleNodeType`` in older QGIS releases.

* ``AlgorithmFlags``: Returns the node's algorithm flags, for algorithm nodes

  Available as ``QgsProcessingToolboxModel.RoleAlgorithmFlags`` in older QGIS releases.

* ``AlgorithmId``: Algorithm ID, for algorithm nodes

  Available as ``QgsProcessingToolboxModel.RoleAlgorithmId`` in older QGIS releases.

* ``AlgorithmName``: Untranslated algorithm name, for algorithm nodes

  Available as ``QgsProcessingToolboxModel.RoleAlgorithmName`` in older QGIS releases.

* ``AlgorithmShortDescription``: Short algorithm description, for algorithm nodes

  Available as ``QgsProcessingToolboxModel.RoleAlgorithmShortDescription`` in older QGIS releases.

* ``AlgorithmTags``: List of algorithm tags, for algorithm nodes

  Available as ``QgsProcessingToolboxModel.RoleAlgorithmTags`` in older QGIS releases.

* ``ProviderFlags``: Returns the node's provider flags

  Available as ``QgsProcessingToolboxModel.RoleProviderFlags`` in older QGIS releases.

* ``ParameterTypeId``: Untranslated parameter type unique identifier for parameter nodes

  .. versionadded:: 3.44


"""
# --
QgsProcessingToolboxModel.CustomRole.baseClass = QgsProcessingToolboxModel
# monkey patching scoped based enum
QgsProcessingToolboxProxyModel.FilterToolbox = QgsProcessingToolboxProxyModel.Filter.Toolbox
QgsProcessingToolboxProxyModel.Filter.FilterToolbox = QgsProcessingToolboxProxyModel.Filter.Toolbox
QgsProcessingToolboxProxyModel.FilterToolbox.is_monkey_patched = True
QgsProcessingToolboxProxyModel.FilterToolbox.__doc__ = "Filters out any algorithms and content which should not be shown in the toolbox"
QgsProcessingToolboxProxyModel.FilterModeler = QgsProcessingToolboxProxyModel.Filter.Modeler
QgsProcessingToolboxProxyModel.Filter.FilterModeler = QgsProcessingToolboxProxyModel.Filter.Modeler
QgsProcessingToolboxProxyModel.FilterModeler.is_monkey_patched = True
QgsProcessingToolboxProxyModel.FilterModeler.__doc__ = "Filters out any algorithms and content which should not be shown in the modeler"
QgsProcessingToolboxProxyModel.FilterInPlace = QgsProcessingToolboxProxyModel.Filter.InPlace
QgsProcessingToolboxProxyModel.Filter.FilterInPlace = QgsProcessingToolboxProxyModel.Filter.InPlace
QgsProcessingToolboxProxyModel.FilterInPlace.is_monkey_patched = True
QgsProcessingToolboxProxyModel.FilterInPlace.__doc__ = "Only show algorithms which support in-place edits"
QgsProcessingToolboxProxyModel.FilterShowKnownIssues = QgsProcessingToolboxProxyModel.Filter.ShowKnownIssues
QgsProcessingToolboxProxyModel.Filter.FilterShowKnownIssues = QgsProcessingToolboxProxyModel.Filter.ShowKnownIssues
QgsProcessingToolboxProxyModel.FilterShowKnownIssues.is_monkey_patched = True
QgsProcessingToolboxProxyModel.FilterShowKnownIssues.__doc__ = "Show algorithms with known issues (hidden by default)"
QgsProcessingToolboxProxyModel.Filter.__doc__ = """Available filter flags for filtering the model

* ``Toolbox``: Filters out any algorithms and content which should not be shown in the toolbox

  Available as ``QgsProcessingToolboxProxyModel.FilterToolbox`` in older QGIS releases.

* ``Modeler``: Filters out any algorithms and content which should not be shown in the modeler

  Available as ``QgsProcessingToolboxProxyModel.FilterModeler`` in older QGIS releases.

* ``InPlace``: Only show algorithms which support in-place edits

  Available as ``QgsProcessingToolboxProxyModel.FilterInPlace`` in older QGIS releases.

* ``ShowKnownIssues``: Show algorithms with known issues (hidden by default)

  Available as ``QgsProcessingToolboxProxyModel.FilterShowKnownIssues`` in older QGIS releases.


"""
# --
QgsProcessingToolboxProxyModel.Filter.baseClass = QgsProcessingToolboxProxyModel
QgsProcessingToolboxProxyModel.Filters.baseClass = QgsProcessingToolboxProxyModel
Filters = QgsProcessingToolboxProxyModel  # dirty hack since SIP seems to introduce the flags in module
try:
    QgsProcessingToolboxModel.__attribute_docs__ = {'recentAlgorithmAdded': 'Emitted whenever recent algorithms are added to the model.\n', 'favoriteAlgorithmAdded': 'Emitted whenever favorite algorithms are added to the model.\n'}
    QgsProcessingToolboxModel.__overridden_methods__ = ['flags', 'data', 'rowCount', 'columnCount', 'index', 'parent', 'mimeData']
    QgsProcessingToolboxModel.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingToolboxModelNode.__abstract_methods__ = ['nodeType']
    QgsProcessingToolboxModelNode.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingToolboxModelRecentNode.__overridden_methods__ = ['nodeType']
    QgsProcessingToolboxModelRecentNode.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingToolboxModelFavoriteNode.__overridden_methods__ = ['nodeType']
    QgsProcessingToolboxModelFavoriteNode.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingToolboxModelParameterGroupNode.__overridden_methods__ = ['nodeType']
    QgsProcessingToolboxModelParameterGroupNode.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingToolboxModelProviderNode.__overridden_methods__ = ['nodeType']
    QgsProcessingToolboxModelProviderNode.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingToolboxModelGroupNode.__overridden_methods__ = ['nodeType']
    QgsProcessingToolboxModelGroupNode.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingToolboxModelAlgorithmNode.__overridden_methods__ = ['nodeType']
    QgsProcessingToolboxModelAlgorithmNode.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingToolboxModelParameterNode.__overridden_methods__ = ['nodeType']
    QgsProcessingToolboxModelParameterNode.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingToolboxProxyModel.__overridden_methods__ = ['filterAcceptsRow', 'lessThan', 'data']
    QgsProcessingToolboxProxyModel.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingtoolboxtreeview.h
try:
    QgsProcessingToolboxTreeView.__overridden_methods__ = ['reset', 'keyPressEvent']
    QgsProcessingToolboxTreeView.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/processing/qgsprocessingwidgetwrapper.h
# monkey patching scoped based enum
QgsProcessingParametersGenerator.Flag.SkipDefaultValueParameters.__doc__ = "Parameters which are unchanged from their default values should not be included"
QgsProcessingParametersGenerator.Flag.SkipValidation.__doc__ = "Skip validation of parameters. \n.. versionadded:: 3.44"
QgsProcessingParametersGenerator.Flag.__doc__ = """Flags controlling parameter generation.

.. versionadded:: 3.24

* ``SkipDefaultValueParameters``: Parameters which are unchanged from their default values should not be included
* ``SkipValidation``: Skip validation of parameters.

  .. versionadded:: 3.44


"""
# --
try:
    QgsAbstractProcessingParameterWidgetWrapper.__attribute_docs__ = {'widgetValueHasChanged': 'Emitted whenever the parameter value (as defined by the wrapped widget)\nis changed.\n'}
    QgsAbstractProcessingParameterWidgetWrapper.__virtual_methods__ = ['setWidgetContext', 'customProperties', 'registerProcessingContextGenerator', 'postInitialize', 'stretch', 'setDialog', 'createLabel']
    QgsAbstractProcessingParameterWidgetWrapper.__abstract_methods__ = ['createWidget', 'setWidgetValue', 'widgetValue']
    QgsAbstractProcessingParameterWidgetWrapper.__overridden_methods__ = ['createExpressionContext']
    QgsAbstractProcessingParameterWidgetWrapper.__signal_arguments__ = {'widgetValueHasChanged': ['wrapper: QgsAbstractProcessingParameterWidgetWrapper']}
    QgsAbstractProcessingParameterWidgetWrapper.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingParameterWidgetFactoryInterface.__virtual_methods__ = ['createModelerWidgetWrapper', 'createParameterDefinitionWidget', 'compatibleParameterTypes', 'compatibleOutputTypes', 'compatibleDataTypes', 'modelerExpressionFormatString', 'defaultModelSource']
    QgsProcessingParameterWidgetFactoryInterface.__abstract_methods__ = ['parameterType', 'createWidgetWrapper']
    QgsProcessingParameterWidgetFactoryInterface.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingContextGenerator.__abstract_methods__ = ['processingContext']
    QgsProcessingContextGenerator.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingParametersGenerator.__abstract_methods__ = ['createProcessingParameters']
    QgsProcessingParametersGenerator.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingHiddenWidgetWrapper.__overridden_methods__ = ['setWidgetValue', 'widgetValue', 'linkedVectorLayer', 'createWidget', 'createLabel']
    QgsProcessingHiddenWidgetWrapper.__group__ = ['processing']
except (NameError, AttributeError):
    pass
try:
    QgsProcessingParameterWidgetContext.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/proj/qgsprojectionselectiondialog.h
try:
    QgsCrsSelectionWidget.__attribute_docs__ = {'crsChanged': 'Emitted when the CRS defined in the widget is changed.\n', 'crsDoubleClicked': 'Emitted when a CRS entry in the widget is double-clicked.\n', 'hasValidSelectionChanged': 'Emitted when the widget has a valid selection or not.\n'}
    QgsCrsSelectionWidget.__signal_arguments__ = {'crsDoubleClicked': ['crs: QgsCoordinateReferenceSystem'], 'hasValidSelectionChanged': ['isValid: bool']}
    QgsCrsSelectionWidget.__group__ = ['proj']
except (NameError, AttributeError):
    pass
try:
    QgsProjectionSelectionDialog.__group__ = ['proj']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/proj/qgsprojectionselectiontreewidget.h
try:
    QgsProjectionSelectionTreeWidget.__attribute_docs__ = {'crsSelected': 'Emitted when a projection is selected in the widget.\n', 'initialized': 'Notifies others that the widget is now fully initialized, including\ndeferred selection of projection.\n\n.. deprecated:: 3.40\n\n   No longer emitted.\n', 'projectionDoubleClicked': 'Emitted when a projection is double clicked in the list.\n', 'hasValidSelectionChanged': 'Emitted when the selection in the tree is changed from a valid selection\nto an invalid selection, or vice-versa.\n\n.. versionadded:: 3.18\n'}
    QgsProjectionSelectionTreeWidget.__overridden_methods__ = ['resizeEvent', 'eventFilter']
    QgsProjectionSelectionTreeWidget.__signal_arguments__ = {'hasValidSelectionChanged': ['isValid: bool']}
    QgsProjectionSelectionTreeWidget.__group__ = ['proj']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/proj/qgsprojectionselectionwidget.h
try:
    QgsProjectionSelectionWidget.__attribute_docs__ = {'crsChanged': 'Emitted when the selected CRS is changed\n', 'cleared': 'Emitted when the not set option is selected.\n'}
    QgsProjectionSelectionWidget.__overridden_methods__ = ['dragEnterEvent', 'dragLeaveEvent', 'dropEvent']
    QgsProjectionSelectionWidget.__signal_arguments__ = {'crsChanged': ['crs: QgsCoordinateReferenceSystem']}
    QgsProjectionSelectionWidget.__group__ = ['proj']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsprojectstorageguiprovider.h
try:
    QgsProjectStorageGuiProvider.__virtual_methods__ = ['visibleName', 'showLoadGui', 'showSaveGui']
    QgsProjectStorageGuiProvider.__abstract_methods__ = ['type']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgspropertyassistantwidget.h
try:
    QgsPropertyAssistantWidget.__overridden_methods__ = ['setDockMode']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgspropertyoverridebutton.h
try:
    QgsPropertyOverrideButton.__attribute_docs__ = {'changed': 'Emitted when property definition changes\n', 'activated': 'Emitted when the activated status of the widget changes\n', 'createAuxiliaryField': 'Emitted when creating a new auxiliary field\n'}
    QgsPropertyOverrideButton.__overridden_methods__ = ['mouseReleaseEvent']
    QgsPropertyOverrideButton.__signal_arguments__ = {'activated': ['isActive: bool']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsproviderconnectioncombobox.h
try:
    QgsProviderConnectionComboBox.__attribute_docs__ = {'connectionChanged': 'Emitted whenever the currently selected connection changes.\n'}
    QgsProviderConnectionComboBox.__signal_arguments__ = {'connectionChanged': ['connection: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsproviderguimetadata.h
try:
    QgsProviderGuiMetadata.__virtual_methods__ = ['registerGui', 'dataItemGuiProviders', 'projectStorageGuiProviders', 'sourceSelectProviders', 'subsetStringEditorProviders', 'sourceWidgetProviders', 'mapLayerConfigWidgetFactories']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsproviderguiregistry.h
try:
    QgsProviderGuiRegistry.__virtual_methods__ = ['sourceSelectProviders', 'projectStorageGuiProviders', 'subsetStringEditorProviders', 'sourceWidgetProviders', 'mapLayerConfigWidgetFactories']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsprovidersourcewidget.h
try:
    QgsProviderSourceWidget.__attribute_docs__ = {'validChanged': 'Emitted whenever the validation status of the widget changes.\n\nIf ``isValid`` is ``False`` then the widget is not valid, and any dialog\nusing the widget should be prevented from being accepted.\n', 'changed': 'Emitted whenever the configuration of the widget changes.\n\n.. versionadded:: 3.30\n'}
    QgsProviderSourceWidget.__virtual_methods__ = ['groupTitle', 'setMapCanvas', 'mapCanvas']
    QgsProviderSourceWidget.__abstract_methods__ = ['setSourceUri', 'sourceUri']
    QgsProviderSourceWidget.__signal_arguments__ = {'validChanged': ['isValid: bool']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsprovidersourcewidgetprovider.h
try:
    QgsProviderSourceWidgetProvider.__virtual_methods__ = ['name']
    QgsProviderSourceWidgetProvider.__abstract_methods__ = ['providerKey', 'canHandleLayer', 'createWidget']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsprovidersublayersdialog.h
try:
    QgsProviderSublayersDialog.__attribute_docs__ = {'layersAdded': 'Emitted when sublayers selected from the dialog should be added to the\nproject.\n'}
    QgsProviderSublayersDialog.__signal_arguments__ = {'layersAdded': ['layers: List[QgsProviderSublayerDetails]']}
except (NameError, AttributeError):
    pass
try:
    QgsProviderSublayerDialogModel.__overridden_methods__ = ['data', 'flags']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsqmlwidgetwrapper.h
try:
    QgsQmlWidgetWrapper.__overridden_methods__ = ['valid', 'createWidget', 'initWidget', 'setFeature']
    QgsQmlWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsquerybuilder.h
try:
    QgsQueryBuilder.saveQueryToFile = staticmethod(QgsQueryBuilder.saveQueryToFile)
    QgsQueryBuilder.loadQueryFromFile = staticmethod(QgsQueryBuilder.loadQueryFromFile)
    QgsQueryBuilder.__virtual_methods__ = ['test']
    QgsQueryBuilder.__overridden_methods__ = ['showEvent', 'subsetString', 'setSubsetString', 'accept', 'reject']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsqueryresultwidget.h
# monkey patching scoped based enum
QgsQueryResultWidget.QueryWidgetMode.SqlQueryMode.__doc__ = "Defaults widget mode for SQL execution and SQL query layer creation."
QgsQueryResultWidget.QueryWidgetMode.QueryLayerUpdateMode.__doc__ = "SQL query layer update mode: the create SQL layer button is renamed to 'Update' and the SQL layer creation group box is expanded."
QgsQueryResultWidget.QueryWidgetMode.__doc__ = """The QueryWidgetMode enum represents various modes for the widget appearance.

* ``SqlQueryMode``: Defaults widget mode for SQL execution and SQL query layer creation.
* ``QueryLayerUpdateMode``: SQL query layer update mode: the create SQL layer button is renamed to 'Update' and the SQL layer creation group box is expanded.

"""
# --
QgsQueryResultWidget.QueryWidgetMode.baseClass = QgsQueryResultWidget
try:
    QgsQueryResultWidget.__attribute_docs__ = {'createSqlVectorLayer': 'Emitted when a new vector SQL (query) layer must be created.\n\n:param providerKey: name of the data provider\n:param connectionUri: the connection URI as returned by\n                      :py:func:`QgsAbstractProviderConnection.uri()`\n:param options: \n', 'firstResultBatchFetched': 'Emitted when the first batch of results has been fetched.\n\n.. note::\n\n   If the query returns no results this signal is not emitted.\n'}
    QgsQueryResultWidget.__signal_arguments__ = {'createSqlVectorLayer': ['providerKey: str', 'connectionUri: str', 'options: QgsAbstractDatabaseProviderConnection.SqlVectorLayerOptions']}
except (NameError, AttributeError):
    pass
try:
    QgsQueryResultDialog.__overridden_methods__ = ['closeEvent']
except (NameError, AttributeError):
    pass
try:
    QgsQueryResultMainWindow.__overridden_methods__ = ['closeEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsrangeslider.h
try:
    QgsRangeSlider.__attribute_docs__ = {'rangeChanged': 'Emitted when the range selected in the widget is changed.\n', 'rangeLimitsChanged': 'Emitted when the limits of values allowed in the widget is changed.\n', 'fixedRangeSizeChanged': "Emitted when the widget's fixed range size is changed.\n\n.. seealso:: :py:func:`fixedRangeSize`\n\n.. seealso:: :py:func:`setFixedRangeSize`\n\n.. versionadded:: 3.38\n"}
    QgsRangeSlider.__overridden_methods__ = ['paintEvent', 'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent', 'keyPressEvent', 'sizeHint', 'minimumSizeHint', 'event']
    QgsRangeSlider.__signal_arguments__ = {'rangeChanged': ['minimum: int', 'maximum: int'], 'rangeLimitsChanged': ['minimum: int', 'maximum: int'], 'fixedRangeSizeChanged': ['size: int']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsrasterattributetabledialog.h
try:
    QgsRasterAttributeTableDialog.__overridden_methods__ = ['reject']
    QgsRasterAttributeTableDialog.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsrasterattributetablemodel.h
try:
    QgsRasterAttributeTableModel.__overridden_methods__ = ['rowCount', 'columnCount', 'data', 'setData', 'headerData', 'flags']
    QgsRasterAttributeTableModel.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsrasterattributetablewidget.h
try:
    QgsRasterAttributeTableWidget.__attribute_docs__ = {'rendererChanged': 'This signal is emitted after a successful classify operation which\nchanged the raster renderer.\n'}
    QgsRasterAttributeTableWidget.__overridden_methods__ = ['setDockMode']
    QgsRasterAttributeTableWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsrasterbandcombobox.h
try:
    QgsRasterBandComboBox.__attribute_docs__ = {'bandChanged': 'Emitted when the currently selected band changes.\n'}
    QgsRasterBandComboBox.displayBandName = staticmethod(QgsRasterBandComboBox.displayBandName)
    QgsRasterBandComboBox.__signal_arguments__ = {'bandChanged': ['band: int']}
    QgsRasterBandComboBox.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsrastercontourrendererwidget.h
try:
    QgsRasterContourRendererWidget.create = staticmethod(QgsRasterContourRendererWidget.create)
    QgsRasterContourRendererWidget.__overridden_methods__ = ['renderer']
    QgsRasterContourRendererWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsrasterformatsaveoptionswidget.h
try:
    QgsRasterFormatSaveOptionsWidget.__attribute_docs__ = {'optionsChanged': 'Emitted when the options configured in the widget are changed.\n'}
    QgsRasterFormatSaveOptionsWidget.__overridden_methods__ = ['showEvent', 'eventFilter']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsrasterhistogramwidget.h
try:
    QgsRasterHistogramWidget.__overridden_methods__ = ['apply']
    QgsRasterHistogramWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsrasterlayerproperties.h
try:
    QgsRasterLayerProperties.__virtual_methods__ = ['addPropertiesPageFactory', 'optionsStackedWidget_CurrentChanged', 'apply', 'rollback']
    QgsRasterLayerProperties.__overridden_methods__ = ['createExpressionContext', 'eventFilter']
    QgsRasterLayerProperties.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsrasterlayersaveasdialog.h
try:
    QgsRasterLayerSaveAsDialog.__overridden_methods__ = ['accept']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsrasterlayertemporalpropertieswidget.h
try:
    QgsRasterLayerTemporalPropertiesWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsrasterminmaxwidget.h
try:
    QgsRasterMinMaxWidget.__attribute_docs__ = {'widgetChanged': 'Emitted when something on the widget has changed. All widgets will fire\nthis event to notify of an internal change.\n', 'load': 'signal emitted when new min/max values are computed from statistics.\n'}
    QgsRasterMinMaxWidget.__signal_arguments__ = {'load': ['bandNo: int', 'min: float', 'max: float']}
    QgsRasterMinMaxWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsrasterpyramidsoptionswidget.h
try:
    QgsRasterPyramidsOptionsWidget.__attribute_docs__ = {'overviewListChanged': 'Emitted when the list of configured overviews is changed.\n', 'someValueChanged': 'Emitted when settings are changed in the widget.\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsrasterrendererwidget.h
try:
    QgsRasterRendererWidget.__attribute_docs__ = {'widgetChanged': 'Emitted when something on the widget has changed. All widgets will fire\nthis event to notify of an internal change.\n'}
    QgsRasterRendererWidget.__virtual_methods__ = ['setMapCanvas', 'min', 'max', 'setMin', 'setMax', 'stdDev', 'setStdDev', 'selectedBand', 'doComputations', 'minMaxWidget', 'contrastEnhancementAlgorithm', 'setContrastEnhancementAlgorithm']
    QgsRasterRendererWidget.__abstract_methods__ = ['renderer']
    QgsRasterRendererWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsrastertransparencywidget.h
try:
    QgsRasterTransparencyWidget.__overridden_methods__ = ['createExpressionContext', 'apply']
    QgsRasterTransparencyWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsratiolockbutton.h
try:
    QgsRatioLockButton.__attribute_docs__ = {'lockChanged': 'Emitted whenever the lock state changes.\n'}
    QgsRatioLockButton.__overridden_methods__ = ['changeEvent', 'showEvent', 'resizeEvent']
    QgsRatioLockButton.__signal_arguments__ = {'lockChanged': ['locked: bool']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/proj/qgsrecentcoordinatereferencesystemsmodel.h
QgsRecentCoordinateReferenceSystemsModel.Roles = QgsRecentCoordinateReferenceSystemsModel.CustomRole
# monkey patching scoped based enum
QgsRecentCoordinateReferenceSystemsModel.RoleCrs = QgsRecentCoordinateReferenceSystemsModel.CustomRole.Crs
QgsRecentCoordinateReferenceSystemsModel.Roles.RoleCrs = QgsRecentCoordinateReferenceSystemsModel.CustomRole.Crs
QgsRecentCoordinateReferenceSystemsModel.RoleCrs.is_monkey_patched = True
QgsRecentCoordinateReferenceSystemsModel.RoleCrs.__doc__ = "Coordinate reference system"
QgsRecentCoordinateReferenceSystemsModel.RoleAuthId = QgsRecentCoordinateReferenceSystemsModel.CustomRole.AuthId
QgsRecentCoordinateReferenceSystemsModel.Roles.RoleAuthId = QgsRecentCoordinateReferenceSystemsModel.CustomRole.AuthId
QgsRecentCoordinateReferenceSystemsModel.RoleAuthId.is_monkey_patched = True
QgsRecentCoordinateReferenceSystemsModel.RoleAuthId.__doc__ = "CRS authority ID"
QgsRecentCoordinateReferenceSystemsModel.CustomRole.__doc__ = """Custom model roles.

* ``Crs``: Coordinate reference system

  Available as ``QgsRecentCoordinateReferenceSystemsModel.RoleCrs`` in older QGIS releases.

* ``AuthId``: CRS authority ID

  Available as ``QgsRecentCoordinateReferenceSystemsModel.RoleAuthId`` in older QGIS releases.


"""
# --
QgsRecentCoordinateReferenceSystemsModel.CustomRole.baseClass = QgsRecentCoordinateReferenceSystemsModel
try:
    QgsRecentCoordinateReferenceSystemsModel.__overridden_methods__ = ['flags', 'data', 'rowCount', 'columnCount', 'index', 'parent']
    QgsRecentCoordinateReferenceSystemsModel.__group__ = ['proj']
except (NameError, AttributeError):
    pass
try:
    QgsRecentCoordinateReferenceSystemsProxyModel.__overridden_methods__ = ['filterAcceptsRow']
    QgsRecentCoordinateReferenceSystemsProxyModel.__group__ = ['proj']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsrelationaggregatesearchwidgetwrapper.h
try:
    QgsRelationAggregateSearchWidgetWrapper.__overridden_methods__ = ['expression', 'valid', 'createWidget', 'applyDirectly', 'setExpression', 'eventFilter']
    QgsRelationAggregateSearchWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsrelationeditorwidget.h
QgsRelationEditorWidget.Button.baseClass = QgsRelationEditorWidget
QgsRelationEditorWidget.Buttons.baseClass = QgsRelationEditorWidget
Buttons = QgsRelationEditorWidget  # dirty hack since SIP seems to introduce the flags in module
try:
    QgsRelationEditorWidget.__overridden_methods__ = ['setEditorContext', 'config', 'setConfig', 'parentFormValueChanged', 'updateUi', 'beforeSetRelationFeature', 'afterSetRelationFeature', 'beforeSetRelations', 'afterSetRelations']
except (NameError, AttributeError):
    pass
try:
    QgsRelationEditorConfigWidget.__overridden_methods__ = ['config', 'setConfig']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsrelationreferencesearchwidgetwrapper.h
try:
    QgsRelationReferenceSearchWidgetWrapper.__overridden_methods__ = ['applyDirectly', 'expression', 'valid', 'supportedFlags', 'defaultFlags', 'createExpression', 'clearWidget', 'setEnabled', 'createWidget', 'initWidget', 'setExpression']
    QgsRelationReferenceSearchWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsrelationreferencewidget.h
try:
    QgsRelationReferenceWidget.__attribute_docs__ = {'foreignKeyChanged': 'Emitted when the foreign key changed\n\n.. deprecated:: 3.10\n', 'foreignKeysChanged': 'Emitted when the foreign keys changed\n\n.. versionadded:: 3.10\n'}
    QgsRelationReferenceWidget.__overridden_methods__ = ['showEvent']
    QgsRelationReferenceWidget.__signal_arguments__ = {'foreignKeysChanged': ['keys: List[object]']}
    QgsRelationReferenceWidget.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsrelationreferencewidgetwrapper.h
try:
    QgsRelationReferenceWidgetWrapper.__overridden_methods__ = ['createWidget', 'initWidget', 'value', 'valid', 'showIndeterminateState', 'additionalFieldValues', 'additionalFields', 'setEnabled', 'parentFormValueChanged', 'updateConstraintWidgetStatus']
    QgsRelationReferenceWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsrelationwidgetwrapper.h
try:
    QgsRelationWidgetWrapper.__attribute_docs__ = {'relatedFeaturesChanged': 'Emit this signal, whenever the related features changed. This happens\nfor example when related features are added, removed, linked or\nunlinked.\n\n.. versionadded:: 3.22\n'}
    QgsRelationWidgetWrapper.__overridden_methods__ = ['createWidget', 'initWidget', 'valid', 'setFeature']
    QgsRelationWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsrendererpropertiesdialog.h
try:
    QgsRendererPropertiesDialog.__attribute_docs__ = {'layerVariablesChanged': 'Emitted when expression context variables on the associated vector\nlayers have been changed. Will request the parent dialog to\nre-synchronize with the variables.\n', 'widgetChanged': 'Emitted when something on the widget has changed. All widgets will fire\nthis event to notify of an internal change.\n', 'showPanel': 'Emit when you require a panel to be show in the interface.\n\n:param panel: The panel widget to show.\n\n.. note::\n\n   If you are connected to this signal you should also connect\n   given panels showPanel signal as they can be nested.\n'}
    QgsRendererPropertiesDialog.__overridden_methods__ = ['keyPressEvent']
    QgsRendererPropertiesDialog.__signal_arguments__ = {'showPanel': ['panel: QgsPanelWidget']}
    QgsRendererPropertiesDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgsrendererrasterpropertieswidget.h
try:
    QgsRendererRasterPropertiesWidget.__overridden_methods__ = ['apply']
    QgsRendererRasterPropertiesWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsrendererwidget.h
try:
    QgsRendererWidget.__attribute_docs__ = {'layerVariablesChanged': 'Emitted when expression context variables on the associated vector\nlayers have been changed. Will request the parent dialog to\nre-synchronize with the variables.\n', 'symbolLevelsChanged': 'Emitted when the symbol levels settings have been changed.\n\n.. deprecated:: 3.20\n\n   No longer emitted.\n'}
    QgsRendererWidget.__virtual_methods__ = ['setContext', 'selectedSymbols', 'refreshSymbolView', 'setSymbolLevels', 'copy', 'paste', 'pasteSymbolToSelection', 'apply']
    QgsRendererWidget.__abstract_methods__ = ['renderer']
    QgsRendererWidget.__overridden_methods__ = ['createExpressionContext', 'setDockMode']
    QgsRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsDataDefinedValueDialog.__abstract_methods__ = ['symbolDataDefined', 'value', 'setDataDefined']
    QgsDataDefinedValueDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsDataDefinedSizeDialog.__overridden_methods__ = ['symbolDataDefined', 'value', 'setDataDefined']
    QgsDataDefinedSizeDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsDataDefinedRotationDialog.__overridden_methods__ = ['symbolDataDefined', 'value', 'setDataDefined']
    QgsDataDefinedRotationDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsDataDefinedWidthDialog.__overridden_methods__ = ['symbolDataDefined', 'value', 'setDataDefined']
    QgsDataDefinedWidthDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsrichtexteditor.h
# monkey patching scoped based enum
QgsRichTextEditor.Mode.QTextDocument.__doc__ = "Default mode, exposes the Qt supported HTML/CSS subset"
QgsRichTextEditor.Mode.QgsTextRenderer.__doc__ = "QGIS text renderer mode, exposes the HTML/CSS subset supported by the QgsTextRenderer class"
QgsRichTextEditor.Mode.PlainText.__doc__ = "Plain text mode"
QgsRichTextEditor.Mode.__doc__ = """Widget modes.

.. versionadded:: 3.40

* ``QTextDocument``: Default mode, exposes the Qt supported HTML/CSS subset
* ``QgsTextRenderer``: QGIS text renderer mode, exposes the HTML/CSS subset supported by the QgsTextRenderer class
* ``PlainText``: Plain text mode

"""
# --
QgsRichTextEditor.Mode.baseClass = QgsRichTextEditor
try:
    QgsRichTextEditor.__attribute_docs__ = {'textChanged': 'Emitted when the text contents are changed.\n\n.. versionadded:: 3.26\n'}
    QgsRichTextEditor.__overridden_methods__ = ['focusInEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsrubberband.h
try:
    QgsRubberBand.__overridden_methods__ = ['updatePosition', 'paint']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsrulebasedrendererwidget.h
try:
    QgsRuleBasedRendererWidget.create = staticmethod(QgsRuleBasedRendererWidget.create)
    QgsRuleBasedRendererWidget.__overridden_methods__ = ['renderer', 'setDockMode', 'setSymbolLevels', 'selectedSymbols', 'refreshSymbolView', 'keyPressEvent', 'copy', 'paste', 'pasteSymbolToSelection']
    QgsRuleBasedRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsRuleBasedRendererModel.__overridden_methods__ = ['flags', 'data', 'headerData', 'rowCount', 'columnCount', 'index', 'parent', 'setData', 'supportedDropActions', 'mimeTypes', 'mimeData', 'dropMimeData', 'removeRows']
    QgsRuleBasedRendererModel.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsRendererRulePropsWidget.__overridden_methods__ = ['setDockMode']
    QgsRendererRulePropsWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsRendererRulePropsDialog.__overridden_methods__ = ['accept']
    QgsRendererRulePropsDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsscalecombobox.h
try:
    QgsScaleComboBox.__attribute_docs__ = {'scaleChanged': 'Emitted when *user* has finished editing/selecting a new scale. The\n``scale`` value indicates the scale denominator, e.g. 1000.0 for a\n1:1000 map.\n'}
    QgsScaleComboBox.toString = staticmethod(QgsScaleComboBox.toString)
    QgsScaleComboBox.toDouble = staticmethod(QgsScaleComboBox.toDouble)
    QgsScaleComboBox.__overridden_methods__ = ['showPopup']
    QgsScaleComboBox.__signal_arguments__ = {'scaleChanged': ['scale: float']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsscalemethodwidget.h
try:
    QgsScaleMethodWidget.__attribute_docs__ = {'methodChanged': 'Emitted when the selected method is changed.\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsscalerangewidget.h
try:
    QgsScaleRangeWidget.__attribute_docs__ = {'rangeChanged': 'Emitted when the scale range set in the widget is changed. The scale\nvalues indicates the scale denominator, e.g. 1000.0 for a 1:1000 map, or\n0 to indicate not set.\n'}
    QgsScaleRangeWidget.__signal_arguments__ = {'rangeChanged': ['min: float', 'max: float']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsscalewidget.h
try:
    QgsScaleWidget.__attribute_docs__ = {'scaleChanged': 'Emitted when *user* has finished editing/selecting a new scale. The\n``scale`` value indicates the scale denominator, e.g. 1000.0 for a\n1:1000 map.\n'}
    QgsScaleWidget.toString = staticmethod(QgsScaleWidget.toString)
    QgsScaleWidget.toDouble = staticmethod(QgsScaleWidget.toDouble)
    QgsScaleWidget.__signal_arguments__ = {'scaleChanged': ['scale: float']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsscreenhelper.h
try:
    QgsScreenHelper.__attribute_docs__ = {'screenDpiChanged': 'Emitted whenever the screen ``dpi`` associated with the widget is\nchanged.\n\n.. seealso:: :py:func:`screenDpi`\n', 'availableGeometryChanged': 'Emitted whenever the available geometry of the screen associated with\nthe widget is changed.\n\n.. seealso:: :py:func:`availableGeometry`\n'}
    QgsScreenHelper.__overridden_methods__ = ['eventFilter']
    QgsScreenHelper.__signal_arguments__ = {'screenDpiChanged': ['dpi: float'], 'availableGeometryChanged': ['geometry: QRect']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsscrollarea.h
try:
    QgsScrollArea.__overridden_methods__ = ['wheelEvent', 'resizeEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgssearchwidgettoolbutton.h
try:
    QgsSearchWidgetToolButton.__attribute_docs__ = {'activeFlagsChanged': 'Emitted when the active flags selected in the widget is changed\n\n:param flags: active flags\n'}
    QgsSearchWidgetToolButton.__signal_arguments__ = {'activeFlagsChanged': ['flags: QgsSearchWidgetWrapper.FilterFlags']}
    QgsSearchWidgetToolButton.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/core/qgssearchwidgetwrapper.h
try:
    QgsSearchWidgetWrapper.__attribute_docs__ = {'expressionChanged': 'Emitted whenever the expression changes\n\n:param exp: The new search expression\n', 'valueChanged': 'Emitted when a user changes the value of the search widget.\n', 'valueCleared': 'Emitted when a user changes the value of the search widget back to an\nempty, default state.\n'}
    QgsSearchWidgetWrapper.exclusiveFilterFlags = staticmethod(QgsSearchWidgetWrapper.exclusiveFilterFlags)
    QgsSearchWidgetWrapper.nonExclusiveFilterFlags = staticmethod(QgsSearchWidgetWrapper.nonExclusiveFilterFlags)
    QgsSearchWidgetWrapper.toString = staticmethod(QgsSearchWidgetWrapper.toString)
    QgsSearchWidgetWrapper.__virtual_methods__ = ['supportedFlags', 'defaultFlags', 'createExpression', 'clearWidget']
    QgsSearchWidgetWrapper.__abstract_methods__ = ['expression', 'applyDirectly', 'setExpression']
    QgsSearchWidgetWrapper.__overridden_methods__ = ['setEnabled', 'setFeature']
    QgsSearchWidgetWrapper.__signal_arguments__ = {'expressionChanged': ['exp: str']}
    QgsSearchWidgetWrapper.__group__ = ['editorwidgets', 'core']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/sensor/qgssensorguiregistry.h
try:
    QgsSensorGuiRegistry.__attribute_docs__ = {'sensorAdded': 'Emitted whenever a new sensor type is added to the registry, with the\nspecified ``type``.\n'}
    QgsSensorGuiRegistry.__signal_arguments__ = {'sensorAdded': ['type: str', 'name: str']}
    QgsSensorGuiRegistry.__group__ = ['sensor']
except (NameError, AttributeError):
    pass
try:
    QgsSensorAbstractGuiMetadata.__virtual_methods__ = ['creationIcon', 'createSensorWidget', 'createSensor']
    QgsSensorAbstractGuiMetadata.__group__ = ['sensor']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/sensor/qgssensorwidget.h
try:
    QgsAbstractSensorWidget.__attribute_docs__ = {'changed': 'Emitted whenever configuration changes happened on this sensor\nconfiguration.\n'}
    QgsAbstractSensorWidget.__abstract_methods__ = ['createSensor', 'updateSensor', 'setSensor']
    QgsAbstractSensorWidget.__group__ = ['sensor']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/settings/qgssettingseditorwidgetregistry.h
try:
    QgsSettingsEditorWidgetRegistry.__group__ = ['settings']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/settings/qgssettingseditorwidgetwrapper.h
try:
    QgsSettingsEditorWidgetWrapper.fromWidget = staticmethod(QgsSettingsEditorWidgetWrapper.fromWidget)
    QgsSettingsEditorWidgetWrapper.__abstract_methods__ = ['id', 'createWrapper', 'setWidgetFromSetting', 'setSettingFromWidget', 'variantValueFromWidget', 'setWidgetFromVariant', 'createEditorPrivate', 'configureEditorPrivate', 'enableAutomaticUpdatePrivate']
    QgsSettingsEditorWidgetWrapper.__group__ = ['settings']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/settings/qgssettingseditorwidgetwrapperimpl.h
# monkey patching scoped based enum
QgsSettingsStringComboBoxWrapper.Mode.Text.__doc__ = "Value is defined as the text entry"
QgsSettingsStringComboBoxWrapper.Mode.Data.__doc__ = "Value is defined as data entry with Qt.UserRole"
QgsSettingsStringComboBoxWrapper.Mode.__doc__ = """Mode to determine if the value is hold in the combo box text or data

* ``Text``: Value is defined as the text entry
* ``Data``: Value is defined as data entry with Qt.UserRole

"""
# --
try:
    QgsSettingsEditorWidgetWrapperTemplate.__virtual_methods__ = ['configureEditorPrivateImplementation']
    QgsSettingsEditorWidgetWrapperTemplate.__abstract_methods__ = ['id', 'setSettingFromWidget', 'setWidgetValue', 'valueFromWidget', 'createWrapper']
    QgsSettingsEditorWidgetWrapperTemplate.__overridden_methods__ = ['id', 'setWidgetFromSetting', 'setSettingFromWidget', 'setWidgetFromVariant', 'variantValueFromWidget', 'createWrapper', 'createEditorPrivate', 'configureEditorPrivate']
    QgsSettingsEditorWidgetWrapperTemplate.__group__ = ['settings']
except (NameError, AttributeError):
    pass
try:
    QgsSettingsStringLineEditWrapper.__overridden_methods__ = ['createWrapper', 'id', 'setSettingFromWidget', 'valueFromWidget', 'setWidgetValue', 'enableAutomaticUpdatePrivate']
    QgsSettingsStringLineEditWrapper.__group__ = ['settings']
except (NameError, AttributeError):
    pass
try:
    QgsSettingsStringComboBoxWrapper.__overridden_methods__ = ['createWrapper', 'id', 'setSettingFromWidget', 'valueFromWidget', 'setWidgetValue', 'enableAutomaticUpdatePrivate']
    QgsSettingsStringComboBoxWrapper.__group__ = ['settings']
except (NameError, AttributeError):
    pass
try:
    QgsSettingsBoolCheckBoxWrapper.__overridden_methods__ = ['createWrapper', 'id', 'setSettingFromWidget', 'valueFromWidget', 'setWidgetValue', 'enableAutomaticUpdatePrivate']
    QgsSettingsBoolCheckBoxWrapper.__group__ = ['settings']
except (NameError, AttributeError):
    pass
try:
    QgsSettingsIntegerSpinBoxWrapper.__overridden_methods__ = ['createWrapper', 'id', 'setSettingFromWidget', 'valueFromWidget', 'setWidgetValue', 'enableAutomaticUpdatePrivate']
    QgsSettingsIntegerSpinBoxWrapper.__group__ = ['settings']
except (NameError, AttributeError):
    pass
try:
    QgsSettingsDoubleSpinBoxWrapper.__overridden_methods__ = ['createWrapper', 'id', 'setSettingFromWidget', 'valueFromWidget', 'setWidgetValue', 'enableAutomaticUpdatePrivate']
    QgsSettingsDoubleSpinBoxWrapper.__group__ = ['settings']
except (NameError, AttributeError):
    pass
try:
    QgsSettingsColorButtonWrapper.__overridden_methods__ = ['createWrapper', 'id', 'setSettingFromWidget', 'valueFromWidget', 'setWidgetValue', 'configureEditorPrivateImplementation', 'enableAutomaticUpdatePrivate']
    QgsSettingsColorButtonWrapper.__group__ = ['settings']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/settings/qgssettingsregistrygui.h
try:
    QgsSettingsRegistryGui.__group__ = ['settings']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/settings/qgssettingstreemodel.h
# monkey patching scoped based enum
QgsSettingsTreeModel.Column.Name.__doc__ = "Name"
QgsSettingsTreeModel.Column.Value.__doc__ = "Value"
QgsSettingsTreeModel.Column.Description.__doc__ = "Description"
QgsSettingsTreeModel.Column.__doc__ = """Columns

* ``Name``: Name
* ``Value``: Value
* ``Description``: Description

"""
# --
try:
    QgsSettingsTreeModel.__overridden_methods__ = ['index', 'parent', 'rowCount', 'columnCount', 'data', 'headerData', 'flags', 'setData']
    QgsSettingsTreeModel.__group__ = ['settings']
except (NameError, AttributeError):
    pass
try:
    QgsSettingsTreeProxyModel.__overridden_methods__ = ['filterAcceptsRow']
    QgsSettingsTreeProxyModel.__group__ = ['settings']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/settings/qgssettingstreewidget.h
try:
    QgsSettingsTreeWidget.__overridden_methods__ = ['searchText', 'highlightText', 'reset']
    QgsSettingsTreeWidget.__group__ = ['settings']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgssinglebandgrayrendererwidget.h
try:
    QgsSingleBandGrayRendererWidget.create = staticmethod(QgsSingleBandGrayRendererWidget.create)
    QgsSingleBandGrayRendererWidget.__overridden_methods__ = ['renderer', 'setMapCanvas', 'min', 'max', 'setMin', 'setMax', 'selectedBand', 'contrastEnhancementAlgorithm', 'setContrastEnhancementAlgorithm', 'doComputations', 'minMaxWidget']
    QgsSingleBandGrayRendererWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/raster/qgssinglebandpseudocolorrendererwidget.h
try:
    QgsSingleBandPseudoColorRendererWidget.create = staticmethod(QgsSingleBandPseudoColorRendererWidget.create)
    QgsSingleBandPseudoColorRendererWidget.__overridden_methods__ = ['renderer', 'setMapCanvas', 'doComputations', 'minMaxWidget', 'min', 'max', 'setMin', 'setMax', 'selectedBand']
    QgsSingleBandPseudoColorRendererWidget.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgssinglesymbolrendererwidget.h
try:
    QgsSingleSymbolRendererWidget.create = staticmethod(QgsSingleSymbolRendererWidget.create)
    QgsSingleSymbolRendererWidget.__overridden_methods__ = ['renderer', 'setContext', 'setDockMode', 'setSymbolLevels']
    QgsSingleSymbolRendererWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsslider.h
try:
    QgsSlider.__overridden_methods__ = ['paintEvent']
    QgsSlider.__signal_arguments__ = {'valueChanged': [': object']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgssmartgroupeditordialog.h
try:
    QgsSmartGroupCondition.__attribute_docs__ = {'removed': 'Emitted when the group with the specified ``id`` is removed.\n'}
    QgsSmartGroupCondition.__signal_arguments__ = {'removed': ['id: int']}
    QgsSmartGroupCondition.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSmartGroupEditorDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgssnaptogridcanvasitem.h
try:
    QgsSnapToGridCanvasItem.__overridden_methods__ = ['paint']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgssourceselectprovider.h
# monkey patching scoped based enum
QgsSourceSelectProvider.Capability.NoCapabilities.__doc__ = "No capabilities"
QgsSourceSelectProvider.Capability.ConfigureFromUri.__doc__ = "The source select widget can be configured from a URI"
QgsSourceSelectProvider.Capability.__doc__ = """The Capability enum describes the capabilities of the source select implementation.

.. versionadded:: 3.38

* ``NoCapabilities``: No capabilities
* ``ConfigureFromUri``: The source select widget can be configured from a URI

"""
# --
QgsSourceSelectProvider.Capability.baseClass = QgsSourceSelectProvider
QgsSourceSelectProvider.Capabilities.baseClass = QgsSourceSelectProvider
Capabilities = QgsSourceSelectProvider  # dirty hack since SIP seems to introduce the flags in module
try:
    QgsSourceSelectProvider.__virtual_methods__ = ['name', 'toolTip', 'ordering', 'capabilities']
    QgsSourceSelectProvider.__abstract_methods__ = ['providerKey', 'text', 'icon', 'createDataSourceWidget']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgssourceselectproviderregistry.h
try:
    QgsSourceSelectProviderRegistry.__attribute_docs__ = {'providerAdded': 'Emitted whenever a provider is added to the registry.\n\n.. versionadded:: 3.30\n', 'providerRemoved': 'Emitted whenever a provider is removed from the registry.\n\n.. versionadded:: 3.30\n'}
    QgsSourceSelectProviderRegistry.__signal_arguments__ = {'providerAdded': ['name: str'], 'providerRemoved': ['name: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsspacerwidgetwrapper.h
try:
    QgsSpacerWidgetWrapper.__overridden_methods__ = ['valid', 'createWidget', 'setFeature']
    QgsSpacerWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsspinbox.h
try:
    QgsSpinBox.__attribute_docs__ = {'returnPressed': 'Emitted when the Return or Enter key is used in the line edit\n\n.. versionadded:: 3.40\n', 'textEdited': 'Emitted when the the value has been manually edited via line edit.\n\n.. versionadded:: 3.40\n', 'editingTimeout': 'Emitted when either:\n\n1. 1 second has elapsed since the last value change in the widget (eg last key press or scroll wheel event)\n2. or, immediately after the widget has lost focus after its value was changed.\n\nThis signal can be used to respond semi-instantly to changes in the spin\nbox, without responding too quickly while the user in the middle of\nsetting the value.\n\n.. seealso:: :py:func:`editingTimeoutInterval`\n\n.. versionadded:: 3.42\n'}
    QgsSpinBox.__overridden_methods__ = ['clear', 'valueFromText', 'validate', 'stepBy', 'changeEvent', 'paintEvent', 'wheelEvent', 'timerEvent', 'focusOutEvent']
    QgsSpinBox.__signal_arguments__ = {'textEdited': ['text: str'], 'editingTimeout': ['value: int']}
    QgsSpinBox.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsstatusbar.h
try:
    QgsStatusBar.__overridden_methods__ = ['changeEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsstoredquerymanager.h
try:
    QgsStoredQueryManager.QueryDetails.__attribute_docs__ = {'name': 'Name of the query.', 'definition': 'Query definition.', 'backend': 'Storage backend.'}
    QgsStoredQueryManager.QueryDetails.__annotations__ = {'name': str, 'definition': str, 'backend': 'Qgis.QueryStorageBackend'}
except (NameError, AttributeError):
    pass
try:
    QgsStoredQueryManager.__attribute_docs__ = {'queryAdded': 'Emitted when a query is added to the manager.\n', 'queryChanged': 'Emitted when an existing query is changed in the manager.\n', 'queryRemoved': 'Emitted when a query is removed from the manager.\n'}
    QgsStoredQueryManager.__signal_arguments__ = {'queryAdded': ['name: str', 'backend: Qgis.QueryStorageBackend'], 'queryChanged': ['name: str', 'backend: Qgis.QueryStorageBackend'], 'queryRemoved': ['name: str', 'backend: Qgis.QueryStorageBackend']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsstyleexportimportdialog.h
try:
    QgsStyleExportImportDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsstylegroupselectiondialog.h
try:
    QgsStyleGroupSelectionDialog.__attribute_docs__ = {'tagSelected': 'tag with tagName has been selected\n', 'tagDeselected': 'tag with tagName has been deselected\n', 'smartgroupSelected': 'smartgroup with groupName has been selected\n', 'smartgroupDeselected': 'smart group with groupName has been deselected\n', 'allDeselected': 'all deselected\n', 'allSelected': 'all selected\n', 'favoritesDeselected': 'Favorites has been deselected\n\n.. versionadded:: 3.14\n', 'favoritesSelected': 'Favorites has need selected\n\n.. versionadded:: 3.14\n'}
    QgsStyleGroupSelectionDialog.__signal_arguments__ = {'tagSelected': ['tagName: str'], 'tagDeselected': ['tagName: str'], 'smartgroupSelected': ['groupName: str'], 'smartgroupDeselected': ['groupName: str']}
    QgsStyleGroupSelectionDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsstyleitemslistwidget.h
try:
    QgsStyleItemsListWidget.__attribute_docs__ = {'selectionChanged': 'Emitted when the selected item is changed in the widget.\n\n:param name: Newly selected item name\n:param type: Newly selected item type\n', 'selectionChangedWithStylePath': 'Emitted when the selected item is changed in the widget.\n\n:param name: Newly selected item name\n:param type: Newly selected item type\n:param stylePath: file path to associated style database\n\n.. versionadded:: 3.26\n', 'saveEntity': 'Emitted when the user has opted to save a new entity to the style\ndatabase, by clicking the "Save" button in the widget.\n\nIt is the caller\'s responsibility to handle this in an appropriate\nmanner given the context of the widget.\n'}
    QgsStyleItemsListWidget.__overridden_methods__ = ['showEvent']
    QgsStyleItemsListWidget.__signal_arguments__ = {'selectionChanged': ['name: str', 'type: QgsStyle.StyleEntity'], 'selectionChangedWithStylePath': ['name: str', 'type: QgsStyle.StyleEntity', 'stylePath: str']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsstylemanagerdialog.h
try:
    QgsStyleManagerDialog.addColorRampStatic = staticmethod(QgsStyleManagerDialog.addColorRampStatic)
    QgsStyleManagerDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsstylesavedialog.h
try:
    QgsStyleSaveDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgssublayersdialog.h
QgsSublayersDialog.PromptMode.baseClass = QgsSublayersDialog
try:
    QgsSublayersDialog.LayerDefinition.__attribute_docs__ = {'layerId': 'Identifier of the layer (one unique layer id may have multiple types though)', 'layerName': 'Name of the layer (not necessarily unique)', 'count': 'Number of features (might be unused)', 'type': 'Extra type depending on the use (e.g. geometry type for vector sublayers)', 'description': 'Description.\n\n.. versionadded:: 3.10'}
    QgsSublayersDialog.LayerDefinition.__annotations__ = {'layerId': int, 'layerName': str, 'count': int, 'type': str, 'description': str}
    QgsSublayersDialog.LayerDefinition.__doc__ = """A structure that defines layers for the purpose of this dialog"""
except (NameError, AttributeError):
    pass
try:
    QgsSublayersDialog.__overridden_methods__ = ['exec']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgssubsetstringeditorinterface.h
try:
    QgsSubsetStringEditorInterface.__abstract_methods__ = ['subsetString', 'setSubsetString']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgssubsetstringeditorprovider.h
try:
    QgsSubsetStringEditorProvider.__virtual_methods__ = ['name', 'canHandleLayerStorageType']
    QgsSubsetStringEditorProvider.__abstract_methods__ = ['providerKey', 'canHandleLayer', 'createDialog']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgssubstitutionlistwidget.h
try:
    QgsSubstitutionListWidget.__attribute_docs__ = {'substitutionsChanged': 'Emitted when the substitution definitions change.\n'}
    QgsSubstitutionListWidget.__signal_arguments__ = {'substitutionsChanged': ['substitutions: QgsStringReplacementCollection']}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgssvgselectorwidget.h
try:
    QgsSvgSelectorWidget.__attribute_docs__ = {'svgSelected': 'Emitted when an SVG is selected in the widget.\n', 'svgParametersChanged': 'Emitted when the parameters have changed\n\n.. versionadded:: 3.18\n'}
    QgsSvgSelectorWidget.__signal_arguments__ = {'svgSelected': ['path: str'], 'svgParametersChanged': ['parameters: Dict[str, QgsProperty]']}
    QgsSvgSelectorWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSvgSelectorListModel.__overridden_methods__ = ['rowCount', 'data']
    QgsSvgSelectorListModel.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSvgSelectorFilterModel.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSvgSelectorGroupsModel.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSvgSelectorDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgssymbolanimationsettingswidget.h
try:
    QgsSymbolAnimationSettingsWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSymbolAnimationSettingsDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgssymbolbuffersettingswidget.h
try:
    QgsSymbolBufferSettingsWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSymbolBufferSettingsDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgssymbolbutton.h
try:
    QgsSymbolButton.__attribute_docs__ = {'changed': "Emitted when the symbol's settings are changed.\n\n.. seealso:: :py:func:`symbol`\n\n.. seealso:: :py:func:`setSymbol`\n"}
    QgsSymbolButton.__overridden_methods__ = ['minimumSizeHint', 'sizeHint', 'changeEvent', 'showEvent', 'resizeEvent', 'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent', 'keyPressEvent', 'dragEnterEvent', 'dragLeaveEvent', 'dropEvent', 'wheelEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgssymbollayerwidget.h
try:
    QgsSymbolLayerWidget.__attribute_docs__ = {'changed': 'Should be emitted whenever configuration changes happened on this symbol\nlayer configuration. If the subsymbol is changed,\n:py:func:`~QgsSymbolLayerWidget.symbolChanged` should be emitted\ninstead.\n', 'symbolChanged': 'Should be emitted whenever the sub symbol changed on this symbol layer\nconfiguration. Normally :py:func:`~QgsSymbolLayerWidget.changed` should\nbe preferred.\n\n.. seealso:: :py:func:`changed`\n'}
    QgsSymbolLayerWidget.__virtual_methods__ = ['setContext']
    QgsSymbolLayerWidget.__abstract_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsSymbolLayerWidget.__overridden_methods__ = ['createExpressionContext']
    QgsSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSimpleLineSymbolLayerWidget.create = staticmethod(QgsSimpleLineSymbolLayerWidget.create)
    QgsSimpleLineSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer', 'setContext', 'resizeEvent']
    QgsSimpleLineSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSimpleMarkerSymbolLayerWidget.create = staticmethod(QgsSimpleMarkerSymbolLayerWidget.create)
    QgsSimpleMarkerSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsSimpleMarkerSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSimpleFillSymbolLayerWidget.create = staticmethod(QgsSimpleFillSymbolLayerWidget.create)
    QgsSimpleFillSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsSimpleFillSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsFilledMarkerSymbolLayerWidget.create = staticmethod(QgsFilledMarkerSymbolLayerWidget.create)
    QgsFilledMarkerSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsFilledMarkerSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsGradientFillSymbolLayerWidget.create = staticmethod(QgsGradientFillSymbolLayerWidget.create)
    QgsGradientFillSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsGradientFillSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsShapeburstFillSymbolLayerWidget.create = staticmethod(QgsShapeburstFillSymbolLayerWidget.create)
    QgsShapeburstFillSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsShapeburstFillSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsMarkerLineSymbolLayerWidget.create = staticmethod(QgsMarkerLineSymbolLayerWidget.create)
    QgsMarkerLineSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer', 'setContext']
    QgsMarkerLineSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsHashedLineSymbolLayerWidget.create = staticmethod(QgsHashedLineSymbolLayerWidget.create)
    QgsHashedLineSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer', 'setContext']
    QgsHashedLineSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSvgMarkerSymbolLayerWidget.create = staticmethod(QgsSvgMarkerSymbolLayerWidget.create)
    QgsSvgMarkerSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer', 'setContext']
    QgsSvgMarkerSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsRasterMarkerSymbolLayerWidget.create = staticmethod(QgsRasterMarkerSymbolLayerWidget.create)
    QgsRasterMarkerSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer', 'setContext']
    QgsRasterMarkerSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsAnimatedMarkerSymbolLayerWidget.create = staticmethod(QgsAnimatedMarkerSymbolLayerWidget.create)
    QgsAnimatedMarkerSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer', 'setContext']
    QgsAnimatedMarkerSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsRasterFillSymbolLayerWidget.create = staticmethod(QgsRasterFillSymbolLayerWidget.create)
    QgsRasterFillSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsRasterFillSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsRasterLineSymbolLayerWidget.create = staticmethod(QgsRasterLineSymbolLayerWidget.create)
    QgsRasterLineSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsRasterLineSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsLineburstSymbolLayerWidget.create = staticmethod(QgsLineburstSymbolLayerWidget.create)
    QgsLineburstSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsLineburstSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsFilledLineSymbolLayerWidget.create = staticmethod(QgsFilledLineSymbolLayerWidget.create)
    QgsFilledLineSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsFilledLineSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSVGFillSymbolLayerWidget.create = staticmethod(QgsSVGFillSymbolLayerWidget.create)
    QgsSVGFillSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer', 'setContext']
    QgsSVGFillSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsLinePatternFillSymbolLayerWidget.create = staticmethod(QgsLinePatternFillSymbolLayerWidget.create)
    QgsLinePatternFillSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsLinePatternFillSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsPointPatternFillSymbolLayerWidget.create = staticmethod(QgsPointPatternFillSymbolLayerWidget.create)
    QgsPointPatternFillSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsPointPatternFillSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsRandomMarkerFillSymbolLayerWidget.create = staticmethod(QgsRandomMarkerFillSymbolLayerWidget.create)
    QgsRandomMarkerFillSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsRandomMarkerFillSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsFontMarkerSymbolLayerWidget.create = staticmethod(QgsFontMarkerSymbolLayerWidget.create)
    QgsFontMarkerSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsFontMarkerSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsCentroidFillSymbolLayerWidget.create = staticmethod(QgsCentroidFillSymbolLayerWidget.create)
    QgsCentroidFillSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsCentroidFillSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsLinearReferencingSymbolLayerWidget.create = staticmethod(QgsLinearReferencingSymbolLayerWidget.create)
    QgsLinearReferencingSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer', 'setContext']
    QgsLinearReferencingSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsGeometryGeneratorSymbolLayerWidget.create = staticmethod(QgsGeometryGeneratorSymbolLayerWidget.create)
    QgsGeometryGeneratorSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsGeometryGeneratorSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgssymbollevelsdialog.h
try:
    QgsSymbolLevelsWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSymbolLevelsDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgssymbolselectordialog.h
try:
    QgsSymbolSelectorWidget.__attribute_docs__ = {'symbolModified': 'Emitted when a symbol is modified in the widget.\n'}
    QgsSymbolSelectorWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
try:
    QgsSymbolSelectorDialog.__attribute_docs__ = {'symbolModified': 'Emitted when the symbol defined in the dialog is modified.\n'}
    QgsSymbolSelectorDialog.__overridden_methods__ = ['keyPressEvent']
    QgsSymbolSelectorDialog.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgssymbolslistwidget.h
try:
    QgsSymbolsListWidget.__attribute_docs__ = {'changed': 'Emitted when the symbol is modified in the widget.\n'}
    QgsSymbolsListWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgssymbolwidgetcontext.h
try:
    QgsSymbolWidgetContext.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/tableeditor/qgstableeditordialog.h
try:
    QgsTableEditorDialog.__attribute_docs__ = {'tableChanged': 'Emitted whenever the table contents are changed.\n', 'includeHeaderChanged': 'Emitted whenever the "include table header" setting is changed.\n'}
    QgsTableEditorDialog.__overridden_methods__ = ['closeEvent']
    QgsTableEditorDialog.__signal_arguments__ = {'includeHeaderChanged': ['included: bool']}
    QgsTableEditorDialog.__group__ = ['tableeditor']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/tableeditor/qgstableeditorwidget.h
try:
    QgsTableEditorWidget.__attribute_docs__ = {'tableChanged': 'Emitted whenever the table contents are changed.\n', 'activeCellChanged': 'Emitted whenever the active (or selected) cell changes in the widget.\n'}
    QgsTableEditorWidget.__overridden_methods__ = ['keyPressEvent']
    QgsTableEditorWidget.__group__ = ['tableeditor']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgstableview.h
try:
    QgsTableView.__overridden_methods__ = ['wheelEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgstablewidgetbase.h
try:
    QgsTableWidgetBase.__attribute_docs__ = {'valueChanged': 'Emitted each time a key or a value is changed.\n'}
    QgsTableWidgetBase.__virtual_methods__ = ['setReadOnly']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgstablewidgetitem.h
try:
    QgsTableWidgetItem.__overridden_methods__ = ['operator<']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/labeling/qgstabpositionwidget.h
try:
    QgsTabPositionWidget.__attribute_docs__ = {'positionsChanged': 'Emitted when positions are changed in the widget.\n'}
    QgsTabPositionWidget.__signal_arguments__ = {'positionsChanged': ['positions: List[QgsTextFormat.Tab]']}
    QgsTabPositionWidget.__group__ = ['labeling']
except (NameError, AttributeError):
    pass
try:
    QgsTabPositionDialog.__group__ = ['labeling']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgstabwidget.h
try:
    QgsTabWidget.__overridden_methods__ = ['tabInserted', 'tabRemoved']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgstemporalcontrollerwidget.h
try:
    QgsTemporalControllerWidget.__overridden_methods__ = ['applySizeConstraintsToStack', 'keyPressEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgstextformatwidget.h
try:
    QgsTextFormatWidget.__attribute_docs__ = {'widgetChanged': 'Emitted when the text format defined by the widget changes\n', 'auxiliaryFieldCreated': 'Emitted when an auxiliary field is created in the widget.\n\n.. versionadded:: 3.10\n'}
    QgsTextFormatWidget.__virtual_methods__ = ['setContext', 'setFormatFromStyle', 'saveFormat']
    QgsTextFormatWidget.__overridden_methods__ = ['createExpressionContext']
except (NameError, AttributeError):
    pass
try:
    QgsTextFormatPanelWidget.__overridden_methods__ = ['setDockMode']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgstextpreview.h
try:
    QgsTextPreview.__overridden_methods__ = ['paintEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgstextwidgetwrapper.h
try:
    QgsTextWidgetWrapper.__overridden_methods__ = ['valid', 'createWidget', 'initWidget', 'setFeature']
    QgsTextWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/tiledscene/qgstiledscenerendererpropertieswidget.h
try:
    QgsTiledSceneRendererPropertiesWidget.__overridden_methods__ = ['syncToLayer', 'setDockMode', 'apply']
    QgsTiledSceneRendererPropertiesWidget.__group__ = ['tiledscene']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/tiledscene/qgstiledscenerendererwidget.h
try:
    QgsTiledSceneRendererWidget.__virtual_methods__ = ['setContext']
    QgsTiledSceneRendererWidget.__abstract_methods__ = ['renderer']
    QgsTiledSceneRendererWidget.__group__ = ['tiledscene']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgstooltipcombobox.h
try:
    QgsToolTipComboBox.__overridden_methods__ = ['event']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgstreewidgetitem.h
try:
    QgsTreeWidgetItemObject.__attribute_docs__ = {'itemEdited': 'Emitted when the contents of the column in the specified item has been\nedited by the user.\n'}
    QgsTreeWidgetItemObject.__overridden_methods__ = ['setData']
    QgsTreeWidgetItemObject.__signal_arguments__ = {'itemEdited': ['item: QTreeWidgetItem', 'column: int']}
except (NameError, AttributeError):
    pass
try:
    QgsTreeWidgetItem.__overridden_methods__ = ['operator<']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsunitselectionwidget.h
try:
    QgsMapUnitScaleWidget.__attribute_docs__ = {'mapUnitScaleChanged': 'Emitted when the settings in the widget are modified.\n\n:param scale: :py:class:`QgsMapUnitScale` reflecting new settings from\n              the widget\n'}
    QgsMapUnitScaleWidget.__signal_arguments__ = {'mapUnitScaleChanged': ['scale: QgsMapUnitScale']}
except (NameError, AttributeError):
    pass
try:
    QgsUnitSelectionWidget.__attribute_docs__ = {'changed': 'Emitted when the selected unit is changed, or the definition of the map\nunit scale is changed.\n'}
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsuserinputwidget.h
try:
    QgsUserInputWidget.__overridden_methods__ = ['paintEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsvaliditycheckresultswidget.h
QgsValidityCheckResultsModel.Roles = QgsValidityCheckResultsModel.CustomRole
# monkey patching scoped based enum
QgsValidityCheckResultsModel.DescriptionRole = QgsValidityCheckResultsModel.CustomRole.Description
QgsValidityCheckResultsModel.Roles.DescriptionRole = QgsValidityCheckResultsModel.CustomRole.Description
QgsValidityCheckResultsModel.DescriptionRole.is_monkey_patched = True
QgsValidityCheckResultsModel.DescriptionRole.__doc__ = "Result detailed description"
QgsValidityCheckResultsModel.CustomRole.__doc__ = """Custom model roles.

.. note::

   Prior to QGIS 3.36 this was available as QgsValidityCheckResultsModel.Roles

.. versionadded:: 3.36

* ``Description``: Result detailed description

  Available as ``QgsValidityCheckResultsModel.DescriptionRole`` in older QGIS releases.


"""
# --
QgsValidityCheckResultsModel.CustomRole.baseClass = QgsValidityCheckResultsModel
try:
    QgsValidityCheckResultsWidget.runChecks = staticmethod(QgsValidityCheckResultsWidget.runChecks)
except (NameError, AttributeError):
    pass
try:
    QgsValidityCheckResultsModel.__overridden_methods__ = ['index', 'parent', 'rowCount', 'columnCount', 'data']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsvaluemapsearchwidgetwrapper.h
try:
    QgsValueMapSearchWidgetWrapper.__overridden_methods__ = ['applyDirectly', 'expression', 'valid', 'supportedFlags', 'defaultFlags', 'createExpression', 'clearWidget', 'setEnabled', 'createWidget', 'initWidget', 'setExpression']
    QgsValueMapSearchWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/qgsvaluerelationsearchwidgetwrapper.h
try:
    QgsValueRelationSearchWidgetWrapper.__overridden_methods__ = ['applyDirectly', 'expression', 'valid', 'supportedFlags', 'defaultFlags', 'createExpression', 'clearWidget', 'setEnabled', 'createWidget', 'initWidget', 'setExpression']
    QgsValueRelationSearchWidgetWrapper.__group__ = ['editorwidgets']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsvariableeditorwidget.h
try:
    QgsVariableEditorWidget.__attribute_docs__ = {'scopeChanged': 'Emitted when the user has modified a scope using the widget.\n'}
    QgsVariableEditorWidget.__overridden_methods__ = ['showEvent']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/symbology/qgsvectorfieldsymbollayerwidget.h
try:
    QgsVectorFieldSymbolLayerWidget.create = staticmethod(QgsVectorFieldSymbolLayerWidget.create)
    QgsVectorFieldSymbolLayerWidget.__overridden_methods__ = ['setSymbolLayer', 'symbolLayer']
    QgsVectorFieldSymbolLayerWidget.__group__ = ['symbology']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/vector/qgsvectorlayerproperties.h
try:
    QgsVectorLayerProperties.__virtual_methods__ = ['syncToLayer', 'apply', 'rollback']
    QgsVectorLayerProperties.__overridden_methods__ = ['eventFilter', 'optionsStackedWidget_CurrentChanged']
    QgsVectorLayerProperties.__group__ = ['vector']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/ogr/qgsvectorlayersaveasdialog.h
# monkey patching scoped based enum
QgsVectorLayerSaveAsDialog.Option.Symbology.__doc__ = "Show symbology options"
QgsVectorLayerSaveAsDialog.Option.DestinationCrs.__doc__ = "Show destination CRS (reprojection) option"
QgsVectorLayerSaveAsDialog.Option.Fields.__doc__ = "Show field customization group"
QgsVectorLayerSaveAsDialog.Option.AddToCanvas.__doc__ = "Show add to map option"
QgsVectorLayerSaveAsDialog.Option.SelectedOnly.__doc__ = "Show selected features only option"
QgsVectorLayerSaveAsDialog.Option.GeometryType.__doc__ = "Show geometry group"
QgsVectorLayerSaveAsDialog.Option.Extent.__doc__ = "Show extent group"
QgsVectorLayerSaveAsDialog.Option.Metadata.__doc__ = "Show metadata options"
QgsVectorLayerSaveAsDialog.Option.AllOptions.__doc__ = ""
QgsVectorLayerSaveAsDialog.Option.__doc__ = """Available dialog options.

* ``Symbology``: Show symbology options
* ``DestinationCrs``: Show destination CRS (reprojection) option
* ``Fields``: Show field customization group
* ``AddToCanvas``: Show add to map option
* ``SelectedOnly``: Show selected features only option
* ``GeometryType``: Show geometry group
* ``Extent``: Show extent group
* ``Metadata``: Show metadata options
* ``AllOptions``: 

"""
# --
QgsVectorLayerSaveAsDialog.Option.baseClass = QgsVectorLayerSaveAsDialog
QgsVectorLayerSaveAsDialog.Options.baseClass = QgsVectorLayerSaveAsDialog
Options = QgsVectorLayerSaveAsDialog  # dirty hack since SIP seems to introduce the flags in module
try:
    QgsVectorLayerSaveAsDialog.__overridden_methods__ = ['accept']
    QgsVectorLayerSaveAsDialog.__group__ = ['ogr']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsvectorlayertemporalpropertieswidget.h
try:
    QgsVectorLayerTemporalPropertiesWidget.__overridden_methods__ = ['createExpressionContext']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/vectortile/qgsvectortilelayerproperties.h
try:
    QgsVectorTileLayerProperties.__group__ = ['vectortile']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsvertexmarker.h
try:
    QgsVertexMarker.__overridden_methods__ = ['paint', 'boundingRect', 'updatePosition']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgsvscrollarea.h
try:
    QgsVScrollArea.__overridden_methods__ = ['eventFilter']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/editorwidgets/core/qgswidgetwrapper.h
# monkey patching scoped based enum
QgsWidgetWrapper.RootPath = QgsWidgetWrapper.Property.RootPath
QgsWidgetWrapper.RootPath.is_monkey_patched = True
QgsWidgetWrapper.RootPath.__doc__ = "Root path for external resource"
QgsWidgetWrapper.DocumentViewerContent = QgsWidgetWrapper.Property.DocumentViewerContent
QgsWidgetWrapper.DocumentViewerContent.is_monkey_patched = True
QgsWidgetWrapper.DocumentViewerContent.__doc__ = "Document type for external resource"
QgsWidgetWrapper.StorageUrl = QgsWidgetWrapper.Property.StorageUrl
QgsWidgetWrapper.StorageUrl.is_monkey_patched = True
QgsWidgetWrapper.StorageUrl.__doc__ = "Storage URL for external resource"
QgsWidgetWrapper.Property.__doc__ = """Data defined properties for different editor widgets.

* ``RootPath``: Root path for external resource
* ``DocumentViewerContent``: Document type for external resource
* ``StorageUrl``: Storage URL for external resource

"""
# --
try:
    QgsWidgetWrapper.__attribute_docs__ = {'contextChanged': 'Signal when :py:class:`QgsAttributeEditorContext` mContext changed\n\n.. versionadded:: 3.4\n'}
    QgsWidgetWrapper.fromWidget = staticmethod(QgsWidgetWrapper.fromWidget)
    QgsWidgetWrapper.__virtual_methods__ = ['initWidget', 'setEnabled']
    QgsWidgetWrapper.__abstract_methods__ = ['valid', 'createWidget', 'setFeature']
    QgsWidgetWrapper.__group__ = ['editorwidgets', 'core']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/gui/qgswindowmanagerinterface.h
try:
    QgsWindowManagerInterface.__abstract_methods__ = ['openStandardDialog']
except (NameError, AttributeError):
    pass


# monkey patching scoped based enum
QgsMapToolCapture.CaptureTechnique = _Qgis.CaptureTechnique
QgsMapToolCapture.StraightSegments = _Qgis.CaptureTechnique.StraightSegments
QgsMapToolCapture.StraightSegments.is_monkey_patched = True
QgsMapToolCapture.StraightSegments.__doc__ = "Default capture mode - capture occurs with straight line segments"
QgsMapToolCapture.CircularString = _Qgis.CaptureTechnique.CircularString
QgsMapToolCapture.CircularString.is_monkey_patched = True
QgsMapToolCapture.CircularString.__doc__ = "Capture in circular strings"
QgsMapToolCapture.Streaming = _Qgis.CaptureTechnique.Streaming
QgsMapToolCapture.Streaming.is_monkey_patched = True
QgsMapToolCapture.Streaming.__doc__ = "Streaming points digitizing mode (points are automatically added as the mouse cursor moves)."
QgsMapToolCapture.Shape = _Qgis.CaptureTechnique.Shape
QgsMapToolCapture.Shape.is_monkey_patched = True
QgsMapToolCapture.Shape.__doc__ = "Digitize shapes."

QgsActionMenu.ActionType = _Qgis.ActionType
# monkey patching scoped based enum
QgsActionMenu.Invalid = _Qgis.ActionType.Invalid
QgsActionMenu.Invalid.is_monkey_patched = True
QgsActionMenu.Invalid.__doc__ = "Invalid"
QgsActionMenu.MapLayerAction = _Qgis.ActionType.MapLayerAction
QgsActionMenu.MapLayerAction.is_monkey_patched = True
QgsActionMenu.MapLayerAction.__doc__ = "Standard actions (defined by core or plugins), corresponds to QgsMapLayerAction class."
QgsActionMenu.AttributeAction = _Qgis.ActionType.AttributeAction
QgsActionMenu.AttributeAction.is_monkey_patched = True
QgsActionMenu.AttributeAction.__doc__ = "Custom actions (manually defined in layer properties), corresponds to QgsAction class."

QgsMapLayerAction.Target = _Qgis.MapLayerActionTarget
# monkey patching scoped based enum
QgsMapLayerAction.Layer = _Qgis.MapLayerActionTarget.Layer
QgsMapLayerAction.Layer.is_monkey_patched = True
QgsMapLayerAction.Layer.__doc__ = "Action targets a complete layer"
QgsMapLayerAction.SingleFeature = _Qgis.MapLayerActionTarget.SingleFeature
QgsMapLayerAction.SingleFeature.is_monkey_patched = True
QgsMapLayerAction.SingleFeature.__doc__ = "Action targets a single feature from a layer"
QgsMapLayerAction.MultipleFeatures = _Qgis.MapLayerActionTarget.MultipleFeatures
QgsMapLayerAction.MultipleFeatures.is_monkey_patched = True
QgsMapLayerAction.MultipleFeatures.__doc__ = "Action targets multiple features from a layer"
QgsMapLayerAction.AllActions = _Qgis.MapLayerActionTarget.AllActions
QgsMapLayerAction.AllActions.is_monkey_patched = True
QgsMapLayerAction.AllActions.__doc__ = ""
QgsMapLayerAction.Targets = _Qgis.MapLayerActionTargets

QgsMapLayerAction.Flag = _Qgis.MapLayerActionFlag
# monkey patching scoped based enum
QgsMapLayerAction.EnabledOnlyWhenEditable = _Qgis.MapLayerActionFlag.EnabledOnlyWhenEditable
QgsMapLayerAction.EnabledOnlyWhenEditable.is_monkey_patched = True
QgsMapLayerAction.EnabledOnlyWhenEditable.__doc__ = "Action should be shown only for editable layers"
QgsMapLayerAction.Flags = _Qgis.MapLayerActionFlags

QgsProcessingGui.WidgetType = _Qgis.ProcessingMode
# monkey patching scoped based enum
QgsProcessingGui.Standard = _Qgis.ProcessingMode.Standard
QgsProcessingGui.Standard.is_monkey_patched = True
QgsProcessingGui.Standard.__doc__ = "Standard (single-run) algorithm mode"
QgsProcessingGui.Batch = _Qgis.ProcessingMode.Batch
QgsProcessingGui.Batch.is_monkey_patched = True
QgsProcessingGui.Batch.__doc__ = "Batch processing mode"
QgsProcessingGui.Modeler = _Qgis.ProcessingMode.Modeler
QgsProcessingGui.Modeler.is_monkey_patched = True
QgsProcessingGui.Modeler.__doc__ = "Modeler mode"


# monkey patch old settings wrappers
QgsSettingsStringEditorWidgetWrapper = QgsSettingsStringLineEditWrapper
QgsSettingsBoolEditorWidgetWrapper = QgsSettingsBoolCheckBoxWrapper
QgsSettingsIntegerEditorWidgetWrapper = QgsSettingsIntegerSpinBoxWrapper
QgsSettingsDoubleEditorWidgetWrapper = QgsSettingsDoubleSpinBoxWrapper
QgsSettingsColorEditorWidgetWrapper = QgsSettingsColorButtonWrapper

# Classes patched
QgsSettingsEnumEditorWidgetWrapper = PyQgsSettingsEnumEditorWidgetWrapper
