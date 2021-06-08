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

from qgis.PyQt.QtCore import NULL
from qgis._core import *

from .additions.edit import edit, QgsEditError
from .additions.fromfunction import fromFunction
from .additions.metaenum import metaEnumFromType, metaEnumFromValue
from .additions.processing import processing_output_layer_repr, processing_source_repr
from .additions.projectdirtyblocker import ProjectDirtyBlocker
from .additions.providermetadata import PyProviderMetadata
from .additions.qgsfeature import mapping_feature
from .additions.qgsfunction import register_function, qgsfunction
from .additions.qgsgeometry import _geometryNonZero, mapping_geometry
from .additions.qgssettings import _qgssettings_enum_value, _qgssettings_set_enum_value, _qgssettings_flag_value
from .additions.qgssettingsentry import PyQgsSettingsEntryEnumFlag
from .additions.qgstaskwrapper import QgsTaskWrapper
from .additions.readwritecontextentercategory import ReadWriteContextEnterCategory
from .additions.runtimeprofiler import ScopedRuntimeProfileContextManager
from .additions.validitycheck import check
from .additions.ranges import datetime_range_repr, date_range_repr

# Injections into classes
QgsFeature.__geo_interface__ = property(mapping_feature)
QgsGeometry.__bool__ = _geometryNonZero
QgsGeometry.__geo_interface__ = property(mapping_geometry)
QgsGeometry.__nonzero__ = _geometryNonZero
QgsProcessingFeatureSourceDefinition.__repr__ = processing_source_repr
QgsProcessingOutputLayerDefinition.__repr__ = processing_output_layer_repr
QgsProject.blockDirtying = ProjectDirtyBlocker
QgsReadWriteContext.enterCategory = ReadWriteContextEnterCategory
QgsRuntimeProfiler.profile = ScopedRuntimeProfileContextManager
QgsSettings.enumValue = _qgssettings_enum_value
QgsSettings.setEnumValue = _qgssettings_set_enum_value
QgsSettings.flagValue = _qgssettings_flag_value
QgsTask.fromFunction = fromFunction
QgsDateTimeRange.__repr__ = datetime_range_repr
QgsDateRange.__repr__ = date_range_repr

# Classes patched
QgsSettingsEntryEnumFlag = PyQgsSettingsEntryEnumFlag

# Classes patched using a derived class
QgsProviderMetadata = PyProviderMetadata

# monkey patch deprecated enum values to maintain API
# TODO - remove for QGIS 4.0
QgsMarkerLineSymbolLayer.Interval = QgsTemplatedLineSymbolLayerBase.Interval
QgsMarkerLineSymbolLayer.Vertex = QgsTemplatedLineSymbolLayerBase.Vertex
QgsMarkerLineSymbolLayer.LastVertex = QgsTemplatedLineSymbolLayerBase.LastVertex
QgsMarkerLineSymbolLayer.FirstVertex = QgsTemplatedLineSymbolLayerBase.FirstVertex
QgsMarkerLineSymbolLayer.CentralPoint = QgsTemplatedLineSymbolLayerBase.CentralPoint
QgsMarkerLineSymbolLayer.CurvePoint = QgsTemplatedLineSymbolLayerBase.CurvePoint

# Monkey patch static const "QgsDataProvider.SUBLAYER_SEPARATOR" which was removed for QGIS 3.12
QgsDataProvider.SUBLAYER_SEPARATOR = QgsDataProvider.sublayerSeparator()

# Monkey patch Qgis vars
Qgis.QGIS_VERSION = Qgis.version()
Qgis.QGIS_VERSION_INT = Qgis.versionInt()
Qgis.QGIS_RELEASE_NAME = Qgis.releaseName()

GEOWKT = geoWkt()
PROJECT_SCALES = Qgis.defaultProjectScales()
GEOPROJ4 = geoProj4()
GEO_EPSG_CRS_AUTHID = geoEpsgCrsAuthId()
GEO_NONE = geoNone()
"""
This folder is completed using sipify.pl script
It is not aimed to be manually edited
"""
# The following has been generated automatically from src/core/qgis.h
QgsMapLayer.LayerType = QgsMapLayerType
# monkey patching scoped based enum
QgsMapLayer.VectorLayer = QgsMapLayerType.VectorLayer
QgsMapLayer.VectorLayer.is_monkey_patched = True
QgsMapLayer.VectorLayer.__doc__ = ""
QgsMapLayer.RasterLayer = QgsMapLayerType.RasterLayer
QgsMapLayer.RasterLayer.is_monkey_patched = True
QgsMapLayer.RasterLayer.__doc__ = ""
QgsMapLayer.PluginLayer = QgsMapLayerType.PluginLayer
QgsMapLayer.PluginLayer.is_monkey_patched = True
QgsMapLayer.PluginLayer.__doc__ = ""
QgsMapLayer.MeshLayer = QgsMapLayerType.MeshLayer
QgsMapLayer.MeshLayer.is_monkey_patched = True
QgsMapLayer.MeshLayer.__doc__ = "Added in 3.2"
QgsMapLayer.VectorTileLayer = QgsMapLayerType.VectorTileLayer
QgsMapLayer.VectorTileLayer.is_monkey_patched = True
QgsMapLayer.VectorTileLayer.__doc__ = "Added in 3.14"
QgsMapLayer.AnnotationLayer = QgsMapLayerType.AnnotationLayer
QgsMapLayer.AnnotationLayer.is_monkey_patched = True
QgsMapLayer.AnnotationLayer.__doc__ = "Contains freeform, georeferenced annotations. Added in QGIS 3.16"
QgsMapLayer.PointCloudLayer = QgsMapLayerType.PointCloudLayer
QgsMapLayer.PointCloudLayer.is_monkey_patched = True
QgsMapLayer.PointCloudLayer.__doc__ = "Added in 3.18"
QgsMapLayerType.__doc__ = 'Types of layers that can be added to a map\n\n.. versionadded:: 3.8\n\n' + '* ``VectorLayer``: ' + QgsMapLayerType.VectorLayer.__doc__ + '\n' + '* ``RasterLayer``: ' + QgsMapLayerType.RasterLayer.__doc__ + '\n' + '* ``PluginLayer``: ' + QgsMapLayerType.PluginLayer.__doc__ + '\n' + '* ``MeshLayer``: ' + QgsMapLayerType.MeshLayer.__doc__ + '\n' + '* ``VectorTileLayer``: ' + QgsMapLayerType.VectorTileLayer.__doc__ + '\n' + '* ``AnnotationLayer``: ' + QgsMapLayerType.AnnotationLayer.__doc__ + '\n' + '* ``PointCloudLayer``: ' + QgsMapLayerType.PointCloudLayer.__doc__
# --
Qgis.MessageLevel.baseClass = Qgis
# monkey patching scoped based enum
Qgis.UnknownDataType = Qgis.DataType.UnknownDataType
Qgis.UnknownDataType.is_monkey_patched = True
Qgis.UnknownDataType.__doc__ = "Unknown or unspecified type"
Qgis.Byte = Qgis.DataType.Byte
Qgis.Byte.is_monkey_patched = True
Qgis.Byte.__doc__ = "Eight bit unsigned integer (quint8)"
Qgis.UInt16 = Qgis.DataType.UInt16
Qgis.UInt16.is_monkey_patched = True
Qgis.UInt16.__doc__ = "Sixteen bit unsigned integer (quint16)"
Qgis.Int16 = Qgis.DataType.Int16
Qgis.Int16.is_monkey_patched = True
Qgis.Int16.__doc__ = "Sixteen bit signed integer (qint16)"
Qgis.UInt32 = Qgis.DataType.UInt32
Qgis.UInt32.is_monkey_patched = True
Qgis.UInt32.__doc__ = "Thirty two bit unsigned integer (quint32)"
Qgis.Int32 = Qgis.DataType.Int32
Qgis.Int32.is_monkey_patched = True
Qgis.Int32.__doc__ = "Thirty two bit signed integer (qint32)"
Qgis.Float32 = Qgis.DataType.Float32
Qgis.Float32.is_monkey_patched = True
Qgis.Float32.__doc__ = "Thirty two bit floating point (float)"
Qgis.Float64 = Qgis.DataType.Float64
Qgis.Float64.is_monkey_patched = True
Qgis.Float64.__doc__ = "Sixty four bit floating point (double)"
Qgis.CInt16 = Qgis.DataType.CInt16
Qgis.CInt16.is_monkey_patched = True
Qgis.CInt16.__doc__ = "Complex Int16"
Qgis.CInt32 = Qgis.DataType.CInt32
Qgis.CInt32.is_monkey_patched = True
Qgis.CInt32.__doc__ = "Complex Int32"
Qgis.CFloat32 = Qgis.DataType.CFloat32
Qgis.CFloat32.is_monkey_patched = True
Qgis.CFloat32.__doc__ = "Complex Float32"
Qgis.CFloat64 = Qgis.DataType.CFloat64
Qgis.CFloat64.is_monkey_patched = True
Qgis.CFloat64.__doc__ = "Complex Float64"
Qgis.ARGB32 = Qgis.DataType.ARGB32
Qgis.ARGB32.is_monkey_patched = True
Qgis.ARGB32.__doc__ = "Color, alpha, red, green, blue, 4 bytes the same as QImage::Format_ARGB32"
Qgis.ARGB32_Premultiplied = Qgis.DataType.ARGB32_Premultiplied
Qgis.ARGB32_Premultiplied.is_monkey_patched = True
Qgis.ARGB32_Premultiplied.__doc__ = "Color, alpha, red, green, blue, 4 bytes  the same as QImage::Format_ARGB32_Premultiplied"
Qgis.DataType.__doc__ = 'Raster data types.\nThis is modified and extended copy of GDALDataType.\n\n' + '* ``UnknownDataType``: ' + Qgis.DataType.UnknownDataType.__doc__ + '\n' + '* ``Byte``: ' + Qgis.DataType.Byte.__doc__ + '\n' + '* ``UInt16``: ' + Qgis.DataType.UInt16.__doc__ + '\n' + '* ``Int16``: ' + Qgis.DataType.Int16.__doc__ + '\n' + '* ``UInt32``: ' + Qgis.DataType.UInt32.__doc__ + '\n' + '* ``Int32``: ' + Qgis.DataType.Int32.__doc__ + '\n' + '* ``Float32``: ' + Qgis.DataType.Float32.__doc__ + '\n' + '* ``Float64``: ' + Qgis.DataType.Float64.__doc__ + '\n' + '* ``CInt16``: ' + Qgis.DataType.CInt16.__doc__ + '\n' + '* ``CInt32``: ' + Qgis.DataType.CInt32.__doc__ + '\n' + '* ``CFloat32``: ' + Qgis.DataType.CFloat32.__doc__ + '\n' + '* ``CFloat64``: ' + Qgis.DataType.CFloat64.__doc__ + '\n' + '* ``ARGB32``: ' + Qgis.DataType.ARGB32.__doc__ + '\n' + '* ``ARGB32_Premultiplied``: ' + Qgis.DataType.ARGB32_Premultiplied.__doc__
# --
Qgis.DataType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.Never = Qgis.PythonMacroMode.Never
Qgis.Never.is_monkey_patched = True
Qgis.Never.__doc__ = "Macros are never run"
Qgis.Ask = Qgis.PythonMacroMode.Ask
Qgis.Ask.is_monkey_patched = True
Qgis.Ask.__doc__ = "User is prompt before running"
Qgis.SessionOnly = Qgis.PythonMacroMode.SessionOnly
Qgis.SessionOnly.is_monkey_patched = True
Qgis.SessionOnly.__doc__ = "Only during this session"
Qgis.Always = Qgis.PythonMacroMode.Always
Qgis.Always.is_monkey_patched = True
Qgis.Always.__doc__ = "Macros are always run"
Qgis.NotForThisSession = Qgis.PythonMacroMode.NotForThisSession
Qgis.NotForThisSession.is_monkey_patched = True
Qgis.NotForThisSession.__doc__ = "Macros will not be run for this session"
Qgis.PythonMacroMode.__doc__ = 'Authorisation to run Python Macros\n\n.. versionadded:: 3.10\n\n' + '* ``Never``: ' + Qgis.PythonMacroMode.Never.__doc__ + '\n' + '* ``Ask``: ' + Qgis.PythonMacroMode.Ask.__doc__ + '\n' + '* ``SessionOnly``: ' + Qgis.PythonMacroMode.SessionOnly.__doc__ + '\n' + '* ``Always``: ' + Qgis.PythonMacroMode.Always.__doc__ + '\n' + '* ``NotForThisSession``: ' + Qgis.PythonMacroMode.NotForThisSession.__doc__
# --
Qgis.PythonMacroMode.baseClass = Qgis
QgsVectorDataProvider.FeatureCountState = Qgis.FeatureCountState
# monkey patching scoped based enum
QgsVectorDataProvider.Uncounted = Qgis.FeatureCountState.Uncounted
QgsVectorDataProvider.Uncounted.is_monkey_patched = True
QgsVectorDataProvider.Uncounted.__doc__ = "Feature count not yet computed"
QgsVectorDataProvider.UnknownCount = Qgis.FeatureCountState.UnknownCount
QgsVectorDataProvider.UnknownCount.is_monkey_patched = True
QgsVectorDataProvider.UnknownCount.__doc__ = "Provider returned an unknown feature count"
Qgis.FeatureCountState.__doc__ = 'Enumeration of feature count states\n\n.. versionadded:: 3.20\n\n' + '* ``Uncounted``: ' + Qgis.FeatureCountState.Uncounted.__doc__ + '\n' + '* ``UnknownCount``: ' + Qgis.FeatureCountState.UnknownCount.__doc__
# --
Qgis.FeatureCountState.baseClass = Qgis
QgsSymbol.SymbolType = Qgis.SymbolType
# monkey patching scoped based enum
QgsSymbol.Marker = Qgis.SymbolType.Marker
QgsSymbol.Marker.is_monkey_patched = True
QgsSymbol.Marker.__doc__ = "Marker symbol"
QgsSymbol.Line = Qgis.SymbolType.Line
QgsSymbol.Line.is_monkey_patched = True
QgsSymbol.Line.__doc__ = "Line symbol"
QgsSymbol.Fill = Qgis.SymbolType.Fill
QgsSymbol.Fill.is_monkey_patched = True
QgsSymbol.Fill.__doc__ = "Fill symbol"
QgsSymbol.Hybrid = Qgis.SymbolType.Hybrid
QgsSymbol.Hybrid.is_monkey_patched = True
QgsSymbol.Hybrid.__doc__ = "Hybrid symbol"
Qgis.SymbolType.__doc__ = 'Symbol types\n\n.. versionadded:: 3.20\n\n' + '* ``Marker``: ' + Qgis.SymbolType.Marker.__doc__ + '\n' + '* ``Line``: ' + Qgis.SymbolType.Line.__doc__ + '\n' + '* ``Fill``: ' + Qgis.SymbolType.Fill.__doc__ + '\n' + '* ``Hybrid``: ' + Qgis.SymbolType.Hybrid.__doc__
# --
Qgis.SymbolType.baseClass = Qgis
QgsSymbol.ScaleMethod = Qgis.ScaleMethod
# monkey patching scoped based enum
QgsSymbol.ScaleArea = Qgis.ScaleMethod.ScaleArea
QgsSymbol.ScaleArea.is_monkey_patched = True
QgsSymbol.ScaleArea.__doc__ = "Calculate scale by the area"
QgsSymbol.ScaleDiameter = Qgis.ScaleMethod.ScaleDiameter
QgsSymbol.ScaleDiameter.is_monkey_patched = True
QgsSymbol.ScaleDiameter.__doc__ = "Calculate scale by the diameter"
Qgis.ScaleMethod.__doc__ = 'Scale methods\n\n.. versionadded:: 3.20\n\n' + '* ``ScaleArea``: ' + Qgis.ScaleMethod.ScaleArea.__doc__ + '\n' + '* ``ScaleDiameter``: ' + Qgis.ScaleMethod.ScaleDiameter.__doc__
# --
Qgis.ScaleMethod.baseClass = Qgis
QgsSymbol.RenderHint = Qgis.SymbolRenderHint
# monkey patching scoped based enum
QgsSymbol.DynamicRotation = Qgis.SymbolRenderHint.DynamicRotation
QgsSymbol.DynamicRotation.is_monkey_patched = True
QgsSymbol.DynamicRotation.__doc__ = "Rotation of symbol may be changed during rendering and symbol should not be cached"
Qgis.SymbolRenderHint.__doc__ = 'Flags controlling behavior of symbols during rendering\n\n.. versionadded:: 3.20\n\n' + '* ``DynamicRotation``: ' + Qgis.SymbolRenderHint.DynamicRotation.__doc__
# --
Qgis.SymbolRenderHint.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SymbolFlag.RendererShouldUseSymbolLevels.__doc__ = "If present, indicates that a QgsFeatureRenderer using the symbol should use symbol levels for best results"
Qgis.SymbolFlag.__doc__ = 'Flags controlling behavior of symbols\n\n.. versionadded:: 3.20\n\n' + '* ``RendererShouldUseSymbolLevels``: ' + Qgis.SymbolFlag.RendererShouldUseSymbolLevels.__doc__
# --
Qgis.SymbolFlag.baseClass = Qgis
QgsSymbol.PreviewFlag = Qgis.SymbolPreviewFlag
# monkey patching scoped based enum
QgsSymbol.FlagIncludeCrosshairsForMarkerSymbols = Qgis.SymbolPreviewFlag.FlagIncludeCrosshairsForMarkerSymbols
QgsSymbol.FlagIncludeCrosshairsForMarkerSymbols.is_monkey_patched = True
QgsSymbol.FlagIncludeCrosshairsForMarkerSymbols.__doc__ = "Include a crosshairs reference image in the background of marker symbol previews"
Qgis.SymbolPreviewFlag.__doc__ = 'Flags for controlling how symbol preview images are generated.\n\n.. versionadded:: 3.20\n\n' + '* ``FlagIncludeCrosshairsForMarkerSymbols``: ' + Qgis.SymbolPreviewFlag.FlagIncludeCrosshairsForMarkerSymbols.__doc__
# --
Qgis.SymbolPreviewFlag.baseClass = Qgis
QgsDataItem.Type = Qgis.BrowserItemType
# monkey patching scoped based enum
QgsDataItem.Collection = Qgis.BrowserItemType.Collection
QgsDataItem.Collection.is_monkey_patched = True
QgsDataItem.Collection.__doc__ = "A collection of items"
QgsDataItem.Directory = Qgis.BrowserItemType.Directory
QgsDataItem.Directory.is_monkey_patched = True
QgsDataItem.Directory.__doc__ = "Represents a file directory"
QgsDataItem.Layer = Qgis.BrowserItemType.Layer
QgsDataItem.Layer.is_monkey_patched = True
QgsDataItem.Layer.__doc__ = "Represents a map layer"
QgsDataItem.Error = Qgis.BrowserItemType.Error
QgsDataItem.Error.is_monkey_patched = True
QgsDataItem.Error.__doc__ = "Contains an error message"
QgsDataItem.Favorites = Qgis.BrowserItemType.Favorites
QgsDataItem.Favorites.is_monkey_patched = True
QgsDataItem.Favorites.__doc__ = "Represents a favorite item"
QgsDataItem.Project = Qgis.BrowserItemType.Project
QgsDataItem.Project.is_monkey_patched = True
QgsDataItem.Project.__doc__ = "Represents a QGIS project"
QgsDataItem.Custom = Qgis.BrowserItemType.Custom
QgsDataItem.Custom.is_monkey_patched = True
QgsDataItem.Custom.__doc__ = "Custom item type"
QgsDataItem.Fields = Qgis.BrowserItemType.Fields
QgsDataItem.Fields.is_monkey_patched = True
QgsDataItem.Fields.__doc__ = "Collection of fields"
QgsDataItem.Field = Qgis.BrowserItemType.Field
QgsDataItem.Field.is_monkey_patched = True
QgsDataItem.Field.__doc__ = "Vector layer field"
Qgis.BrowserItemType.__doc__ = 'Browser item types.\n\n.. versionadded:: 3.20\n\n' + '* ``Collection``: ' + Qgis.BrowserItemType.Collection.__doc__ + '\n' + '* ``Directory``: ' + Qgis.BrowserItemType.Directory.__doc__ + '\n' + '* ``Layer``: ' + Qgis.BrowserItemType.Layer.__doc__ + '\n' + '* ``Error``: ' + Qgis.BrowserItemType.Error.__doc__ + '\n' + '* ``Favorites``: ' + Qgis.BrowserItemType.Favorites.__doc__ + '\n' + '* ``Project``: ' + Qgis.BrowserItemType.Project.__doc__ + '\n' + '* ``Custom``: ' + Qgis.BrowserItemType.Custom.__doc__ + '\n' + '* ``Fields``: ' + Qgis.BrowserItemType.Fields.__doc__ + '\n' + '* ``Field``: ' + Qgis.BrowserItemType.Field.__doc__
# --
Qgis.BrowserItemType.baseClass = Qgis
QgsDataItem.State = Qgis.BrowserItemState
# monkey patching scoped based enum
QgsDataItem.NotPopulated = Qgis.BrowserItemState.NotPopulated
QgsDataItem.NotPopulated.is_monkey_patched = True
QgsDataItem.NotPopulated.__doc__ = "Children not yet created"
QgsDataItem.Populating = Qgis.BrowserItemState.Populating
QgsDataItem.Populating.is_monkey_patched = True
QgsDataItem.Populating.__doc__ = "Creating children in separate thread (populating or refreshing)"
QgsDataItem.Populated = Qgis.BrowserItemState.Populated
QgsDataItem.Populated.is_monkey_patched = True
QgsDataItem.Populated.__doc__ = "Children created"
Qgis.BrowserItemState.__doc__ = 'Browser item states.\n\n.. versionadded:: 3.20\n\n' + '* ``NotPopulated``: ' + Qgis.BrowserItemState.NotPopulated.__doc__ + '\n' + '* ``Populating``: ' + Qgis.BrowserItemState.Populating.__doc__ + '\n' + '* ``Populated``: ' + Qgis.BrowserItemState.Populated.__doc__
# --
Qgis.BrowserItemState.baseClass = Qgis
QgsDataItem.Capability = Qgis.BrowserItemCapability
# monkey patching scoped based enum
QgsDataItem.NoCapabilities = Qgis.BrowserItemCapability.NoCapabilities
QgsDataItem.NoCapabilities.is_monkey_patched = True
QgsDataItem.NoCapabilities.__doc__ = "Item has no capabilities"
QgsDataItem.SetCrs = Qgis.BrowserItemCapability.SetCrs
QgsDataItem.SetCrs.is_monkey_patched = True
QgsDataItem.SetCrs.__doc__ = "Can set CRS on layer or group of layers. \deprecated since QGIS 3.6 -- no longer used by QGIS and will be removed in QGIS 4.0"
QgsDataItem.Fertile = Qgis.BrowserItemCapability.Fertile
QgsDataItem.Fertile.is_monkey_patched = True
QgsDataItem.Fertile.__doc__ = "Can create children. Even items without this capability may have children, but cannot create them, it means that children are created by item ancestors."
QgsDataItem.Fast = Qgis.BrowserItemCapability.Fast
QgsDataItem.Fast.is_monkey_patched = True
QgsDataItem.Fast.__doc__ = "CreateChildren() is fast enough to be run in main thread when refreshing items, most root items (wms,wfs,wcs,postgres...) are considered fast because they are reading data only from QgsSettings"
QgsDataItem.Collapse = Qgis.BrowserItemCapability.Collapse
QgsDataItem.Collapse.is_monkey_patched = True
QgsDataItem.Collapse.__doc__ = "The collapse/expand status for this items children should be ignored in order to avoid undesired network connections (wms etc.)"
QgsDataItem.Rename = Qgis.BrowserItemCapability.Rename
QgsDataItem.Rename.is_monkey_patched = True
QgsDataItem.Rename.__doc__ = "Item can be renamed"
QgsDataItem.Delete = Qgis.BrowserItemCapability.Delete
QgsDataItem.Delete.is_monkey_patched = True
QgsDataItem.Delete.__doc__ = "Item can be deleted"
Qgis.BrowserItemCapability.__doc__ = 'Browser item capabilities.\n\n.. versionadded:: 3.20\n\n' + '* ``NoCapabilities``: ' + Qgis.BrowserItemCapability.NoCapabilities.__doc__ + '\n' + '* ``SetCrs``: ' + Qgis.BrowserItemCapability.SetCrs.__doc__ + '\n' + '* ``Fertile``: ' + Qgis.BrowserItemCapability.Fertile.__doc__ + '\n' + '* ``Fast``: ' + Qgis.BrowserItemCapability.Fast.__doc__ + '\n' + '* ``Collapse``: ' + Qgis.BrowserItemCapability.Collapse.__doc__ + '\n' + '* ``Rename``: ' + Qgis.BrowserItemCapability.Rename.__doc__ + '\n' + '* ``Delete``: ' + Qgis.BrowserItemCapability.Delete.__doc__
# --
Qgis.BrowserItemCapability.baseClass = Qgis
QgsLayerItem.LayerType = Qgis.BrowserLayerType
# monkey patching scoped based enum
QgsLayerItem.NoType = Qgis.BrowserLayerType.NoType
QgsLayerItem.NoType.is_monkey_patched = True
QgsLayerItem.NoType.__doc__ = "No type"
QgsLayerItem.Vector = Qgis.BrowserLayerType.Vector
QgsLayerItem.Vector.is_monkey_patched = True
QgsLayerItem.Vector.__doc__ = "Generic vector layer"
QgsLayerItem.Raster = Qgis.BrowserLayerType.Raster
QgsLayerItem.Raster.is_monkey_patched = True
QgsLayerItem.Raster.__doc__ = "Raster layer"
QgsLayerItem.Point = Qgis.BrowserLayerType.Point
QgsLayerItem.Point.is_monkey_patched = True
QgsLayerItem.Point.__doc__ = "Vector point layer"
QgsLayerItem.Line = Qgis.BrowserLayerType.Line
QgsLayerItem.Line.is_monkey_patched = True
QgsLayerItem.Line.__doc__ = "Vector line layer"
QgsLayerItem.Polygon = Qgis.BrowserLayerType.Polygon
QgsLayerItem.Polygon.is_monkey_patched = True
QgsLayerItem.Polygon.__doc__ = "Vector polygon layer"
QgsLayerItem.TableLayer = Qgis.BrowserLayerType.TableLayer
QgsLayerItem.TableLayer.is_monkey_patched = True
QgsLayerItem.TableLayer.__doc__ = "Vector non-spatial layer"
QgsLayerItem.Database = Qgis.BrowserLayerType.Database
QgsLayerItem.Database.is_monkey_patched = True
QgsLayerItem.Database.__doc__ = "Database layer"
QgsLayerItem.Table = Qgis.BrowserLayerType.Table
QgsLayerItem.Table.is_monkey_patched = True
QgsLayerItem.Table.__doc__ = "Database table"
QgsLayerItem.Plugin = Qgis.BrowserLayerType.Plugin
QgsLayerItem.Plugin.is_monkey_patched = True
QgsLayerItem.Plugin.__doc__ = "Plugin based layer"
QgsLayerItem.Mesh = Qgis.BrowserLayerType.Mesh
QgsLayerItem.Mesh.is_monkey_patched = True
QgsLayerItem.Mesh.__doc__ = "Mesh layer"
QgsLayerItem.VectorTile = Qgis.BrowserLayerType.VectorTile
QgsLayerItem.VectorTile.is_monkey_patched = True
QgsLayerItem.VectorTile.__doc__ = "Vector tile layer"
QgsLayerItem.PointCloud = Qgis.BrowserLayerType.PointCloud
QgsLayerItem.PointCloud.is_monkey_patched = True
QgsLayerItem.PointCloud.__doc__ = "Point cloud layer"
Qgis.BrowserLayerType.__doc__ = 'Browser item layer types\n\n.. versionadded:: 3.20\n\n' + '* ``NoType``: ' + Qgis.BrowserLayerType.NoType.__doc__ + '\n' + '* ``Vector``: ' + Qgis.BrowserLayerType.Vector.__doc__ + '\n' + '* ``Raster``: ' + Qgis.BrowserLayerType.Raster.__doc__ + '\n' + '* ``Point``: ' + Qgis.BrowserLayerType.Point.__doc__ + '\n' + '* ``Line``: ' + Qgis.BrowserLayerType.Line.__doc__ + '\n' + '* ``Polygon``: ' + Qgis.BrowserLayerType.Polygon.__doc__ + '\n' + '* ``TableLayer``: ' + Qgis.BrowserLayerType.TableLayer.__doc__ + '\n' + '* ``Database``: ' + Qgis.BrowserLayerType.Database.__doc__ + '\n' + '* ``Table``: ' + Qgis.BrowserLayerType.Table.__doc__ + '\n' + '* ``Plugin``: ' + Qgis.BrowserLayerType.Plugin.__doc__ + '\n' + '* ``Mesh``: ' + Qgis.BrowserLayerType.Mesh.__doc__ + '\n' + '* ``VectorTile``: ' + Qgis.BrowserLayerType.VectorTile.__doc__ + '\n' + '* ``PointCloud``: ' + Qgis.BrowserLayerType.PointCloud.__doc__
# --
Qgis.BrowserLayerType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.BrowserDirectoryMonitoring.Default.__doc__ = "Use default logic to determine whether directory should be monitored"
Qgis.BrowserDirectoryMonitoring.NeverMonitor.__doc__ = "Never monitor the directory, regardless of the default logic"
Qgis.BrowserDirectoryMonitoring.AlwaysMonitor.__doc__ = "Always monitor the directory, regardless of the default logic"
Qgis.BrowserDirectoryMonitoring.__doc__ = 'Browser directory item monitoring switches.\n\n.. versionadded:: 3.20\n\n' + '* ``Default``: ' + Qgis.BrowserDirectoryMonitoring.Default.__doc__ + '\n' + '* ``NeverMonitor``: ' + Qgis.BrowserDirectoryMonitoring.NeverMonitor.__doc__ + '\n' + '* ``AlwaysMonitor``: ' + Qgis.BrowserDirectoryMonitoring.AlwaysMonitor.__doc__
# --
Qgis.BrowserDirectoryMonitoring.baseClass = Qgis
QgsVectorLayerExporter.ExportError = Qgis.VectorExportResult
# monkey patching scoped based enum
QgsVectorLayerExporter.NoError = Qgis.VectorExportResult.Success
QgsVectorLayerExporter.NoError.is_monkey_patched = True
QgsVectorLayerExporter.NoError.__doc__ = "No errors were encountered"
QgsVectorLayerExporter.ErrCreateDataSource = Qgis.VectorExportResult.ErrorCreatingDataSource
QgsVectorLayerExporter.ErrCreateDataSource.is_monkey_patched = True
QgsVectorLayerExporter.ErrCreateDataSource.__doc__ = "Could not create the destination data source"
QgsVectorLayerExporter.ErrCreateLayer = Qgis.VectorExportResult.ErrorCreatingLayer
QgsVectorLayerExporter.ErrCreateLayer.is_monkey_patched = True
QgsVectorLayerExporter.ErrCreateLayer.__doc__ = "Could not create destination layer"
QgsVectorLayerExporter.ErrAttributeTypeUnsupported = Qgis.VectorExportResult.ErrorAttributeTypeUnsupported
QgsVectorLayerExporter.ErrAttributeTypeUnsupported.is_monkey_patched = True
QgsVectorLayerExporter.ErrAttributeTypeUnsupported.__doc__ = "Source layer has an attribute type which could not be handled by destination"
QgsVectorLayerExporter.ErrAttributeCreationFailed = Qgis.VectorExportResult.ErrorAttributeCreationFailed
QgsVectorLayerExporter.ErrAttributeCreationFailed.is_monkey_patched = True
QgsVectorLayerExporter.ErrAttributeCreationFailed.__doc__ = "Destination provider was unable to create an attribute"
QgsVectorLayerExporter.ErrProjection = Qgis.VectorExportResult.ErrorProjectingFeatures
QgsVectorLayerExporter.ErrProjection.is_monkey_patched = True
QgsVectorLayerExporter.ErrProjection.__doc__ = "An error occurred while reprojecting features to destination CRS"
QgsVectorLayerExporter.ErrFeatureWriteFailed = Qgis.VectorExportResult.ErrorFeatureWriteFailed
QgsVectorLayerExporter.ErrFeatureWriteFailed.is_monkey_patched = True
QgsVectorLayerExporter.ErrFeatureWriteFailed.__doc__ = "An error occurred while writing a feature to the destination"
QgsVectorLayerExporter.ErrInvalidLayer = Qgis.VectorExportResult.ErrorInvalidLayer
QgsVectorLayerExporter.ErrInvalidLayer.is_monkey_patched = True
QgsVectorLayerExporter.ErrInvalidLayer.__doc__ = "Could not access newly created destination layer"
QgsVectorLayerExporter.ErrInvalidProvider = Qgis.VectorExportResult.ErrorInvalidProvider
QgsVectorLayerExporter.ErrInvalidProvider.is_monkey_patched = True
QgsVectorLayerExporter.ErrInvalidProvider.__doc__ = "Could not find a matching provider key"
QgsVectorLayerExporter.ErrProviderUnsupportedFeature = Qgis.VectorExportResult.ErrorProviderUnsupportedFeature
QgsVectorLayerExporter.ErrProviderUnsupportedFeature.is_monkey_patched = True
QgsVectorLayerExporter.ErrProviderUnsupportedFeature.__doc__ = "Provider does not support creation of empty layers"
QgsVectorLayerExporter.ErrConnectionFailed = Qgis.VectorExportResult.ErrorConnectionFailed
QgsVectorLayerExporter.ErrConnectionFailed.is_monkey_patched = True
QgsVectorLayerExporter.ErrConnectionFailed.__doc__ = "Could not connect to destination"
QgsVectorLayerExporter.ErrUserCanceled = Qgis.VectorExportResult.UserCanceled
QgsVectorLayerExporter.ErrUserCanceled.is_monkey_patched = True
QgsVectorLayerExporter.ErrUserCanceled.__doc__ = "User canceled the export"
Qgis.VectorExportResult.__doc__ = 'Vector layer export result codes.\n\n.. versionadded:: 3.20\n\n' + '* ``NoError``: ' + Qgis.VectorExportResult.Success.__doc__ + '\n' + '* ``ErrCreateDataSource``: ' + Qgis.VectorExportResult.ErrorCreatingDataSource.__doc__ + '\n' + '* ``ErrCreateLayer``: ' + Qgis.VectorExportResult.ErrorCreatingLayer.__doc__ + '\n' + '* ``ErrAttributeTypeUnsupported``: ' + Qgis.VectorExportResult.ErrorAttributeTypeUnsupported.__doc__ + '\n' + '* ``ErrAttributeCreationFailed``: ' + Qgis.VectorExportResult.ErrorAttributeCreationFailed.__doc__ + '\n' + '* ``ErrProjection``: ' + Qgis.VectorExportResult.ErrorProjectingFeatures.__doc__ + '\n' + '* ``ErrFeatureWriteFailed``: ' + Qgis.VectorExportResult.ErrorFeatureWriteFailed.__doc__ + '\n' + '* ``ErrInvalidLayer``: ' + Qgis.VectorExportResult.ErrorInvalidLayer.__doc__ + '\n' + '* ``ErrInvalidProvider``: ' + Qgis.VectorExportResult.ErrorInvalidProvider.__doc__ + '\n' + '* ``ErrProviderUnsupportedFeature``: ' + Qgis.VectorExportResult.ErrorProviderUnsupportedFeature.__doc__ + '\n' + '* ``ErrConnectionFailed``: ' + Qgis.VectorExportResult.ErrorConnectionFailed.__doc__ + '\n' + '* ``ErrUserCanceled``: ' + Qgis.VectorExportResult.UserCanceled.__doc__
# --
Qgis.VectorExportResult.baseClass = Qgis
# monkey patching scoped based enum
Qgis.DriveType.Unknown.__doc__ = "Unknown type"
Qgis.DriveType.Invalid.__doc__ = "Invalid path"
Qgis.DriveType.Removable.__doc__ = "Removable drive"
Qgis.DriveType.Fixed.__doc__ = "Fixed drive"
Qgis.DriveType.Remote.__doc__ = "Remote drive"
Qgis.DriveType.CdRom.__doc__ = "CD-ROM"
Qgis.DriveType.RamDisk.__doc__ = "RAM disk"
Qgis.DriveType.__doc__ = 'Drive types\n\n.. versionadded:: 3.20\n\n' + '* ``Unknown``: ' + Qgis.DriveType.Unknown.__doc__ + '\n' + '* ``Invalid``: ' + Qgis.DriveType.Invalid.__doc__ + '\n' + '* ``Removable``: ' + Qgis.DriveType.Removable.__doc__ + '\n' + '* ``Fixed``: ' + Qgis.DriveType.Fixed.__doc__ + '\n' + '* ``Remote``: ' + Qgis.DriveType.Remote.__doc__ + '\n' + '* ``CdRom``: ' + Qgis.DriveType.CdRom.__doc__ + '\n' + '* ``RamDisk``: ' + Qgis.DriveType.RamDisk.__doc__
# --
Qgis.DriveType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.UnplacedLabelVisibility.FollowEngineSetting.__doc__ = "Respect the label engine setting"
Qgis.UnplacedLabelVisibility.NeverShow.__doc__ = "Never show unplaced labels, regardless of the engine setting"
Qgis.UnplacedLabelVisibility.__doc__ = 'Unplaced label visibility.\n\n.. versionadded:: 3.20\n\n' + '* ``FollowEngineSetting``: ' + Qgis.UnplacedLabelVisibility.FollowEngineSetting.__doc__ + '\n' + '* ``NeverShow``: ' + Qgis.UnplacedLabelVisibility.NeverShow.__doc__
# --
Qgis.UnplacedLabelVisibility.baseClass = Qgis
# The following has been generated automatically from src/core/providers/qgsabstractdatabaseproviderconnection.h
QgsAbstractDatabaseProviderConnection.TableFlag.baseClass = QgsAbstractDatabaseProviderConnection
QgsAbstractDatabaseProviderConnection.TableFlags.baseClass = QgsAbstractDatabaseProviderConnection
TableFlags = QgsAbstractDatabaseProviderConnection  # dirty hack since SIP seems to introduce the flags in module
QgsAbstractDatabaseProviderConnection.Capability.baseClass = QgsAbstractDatabaseProviderConnection
QgsAbstractDatabaseProviderConnection.Capabilities.baseClass = QgsAbstractDatabaseProviderConnection
Capabilities = QgsAbstractDatabaseProviderConnection  # dirty hack since SIP seems to introduce the flags in module
QgsAbstractDatabaseProviderConnection.GeometryColumnCapability.baseClass = QgsAbstractDatabaseProviderConnection
QgsAbstractDatabaseProviderConnection.GeometryColumnCapabilities.baseClass = QgsAbstractDatabaseProviderConnection
GeometryColumnCapabilities = QgsAbstractDatabaseProviderConnection  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/geometry/qgsabstractgeometry.h
QgsAbstractGeometry.SegmentationToleranceType.baseClass = QgsAbstractGeometry
# The following has been generated automatically from src/core/editform/qgsattributeeditorrelation.h
QgsAttributeEditorRelation.Button.baseClass = QgsAttributeEditorRelation
QgsAttributeEditorRelation.Buttons.baseClass = QgsAttributeEditorRelation
Buttons = QgsAttributeEditorRelation  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/auth/qgsauthmanager.h
QgsAuthManager.MessageLevel.baseClass = QgsAuthManager
# The following has been generated automatically from src/core/qgsdatasourceuri.h
QgsDataSourceUri.SslMode.baseClass = QgsDataSourceUri
# The following has been generated automatically from src/core/qgsdefaultvalue.h
QgsDefaultValue.__bool__ = lambda self: self.isValid()
# The following has been generated automatically from src/core/dxf/qgsdxfexport.h
# monkey patching scoped based enum
QgsDxfExport.ExportResult.Success.__doc__ = "Successful export"
QgsDxfExport.ExportResult.InvalidDeviceError.__doc__ = "Invalid device error"
QgsDxfExport.ExportResult.DeviceNotWritableError.__doc__ = "Device not writable error"
QgsDxfExport.ExportResult.EmptyExtentError.__doc__ = "Empty extent, no extent given and no extent could be derived from layers"
QgsDxfExport.ExportResult.__doc__ = 'The result of an export as dxf operation\n\n.. versionadded:: 3.10.1\n\n' + '* ``Success``: ' + QgsDxfExport.ExportResult.Success.__doc__ + '\n' + '* ``InvalidDeviceError``: ' + QgsDxfExport.ExportResult.InvalidDeviceError.__doc__ + '\n' + '* ``DeviceNotWritableError``: ' + QgsDxfExport.ExportResult.DeviceNotWritableError.__doc__ + '\n' + '* ``EmptyExtentError``: ' + QgsDxfExport.ExportResult.EmptyExtentError.__doc__
# --
# monkey patching scoped based enum
QgsDxfExport.VAlign.VBaseLine.__doc__ = "Top (0)"
QgsDxfExport.VAlign.VBottom.__doc__ = "Bottom (1)"
QgsDxfExport.VAlign.VMiddle.__doc__ = "Middle (2)"
QgsDxfExport.VAlign.VTop.__doc__ = "Top (3)"
QgsDxfExport.VAlign.Undefined.__doc__ = "Undefined"
QgsDxfExport.VAlign.__doc__ = 'Vertical alignments.\n\n' + '* ``VBaseLine``: ' + QgsDxfExport.VAlign.VBaseLine.__doc__ + '\n' + '* ``VBottom``: ' + QgsDxfExport.VAlign.VBottom.__doc__ + '\n' + '* ``VMiddle``: ' + QgsDxfExport.VAlign.VMiddle.__doc__ + '\n' + '* ``VTop``: ' + QgsDxfExport.VAlign.VTop.__doc__ + '\n' + '* ``Undefined``: ' + QgsDxfExport.VAlign.Undefined.__doc__
# --
# monkey patching scoped based enum
QgsDxfExport.HAlign.HLeft.__doc__ = "Left (0)"
QgsDxfExport.HAlign.HCenter.__doc__ = "Centered (1)"
QgsDxfExport.HAlign.HRight.__doc__ = "Right (2)"
QgsDxfExport.HAlign.HAligned.__doc__ = "Aligned = (3) (if VAlign==0)"
QgsDxfExport.HAlign.HMiddle.__doc__ = "Middle = (4) (if VAlign==0)"
QgsDxfExport.HAlign.HFit.__doc__ = "Fit into point = (5) (if VAlign==0)"
QgsDxfExport.HAlign.Undefined.__doc__ = "Undefined"
QgsDxfExport.HAlign.__doc__ = 'Horizontal alignments.\n\n' + '* ``HLeft``: ' + QgsDxfExport.HAlign.HLeft.__doc__ + '\n' + '* ``HCenter``: ' + QgsDxfExport.HAlign.HCenter.__doc__ + '\n' + '* ``HRight``: ' + QgsDxfExport.HAlign.HRight.__doc__ + '\n' + '* ``HAligned``: ' + QgsDxfExport.HAlign.HAligned.__doc__ + '\n' + '* ``HMiddle``: ' + QgsDxfExport.HAlign.HMiddle.__doc__ + '\n' + '* ``HFit``: ' + QgsDxfExport.HAlign.HFit.__doc__ + '\n' + '* ``Undefined``: ' + QgsDxfExport.HAlign.Undefined.__doc__
# --
# The following has been generated automatically from src/core/editform/qgseditformconfig.h
QgsEditFormConfig.EditorLayout.baseClass = QgsEditFormConfig
QgsEditFormConfig.FeatureFormSuppress.baseClass = QgsEditFormConfig
QgsEditFormConfig.PythonInitCodeSource.baseClass = QgsEditFormConfig
# The following has been generated automatically from src/core/qgsfieldproxymodel.h
QgsFieldProxyModel.Filters.baseClass = QgsFieldProxyModel
Filters = QgsFieldProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/geocoding/qgsgeocoder.h
# monkey patching scoped based enum
QgsGeocoderInterface.Flag.GeocodesStrings.__doc__ = "Can geocode string input values"
QgsGeocoderInterface.Flag.GeocodesFeatures.__doc__ = "Can geocode QgsFeature input values"
QgsGeocoderInterface.Flag.__doc__ = 'Capability flags for the geocoder.\n\n' + '* ``GeocodesStrings``: ' + QgsGeocoderInterface.Flag.GeocodesStrings.__doc__ + '\n' + '* ``GeocodesFeatures``: ' + QgsGeocoderInterface.Flag.GeocodesFeatures.__doc__
# --
# The following has been generated automatically from src/core/geometry/qgsgeometry.h
QgsGeometry.OperationResult.baseClass = QgsGeometry
QgsGeometry.BufferSide.baseClass = QgsGeometry
QgsGeometry.EndCapStyle.baseClass = QgsGeometry
QgsGeometry.JoinStyle.baseClass = QgsGeometry
# The following has been generated automatically from src/core/geocms/geonode/qgsgeonoderequest.h
# monkey patching scoped based enum
QgsGeoNodeRequest.BackendServer.Unknown.__doc__ = "Unknown backend"
QgsGeoNodeRequest.BackendServer.QgisServer.__doc__ = "QGIS server used as backend"
QgsGeoNodeRequest.BackendServer.Geoserver.__doc__ = "Geoserver used as backend"
QgsGeoNodeRequest.BackendServer.__doc__ = 'GeoNode backend server type.\n\n' + '* ``Unknown``: ' + QgsGeoNodeRequest.BackendServer.Unknown.__doc__ + '\n' + '* ``QgisServer``: ' + QgsGeoNodeRequest.BackendServer.QgisServer.__doc__ + '\n' + '* ``Geoserver``: ' + QgsGeoNodeRequest.BackendServer.Geoserver.__doc__
# --
# The following has been generated automatically from src/core/labeling/qgslabellinesettings.h
# monkey patching scoped based enum
QgsLabelLineSettings.DirectionSymbolPlacement.SymbolLeftRight.__doc__ = "Place direction symbols on left/right of label"
QgsLabelLineSettings.DirectionSymbolPlacement.SymbolAbove.__doc__ = "Place direction symbols on above label"
QgsLabelLineSettings.DirectionSymbolPlacement.SymbolBelow.__doc__ = "Place direction symbols on below label"
QgsLabelLineSettings.DirectionSymbolPlacement.__doc__ = 'Placement options for direction symbols.\n\n' + '* ``SymbolLeftRight``: ' + QgsLabelLineSettings.DirectionSymbolPlacement.SymbolLeftRight.__doc__ + '\n' + '* ``SymbolAbove``: ' + QgsLabelLineSettings.DirectionSymbolPlacement.SymbolAbove.__doc__ + '\n' + '* ``SymbolBelow``: ' + QgsLabelLineSettings.DirectionSymbolPlacement.SymbolBelow.__doc__
# --
# monkey patching scoped based enum
QgsLabelLineSettings.AnchorType.HintOnly.__doc__ = "Line anchor is a hint for preferred placement only, but other placements close to the hint are permitted"
QgsLabelLineSettings.AnchorType.Strict.__doc__ = "Line anchor is a strict placement, and other placements are not permitted"
QgsLabelLineSettings.AnchorType.__doc__ = 'Line anchor types\n\n' + '* ``HintOnly``: ' + QgsLabelLineSettings.AnchorType.HintOnly.__doc__ + '\n' + '* ``Strict``: ' + QgsLabelLineSettings.AnchorType.Strict.__doc__
# --
# monkey patching scoped based enum
QgsLabelLineSettings.AnchorClipping.UseVisiblePartsOfLine.__doc__ = "Only visible parts of lines are considered when calculating the line anchor for labels"
QgsLabelLineSettings.AnchorClipping.UseEntireLine.__doc__ = "Entire original feature line geometry is used when calculating the line anchor for labels"
QgsLabelLineSettings.AnchorClipping.__doc__ = 'Clipping behavior for line anchor calculation.\n\n.. versionadded:: 3.20\n\n' + '* ``UseVisiblePartsOfLine``: ' + QgsLabelLineSettings.AnchorClipping.UseVisiblePartsOfLine.__doc__ + '\n' + '* ``UseEntireLine``: ' + QgsLabelLineSettings.AnchorClipping.UseEntireLine.__doc__
# --
# The following has been generated automatically from src/core/layout/qgslayoutmanager.h
QgsLayoutManagerProxyModel.Filters.baseClass = QgsLayoutManagerProxyModel
Filters = QgsLayoutManagerProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/locator/qgslocatorfilter.h
QgsLocatorFilter.Priority.baseClass = QgsLocatorFilter
QgsLocatorFilter.Flags.baseClass = QgsLocatorFilter
Flags = QgsLocatorFilter  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/qgsmapclippingregion.h
# monkey patching scoped based enum
QgsMapClippingRegion.FeatureClippingType.ClipToIntersection.__doc__ = "Clip the geometry of these features to the region prior to rendering (i.e. feature boundaries will follow the clip region)"
QgsMapClippingRegion.FeatureClippingType.ClipPainterOnly.__doc__ = "Applying clipping on the painter only (i.e. feature boundaries will be unchanged, but may be invisible where the feature falls outside the clipping region)"
QgsMapClippingRegion.FeatureClippingType.NoClipping.__doc__ = "Only render features which intersect the clipping region, but do not clip these features to the region"
QgsMapClippingRegion.FeatureClippingType.__doc__ = 'Feature clipping behavior, which controls how features from vector layers\nwill be clipped.\n\n' + '* ``ClipToIntersection``: ' + QgsMapClippingRegion.FeatureClippingType.ClipToIntersection.__doc__ + '\n' + '* ``ClipPainterOnly``: ' + QgsMapClippingRegion.FeatureClippingType.ClipPainterOnly.__doc__ + '\n' + '* ``NoClipping``: ' + QgsMapClippingRegion.FeatureClippingType.NoClipping.__doc__
# --
# The following has been generated automatically from src/core/qgsmaplayer.h
QgsMapLayer.LayerFlag.baseClass = QgsMapLayer
QgsMapLayer.LayerFlags.baseClass = QgsMapLayer
LayerFlags = QgsMapLayer  # dirty hack since SIP seems to introduce the flags in module
QgsMapLayer.StyleCategory.baseClass = QgsMapLayer
QgsMapLayer.StyleCategories.baseClass = QgsMapLayer
StyleCategories = QgsMapLayer  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/qgsmaplayermodel.h
QgsMapLayerModel.ItemDataRole.baseClass = QgsMapLayerModel
# The following has been generated automatically from src/core/qgsmaplayerproxymodel.h
QgsMapLayerProxyModel.Filters.baseClass = QgsMapLayerProxyModel
Filters = QgsMapLayerProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/qgsmapsettingsutils.h
# monkey patching scoped based enum
QgsMapSettingsUtils.EffectsCheckFlag.IgnoreGeoPdfSupportedEffects.__doc__ = "Ignore advanced effects which are supported in GeoPDF exports"
QgsMapSettingsUtils.EffectsCheckFlag.__doc__ = 'Flags for controlling the behavior of :py:func:`~QgsMapSettingsUtils.containsAdvancedEffects`\n\n.. versionadded:: 3.14\n\n' + '* ``IgnoreGeoPdfSupportedEffects``: ' + QgsMapSettingsUtils.EffectsCheckFlag.IgnoreGeoPdfSupportedEffects.__doc__
# --
# The following has been generated automatically from src/core/network/qgsnetworkcontentfetcherregistry.h
QgsNetworkContentFetcherRegistry.FetchingMode.baseClass = QgsNetworkContentFetcherRegistry
# The following has been generated automatically from src/core/pointcloud/qgspointcloudattributemodel.h
QgsPointCloudAttributeProxyModel.Filters.baseClass = QgsPointCloudAttributeProxyModel
Filters = QgsPointCloudAttributeProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/processing/qgsprocessingutils.h
# monkey patching scoped based enum
QgsProcessingUtils.UnknownType = QgsProcessingUtils.LayerHint.UnknownType
QgsProcessingUtils.UnknownType.is_monkey_patched = True
QgsProcessingUtils.LayerHint.UnknownType.__doc__ = "Unknown layer type"
QgsProcessingUtils.Vector = QgsProcessingUtils.LayerHint.Vector
QgsProcessingUtils.Vector.is_monkey_patched = True
QgsProcessingUtils.LayerHint.Vector.__doc__ = "Vector layer type"
QgsProcessingUtils.Raster = QgsProcessingUtils.LayerHint.Raster
QgsProcessingUtils.Raster.is_monkey_patched = True
QgsProcessingUtils.LayerHint.Raster.__doc__ = "Raster layer type"
QgsProcessingUtils.Mesh = QgsProcessingUtils.LayerHint.Mesh
QgsProcessingUtils.Mesh.is_monkey_patched = True
QgsProcessingUtils.LayerHint.Mesh.__doc__ = "Mesh layer type, since QGIS 3.6"
QgsProcessingUtils.LayerHint.__doc__ = 'Layer type hints.\n\n.. versionadded:: 3.4\n\n' + '* ``UnknownType``: ' + QgsProcessingUtils.LayerHint.UnknownType.__doc__ + '\n' + '* ``Vector``: ' + QgsProcessingUtils.LayerHint.Vector.__doc__ + '\n' + '* ``Raster``: ' + QgsProcessingUtils.LayerHint.Raster.__doc__ + '\n' + '* ``Mesh``: ' + QgsProcessingUtils.LayerHint.Mesh.__doc__
# --
# The following has been generated automatically from src/core/project/qgsproject.h
# monkey patching scoped based enum
QgsProject.FlagDontResolveLayers = QgsProject.ReadFlag.FlagDontResolveLayers
QgsProject.FlagDontResolveLayers.is_monkey_patched = True
QgsProject.ReadFlag.FlagDontResolveLayers.__doc__ = "Don't resolve layer paths (i.e. don't load any layer content). Dramatically improves project read time if the actual data from the layers is not required."
QgsProject.FlagDontLoadLayouts = QgsProject.ReadFlag.FlagDontLoadLayouts
QgsProject.FlagDontLoadLayouts.is_monkey_patched = True
QgsProject.ReadFlag.FlagDontLoadLayouts.__doc__ = "Don't load print layouts. Improves project read time if layouts are not required, and allows projects to be safely read in background threads (since print layouts are not thread safe)."
QgsProject.FlagTrustLayerMetadata = QgsProject.ReadFlag.FlagTrustLayerMetadata
QgsProject.FlagTrustLayerMetadata.is_monkey_patched = True
QgsProject.ReadFlag.FlagTrustLayerMetadata.__doc__ = "Trust layer metadata. Improves project read time. Do not use it if layers' extent is not fixed during the project's use by QGIS and QGIS Server."
QgsProject.FlagDontStoreOriginalStyles = QgsProject.ReadFlag.FlagDontStoreOriginalStyles
QgsProject.FlagDontStoreOriginalStyles.is_monkey_patched = True
QgsProject.ReadFlag.FlagDontStoreOriginalStyles.__doc__ = "Skip the initial XML style storage for layers. Useful for minimising project load times in non-interactive contexts."
QgsProject.ReadFlag.__doc__ = 'Flags which control project read behavior.\n\n.. versionadded:: 3.10\n\n' + '* ``FlagDontResolveLayers``: ' + QgsProject.ReadFlag.FlagDontResolveLayers.__doc__ + '\n' + '* ``FlagDontLoadLayouts``: ' + QgsProject.ReadFlag.FlagDontLoadLayouts.__doc__ + '\n' + '* ``FlagTrustLayerMetadata``: ' + QgsProject.ReadFlag.FlagTrustLayerMetadata.__doc__ + '\n' + '* ``FlagDontStoreOriginalStyles``: ' + QgsProject.ReadFlag.FlagDontStoreOriginalStyles.__doc__
# --
# monkey patching scoped based enum
QgsProject.FileFormat.Qgz.__doc__ = "Archive file format, supports auxiliary data"
QgsProject.FileFormat.Qgs.__doc__ = "Project saved in a clear text, does not support auxiliary data"
QgsProject.FileFormat.__doc__ = 'Flags which control project read behavior.\n\n.. versionadded:: 3.12\n\n' + '* ``Qgz``: ' + QgsProject.FileFormat.Qgz.__doc__ + '\n' + '* ``Qgs``: ' + QgsProject.FileFormat.Qgs.__doc__
# --
QgsProject.FileFormat.baseClass = QgsProject
# monkey patching scoped based enum
QgsProject.AvoidIntersectionsMode.AllowIntersections.__doc__ = "Overlap with any feature allowed when digitizing new features"
QgsProject.AvoidIntersectionsMode.AvoidIntersectionsCurrentLayer.__doc__ = "Overlap with features from the active layer when digitizing new features not allowed"
QgsProject.AvoidIntersectionsMode.AvoidIntersectionsLayers.__doc__ = "Overlap with features from a specified list of layers when digitizing new features not allowed"
QgsProject.AvoidIntersectionsMode.__doc__ = 'Flags which control how intersections of pre-existing feature are handled when digitizing new features.\n\n.. versionadded:: 3.14\n\n' + '* ``AllowIntersections``: ' + QgsProject.AvoidIntersectionsMode.AllowIntersections.__doc__ + '\n' + '* ``AvoidIntersectionsCurrentLayer``: ' + QgsProject.AvoidIntersectionsMode.AvoidIntersectionsCurrentLayer.__doc__ + '\n' + '* ``AvoidIntersectionsLayers``: ' + QgsProject.AvoidIntersectionsMode.AvoidIntersectionsLayers.__doc__
# --
QgsProject.AvoidIntersectionsMode.baseClass = QgsProject
# The following has been generated automatically from src/core/qgsproviderconnectionmodel.h
QgsProviderConnectionModel.Role.baseClass = QgsProviderConnectionModel
# The following has been generated automatically from src/core/providers/qgsprovidermetadata.h
QgsMeshDriverMetadata.MeshDriverCapability.baseClass = QgsMeshDriverMetadata
QgsMeshDriverMetadata.MeshDriverCapabilities.baseClass = QgsMeshDriverMetadata
MeshDriverCapabilities = QgsMeshDriverMetadata  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
QgsProviderMetadata.FilterType.FilterVector.__doc__ = "Vector layers"
QgsProviderMetadata.FilterType.FilterRaster.__doc__ = "Raster layers"
QgsProviderMetadata.FilterType.FilterMesh.__doc__ = "Mesh layers"
QgsProviderMetadata.FilterType.FilterMeshDataset.__doc__ = "Mesh datasets"
QgsProviderMetadata.FilterType.FilterPointCloud.__doc__ = "Point clouds (since QGIS 3.18)"
QgsProviderMetadata.FilterType.__doc__ = 'Type of file filters\n\n.. versionadded:: 3.10\n\n' + '* ``FilterVector``: ' + QgsProviderMetadata.FilterType.FilterVector.__doc__ + '\n' + '* ``FilterRaster``: ' + QgsProviderMetadata.FilterType.FilterRaster.__doc__ + '\n' + '* ``FilterMesh``: ' + QgsProviderMetadata.FilterType.FilterMesh.__doc__ + '\n' + '* ``FilterMeshDataset``: ' + QgsProviderMetadata.FilterType.FilterMeshDataset.__doc__ + '\n' + '* ``FilterPointCloud``: ' + QgsProviderMetadata.FilterType.FilterPointCloud.__doc__
# --
# The following has been generated automatically from src/core/raster/qgsrasterdataprovider.h
# monkey patching scoped based enum
QgsRasterDataProvider.ResamplingMethod.Nearest.__doc__ = "Nearest-neighbour resampling"
QgsRasterDataProvider.ResamplingMethod.Bilinear.__doc__ = "Bilinear (2x2 kernel) resampling"
QgsRasterDataProvider.ResamplingMethod.Cubic.__doc__ = "Cubic Convolution Approximation (4x4 kernel) resampling"
QgsRasterDataProvider.ResamplingMethod.CubicSpline.__doc__ = "Cubic B-Spline Approximation (4x4 kernel)"
QgsRasterDataProvider.ResamplingMethod.Lanczos.__doc__ = "Lanczos windowed sinc interpolation (6x6 kernel)"
QgsRasterDataProvider.ResamplingMethod.Average.__doc__ = "Average resampling"
QgsRasterDataProvider.ResamplingMethod.Mode.__doc__ = "Mode (selects the value which appears most often of all the sampled points)"
QgsRasterDataProvider.ResamplingMethod.Gauss.__doc__ = "Gauss blurring"
QgsRasterDataProvider.ResamplingMethod.__doc__ = 'Resampling method for provider-level resampling.\n\n.. versionadded:: 3.16\n\n' + '* ``Nearest``: ' + QgsRasterDataProvider.ResamplingMethod.Nearest.__doc__ + '\n' + '* ``Bilinear``: ' + QgsRasterDataProvider.ResamplingMethod.Bilinear.__doc__ + '\n' + '* ``Cubic``: ' + QgsRasterDataProvider.ResamplingMethod.Cubic.__doc__ + '\n' + '* ``CubicSpline``: ' + QgsRasterDataProvider.ResamplingMethod.CubicSpline.__doc__ + '\n' + '* ``Lanczos``: ' + QgsRasterDataProvider.ResamplingMethod.Lanczos.__doc__ + '\n' + '* ``Average``: ' + QgsRasterDataProvider.ResamplingMethod.Average.__doc__ + '\n' + '* ``Mode``: ' + QgsRasterDataProvider.ResamplingMethod.Mode.__doc__ + '\n' + '* ``Gauss``: ' + QgsRasterDataProvider.ResamplingMethod.Gauss.__doc__
# --
# The following has been generated automatically from src/core/raster/qgsrasterpipe.h
# monkey patching scoped based enum
QgsRasterPipe.ResamplingStage.ResampleFilter.__doc__ = ""
QgsRasterPipe.ResamplingStage.Provider.__doc__ = ""
QgsRasterPipe.ResamplingStage.__doc__ = 'Stage at which resampling occurs.\n\n.. versionadded:: 3.16\n\n' + '* ``ResampleFilter``: ' + QgsRasterPipe.ResamplingStage.ResampleFilter.__doc__ + '\n' + '* ``Provider``: ' + QgsRasterPipe.ResamplingStage.Provider.__doc__
# --
# The following has been generated automatically from src/core/raster/qgsrasterprojector.h
QgsRasterProjector.Precision.baseClass = QgsRasterProjector
# The following has been generated automatically from src/core/qgsrelation.h
QgsRelation.RelationType.baseClass = QgsRelation
QgsRelation.RelationStrength.baseClass = QgsRelation
# The following has been generated automatically from src/core/scalebar/qgsscalebarrenderer.h
# monkey patching scoped based enum
QgsScaleBarRenderer.Flag.FlagUsesLineSymbol.__doc__ = "Renderer utilizes the scalebar line symbol (see QgsScaleBarSettings::lineSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesFillSymbol.__doc__ = "Renderer utilizes the scalebar fill symbol (see QgsScaleBarSettings::fillSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesAlternateFillSymbol.__doc__ = "Renderer utilizes the alternate scalebar fill symbol (see QgsScaleBarSettings::alternateFillSymbol() )"
QgsScaleBarRenderer.Flag.FlagRespectsUnits.__doc__ = "Renderer respects the QgsScaleBarSettings::units() setting"
QgsScaleBarRenderer.Flag.FlagRespectsMapUnitsPerScaleBarUnit.__doc__ = "Renderer respects the QgsScaleBarSettings::mapUnitsPerScaleBarUnit() setting"
QgsScaleBarRenderer.Flag.FlagUsesUnitLabel.__doc__ = "Renderer uses the QgsScaleBarSettings::unitLabel() setting"
QgsScaleBarRenderer.Flag.FlagUsesSegments.__doc__ = "Renderer uses the scalebar segments"
QgsScaleBarRenderer.Flag.FlagUsesLabelBarSpace.__doc__ = "Renderer uses the QgsScaleBarSettings::labelBarSpace() setting"
QgsScaleBarRenderer.Flag.FlagUsesLabelVerticalPlacement.__doc__ = "Renderer uses the QgsScaleBarSettings::labelVerticalPlacement() setting"
QgsScaleBarRenderer.Flag.FlagUsesLabelHorizontalPlacement.__doc__ = "Renderer uses the QgsScaleBarSettings::labelHorizontalPlacement() setting"
QgsScaleBarRenderer.Flag.FlagUsesAlignment.__doc__ = "Renderer uses the QgsScaleBarSettings::alignment() setting"
QgsScaleBarRenderer.Flag.FlagUsesSubdivisions.__doc__ = "Renderer uses the scalebar subdivisions (see QgsScaleBarSettings::numberOfSubdivisions() )"
QgsScaleBarRenderer.Flag.FlagUsesDivisionSymbol.__doc__ = "Renderer utilizes the scalebar division symbol (see QgsScaleBarSettings::divisionLineSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesSubdivisionSymbol.__doc__ = "Renderer utilizes the scalebar subdivision symbol (see QgsScaleBarSettings::subdivisionLineSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesSubdivisionsHeight.__doc__ = "Renderer uses the scalebar subdivisions height (see QgsScaleBarSettings::subdivisionsHeight() )"
QgsScaleBarRenderer.Flag.__doc__ = 'Flags which control scalebar renderer behavior.\n\n.. versionadded:: 3.14\n\n' + '* ``FlagUsesLineSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesLineSymbol.__doc__ + '\n' + '* ``FlagUsesFillSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesFillSymbol.__doc__ + '\n' + '* ``FlagUsesAlternateFillSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesAlternateFillSymbol.__doc__ + '\n' + '* ``FlagRespectsUnits``: ' + QgsScaleBarRenderer.Flag.FlagRespectsUnits.__doc__ + '\n' + '* ``FlagRespectsMapUnitsPerScaleBarUnit``: ' + QgsScaleBarRenderer.Flag.FlagRespectsMapUnitsPerScaleBarUnit.__doc__ + '\n' + '* ``FlagUsesUnitLabel``: ' + QgsScaleBarRenderer.Flag.FlagUsesUnitLabel.__doc__ + '\n' + '* ``FlagUsesSegments``: ' + QgsScaleBarRenderer.Flag.FlagUsesSegments.__doc__ + '\n' + '* ``FlagUsesLabelBarSpace``: ' + QgsScaleBarRenderer.Flag.FlagUsesLabelBarSpace.__doc__ + '\n' + '* ``FlagUsesLabelVerticalPlacement``: ' + QgsScaleBarRenderer.Flag.FlagUsesLabelVerticalPlacement.__doc__ + '\n' + '* ``FlagUsesLabelHorizontalPlacement``: ' + QgsScaleBarRenderer.Flag.FlagUsesLabelHorizontalPlacement.__doc__ + '\n' + '* ``FlagUsesAlignment``: ' + QgsScaleBarRenderer.Flag.FlagUsesAlignment.__doc__ + '\n' + '* ``FlagUsesSubdivisions``: ' + QgsScaleBarRenderer.Flag.FlagUsesSubdivisions.__doc__ + '\n' + '* ``FlagUsesDivisionSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesDivisionSymbol.__doc__ + '\n' + '* ``FlagUsesSubdivisionSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesSubdivisionSymbol.__doc__ + '\n' + '* ``FlagUsesSubdivisionsHeight``: ' + QgsScaleBarRenderer.Flag.FlagUsesSubdivisionsHeight.__doc__
# --
# The following has been generated automatically from src/core/settings/qgssettingsentry.h
# monkey patching scoped based enum
QgsSettingsEntryBase.SettingsType.Variant.__doc__ = "Generic variant"
QgsSettingsEntryBase.SettingsType.String.__doc__ = "String"
QgsSettingsEntryBase.SettingsType.StringList.__doc__ = "List of strings"
QgsSettingsEntryBase.SettingsType.Bool.__doc__ = "Boolean"
QgsSettingsEntryBase.SettingsType.Integer.__doc__ = "Integer"
QgsSettingsEntryBase.SettingsType.Double.__doc__ = "Double precision numer"
QgsSettingsEntryBase.SettingsType.EnumFlag.__doc__ = "Enum or Flag"
QgsSettingsEntryBase.SettingsType.Color.__doc__ = "Color"
QgsSettingsEntryBase.SettingsType.__doc__ = 'Types of settings entries\n\n' + '* ``Variant``: ' + QgsSettingsEntryBase.SettingsType.Variant.__doc__ + '\n' + '* ``String``: ' + QgsSettingsEntryBase.SettingsType.String.__doc__ + '\n' + '* ``StringList``: ' + QgsSettingsEntryBase.SettingsType.StringList.__doc__ + '\n' + '* ``Bool``: ' + QgsSettingsEntryBase.SettingsType.Bool.__doc__ + '\n' + '* ``Integer``: ' + QgsSettingsEntryBase.SettingsType.Integer.__doc__ + '\n' + '* ``Double``: ' + QgsSettingsEntryBase.SettingsType.Double.__doc__ + '\n' + '* ``EnumFlag``: ' + QgsSettingsEntryBase.SettingsType.EnumFlag.__doc__ + '\n' + '* ``Color``: ' + QgsSettingsEntryBase.SettingsType.Color.__doc__
# --
# The following has been generated automatically from src/core/qgssnappingconfig.h
QgsSnappingConfig.SnappingMode.baseClass = QgsSnappingConfig
QgsSnappingConfig.SnappingTypes.baseClass = QgsSnappingConfig
QgsSnappingConfig.SnappingTypeFlag.baseClass = QgsSnappingConfig
SnappingTypeFlag = QgsSnappingConfig  # dirty hack since SIP seems to introduce the flags in module
QgsSnappingConfig.ScaleDependencyMode.baseClass = QgsSnappingConfig
# The following has been generated automatically from src/core/symbology/qgsstyle.h
# monkey patching scoped based enum
QgsStyle.TextFormatContext.Labeling.__doc__ = "Text format used in labeling"
QgsStyle.TextFormatContext.__doc__ = 'Text format context.\n\n.. versionadded:: 3.20\n\n' + '* ``Labeling``: ' + QgsStyle.TextFormatContext.Labeling.__doc__
# --
# The following has been generated automatically from src/core/symbology/qgsstyleentityvisitor.h
# monkey patching scoped based enum
QgsStyleEntityVisitorInterface.NodeType.Project.__doc__ = "QGIS Project node"
QgsStyleEntityVisitorInterface.NodeType.Layer.__doc__ = "Map layer"
QgsStyleEntityVisitorInterface.NodeType.SymbolRule.__doc__ = "Rule based symbology or label child rule"
QgsStyleEntityVisitorInterface.NodeType.Layouts.__doc__ = "Layout collection"
QgsStyleEntityVisitorInterface.NodeType.PrintLayout.__doc__ = "An individual print layout"
QgsStyleEntityVisitorInterface.NodeType.LayoutItem.__doc__ = "Individual item in a print layout"
QgsStyleEntityVisitorInterface.NodeType.Report.__doc__ = "A QGIS print report"
QgsStyleEntityVisitorInterface.NodeType.ReportHeader.__doc__ = "Report header section"
QgsStyleEntityVisitorInterface.NodeType.ReportFooter.__doc__ = "Report footer section"
QgsStyleEntityVisitorInterface.NodeType.ReportSection.__doc__ = "Report sub section"
QgsStyleEntityVisitorInterface.NodeType.Annotations.__doc__ = "Annotations collection"
QgsStyleEntityVisitorInterface.NodeType.Annotation.__doc__ = "An individual annotation"
QgsStyleEntityVisitorInterface.NodeType.__doc__ = 'Describes the types of nodes which may be visited by the visitor.\n\n' + '* ``Project``: ' + QgsStyleEntityVisitorInterface.NodeType.Project.__doc__ + '\n' + '* ``Layer``: ' + QgsStyleEntityVisitorInterface.NodeType.Layer.__doc__ + '\n' + '* ``SymbolRule``: ' + QgsStyleEntityVisitorInterface.NodeType.SymbolRule.__doc__ + '\n' + '* ``Layouts``: ' + QgsStyleEntityVisitorInterface.NodeType.Layouts.__doc__ + '\n' + '* ``PrintLayout``: ' + QgsStyleEntityVisitorInterface.NodeType.PrintLayout.__doc__ + '\n' + '* ``LayoutItem``: ' + QgsStyleEntityVisitorInterface.NodeType.LayoutItem.__doc__ + '\n' + '* ``Report``: ' + QgsStyleEntityVisitorInterface.NodeType.Report.__doc__ + '\n' + '* ``ReportHeader``: ' + QgsStyleEntityVisitorInterface.NodeType.ReportHeader.__doc__ + '\n' + '* ``ReportFooter``: ' + QgsStyleEntityVisitorInterface.NodeType.ReportFooter.__doc__ + '\n' + '* ``ReportSection``: ' + QgsStyleEntityVisitorInterface.NodeType.ReportSection.__doc__ + '\n' + '* ``Annotations``: ' + QgsStyleEntityVisitorInterface.NodeType.Annotations.__doc__ + '\n' + '* ``Annotation``: ' + QgsStyleEntityVisitorInterface.NodeType.Annotation.__doc__
# --
# The following has been generated automatically from src/core/qgstaskmanager.h
QgsTask.TaskStatus.baseClass = QgsTask
# The following has been generated automatically from src/core/textrenderer/qgstextcharacterformat.h
# monkey patching scoped based enum
QgsTextCharacterFormat.BooleanValue.NotSet.__doc__ = "Property is not set"
QgsTextCharacterFormat.BooleanValue.SetTrue.__doc__ = "Property is set and ``True``"
QgsTextCharacterFormat.BooleanValue.SetFalse.__doc__ = "Property is set and ``False``"
QgsTextCharacterFormat.BooleanValue.__doc__ = 'Status values for boolean format properties\n\n' + '* ``NotSet``: ' + QgsTextCharacterFormat.BooleanValue.NotSet.__doc__ + '\n' + '* ``SetTrue``: ' + QgsTextCharacterFormat.BooleanValue.SetTrue.__doc__ + '\n' + '* ``SetFalse``: ' + QgsTextCharacterFormat.BooleanValue.SetFalse.__doc__
# --
# The following has been generated automatically from src/core/qgstolerance.h
QgsTolerance.UnitType.baseClass = QgsTolerance
# The following has been generated automatically from src/core/qgsunittypes.h
QgsUnitTypes.SystemOfMeasurement.baseClass = QgsUnitTypes
QgsUnitTypes.DistanceUnit.baseClass = QgsUnitTypes
QgsUnitTypes.AreaUnit.baseClass = QgsUnitTypes
QgsUnitTypes.VolumeUnit.baseClass = QgsUnitTypes
QgsUnitTypes.AngleUnit.baseClass = QgsUnitTypes
QgsUnitTypes.TemporalUnit.baseClass = QgsUnitTypes
QgsUnitTypes.RenderUnit.baseClass = QgsUnitTypes
QgsUnitTypes.LayoutUnit.baseClass = QgsUnitTypes
# The following has been generated automatically from src/core/vector/qgsvectorlayer.h
QgsVectorLayer.EditResult.baseClass = QgsVectorLayer
QgsVectorLayer.SelectBehavior.baseClass = QgsVectorLayer
# The following has been generated automatically from src/core/vector/qgsvectorlayerserverproperties.h
QgsVectorLayerServerProperties.PredefinedWmsDimensionName.baseClass = QgsVectorLayerServerProperties
# The following has been generated automatically from src/core/qgsvectorsimplifymethod.h
QgsVectorSimplifyMethod.SimplifyHint.baseClass = QgsVectorSimplifyMethod
QgsVectorSimplifyMethod.SimplifyHints.baseClass = QgsVectorSimplifyMethod
SimplifyHints = QgsVectorSimplifyMethod  # dirty hack since SIP seems to introduce the flags in module
QgsVectorSimplifyMethod.SimplifyAlgorithm.baseClass = QgsVectorSimplifyMethod
# The following has been generated automatically from src/core/geometry/qgswkbtypes.h
QgsWkbTypes.Type.baseClass = QgsWkbTypes
QgsWkbTypes.GeometryType.baseClass = QgsWkbTypes
