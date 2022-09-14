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

from PyQt5.QtCore import NULL
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
QgsMarkerLineSymbolLayer.Interval = Qgis.MarkerLinePlacement.Interval
QgsMarkerLineSymbolLayer.Vertex = Qgis.MarkerLinePlacement.Vertex
QgsMarkerLineSymbolLayer.LastVertex = Qgis.MarkerLinePlacement.LastVertex
QgsMarkerLineSymbolLayer.FirstVertex = Qgis.MarkerLinePlacement.FirstVertex
QgsMarkerLineSymbolLayer.CentralPoint = Qgis.MarkerLinePlacement.CentralPoint
QgsMarkerLineSymbolLayer.CurvePoint = Qgis.MarkerLinePlacement.CurvePoint

QgsRasterFillSymbolLayer.FillCoordinateMode = Qgis.SymbolCoordinateReference
QgsRasterFillSymbolLayer.Feature = Qgis.SymbolCoordinateReference.Feature
QgsRasterFillSymbolLayer.Viewport = Qgis.SymbolCoordinateReference.Viewport

QgsShapeburstFillSymbolLayer.ShapeburstColorType = Qgis.GradientColorSource
QgsShapeburstFillSymbolLayer.SimpleTwoColor = Qgis.GradientColorSource.SimpleTwoColor
QgsShapeburstFillSymbolLayer.ColorRamp = Qgis.GradientColorSource.ColorRamp

QgsVectorLayer.VertexMarkerType = Qgis.VertexMarkerType
QgsVectorLayer.SemiTransparentCircle = Qgis.VertexMarkerType.SemiTransparentCircle
QgsVectorLayer.SemiTransparentCircle.is_monkey_patched = True
QgsVectorLayer.SemiTransparentCircle.__doc__ = "Semi-transparent circle marker"
QgsVectorLayer.Cross = Qgis.VertexMarkerType.Cross
QgsVectorLayer.Cross.is_monkey_patched = True
QgsVectorLayer.Cross.__doc__ = "Cross marker"
QgsVectorLayer.NoMarker = Qgis.VertexMarkerType.NoMarker
QgsVectorLayer.NoMarker.is_monkey_patched = True
QgsVectorLayer.NoMarker.__doc__ = "No marker"

QgsSymbol.RenderHints = Qgis.SymbolRenderHints
QgsSymbol.PreviewFlags = Qgis.SymbolPreviewFlags
QgsDataItem.Capabilities = Qgis.BrowserItemCapabilities
QgsGeometry.ValidityFlags = Qgis.GeometryValidityFlags

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
QgsMapLayer.VectorLayer.__doc__ = "Vector layer"
QgsMapLayer.RasterLayer = QgsMapLayerType.RasterLayer
QgsMapLayer.RasterLayer.is_monkey_patched = True
QgsMapLayer.RasterLayer.__doc__ = "Raster layer"
QgsMapLayer.PluginLayer = QgsMapLayerType.PluginLayer
QgsMapLayer.PluginLayer.is_monkey_patched = True
QgsMapLayer.PluginLayer.__doc__ = "Plugin based layer"
QgsMapLayer.MeshLayer = QgsMapLayerType.MeshLayer
QgsMapLayer.MeshLayer.is_monkey_patched = True
QgsMapLayer.MeshLayer.__doc__ = "Mesh layer. Added in QGIS 3.2"
QgsMapLayer.VectorTileLayer = QgsMapLayerType.VectorTileLayer
QgsMapLayer.VectorTileLayer.is_monkey_patched = True
QgsMapLayer.VectorTileLayer.__doc__ = "Vector tile layer. Added in QGIS 3.14"
QgsMapLayer.AnnotationLayer = QgsMapLayerType.AnnotationLayer
QgsMapLayer.AnnotationLayer.is_monkey_patched = True
QgsMapLayer.AnnotationLayer.__doc__ = "Contains freeform, georeferenced annotations. Added in QGIS 3.16"
QgsMapLayer.PointCloudLayer = QgsMapLayerType.PointCloudLayer
QgsMapLayer.PointCloudLayer.is_monkey_patched = True
QgsMapLayer.PointCloudLayer.__doc__ = "Point cloud layer. Added in QGIS 3.18"
QgsMapLayer.GroupLayer = QgsMapLayerType.GroupLayer
QgsMapLayer.GroupLayer.is_monkey_patched = True
QgsMapLayer.GroupLayer.__doc__ = "Composite group layer. Added in QGIS 3.24"
QgsMapLayerType.__doc__ = 'Types of layers that can be added to a map\n\n.. versionadded:: 3.8\n\n' + '* ``VectorLayer``: ' + QgsMapLayerType.VectorLayer.__doc__ + '\n' + '* ``RasterLayer``: ' + QgsMapLayerType.RasterLayer.__doc__ + '\n' + '* ``PluginLayer``: ' + QgsMapLayerType.PluginLayer.__doc__ + '\n' + '* ``MeshLayer``: ' + QgsMapLayerType.MeshLayer.__doc__ + '\n' + '* ``VectorTileLayer``: ' + QgsMapLayerType.VectorTileLayer.__doc__ + '\n' + '* ``AnnotationLayer``: ' + QgsMapLayerType.AnnotationLayer.__doc__ + '\n' + '* ``PointCloudLayer``: ' + QgsMapLayerType.PointCloudLayer.__doc__ + '\n' + '* ``GroupLayer``: ' + QgsMapLayerType.GroupLayer.__doc__
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
Qgis.ARGB32.__doc__ = "Color, alpha, red, green, blue, 4 bytes the same as QImage.Format_ARGB32"
Qgis.ARGB32_Premultiplied = Qgis.DataType.ARGB32_Premultiplied
Qgis.ARGB32_Premultiplied.is_monkey_patched = True
Qgis.ARGB32_Premultiplied.__doc__ = "Color, alpha, red, green, blue, 4 bytes  the same as QImage.Format_ARGB32_Premultiplied"
Qgis.DataType.__doc__ = 'Raster data types.\nThis is modified and extended copy of GDALDataType.\n\n' + '* ``UnknownDataType``: ' + Qgis.DataType.UnknownDataType.__doc__ + '\n' + '* ``Byte``: ' + Qgis.DataType.Byte.__doc__ + '\n' + '* ``UInt16``: ' + Qgis.DataType.UInt16.__doc__ + '\n' + '* ``Int16``: ' + Qgis.DataType.Int16.__doc__ + '\n' + '* ``UInt32``: ' + Qgis.DataType.UInt32.__doc__ + '\n' + '* ``Int32``: ' + Qgis.DataType.Int32.__doc__ + '\n' + '* ``Float32``: ' + Qgis.DataType.Float32.__doc__ + '\n' + '* ``Float64``: ' + Qgis.DataType.Float64.__doc__ + '\n' + '* ``CInt16``: ' + Qgis.DataType.CInt16.__doc__ + '\n' + '* ``CInt32``: ' + Qgis.DataType.CInt32.__doc__ + '\n' + '* ``CFloat32``: ' + Qgis.DataType.CFloat32.__doc__ + '\n' + '* ``CFloat64``: ' + Qgis.DataType.CFloat64.__doc__ + '\n' + '* ``ARGB32``: ' + Qgis.DataType.ARGB32.__doc__ + '\n' + '* ``ARGB32_Premultiplied``: ' + Qgis.DataType.ARGB32_Premultiplied.__doc__
# --
Qgis.DataType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.CaptureTechnique.StraightSegments.__doc__ = "Default capture mode - capture occurs with straight line segments"
Qgis.CaptureTechnique.CircularString.__doc__ = "Capture in circular strings"
Qgis.CaptureTechnique.Streaming.__doc__ = "Streaming points digitizing mode (points are automatically added as the mouse cursor moves)."
Qgis.CaptureTechnique.Shape.__doc__ = "Digitize shapes."
Qgis.CaptureTechnique.__doc__ = 'Capture technique.\n\n.. versionadded:: 3.26\n\n' + '* ``StraightSegments``: ' + Qgis.CaptureTechnique.StraightSegments.__doc__ + '\n' + '* ``CircularString``: ' + Qgis.CaptureTechnique.CircularString.__doc__ + '\n' + '* ``Streaming``: ' + Qgis.CaptureTechnique.Streaming.__doc__ + '\n' + '* ``Shape``: ' + Qgis.CaptureTechnique.Shape.__doc__
# --
Qgis.CaptureTechnique.baseClass = Qgis
# monkey patching scoped based enum
Qgis.VectorLayerTypeFlag.SqlQuery.__doc__ = "SQL query layer"
Qgis.VectorLayerTypeFlag.__doc__ = 'Vector layer type flags.\n\n.. versionadded:: 3.24\n\n' + '* ``SqlQuery``: ' + Qgis.VectorLayerTypeFlag.SqlQuery.__doc__
# --
Qgis.VectorLayerTypeFlag.baseClass = Qgis
Qgis.VectorLayerTypeFlags.baseClass = Qgis
VectorLayerTypeFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
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
QgsSettingsEntryBase.SettingsType = Qgis.SettingsType
# monkey patching scoped based enum
QgsSettingsEntryBase.Variant = Qgis.SettingsType.Variant
QgsSettingsEntryBase.Variant.is_monkey_patched = True
QgsSettingsEntryBase.Variant.__doc__ = "Generic variant"
QgsSettingsEntryBase.String = Qgis.SettingsType.String
QgsSettingsEntryBase.String.is_monkey_patched = True
QgsSettingsEntryBase.String.__doc__ = "String"
QgsSettingsEntryBase.StringList = Qgis.SettingsType.StringList
QgsSettingsEntryBase.StringList.is_monkey_patched = True
QgsSettingsEntryBase.StringList.__doc__ = "List of strings"
QgsSettingsEntryBase.Bool = Qgis.SettingsType.Bool
QgsSettingsEntryBase.Bool.is_monkey_patched = True
QgsSettingsEntryBase.Bool.__doc__ = "Boolean"
QgsSettingsEntryBase.Integer = Qgis.SettingsType.Integer
QgsSettingsEntryBase.Integer.is_monkey_patched = True
QgsSettingsEntryBase.Integer.__doc__ = "Integer"
QgsSettingsEntryBase.Double = Qgis.SettingsType.Double
QgsSettingsEntryBase.Double.is_monkey_patched = True
QgsSettingsEntryBase.Double.__doc__ = "Double precision number"
QgsSettingsEntryBase.EnumFlag = Qgis.SettingsType.EnumFlag
QgsSettingsEntryBase.EnumFlag.is_monkey_patched = True
QgsSettingsEntryBase.EnumFlag.__doc__ = "Enum or Flag"
QgsSettingsEntryBase.Color = Qgis.SettingsType.Color
QgsSettingsEntryBase.Color.is_monkey_patched = True
QgsSettingsEntryBase.Color.__doc__ = "Color"
Qgis.SettingsType.__doc__ = 'Types of settings entries\n\n.. versionadded:: 3.26\n\n' + '* ``Variant``: ' + Qgis.SettingsType.Variant.__doc__ + '\n' + '* ``String``: ' + Qgis.SettingsType.String.__doc__ + '\n' + '* ``StringList``: ' + Qgis.SettingsType.StringList.__doc__ + '\n' + '* ``Bool``: ' + Qgis.SettingsType.Bool.__doc__ + '\n' + '* ``Integer``: ' + Qgis.SettingsType.Integer.__doc__ + '\n' + '* ``Double``: ' + Qgis.SettingsType.Double.__doc__ + '\n' + '* ``EnumFlag``: ' + Qgis.SettingsType.EnumFlag.__doc__ + '\n' + '* ``Color``: ' + Qgis.SettingsType.Color.__doc__
# --
Qgis.SettingsType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SettingsOption.SaveFormerValue.__doc__ = ""
Qgis.SettingsOption.SaveEnumFlagAsInt.__doc__ = ""
Qgis.SettingsOption.__doc__ = 'Settings options\n\n.. versionadded:: 3.26\n\n' + '* ``SaveFormerValue``: ' + Qgis.SettingsOption.SaveFormerValue.__doc__ + '\n' + '* ``SaveEnumFlagAsInt``: ' + Qgis.SettingsOption.SaveEnumFlagAsInt.__doc__
# --
Qgis.SettingsOption.baseClass = Qgis
Qgis.SettingsOptions.baseClass = Qgis
SettingsOptions = Qgis  # dirty hack since SIP seems to introduce the flags in module
QgsSnappingConfig.SnappingMode = Qgis.SnappingMode
# monkey patching scoped based enum
QgsSnappingConfig.ActiveLayer = Qgis.SnappingMode.ActiveLayer
QgsSnappingConfig.ActiveLayer.is_monkey_patched = True
QgsSnappingConfig.ActiveLayer.__doc__ = "On the active layer"
QgsSnappingConfig.AllLayers = Qgis.SnappingMode.AllLayers
QgsSnappingConfig.AllLayers.is_monkey_patched = True
QgsSnappingConfig.AllLayers.__doc__ = "On all vector layers"
QgsSnappingConfig.AdvancedConfiguration = Qgis.SnappingMode.AdvancedConfiguration
QgsSnappingConfig.AdvancedConfiguration.is_monkey_patched = True
QgsSnappingConfig.AdvancedConfiguration.__doc__ = "On a per layer configuration basis"
Qgis.SnappingMode.__doc__ = 'SnappingMode defines on which layer the snapping is performed\n\n.. versionadded:: 3.26\n\n' + '* ``ActiveLayer``: ' + Qgis.SnappingMode.ActiveLayer.__doc__ + '\n' + '* ``AllLayers``: ' + Qgis.SnappingMode.AllLayers.__doc__ + '\n' + '* ``AdvancedConfiguration``: ' + Qgis.SnappingMode.AdvancedConfiguration.__doc__
# --
Qgis.SnappingMode.baseClass = Qgis
QgsSnappingConfig.SnappingTypes = Qgis.SnappingType
# monkey patching scoped based enum
QgsSnappingConfig.NoSnapFlag = Qgis.SnappingType.NoSnap
QgsSnappingConfig.NoSnapFlag.is_monkey_patched = True
QgsSnappingConfig.NoSnapFlag.__doc__ = "No snapping"
QgsSnappingConfig.VertexFlag = Qgis.SnappingType.Vertex
QgsSnappingConfig.VertexFlag.is_monkey_patched = True
QgsSnappingConfig.VertexFlag.__doc__ = "On vertices"
QgsSnappingConfig.SegmentFlag = Qgis.SnappingType.Segment
QgsSnappingConfig.SegmentFlag.is_monkey_patched = True
QgsSnappingConfig.SegmentFlag.__doc__ = "On segments"
QgsSnappingConfig.AreaFlag = Qgis.SnappingType.Area
QgsSnappingConfig.AreaFlag.is_monkey_patched = True
QgsSnappingConfig.AreaFlag.__doc__ = "On Area"
QgsSnappingConfig.CentroidFlag = Qgis.SnappingType.Centroid
QgsSnappingConfig.CentroidFlag.is_monkey_patched = True
QgsSnappingConfig.CentroidFlag.__doc__ = "On centroid"
QgsSnappingConfig.MiddleOfSegmentFlag = Qgis.SnappingType.MiddleOfSegment
QgsSnappingConfig.MiddleOfSegmentFlag.is_monkey_patched = True
QgsSnappingConfig.MiddleOfSegmentFlag.__doc__ = "On Middle segment"
QgsSnappingConfig.LineEndpointFlag = Qgis.SnappingType.LineEndpoint
QgsSnappingConfig.LineEndpointFlag.is_monkey_patched = True
QgsSnappingConfig.LineEndpointFlag.__doc__ = "Start or end points of lines, or first vertex in polygon rings only (since QGIS 3.20)"
Qgis.SnappingType.__doc__ = 'SnappingTypeFlag defines on what object the snapping is performed\n\n.. versionadded:: 3.26\n\n' + '* ``NoSnapFlag``: ' + Qgis.SnappingType.NoSnap.__doc__ + '\n' + '* ``VertexFlag``: ' + Qgis.SnappingType.Vertex.__doc__ + '\n' + '* ``SegmentFlag``: ' + Qgis.SnappingType.Segment.__doc__ + '\n' + '* ``AreaFlag``: ' + Qgis.SnappingType.Area.__doc__ + '\n' + '* ``CentroidFlag``: ' + Qgis.SnappingType.Centroid.__doc__ + '\n' + '* ``MiddleOfSegmentFlag``: ' + Qgis.SnappingType.MiddleOfSegment.__doc__ + '\n' + '* ``LineEndpointFlag``: ' + Qgis.SnappingType.LineEndpoint.__doc__
# --
Qgis.SnappingType.baseClass = Qgis
QgsSnappingConfig.SnappingTypeFlag = Qgis.SnappingTypes
Qgis.SnappingTypes.baseClass = Qgis
SnappingTypes = Qgis  # dirty hack since SIP seems to introduce the flags in module
QgsSymbol.RenderHint = Qgis.SymbolRenderHint
# monkey patching scoped based enum
QgsSymbol.DynamicRotation = Qgis.SymbolRenderHint.DynamicRotation
QgsSymbol.DynamicRotation.is_monkey_patched = True
QgsSymbol.DynamicRotation.__doc__ = "Rotation of symbol may be changed during rendering and symbol should not be cached"
Qgis.SymbolRenderHint.__doc__ = 'Flags controlling behavior of symbols during rendering\n\n.. versionadded:: 3.20\n\n' + '* ``DynamicRotation``: ' + Qgis.SymbolRenderHint.DynamicRotation.__doc__
# --
Qgis.SymbolRenderHint.baseClass = Qgis
QgsSymbol.RenderHints = Qgis.SymbolRenderHints
Qgis.SymbolRenderHints.baseClass = Qgis
SymbolRenderHints = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.SymbolFlag.RendererShouldUseSymbolLevels.__doc__ = "If present, indicates that a QgsFeatureRenderer using the symbol should use symbol levels for best results"
Qgis.SymbolFlag.__doc__ = 'Flags controlling behavior of symbols\n\n.. versionadded:: 3.20\n\n' + '* ``RendererShouldUseSymbolLevels``: ' + Qgis.SymbolFlag.RendererShouldUseSymbolLevels.__doc__
# --
Qgis.SymbolFlag.baseClass = Qgis
Qgis.SymbolFlags.baseClass = Qgis
SymbolFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
QgsSymbol.PreviewFlag = Qgis.SymbolPreviewFlag
# monkey patching scoped based enum
QgsSymbol.FlagIncludeCrosshairsForMarkerSymbols = Qgis.SymbolPreviewFlag.FlagIncludeCrosshairsForMarkerSymbols
QgsSymbol.FlagIncludeCrosshairsForMarkerSymbols.is_monkey_patched = True
QgsSymbol.FlagIncludeCrosshairsForMarkerSymbols.__doc__ = "Include a crosshairs reference image in the background of marker symbol previews"
Qgis.SymbolPreviewFlag.__doc__ = 'Flags for controlling how symbol preview images are generated.\n\n.. versionadded:: 3.20\n\n' + '* ``FlagIncludeCrosshairsForMarkerSymbols``: ' + Qgis.SymbolPreviewFlag.FlagIncludeCrosshairsForMarkerSymbols.__doc__
# --
Qgis.SymbolPreviewFlag.baseClass = Qgis
QgsSymbol.SymbolPreviewFlags = Qgis.SymbolPreviewFlags
Qgis.SymbolPreviewFlags.baseClass = Qgis
SymbolPreviewFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.SymbolLayerFlag.DisableFeatureClipping.__doc__ = "If present, indicates that features should never be clipped to the map extent during rendering"
Qgis.SymbolLayerFlag.__doc__ = 'Flags controlling behavior of symbol layers\n\n.. versionadded:: 3.22\n\n' + '* ``DisableFeatureClipping``: ' + Qgis.SymbolLayerFlag.DisableFeatureClipping.__doc__
# --
Qgis.SymbolLayerFlag.baseClass = Qgis
Qgis.SymbolLayerFlags.baseClass = Qgis
SymbolLayerFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
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
QgsDataItem.ItemRepresentsFile = Qgis.BrowserItemCapability.ItemRepresentsFile
QgsDataItem.ItemRepresentsFile.is_monkey_patched = True
QgsDataItem.ItemRepresentsFile.__doc__ = "Item's path() directly represents a file on disk (since QGIS 3.22)"
QgsDataItem.RefreshChildrenWhenItemIsRefreshed = Qgis.BrowserItemCapability.RefreshChildrenWhenItemIsRefreshed
QgsDataItem.RefreshChildrenWhenItemIsRefreshed.is_monkey_patched = True
QgsDataItem.RefreshChildrenWhenItemIsRefreshed.__doc__ = "When the item is refreshed, all its populated children will also be refreshed in turn (since QGIS 3.26)"
Qgis.BrowserItemCapability.__doc__ = 'Browser item capabilities.\n\n.. versionadded:: 3.20\n\n' + '* ``NoCapabilities``: ' + Qgis.BrowserItemCapability.NoCapabilities.__doc__ + '\n' + '* ``SetCrs``: ' + Qgis.BrowserItemCapability.SetCrs.__doc__ + '\n' + '* ``Fertile``: ' + Qgis.BrowserItemCapability.Fertile.__doc__ + '\n' + '* ``Fast``: ' + Qgis.BrowserItemCapability.Fast.__doc__ + '\n' + '* ``Collapse``: ' + Qgis.BrowserItemCapability.Collapse.__doc__ + '\n' + '* ``Rename``: ' + Qgis.BrowserItemCapability.Rename.__doc__ + '\n' + '* ``Delete``: ' + Qgis.BrowserItemCapability.Delete.__doc__ + '\n' + '* ``ItemRepresentsFile``: ' + Qgis.BrowserItemCapability.ItemRepresentsFile.__doc__ + '\n' + '* ``RefreshChildrenWhenItemIsRefreshed``: ' + Qgis.BrowserItemCapability.RefreshChildrenWhenItemIsRefreshed.__doc__
# --
Qgis.BrowserItemCapability.baseClass = Qgis
QgsDataItem.Capabilities = Qgis.BrowserItemCapabilities
Qgis.BrowserItemCapabilities.baseClass = Qgis
BrowserItemCapabilities = Qgis  # dirty hack since SIP seems to introduce the flags in module
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
# monkey patching scoped based enum
Qgis.HttpMethod.Get.__doc__ = "GET method"
Qgis.HttpMethod.Post.__doc__ = "POST method"
Qgis.HttpMethod.__doc__ = 'Different methods of HTTP requests\n\n.. versionadded:: 3.22\n\n' + '* ``Get``: ' + Qgis.HttpMethod.Get.__doc__ + '\n' + '* ``Post``: ' + Qgis.HttpMethod.Post.__doc__
# --
Qgis.HttpMethod.baseClass = Qgis
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
Qgis.SqlLayerDefinitionCapability.SubsetStringFilter.__doc__ = "SQL layer definition supports subset string filter"
Qgis.SqlLayerDefinitionCapability.GeometryColumn.__doc__ = "SQL layer definition supports geometry column"
Qgis.SqlLayerDefinitionCapability.PrimaryKeys.__doc__ = "SQL layer definition supports primary keys"
Qgis.SqlLayerDefinitionCapability.UnstableFeatureIds.__doc__ = "SQL layer definition supports disabling select at id"
Qgis.SqlLayerDefinitionCapability.__doc__ = 'SqlLayerDefinitionCapability enum lists the arguments supported by the provider when creating SQL query layers.\n\n.. versionadded:: 3.22\n\n' + '* ``SubsetStringFilter``: ' + Qgis.SqlLayerDefinitionCapability.SubsetStringFilter.__doc__ + '\n' + '* ``GeometryColumn``: ' + Qgis.SqlLayerDefinitionCapability.GeometryColumn.__doc__ + '\n' + '* ``PrimaryKeys``: ' + Qgis.SqlLayerDefinitionCapability.PrimaryKeys.__doc__ + '\n' + '* ``UnstableFeatureIds``: ' + Qgis.SqlLayerDefinitionCapability.UnstableFeatureIds.__doc__
# --
Qgis.SqlLayerDefinitionCapability.baseClass = Qgis
Qgis.SqlLayerDefinitionCapabilities.baseClass = Qgis
SqlLayerDefinitionCapabilities = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.SqlKeywordCategory.Keyword.__doc__ = "SQL keyword"
Qgis.SqlKeywordCategory.Constant.__doc__ = "SQL constant"
Qgis.SqlKeywordCategory.Function.__doc__ = "SQL generic function"
Qgis.SqlKeywordCategory.Geospatial.__doc__ = "SQL spatial function"
Qgis.SqlKeywordCategory.Operator.__doc__ = "SQL operator"
Qgis.SqlKeywordCategory.Math.__doc__ = "SQL math function"
Qgis.SqlKeywordCategory.Aggregate.__doc__ = "SQL aggregate function"
Qgis.SqlKeywordCategory.String.__doc__ = "SQL string function"
Qgis.SqlKeywordCategory.Identifier.__doc__ = "SQL identifier"
Qgis.SqlKeywordCategory.__doc__ = 'SqlKeywordCategory enum represents the categories of the SQL keywords used by the SQL query editor.\n\n.. note::\n\n   The category has currently no usage, but it was planned for future uses.\n\n.. versionadded:: 3.22\n\n' + '* ``Keyword``: ' + Qgis.SqlKeywordCategory.Keyword.__doc__ + '\n' + '* ``Constant``: ' + Qgis.SqlKeywordCategory.Constant.__doc__ + '\n' + '* ``Function``: ' + Qgis.SqlKeywordCategory.Function.__doc__ + '\n' + '* ``Geospatial``: ' + Qgis.SqlKeywordCategory.Geospatial.__doc__ + '\n' + '* ``Operator``: ' + Qgis.SqlKeywordCategory.Operator.__doc__ + '\n' + '* ``Math``: ' + Qgis.SqlKeywordCategory.Math.__doc__ + '\n' + '* ``Aggregate``: ' + Qgis.SqlKeywordCategory.Aggregate.__doc__ + '\n' + '* ``String``: ' + Qgis.SqlKeywordCategory.String.__doc__ + '\n' + '* ``Identifier``: ' + Qgis.SqlKeywordCategory.Identifier.__doc__
# --
Qgis.SqlKeywordCategory.baseClass = Qgis
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
QgsNetworkContentFetcherRegistry.FetchingMode = Qgis.ActionStart
# monkey patching scoped based enum
QgsNetworkContentFetcherRegistry.DownloadLater = Qgis.ActionStart.Deferred
QgsNetworkContentFetcherRegistry.DownloadLater.is_monkey_patched = True
QgsNetworkContentFetcherRegistry.DownloadLater.__doc__ = "Do not start immediately the action"
QgsNetworkContentFetcherRegistry.DownloadImmediately = Qgis.ActionStart.Immediate
QgsNetworkContentFetcherRegistry.DownloadImmediately.is_monkey_patched = True
QgsNetworkContentFetcherRegistry.DownloadImmediately.__doc__ = "Action will start immediately"
Qgis.ActionStart.__doc__ = 'Enum to determine when an operation would begin\n\n.. versionadded:: 3.22\n\n' + '* ``DownloadLater``: ' + Qgis.ActionStart.Deferred.__doc__ + '\n' + '* ``DownloadImmediately``: ' + Qgis.ActionStart.Immediate.__doc__
# --
Qgis.ActionStart.baseClass = Qgis
# monkey patching scoped based enum
Qgis.UnplacedLabelVisibility.FollowEngineSetting.__doc__ = "Respect the label engine setting"
Qgis.UnplacedLabelVisibility.NeverShow.__doc__ = "Never show unplaced labels, regardless of the engine setting"
Qgis.UnplacedLabelVisibility.__doc__ = 'Unplaced label visibility.\n\n.. versionadded:: 3.20\n\n' + '* ``FollowEngineSetting``: ' + Qgis.UnplacedLabelVisibility.FollowEngineSetting.__doc__ + '\n' + '* ``NeverShow``: ' + Qgis.UnplacedLabelVisibility.NeverShow.__doc__
# --
Qgis.UnplacedLabelVisibility.baseClass = Qgis
# monkey patching scoped based enum
Qgis.LabelOverlapHandling.PreventOverlap.__doc__ = "Do not allow labels to overlap other labels"
Qgis.LabelOverlapHandling.AllowOverlapIfRequired.__doc__ = "Avoids overlapping labels when possible, but permit overlaps if labels for features cannot otherwise be placed"
Qgis.LabelOverlapHandling.AllowOverlapAtNoCost.__doc__ = "Labels may freely overlap other labels, at no cost"
Qgis.LabelOverlapHandling.__doc__ = 'Label overlap handling.\n\n.. versionadded:: 3.26\n\n' + '* ``PreventOverlap``: ' + Qgis.LabelOverlapHandling.PreventOverlap.__doc__ + '\n' + '* ``AllowOverlapIfRequired``: ' + Qgis.LabelOverlapHandling.AllowOverlapIfRequired.__doc__ + '\n' + '* ``AllowOverlapAtNoCost``: ' + Qgis.LabelOverlapHandling.AllowOverlapAtNoCost.__doc__
# --
Qgis.LabelOverlapHandling.baseClass = Qgis
QgsPalLayerSettings.Placement = Qgis.LabelPlacement
# monkey patching scoped based enum
QgsPalLayerSettings.AroundPoint = Qgis.LabelPlacement.AroundPoint
QgsPalLayerSettings.AroundPoint.is_monkey_patched = True
QgsPalLayerSettings.AroundPoint.__doc__ = "Arranges candidates in a circle around a point (or centroid of a polygon). Applies to point or polygon layers only."
QgsPalLayerSettings.OverPoint = Qgis.LabelPlacement.OverPoint
QgsPalLayerSettings.OverPoint.is_monkey_patched = True
QgsPalLayerSettings.OverPoint.__doc__ = "Arranges candidates over a point (or centroid of a polygon), or at a preset offset from the point. Applies to point or polygon layers only."
QgsPalLayerSettings.Line = Qgis.LabelPlacement.Line
QgsPalLayerSettings.Line.is_monkey_patched = True
QgsPalLayerSettings.Line.__doc__ = "Arranges candidates parallel to a generalised line representing the feature or parallel to a polygon's perimeter. Applies to line or polygon layers only."
QgsPalLayerSettings.Curved = Qgis.LabelPlacement.Curved
QgsPalLayerSettings.Curved.is_monkey_patched = True
QgsPalLayerSettings.Curved.__doc__ = "Arranges candidates following the curvature of a line feature. Applies to line layers only."
QgsPalLayerSettings.Horizontal = Qgis.LabelPlacement.Horizontal
QgsPalLayerSettings.Horizontal.is_monkey_patched = True
QgsPalLayerSettings.Horizontal.__doc__ = "Arranges horizontal candidates scattered throughout a polygon feature. Applies to polygon layers only."
QgsPalLayerSettings.Free = Qgis.LabelPlacement.Free
QgsPalLayerSettings.Free.is_monkey_patched = True
QgsPalLayerSettings.Free.__doc__ = "Arranges candidates scattered throughout a polygon feature. Candidates are rotated to respect the polygon's orientation. Applies to polygon layers only."
QgsPalLayerSettings.OrderedPositionsAroundPoint = Qgis.LabelPlacement.OrderedPositionsAroundPoint
QgsPalLayerSettings.OrderedPositionsAroundPoint.is_monkey_patched = True
QgsPalLayerSettings.OrderedPositionsAroundPoint.__doc__ = "Candidates are placed in predefined positions around a point. Preference is given to positions with greatest cartographic appeal, e.g., top right, bottom right, etc. Applies to point layers only."
QgsPalLayerSettings.PerimeterCurved = Qgis.LabelPlacement.PerimeterCurved
QgsPalLayerSettings.PerimeterCurved.is_monkey_patched = True
QgsPalLayerSettings.PerimeterCurved.__doc__ = "Arranges candidates following the curvature of a polygon's boundary. Applies to polygon layers only."
QgsPalLayerSettings.OutsidePolygons = Qgis.LabelPlacement.OutsidePolygons
QgsPalLayerSettings.OutsidePolygons.is_monkey_patched = True
QgsPalLayerSettings.OutsidePolygons.__doc__ = "Candidates are placed outside of polygon boundaries. Applies to polygon layers only. Since QGIS 3.14"
Qgis.LabelPlacement.__doc__ = 'Placement modes which determine how label candidates are generated for a feature.\n\n.. note::\n\n   Prior to QGIS 3.26 this was available as :py:class:`QgsPalLayerSettings`.Placement\n\n.. versionadded:: 3.26\n\n' + '* ``AroundPoint``: ' + Qgis.LabelPlacement.AroundPoint.__doc__ + '\n' + '* ``OverPoint``: ' + Qgis.LabelPlacement.OverPoint.__doc__ + '\n' + '* ``Line``: ' + Qgis.LabelPlacement.Line.__doc__ + '\n' + '* ``Curved``: ' + Qgis.LabelPlacement.Curved.__doc__ + '\n' + '* ``Horizontal``: ' + Qgis.LabelPlacement.Horizontal.__doc__ + '\n' + '* ``Free``: ' + Qgis.LabelPlacement.Free.__doc__ + '\n' + '* ``OrderedPositionsAroundPoint``: ' + Qgis.LabelPlacement.OrderedPositionsAroundPoint.__doc__ + '\n' + '* ``PerimeterCurved``: ' + Qgis.LabelPlacement.PerimeterCurved.__doc__ + '\n' + '* ``OutsidePolygons``: ' + Qgis.LabelPlacement.OutsidePolygons.__doc__
# --
Qgis.LabelPlacement.baseClass = Qgis
QgsPalLayerSettings.PredefinedPointPosition = Qgis.LabelPredefinedPointPosition
# monkey patching scoped based enum
QgsPalLayerSettings.TopLeft = Qgis.LabelPredefinedPointPosition.TopLeft
QgsPalLayerSettings.TopLeft.is_monkey_patched = True
QgsPalLayerSettings.TopLeft.__doc__ = "Label on top-left of point"
QgsPalLayerSettings.TopSlightlyLeft = Qgis.LabelPredefinedPointPosition.TopSlightlyLeft
QgsPalLayerSettings.TopSlightlyLeft.is_monkey_patched = True
QgsPalLayerSettings.TopSlightlyLeft.__doc__ = "Label on top of point, slightly left of center"
QgsPalLayerSettings.TopMiddle = Qgis.LabelPredefinedPointPosition.TopMiddle
QgsPalLayerSettings.TopMiddle.is_monkey_patched = True
QgsPalLayerSettings.TopMiddle.__doc__ = "Label directly above point"
QgsPalLayerSettings.TopSlightlyRight = Qgis.LabelPredefinedPointPosition.TopSlightlyRight
QgsPalLayerSettings.TopSlightlyRight.is_monkey_patched = True
QgsPalLayerSettings.TopSlightlyRight.__doc__ = "Label on top of point, slightly right of center"
QgsPalLayerSettings.TopRight = Qgis.LabelPredefinedPointPosition.TopRight
QgsPalLayerSettings.TopRight.is_monkey_patched = True
QgsPalLayerSettings.TopRight.__doc__ = "Label on top-right of point"
QgsPalLayerSettings.MiddleLeft = Qgis.LabelPredefinedPointPosition.MiddleLeft
QgsPalLayerSettings.MiddleLeft.is_monkey_patched = True
QgsPalLayerSettings.MiddleLeft.__doc__ = "Label on left of point"
QgsPalLayerSettings.MiddleRight = Qgis.LabelPredefinedPointPosition.MiddleRight
QgsPalLayerSettings.MiddleRight.is_monkey_patched = True
QgsPalLayerSettings.MiddleRight.__doc__ = "Label on right of point"
QgsPalLayerSettings.BottomLeft = Qgis.LabelPredefinedPointPosition.BottomLeft
QgsPalLayerSettings.BottomLeft.is_monkey_patched = True
QgsPalLayerSettings.BottomLeft.__doc__ = "Label on bottom-left of point"
QgsPalLayerSettings.BottomSlightlyLeft = Qgis.LabelPredefinedPointPosition.BottomSlightlyLeft
QgsPalLayerSettings.BottomSlightlyLeft.is_monkey_patched = True
QgsPalLayerSettings.BottomSlightlyLeft.__doc__ = "Label below point, slightly left of center"
QgsPalLayerSettings.BottomMiddle = Qgis.LabelPredefinedPointPosition.BottomMiddle
QgsPalLayerSettings.BottomMiddle.is_monkey_patched = True
QgsPalLayerSettings.BottomMiddle.__doc__ = "Label directly below point"
QgsPalLayerSettings.BottomSlightlyRight = Qgis.LabelPredefinedPointPosition.BottomSlightlyRight
QgsPalLayerSettings.BottomSlightlyRight.is_monkey_patched = True
QgsPalLayerSettings.BottomSlightlyRight.__doc__ = "Label below point, slightly right of center"
QgsPalLayerSettings.BottomRight = Qgis.LabelPredefinedPointPosition.BottomRight
QgsPalLayerSettings.BottomRight.is_monkey_patched = True
QgsPalLayerSettings.BottomRight.__doc__ = "Label on bottom right of point"
Qgis.LabelPredefinedPointPosition.__doc__ = 'Positions for labels when using the Qgis.LabelPlacement.OrderedPositionsAroundPoint placement mode.\n\n.. note::\n\n   Prior to QGIS 3.26 this was available as :py:class:`QgsPalLayerSettings`.PredefinedPointPosition\n\n.. versionadded:: 3.26\n\n' + '* ``TopLeft``: ' + Qgis.LabelPredefinedPointPosition.TopLeft.__doc__ + '\n' + '* ``TopSlightlyLeft``: ' + Qgis.LabelPredefinedPointPosition.TopSlightlyLeft.__doc__ + '\n' + '* ``TopMiddle``: ' + Qgis.LabelPredefinedPointPosition.TopMiddle.__doc__ + '\n' + '* ``TopSlightlyRight``: ' + Qgis.LabelPredefinedPointPosition.TopSlightlyRight.__doc__ + '\n' + '* ``TopRight``: ' + Qgis.LabelPredefinedPointPosition.TopRight.__doc__ + '\n' + '* ``MiddleLeft``: ' + Qgis.LabelPredefinedPointPosition.MiddleLeft.__doc__ + '\n' + '* ``MiddleRight``: ' + Qgis.LabelPredefinedPointPosition.MiddleRight.__doc__ + '\n' + '* ``BottomLeft``: ' + Qgis.LabelPredefinedPointPosition.BottomLeft.__doc__ + '\n' + '* ``BottomSlightlyLeft``: ' + Qgis.LabelPredefinedPointPosition.BottomSlightlyLeft.__doc__ + '\n' + '* ``BottomMiddle``: ' + Qgis.LabelPredefinedPointPosition.BottomMiddle.__doc__ + '\n' + '* ``BottomSlightlyRight``: ' + Qgis.LabelPredefinedPointPosition.BottomSlightlyRight.__doc__ + '\n' + '* ``BottomRight``: ' + Qgis.LabelPredefinedPointPosition.BottomRight.__doc__
# --
Qgis.LabelPredefinedPointPosition.baseClass = Qgis
QgsPalLayerSettings.OffsetType = Qgis.LabelOffsetType
# monkey patching scoped based enum
QgsPalLayerSettings.FromPoint = Qgis.LabelOffsetType.FromPoint
QgsPalLayerSettings.FromPoint.is_monkey_patched = True
QgsPalLayerSettings.FromPoint.__doc__ = "Offset distance applies from point geometry"
QgsPalLayerSettings.FromSymbolBounds = Qgis.LabelOffsetType.FromSymbolBounds
QgsPalLayerSettings.FromSymbolBounds.is_monkey_patched = True
QgsPalLayerSettings.FromSymbolBounds.__doc__ = "Offset distance applies from rendered symbol bounds"
Qgis.LabelOffsetType.__doc__ = 'Behavior modifier for label offset and distance, only applies in some\nlabel placement modes.\n\n.. note::\n\n   Prior to QGIS 3.26 this was available as :py:class:`QgsPalLayerSettings`.OffsetType\n\n.. versionadded:: 3.26\n\n' + '* ``FromPoint``: ' + Qgis.LabelOffsetType.FromPoint.__doc__ + '\n' + '* ``FromSymbolBounds``: ' + Qgis.LabelOffsetType.FromSymbolBounds.__doc__
# --
Qgis.LabelOffsetType.baseClass = Qgis
QgsPalLayerSettings.QuadrantPosition = Qgis.LabelQuadrantPosition
# monkey patching scoped based enum
QgsPalLayerSettings.QuadrantAboveLeft = Qgis.LabelQuadrantPosition.AboveLeft
QgsPalLayerSettings.QuadrantAboveLeft.is_monkey_patched = True
QgsPalLayerSettings.QuadrantAboveLeft.__doc__ = "Above left"
QgsPalLayerSettings.QuadrantAbove = Qgis.LabelQuadrantPosition.Above
QgsPalLayerSettings.QuadrantAbove.is_monkey_patched = True
QgsPalLayerSettings.QuadrantAbove.__doc__ = "Above center"
QgsPalLayerSettings.QuadrantAboveRight = Qgis.LabelQuadrantPosition.AboveRight
QgsPalLayerSettings.QuadrantAboveRight.is_monkey_patched = True
QgsPalLayerSettings.QuadrantAboveRight.__doc__ = "Above right"
QgsPalLayerSettings.QuadrantLeft = Qgis.LabelQuadrantPosition.Left
QgsPalLayerSettings.QuadrantLeft.is_monkey_patched = True
QgsPalLayerSettings.QuadrantLeft.__doc__ = "Left middle"
QgsPalLayerSettings.QuadrantOver = Qgis.LabelQuadrantPosition.Over
QgsPalLayerSettings.QuadrantOver.is_monkey_patched = True
QgsPalLayerSettings.QuadrantOver.__doc__ = "Center middle"
QgsPalLayerSettings.QuadrantRight = Qgis.LabelQuadrantPosition.Right
QgsPalLayerSettings.QuadrantRight.is_monkey_patched = True
QgsPalLayerSettings.QuadrantRight.__doc__ = "Right middle"
QgsPalLayerSettings.QuadrantBelowLeft = Qgis.LabelQuadrantPosition.BelowLeft
QgsPalLayerSettings.QuadrantBelowLeft.is_monkey_patched = True
QgsPalLayerSettings.QuadrantBelowLeft.__doc__ = "Below left"
QgsPalLayerSettings.QuadrantBelow = Qgis.LabelQuadrantPosition.Below
QgsPalLayerSettings.QuadrantBelow.is_monkey_patched = True
QgsPalLayerSettings.QuadrantBelow.__doc__ = "Below center"
QgsPalLayerSettings.QuadrantBelowRight = Qgis.LabelQuadrantPosition.BelowRight
QgsPalLayerSettings.QuadrantBelowRight.is_monkey_patched = True
QgsPalLayerSettings.QuadrantBelowRight.__doc__ = "BelowRight"
Qgis.LabelQuadrantPosition.__doc__ = 'Label quadrant positions\n\n.. note::\n\n   Prior to QGIS 3.26 this was available as :py:class:`QgsPalLayerSettings`.QuadrantPosition\n\n.. versionadded:: 3.26\n\n' + '* ``QuadrantAboveLeft``: ' + Qgis.LabelQuadrantPosition.AboveLeft.__doc__ + '\n' + '* ``QuadrantAbove``: ' + Qgis.LabelQuadrantPosition.Above.__doc__ + '\n' + '* ``QuadrantAboveRight``: ' + Qgis.LabelQuadrantPosition.AboveRight.__doc__ + '\n' + '* ``QuadrantLeft``: ' + Qgis.LabelQuadrantPosition.Left.__doc__ + '\n' + '* ``QuadrantOver``: ' + Qgis.LabelQuadrantPosition.Over.__doc__ + '\n' + '* ``QuadrantRight``: ' + Qgis.LabelQuadrantPosition.Right.__doc__ + '\n' + '* ``QuadrantBelowLeft``: ' + Qgis.LabelQuadrantPosition.BelowLeft.__doc__ + '\n' + '* ``QuadrantBelow``: ' + Qgis.LabelQuadrantPosition.Below.__doc__ + '\n' + '* ``QuadrantBelowRight``: ' + Qgis.LabelQuadrantPosition.BelowRight.__doc__
# --
Qgis.LabelQuadrantPosition.baseClass = Qgis
QgsPalLayerSettings.UpsideDownLabels = Qgis.UpsideDownLabelHandling
# monkey patching scoped based enum
QgsPalLayerSettings.Upright = Qgis.UpsideDownLabelHandling.FlipUpsideDownLabels
QgsPalLayerSettings.Upright.is_monkey_patched = True
QgsPalLayerSettings.Upright.__doc__ = "Upside-down labels (90 <= angle < 270) are shown upright"
QgsPalLayerSettings.ShowDefined = Qgis.UpsideDownLabelHandling.AllowUpsideDownWhenRotationIsDefined
QgsPalLayerSettings.ShowDefined.is_monkey_patched = True
QgsPalLayerSettings.ShowDefined.__doc__ = "Show upside down when rotation is layer- or data-defined"
QgsPalLayerSettings.ShowAll = Qgis.UpsideDownLabelHandling.AlwaysAllowUpsideDown
QgsPalLayerSettings.ShowAll.is_monkey_patched = True
QgsPalLayerSettings.ShowAll.__doc__ = "Show upside down for all labels, including dynamic ones"
Qgis.UpsideDownLabelHandling.__doc__ = 'Handling techniques for upside down labels.\n\n.. note::\n\n   Prior to QGIS 3.26 this was available as :py:class:`QgsPalLayerSettings`.UpsideDownLabels\n\n.. versionadded:: 3.26\n\n' + '* ``Upright``: ' + Qgis.UpsideDownLabelHandling.FlipUpsideDownLabels.__doc__ + '\n' + '* ``ShowDefined``: ' + Qgis.UpsideDownLabelHandling.AllowUpsideDownWhenRotationIsDefined.__doc__ + '\n' + '* ``ShowAll``: ' + Qgis.UpsideDownLabelHandling.AlwaysAllowUpsideDown.__doc__
# --
Qgis.UpsideDownLabelHandling.baseClass = Qgis
QgsPalLayerSettings.MultiLineAlign = Qgis.LabelMultiLineAlignment
# monkey patching scoped based enum
QgsPalLayerSettings.MultiLeft = Qgis.LabelMultiLineAlignment.Left
QgsPalLayerSettings.MultiLeft.is_monkey_patched = True
QgsPalLayerSettings.MultiLeft.__doc__ = "Left align"
QgsPalLayerSettings.MultiCenter = Qgis.LabelMultiLineAlignment.Center
QgsPalLayerSettings.MultiCenter.is_monkey_patched = True
QgsPalLayerSettings.MultiCenter.__doc__ = "Center align"
QgsPalLayerSettings.MultiRight = Qgis.LabelMultiLineAlignment.Right
QgsPalLayerSettings.MultiRight.is_monkey_patched = True
QgsPalLayerSettings.MultiRight.__doc__ = "Right align"
QgsPalLayerSettings.MultiFollowPlacement = Qgis.LabelMultiLineAlignment.FollowPlacement
QgsPalLayerSettings.MultiFollowPlacement.is_monkey_patched = True
QgsPalLayerSettings.MultiFollowPlacement.__doc__ = "Alignment follows placement of label, e.g., labels to the left of a feature will be drawn with right alignment"
QgsPalLayerSettings.MultiJustify = Qgis.LabelMultiLineAlignment.Justify
QgsPalLayerSettings.MultiJustify.is_monkey_patched = True
QgsPalLayerSettings.MultiJustify.__doc__ = "Justified"
Qgis.LabelMultiLineAlignment.__doc__ = 'Text alignment for multi-line labels.\n\n.. note::\n\n   Prior to QGIS 3.26 this was available as :py:class:`QgsPalLayerSettings`.MultiLineAlign\n\n.. versionadded:: 3.26\n\n' + '* ``MultiLeft``: ' + Qgis.LabelMultiLineAlignment.Left.__doc__ + '\n' + '* ``MultiCenter``: ' + Qgis.LabelMultiLineAlignment.Center.__doc__ + '\n' + '* ``MultiRight``: ' + Qgis.LabelMultiLineAlignment.Right.__doc__ + '\n' + '* ``MultiFollowPlacement``: ' + Qgis.LabelMultiLineAlignment.FollowPlacement.__doc__ + '\n' + '* ``MultiJustify``: ' + Qgis.LabelMultiLineAlignment.Justify.__doc__
# --
Qgis.LabelMultiLineAlignment.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SublayerQueryFlag.FastScan.__doc__ = "Indicates that the provider must scan for sublayers using the fastest possible approach -- e.g. by first checking that a uri has an extension which is known to be readable by the provider"
Qgis.SublayerQueryFlag.ResolveGeometryType.__doc__ = "Attempt to resolve the geometry type for vector sublayers"
Qgis.SublayerQueryFlag.CountFeatures.__doc__ = "Count features in vector sublayers"
Qgis.SublayerQueryFlag.IncludeSystemTables.__doc__ = "Include system or internal tables (these are not included by default)"
Qgis.SublayerQueryFlag.__doc__ = 'Flags which control how data providers will scan for sublayers in a dataset.\n\n.. versionadded:: 3.22\n\n' + '* ``FastScan``: ' + Qgis.SublayerQueryFlag.FastScan.__doc__ + '\n' + '* ``ResolveGeometryType``: ' + Qgis.SublayerQueryFlag.ResolveGeometryType.__doc__ + '\n' + '* ``CountFeatures``: ' + Qgis.SublayerQueryFlag.CountFeatures.__doc__ + '\n' + '* ``IncludeSystemTables``: ' + Qgis.SublayerQueryFlag.IncludeSystemTables.__doc__
# --
Qgis.SublayerQueryFlag.baseClass = Qgis
Qgis.SublayerQueryFlags.baseClass = Qgis
SublayerQueryFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.SublayerFlag.SystemTable.__doc__ = "Sublayer is a system or internal table, which should be hidden by default"
Qgis.SublayerFlag.__doc__ = 'Flags which reflect the properties of sublayers in a dataset.\n\n.. versionadded:: 3.22\n\n' + '* ``SystemTable``: ' + Qgis.SublayerFlag.SystemTable.__doc__
# --
Qgis.SublayerFlag.baseClass = Qgis
Qgis.SublayerFlags.baseClass = Qgis
SublayerFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
QgsRasterPipe.Role = Qgis.RasterPipeInterfaceRole
# monkey patching scoped based enum
QgsRasterPipe.UnknownRole = Qgis.RasterPipeInterfaceRole.Unknown
QgsRasterPipe.UnknownRole.is_monkey_patched = True
QgsRasterPipe.UnknownRole.__doc__ = "Unknown role"
QgsRasterPipe.ProviderRole = Qgis.RasterPipeInterfaceRole.Provider
QgsRasterPipe.ProviderRole.is_monkey_patched = True
QgsRasterPipe.ProviderRole.__doc__ = "Data provider role"
QgsRasterPipe.RendererRole = Qgis.RasterPipeInterfaceRole.Renderer
QgsRasterPipe.RendererRole.is_monkey_patched = True
QgsRasterPipe.RendererRole.__doc__ = "Raster renderer role"
QgsRasterPipe.BrightnessRole = Qgis.RasterPipeInterfaceRole.Brightness
QgsRasterPipe.BrightnessRole.is_monkey_patched = True
QgsRasterPipe.BrightnessRole.__doc__ = "Brightness filter role"
QgsRasterPipe.ResamplerRole = Qgis.RasterPipeInterfaceRole.Resampler
QgsRasterPipe.ResamplerRole.is_monkey_patched = True
QgsRasterPipe.ResamplerRole.__doc__ = "Resampler role"
QgsRasterPipe.ProjectorRole = Qgis.RasterPipeInterfaceRole.Projector
QgsRasterPipe.ProjectorRole.is_monkey_patched = True
QgsRasterPipe.ProjectorRole.__doc__ = "Projector role"
QgsRasterPipe.NullerRole = Qgis.RasterPipeInterfaceRole.Nuller
QgsRasterPipe.NullerRole.is_monkey_patched = True
QgsRasterPipe.NullerRole.__doc__ = "Raster nuller role"
QgsRasterPipe.HueSaturationRole = Qgis.RasterPipeInterfaceRole.HueSaturation
QgsRasterPipe.HueSaturationRole.is_monkey_patched = True
QgsRasterPipe.HueSaturationRole.__doc__ = "Hue/saturation filter role (also applies grayscale/color inversion)"
Qgis.RasterPipeInterfaceRole.__doc__ = 'Raster pipe interface roles.\n\n.. versionadded:: 3.22\n\n' + '* ``UnknownRole``: ' + Qgis.RasterPipeInterfaceRole.Unknown.__doc__ + '\n' + '* ``ProviderRole``: ' + Qgis.RasterPipeInterfaceRole.Provider.__doc__ + '\n' + '* ``RendererRole``: ' + Qgis.RasterPipeInterfaceRole.Renderer.__doc__ + '\n' + '* ``BrightnessRole``: ' + Qgis.RasterPipeInterfaceRole.Brightness.__doc__ + '\n' + '* ``ResamplerRole``: ' + Qgis.RasterPipeInterfaceRole.Resampler.__doc__ + '\n' + '* ``ProjectorRole``: ' + Qgis.RasterPipeInterfaceRole.Projector.__doc__ + '\n' + '* ``NullerRole``: ' + Qgis.RasterPipeInterfaceRole.Nuller.__doc__ + '\n' + '* ``HueSaturationRole``: ' + Qgis.RasterPipeInterfaceRole.HueSaturation.__doc__
# --
Qgis.RasterPipeInterfaceRole.baseClass = Qgis
QgsRasterPipe.ResamplingStage = Qgis.RasterResamplingStage
# monkey patching scoped based enum
QgsRasterPipe.ResampleFilter = Qgis.RasterResamplingStage.ResampleFilter
QgsRasterPipe.ResampleFilter.is_monkey_patched = True
QgsRasterPipe.ResampleFilter.__doc__ = ""
QgsRasterPipe.Provider = Qgis.RasterResamplingStage.Provider
QgsRasterPipe.Provider.is_monkey_patched = True
QgsRasterPipe.Provider.__doc__ = ""
Qgis.RasterResamplingStage.__doc__ = 'Stage at which raster resampling occurs.\n\n.. versionadded:: 3.22\n\n' + '* ``ResampleFilter``: ' + Qgis.RasterResamplingStage.ResampleFilter.__doc__ + '\n' + '* ``Provider``: ' + Qgis.RasterResamplingStage.Provider.__doc__
# --
Qgis.RasterResamplingStage.baseClass = Qgis
# monkey patching scoped based enum
Qgis.MeshEditingErrorType.NoError.__doc__ = "No type"
Qgis.MeshEditingErrorType.InvalidFace.__doc__ = "An error occurs due to an invalid face (for example, vertex indexes are unordered)"
Qgis.MeshEditingErrorType.TooManyVerticesInFace.__doc__ = "A face has more vertices than the maximum number supported per face"
Qgis.MeshEditingErrorType.FlatFace.__doc__ = "A flat face is present"
Qgis.MeshEditingErrorType.UniqueSharedVertex.__doc__ = "A least two faces share only one vertices"
Qgis.MeshEditingErrorType.InvalidVertex.__doc__ = "An error occurs due to an invalid vertex (for example, vertex index is out of range the available vertex)"
Qgis.MeshEditingErrorType.ManifoldFace.__doc__ = "ManifoldFace"
Qgis.MeshEditingErrorType.__doc__ = 'Type of error that can occur during mesh frame editing.\n\n.. versionadded:: 3.22\n\n' + '* ``NoError``: ' + Qgis.MeshEditingErrorType.NoError.__doc__ + '\n' + '* ``InvalidFace``: ' + Qgis.MeshEditingErrorType.InvalidFace.__doc__ + '\n' + '* ``TooManyVerticesInFace``: ' + Qgis.MeshEditingErrorType.TooManyVerticesInFace.__doc__ + '\n' + '* ``FlatFace``: ' + Qgis.MeshEditingErrorType.FlatFace.__doc__ + '\n' + '* ``UniqueSharedVertex``: ' + Qgis.MeshEditingErrorType.UniqueSharedVertex.__doc__ + '\n' + '* ``InvalidVertex``: ' + Qgis.MeshEditingErrorType.InvalidVertex.__doc__ + '\n' + '* ``ManifoldFace``: ' + Qgis.MeshEditingErrorType.ManifoldFace.__doc__
# --
Qgis.MeshEditingErrorType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.FilePathType.Absolute.__doc__ = "Absolute path"
Qgis.FilePathType.Relative.__doc__ = "Relative path"
Qgis.FilePathType.__doc__ = 'File path types.\n\n.. versionadded:: 3.22\n\n' + '* ``Absolute``: ' + Qgis.FilePathType.Absolute.__doc__ + '\n' + '* ``Relative``: ' + Qgis.FilePathType.Relative.__doc__
# --
Qgis.FilePathType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SublayerPromptMode.AlwaysAsk.__doc__ = "Always ask users to select from available sublayers, if sublayers are present"
Qgis.SublayerPromptMode.AskExcludingRasterBands.__doc__ = "Ask users to select from available sublayers, unless only raster bands are present"
Qgis.SublayerPromptMode.NeverAskSkip.__doc__ = "Never ask users to select sublayers, instead don't load anything"
Qgis.SublayerPromptMode.NeverAskLoadAll.__doc__ = "Never ask users to select sublayers, instead automatically load all available sublayers"
Qgis.SublayerPromptMode.__doc__ = 'Specifies how to handle layer sources with multiple sublayers.\n\n.. versionadded:: 3.22\n\n' + '* ``AlwaysAsk``: ' + Qgis.SublayerPromptMode.AlwaysAsk.__doc__ + '\n' + '* ``AskExcludingRasterBands``: ' + Qgis.SublayerPromptMode.AskExcludingRasterBands.__doc__ + '\n' + '* ``NeverAskSkip``: ' + Qgis.SublayerPromptMode.NeverAskSkip.__doc__ + '\n' + '* ``NeverAskLoadAll``: ' + Qgis.SublayerPromptMode.NeverAskLoadAll.__doc__
# --
Qgis.SublayerPromptMode.baseClass = Qgis
QgsVectorLayer.SelectBehavior = Qgis.SelectBehavior
# monkey patching scoped based enum
QgsVectorLayer.SetSelection = Qgis.SelectBehavior.SetSelection
QgsVectorLayer.SetSelection.is_monkey_patched = True
QgsVectorLayer.SetSelection.__doc__ = "Set selection, removing any existing selection"
QgsVectorLayer.AddToSelection = Qgis.SelectBehavior.AddToSelection
QgsVectorLayer.AddToSelection.is_monkey_patched = True
QgsVectorLayer.AddToSelection.__doc__ = "Add selection to current selection"
QgsVectorLayer.IntersectSelection = Qgis.SelectBehavior.IntersectSelection
QgsVectorLayer.IntersectSelection.is_monkey_patched = True
QgsVectorLayer.IntersectSelection.__doc__ = "Modify current selection to include only select features which match"
QgsVectorLayer.RemoveFromSelection = Qgis.SelectBehavior.RemoveFromSelection
QgsVectorLayer.RemoveFromSelection.is_monkey_patched = True
QgsVectorLayer.RemoveFromSelection.__doc__ = "Remove from current selection"
Qgis.SelectBehavior.__doc__ = 'Specifies how a selection should be applied.\n\n.. versionadded:: 3.22\n\n' + '* ``SetSelection``: ' + Qgis.SelectBehavior.SetSelection.__doc__ + '\n' + '* ``AddToSelection``: ' + Qgis.SelectBehavior.AddToSelection.__doc__ + '\n' + '* ``IntersectSelection``: ' + Qgis.SelectBehavior.IntersectSelection.__doc__ + '\n' + '* ``RemoveFromSelection``: ' + Qgis.SelectBehavior.RemoveFromSelection.__doc__
# --
Qgis.SelectBehavior.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SelectGeometryRelationship.Intersect.__doc__ = "Select where features intersect the reference geometry"
Qgis.SelectGeometryRelationship.Within.__doc__ = "Select where features are within the reference geometry"
Qgis.SelectGeometryRelationship.__doc__ = 'Geometry relationship test to apply for selecting features.\n\n.. versionadded:: 3.28\n\n' + '* ``Intersect``: ' + Qgis.SelectGeometryRelationship.Intersect.__doc__ + '\n' + '* ``Within``: ' + Qgis.SelectGeometryRelationship.Within.__doc__
# --
Qgis.SelectGeometryRelationship.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SelectionFlag.SingleFeatureSelection.__doc__ = "Select only a single feature, picking the \"best\" match for the selection geometry"
Qgis.SelectionFlag.ToggleSelection.__doc__ = "Enables a \"toggle\" selection mode, where previously selected matching features will be deselected and previously deselected features will be selected. This flag works only when the SingleFeatureSelection flag is also set."
Qgis.SelectionFlag.__doc__ = 'Flags which control feature selection behavior.\n\n.. versionadded:: 3.28\n\n' + '* ``SingleFeatureSelection``: ' + Qgis.SelectionFlag.SingleFeatureSelection.__doc__ + '\n' + '* ``ToggleSelection``: ' + Qgis.SelectionFlag.ToggleSelection.__doc__
# --
Qgis.SelectionFlag.baseClass = Qgis
Qgis.SelectionFlags.baseClass = Qgis
SelectionFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
QgsVectorLayer.EditResult = Qgis.VectorEditResult
# monkey patching scoped based enum
QgsVectorLayer.Success = Qgis.VectorEditResult.Success
QgsVectorLayer.Success.is_monkey_patched = True
QgsVectorLayer.Success.__doc__ = "Edit operation was successful"
QgsVectorLayer.EmptyGeometry = Qgis.VectorEditResult.EmptyGeometry
QgsVectorLayer.EmptyGeometry.is_monkey_patched = True
QgsVectorLayer.EmptyGeometry.__doc__ = "Edit operation resulted in an empty geometry"
QgsVectorLayer.EditFailed = Qgis.VectorEditResult.EditFailed
QgsVectorLayer.EditFailed.is_monkey_patched = True
QgsVectorLayer.EditFailed.__doc__ = "Edit operation failed"
QgsVectorLayer.FetchFeatureFailed = Qgis.VectorEditResult.FetchFeatureFailed
QgsVectorLayer.FetchFeatureFailed.is_monkey_patched = True
QgsVectorLayer.FetchFeatureFailed.__doc__ = "Unable to fetch requested feature"
QgsVectorLayer.InvalidLayer = Qgis.VectorEditResult.InvalidLayer
QgsVectorLayer.InvalidLayer.is_monkey_patched = True
QgsVectorLayer.InvalidLayer.__doc__ = "Edit failed due to invalid layer"
Qgis.VectorEditResult.__doc__ = 'Specifies the result of a vector layer edit operation\n\n.. versionadded:: 3.22\n\n' + '* ``Success``: ' + Qgis.VectorEditResult.Success.__doc__ + '\n' + '* ``EmptyGeometry``: ' + Qgis.VectorEditResult.EmptyGeometry.__doc__ + '\n' + '* ``EditFailed``: ' + Qgis.VectorEditResult.EditFailed.__doc__ + '\n' + '* ``FetchFeatureFailed``: ' + Qgis.VectorEditResult.FetchFeatureFailed.__doc__ + '\n' + '* ``InvalidLayer``: ' + Qgis.VectorEditResult.InvalidLayer.__doc__
# --
Qgis.VectorEditResult.baseClass = Qgis
QgsSymbolLayerUtils.VertexMarkerType = Qgis.VertexMarkerType
# monkey patching scoped based enum
QgsSymbolLayerUtils.SemiTransparentCircle = Qgis.VertexMarkerType.SemiTransparentCircle
QgsSymbolLayerUtils.SemiTransparentCircle.is_monkey_patched = True
QgsSymbolLayerUtils.SemiTransparentCircle.__doc__ = "Semi-transparent circle marker"
QgsSymbolLayerUtils.Cross = Qgis.VertexMarkerType.Cross
QgsSymbolLayerUtils.Cross.is_monkey_patched = True
QgsSymbolLayerUtils.Cross.__doc__ = "Cross marker"
QgsSymbolLayerUtils.NoMarker = Qgis.VertexMarkerType.NoMarker
QgsSymbolLayerUtils.NoMarker.is_monkey_patched = True
QgsSymbolLayerUtils.NoMarker.__doc__ = "No marker"
Qgis.VertexMarkerType.__doc__ = 'Editing vertex markers, used for showing vertices during a edit operation.\n\n.. versionadded:: 3.22\n\n' + '* ``SemiTransparentCircle``: ' + Qgis.VertexMarkerType.SemiTransparentCircle.__doc__ + '\n' + '* ``Cross``: ' + Qgis.VertexMarkerType.Cross.__doc__ + '\n' + '* ``NoMarker``: ' + Qgis.VertexMarkerType.NoMarker.__doc__
# --
Qgis.VertexMarkerType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.ContentStatus.NotStarted.__doc__ = "Content fetching/storing has not started yet"
Qgis.ContentStatus.Running.__doc__ = "Content fetching/storing is in progress"
Qgis.ContentStatus.Finished.__doc__ = "Content fetching/storing is finished and successful"
Qgis.ContentStatus.Failed.__doc__ = "Content fetching/storing has failed"
Qgis.ContentStatus.Canceled.__doc__ = "Content fetching/storing has been canceled"
Qgis.ContentStatus.__doc__ = 'Status for fetched or stored content\n\n.. versionadded:: 3.22\n\n' + '* ``NotStarted``: ' + Qgis.ContentStatus.NotStarted.__doc__ + '\n' + '* ``Running``: ' + Qgis.ContentStatus.Running.__doc__ + '\n' + '* ``Finished``: ' + Qgis.ContentStatus.Finished.__doc__ + '\n' + '* ``Failed``: ' + Qgis.ContentStatus.Failed.__doc__ + '\n' + '* ``Canceled``: ' + Qgis.ContentStatus.Canceled.__doc__
# --
Qgis.ContentStatus.baseClass = Qgis
# monkey patching scoped based enum
Qgis.GpsQualityIndicator.Unknown.__doc__ = "Unknown"
Qgis.GpsQualityIndicator.Invalid.__doc__ = "Invalid"
Qgis.GpsQualityIndicator.GPS.__doc__ = "Standalone"
Qgis.GpsQualityIndicator.DGPS.__doc__ = "Differential GPS"
Qgis.GpsQualityIndicator.PPS.__doc__ = "PPS"
Qgis.GpsQualityIndicator.RTK.__doc__ = "Real-time-kynematic"
Qgis.GpsQualityIndicator.FloatRTK.__doc__ = "Float real-time-kynematic"
Qgis.GpsQualityIndicator.Estimated.__doc__ = "Estimated"
Qgis.GpsQualityIndicator.Manual.__doc__ = "Manual input mode"
Qgis.GpsQualityIndicator.Simulation.__doc__ = "Simulation mode"
Qgis.GpsQualityIndicator.__doc__ = 'GPS signal quality indicator\n\n.. versionadded:: 3.22.6\n\n' + '* ``Unknown``: ' + Qgis.GpsQualityIndicator.Unknown.__doc__ + '\n' + '* ``Invalid``: ' + Qgis.GpsQualityIndicator.Invalid.__doc__ + '\n' + '* ``GPS``: ' + Qgis.GpsQualityIndicator.GPS.__doc__ + '\n' + '* ``DGPS``: ' + Qgis.GpsQualityIndicator.DGPS.__doc__ + '\n' + '* ``PPS``: ' + Qgis.GpsQualityIndicator.PPS.__doc__ + '\n' + '* ``RTK``: ' + Qgis.GpsQualityIndicator.RTK.__doc__ + '\n' + '* ``FloatRTK``: ' + Qgis.GpsQualityIndicator.FloatRTK.__doc__ + '\n' + '* ``Estimated``: ' + Qgis.GpsQualityIndicator.Estimated.__doc__ + '\n' + '* ``Manual``: ' + Qgis.GpsQualityIndicator.Manual.__doc__ + '\n' + '* ``Simulation``: ' + Qgis.GpsQualityIndicator.Simulation.__doc__
# --
Qgis.GpsQualityIndicator.baseClass = Qgis
# monkey patching scoped based enum
Qgis.BabelFormatCapability.Import.__doc__ = "Format supports importing"
Qgis.BabelFormatCapability.Export.__doc__ = "Format supports exporting"
Qgis.BabelFormatCapability.Waypoints.__doc__ = "Format supports waypoints"
Qgis.BabelFormatCapability.Routes.__doc__ = "Format supports routes"
Qgis.BabelFormatCapability.Tracks.__doc__ = "Format supports tracks"
Qgis.BabelFormatCapability.__doc__ = 'Babel GPS format capabilities.\n\n.. versionadded:: 3.22\n\n' + '* ``Import``: ' + Qgis.BabelFormatCapability.Import.__doc__ + '\n' + '* ``Export``: ' + Qgis.BabelFormatCapability.Export.__doc__ + '\n' + '* ``Waypoints``: ' + Qgis.BabelFormatCapability.Waypoints.__doc__ + '\n' + '* ``Routes``: ' + Qgis.BabelFormatCapability.Routes.__doc__ + '\n' + '* ``Tracks``: ' + Qgis.BabelFormatCapability.Tracks.__doc__
# --
Qgis.BabelFormatCapability.baseClass = Qgis
Qgis.BabelFormatCapabilities.baseClass = Qgis
BabelFormatCapabilities = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.BabelCommandFlag.QuoteFilePaths.__doc__ = "File paths should be enclosed in quotations and escaped"
Qgis.BabelCommandFlag.__doc__ = 'Babel command flags, which control how commands and arguments\nare generated for executing GPSBabel processes.\n\n.. versionadded:: 3.22\n\n' + '* ``QuoteFilePaths``: ' + Qgis.BabelCommandFlag.QuoteFilePaths.__doc__
# --
Qgis.BabelCommandFlag.baseClass = Qgis
Qgis.BabelCommandFlags.baseClass = Qgis
BabelCommandFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.GpsFeatureType.Waypoint.__doc__ = "Waypoint"
Qgis.GpsFeatureType.Route.__doc__ = "Route"
Qgis.GpsFeatureType.Track.__doc__ = "Track"
Qgis.GpsFeatureType.__doc__ = 'GPS feature types.\n\n.. versionadded:: 3.22\n\n' + '* ``Waypoint``: ' + Qgis.GpsFeatureType.Waypoint.__doc__ + '\n' + '* ``Route``: ' + Qgis.GpsFeatureType.Route.__doc__ + '\n' + '* ``Track``: ' + Qgis.GpsFeatureType.Track.__doc__
# --
Qgis.GpsFeatureType.baseClass = Qgis
QgsGeometry.OperationResult = Qgis.GeometryOperationResult
# monkey patching scoped based enum
QgsGeometry.Success = Qgis.GeometryOperationResult.Success
QgsGeometry.Success.is_monkey_patched = True
QgsGeometry.Success.__doc__ = "Operation succeeded"
QgsGeometry.NothingHappened = Qgis.GeometryOperationResult.NothingHappened
QgsGeometry.NothingHappened.is_monkey_patched = True
QgsGeometry.NothingHappened.__doc__ = "Nothing happened, without any error"
QgsGeometry.InvalidBaseGeometry = Qgis.GeometryOperationResult.InvalidBaseGeometry
QgsGeometry.InvalidBaseGeometry.is_monkey_patched = True
QgsGeometry.InvalidBaseGeometry.__doc__ = "The base geometry on which the operation is done is invalid or empty"
QgsGeometry.InvalidInputGeometryType = Qgis.GeometryOperationResult.InvalidInputGeometryType
QgsGeometry.InvalidInputGeometryType.is_monkey_patched = True
QgsGeometry.InvalidInputGeometryType.__doc__ = "The input geometry (ring, part, split line, etc.) has not the correct geometry type"
QgsGeometry.SelectionIsEmpty = Qgis.GeometryOperationResult.SelectionIsEmpty
QgsGeometry.SelectionIsEmpty.is_monkey_patched = True
QgsGeometry.SelectionIsEmpty.__doc__ = "No features were selected"
QgsGeometry.SelectionIsGreaterThanOne = Qgis.GeometryOperationResult.SelectionIsGreaterThanOne
QgsGeometry.SelectionIsGreaterThanOne.is_monkey_patched = True
QgsGeometry.SelectionIsGreaterThanOne.__doc__ = "More than one features were selected"
QgsGeometry.GeometryEngineError = Qgis.GeometryOperationResult.GeometryEngineError
QgsGeometry.GeometryEngineError.is_monkey_patched = True
QgsGeometry.GeometryEngineError.__doc__ = "Geometry engine misses a method implemented or an error occurred in the geometry engine"
QgsGeometry.LayerNotEditable = Qgis.GeometryOperationResult.LayerNotEditable
QgsGeometry.LayerNotEditable.is_monkey_patched = True
QgsGeometry.LayerNotEditable.__doc__ = "Cannot edit layer"
QgsGeometry.AddPartSelectedGeometryNotFound = Qgis.GeometryOperationResult.AddPartSelectedGeometryNotFound
QgsGeometry.AddPartSelectedGeometryNotFound.is_monkey_patched = True
QgsGeometry.AddPartSelectedGeometryNotFound.__doc__ = "The selected geometry cannot be found"
QgsGeometry.AddPartNotMultiGeometry = Qgis.GeometryOperationResult.AddPartNotMultiGeometry
QgsGeometry.AddPartNotMultiGeometry.is_monkey_patched = True
QgsGeometry.AddPartNotMultiGeometry.__doc__ = "The source geometry is not multi"
QgsGeometry.AddRingNotClosed = Qgis.GeometryOperationResult.AddRingNotClosed
QgsGeometry.AddRingNotClosed.is_monkey_patched = True
QgsGeometry.AddRingNotClosed.__doc__ = "The input ring is not closed"
QgsGeometry.AddRingNotValid = Qgis.GeometryOperationResult.AddRingNotValid
QgsGeometry.AddRingNotValid.is_monkey_patched = True
QgsGeometry.AddRingNotValid.__doc__ = "The input ring is not valid"
QgsGeometry.AddRingCrossesExistingRings = Qgis.GeometryOperationResult.AddRingCrossesExistingRings
QgsGeometry.AddRingCrossesExistingRings.is_monkey_patched = True
QgsGeometry.AddRingCrossesExistingRings.__doc__ = "The input ring crosses existing rings (it is not disjoint)"
QgsGeometry.AddRingNotInExistingFeature = Qgis.GeometryOperationResult.AddRingNotInExistingFeature
QgsGeometry.AddRingNotInExistingFeature.is_monkey_patched = True
QgsGeometry.AddRingNotInExistingFeature.__doc__ = "The input ring doesn't have any existing ring to fit into"
QgsGeometry.SplitCannotSplitPoint = Qgis.GeometryOperationResult.SplitCannotSplitPoint
QgsGeometry.SplitCannotSplitPoint.is_monkey_patched = True
QgsGeometry.SplitCannotSplitPoint.__doc__ = "Cannot split points"
Qgis.GeometryOperationResult.__doc__ = 'Split features */\n\n' + '* ``Success``: ' + Qgis.GeometryOperationResult.Success.__doc__ + '\n' + '* ``NothingHappened``: ' + Qgis.GeometryOperationResult.NothingHappened.__doc__ + '\n' + '* ``InvalidBaseGeometry``: ' + Qgis.GeometryOperationResult.InvalidBaseGeometry.__doc__ + '\n' + '* ``InvalidInputGeometryType``: ' + Qgis.GeometryOperationResult.InvalidInputGeometryType.__doc__ + '\n' + '* ``SelectionIsEmpty``: ' + Qgis.GeometryOperationResult.SelectionIsEmpty.__doc__ + '\n' + '* ``SelectionIsGreaterThanOne``: ' + Qgis.GeometryOperationResult.SelectionIsGreaterThanOne.__doc__ + '\n' + '* ``GeometryEngineError``: ' + Qgis.GeometryOperationResult.GeometryEngineError.__doc__ + '\n' + '* ``LayerNotEditable``: ' + Qgis.GeometryOperationResult.LayerNotEditable.__doc__ + '\n' + '* ``AddPartSelectedGeometryNotFound``: ' + Qgis.GeometryOperationResult.AddPartSelectedGeometryNotFound.__doc__ + '\n' + '* ``AddPartNotMultiGeometry``: ' + Qgis.GeometryOperationResult.AddPartNotMultiGeometry.__doc__ + '\n' + '* ``AddRingNotClosed``: ' + Qgis.GeometryOperationResult.AddRingNotClosed.__doc__ + '\n' + '* ``AddRingNotValid``: ' + Qgis.GeometryOperationResult.AddRingNotValid.__doc__ + '\n' + '* ``AddRingCrossesExistingRings``: ' + Qgis.GeometryOperationResult.AddRingCrossesExistingRings.__doc__ + '\n' + '* ``AddRingNotInExistingFeature``: ' + Qgis.GeometryOperationResult.AddRingNotInExistingFeature.__doc__ + '\n' + '* ``SplitCannotSplitPoint``: ' + Qgis.GeometryOperationResult.SplitCannotSplitPoint.__doc__
# --
Qgis.GeometryOperationResult.baseClass = Qgis
QgsGeometry.ValidityFlag = Qgis.GeometryValidityFlag
# monkey patching scoped based enum
QgsGeometry.FlagAllowSelfTouchingHoles = Qgis.GeometryValidityFlag.AllowSelfTouchingHoles
QgsGeometry.FlagAllowSelfTouchingHoles.is_monkey_patched = True
QgsGeometry.FlagAllowSelfTouchingHoles.__doc__ = "Indicates that self-touching holes are permitted. OGC validity states that self-touching holes are NOT permitted, whilst other vendor validity checks (e.g. ESRI) permit self-touching holes."
Qgis.GeometryValidityFlag.__doc__ = 'Geometry validity check flags.\n\n.. versionadded:: 3.22\n\n' + '* ``FlagAllowSelfTouchingHoles``: ' + Qgis.GeometryValidityFlag.AllowSelfTouchingHoles.__doc__
# --
QgsGeometry.ValidityFlags = Qgis.GeometryValidityFlags
Qgis.GeometryValidityFlag.baseClass = Qgis
Qgis.GeometryValidityFlags.baseClass = Qgis
GeometryValidityFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
QgsGeometry.ValidationMethod = Qgis.GeometryValidationEngine
# monkey patching scoped based enum
QgsGeometry.ValidatorQgisInternal = Qgis.GeometryValidationEngine.QgisInternal
QgsGeometry.ValidatorQgisInternal.is_monkey_patched = True
QgsGeometry.ValidatorQgisInternal.__doc__ = "Use internal QgsGeometryValidator method"
QgsGeometry.ValidatorGeos = Qgis.GeometryValidationEngine.Geos
QgsGeometry.ValidatorGeos.is_monkey_patched = True
QgsGeometry.ValidatorGeos.__doc__ = "Use GEOS validation methods"
Qgis.GeometryValidationEngine.__doc__ = 'Available engines for validating geometries.\n\n.. versionadded:: 3.22\n\n' + '* ``ValidatorQgisInternal``: ' + Qgis.GeometryValidationEngine.QgisInternal.__doc__ + '\n' + '* ``ValidatorGeos``: ' + Qgis.GeometryValidationEngine.Geos.__doc__
# --
Qgis.GeometryValidationEngine.baseClass = Qgis
QgsGeometry.BufferSide = Qgis.BufferSide
# monkey patching scoped based enum
QgsGeometry.SideLeft = Qgis.BufferSide.Left
QgsGeometry.SideLeft.is_monkey_patched = True
QgsGeometry.SideLeft.__doc__ = "Buffer to left of line"
QgsGeometry.SideRight = Qgis.BufferSide.Right
QgsGeometry.SideRight.is_monkey_patched = True
QgsGeometry.SideRight.__doc__ = "Buffer to right of line"
Qgis.BufferSide.__doc__ = 'Side of line to buffer.\n\n.. versionadded:: 3.22\n\n' + '* ``SideLeft``: ' + Qgis.BufferSide.Left.__doc__ + '\n' + '* ``SideRight``: ' + Qgis.BufferSide.Right.__doc__
# --
Qgis.BufferSide.baseClass = Qgis
QgsGeometry.EndCapStyle = Qgis.EndCapStyle
# monkey patching scoped based enum
QgsGeometry.CapRound = Qgis.EndCapStyle.Round
QgsGeometry.CapRound.is_monkey_patched = True
QgsGeometry.CapRound.__doc__ = "Round cap"
QgsGeometry.CapFlat = Qgis.EndCapStyle.Flat
QgsGeometry.CapFlat.is_monkey_patched = True
QgsGeometry.CapFlat.__doc__ = "Flat cap (in line with start/end of line)"
QgsGeometry.CapSquare = Qgis.EndCapStyle.Square
QgsGeometry.CapSquare.is_monkey_patched = True
QgsGeometry.CapSquare.__doc__ = "Square cap (extends past start/end of line by buffer distance)"
Qgis.EndCapStyle.__doc__ = 'End cap styles for buffers.\n\n.. versionadded:: 3.22\n\n' + '* ``CapRound``: ' + Qgis.EndCapStyle.Round.__doc__ + '\n' + '* ``CapFlat``: ' + Qgis.EndCapStyle.Flat.__doc__ + '\n' + '* ``CapSquare``: ' + Qgis.EndCapStyle.Square.__doc__
# --
Qgis.EndCapStyle.baseClass = Qgis
QgsGeometry.JoinStyle = Qgis.JoinStyle
# monkey patching scoped based enum
QgsGeometry.JoinStyleRound = Qgis.JoinStyle.Round
QgsGeometry.JoinStyleRound.is_monkey_patched = True
QgsGeometry.JoinStyleRound.__doc__ = "Use rounded joins"
QgsGeometry.JoinStyleMiter = Qgis.JoinStyle.Miter
QgsGeometry.JoinStyleMiter.is_monkey_patched = True
QgsGeometry.JoinStyleMiter.__doc__ = "Use mitered joins"
QgsGeometry.JoinStyleBevel = Qgis.JoinStyle.Bevel
QgsGeometry.JoinStyleBevel.is_monkey_patched = True
QgsGeometry.JoinStyleBevel.__doc__ = "Use beveled joins"
Qgis.JoinStyle.__doc__ = 'Join styles for buffers.\n\n.. versionadded:: 3.22\n\n' + '* ``JoinStyleRound``: ' + Qgis.JoinStyle.Round.__doc__ + '\n' + '* ``JoinStyleMiter``: ' + Qgis.JoinStyle.Miter.__doc__ + '\n' + '* ``JoinStyleBevel``: ' + Qgis.JoinStyle.Bevel.__doc__
# --
Qgis.JoinStyle.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SpatialFilterType.NoFilter.__doc__ = "No spatial filtering of features"
Qgis.SpatialFilterType.BoundingBox.__doc__ = "Filter using a bounding box"
Qgis.SpatialFilterType.DistanceWithin.__doc__ = "Filter by distance to reference geometry"
Qgis.SpatialFilterType.__doc__ = 'Feature request spatial filter types.\n\n.. versionadded:: 3.22\n\n' + '* ``NoFilter``: ' + Qgis.SpatialFilterType.NoFilter.__doc__ + '\n' + '* ``BoundingBox``: ' + Qgis.SpatialFilterType.BoundingBox.__doc__ + '\n' + '* ``DistanceWithin``: ' + Qgis.SpatialFilterType.DistanceWithin.__doc__
# --
Qgis.SpatialFilterType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.FileOperationFlag.IncludeMetadataFile.__doc__ = "Indicates that any associated .qmd metadata file should be included with the operation"
Qgis.FileOperationFlag.IncludeStyleFile.__doc__ = "Indicates that any associated .qml styling file should be included with the operation"
Qgis.FileOperationFlag.__doc__ = 'File operation flags.\n\n.. versionadded:: 3.22\n\n' + '* ``IncludeMetadataFile``: ' + Qgis.FileOperationFlag.IncludeMetadataFile.__doc__ + '\n' + '* ``IncludeStyleFile``: ' + Qgis.FileOperationFlag.IncludeStyleFile.__doc__
# --
Qgis.FileOperationFlag.baseClass = Qgis
Qgis.FileOperationFlags.baseClass = Qgis
FileOperationFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.MapLayerProperty.UsersCannotToggleEditing.__doc__ = "Indicates that users are not allowed to toggle editing for this layer. Note that this does not imply that the layer is non-editable (see isEditable(), supportsEditing() ), rather that the editable status of the layer cannot be changed by users manually. Since QGIS 3.22."
Qgis.MapLayerProperty.IsBasemapLayer.__doc__ = "Layer is considered a 'basemap' layer, and certain properties of the layer should be ignored when calculating project-level properties. For instance, the extent of basemap layers is ignored when calculating the extent of a project, as these layers are typically global and extend outside of a project's area of interest. Since QGIS 3.26."
Qgis.MapLayerProperty.__doc__ = 'Generic map layer properties.\n\n.. versionadded:: 3.22\n\n' + '* ``UsersCannotToggleEditing``: ' + Qgis.MapLayerProperty.UsersCannotToggleEditing.__doc__ + '\n' + '* ``IsBasemapLayer``: ' + Qgis.MapLayerProperty.IsBasemapLayer.__doc__
# --
Qgis.MapLayerProperty.baseClass = Qgis
Qgis.MapLayerProperties.baseClass = Qgis
MapLayerProperties = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.DataProviderFlag.IsBasemapSource.__doc__ = "Associated source should be considered a 'basemap' layer. See Qgis.MapLayerProperty.IsBasemapLayer."
Qgis.DataProviderFlag.__doc__ = 'Generic data provider flags.\n\n.. versionadded:: 3.26\n\n' + '* ``IsBasemapSource``: ' + Qgis.DataProviderFlag.IsBasemapSource.__doc__
# --
Qgis.DataProviderFlag.baseClass = Qgis
Qgis.DataProviderFlags.baseClass = Qgis
DataProviderFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.CrsAxisDirection.North.__doc__ = "North"
Qgis.CrsAxisDirection.NorthNorthEast.__doc__ = "North North East"
Qgis.CrsAxisDirection.NorthEast.__doc__ = "North East"
Qgis.CrsAxisDirection.EastNorthEast.__doc__ = "East North East"
Qgis.CrsAxisDirection.East.__doc__ = "East"
Qgis.CrsAxisDirection.EastSouthEast.__doc__ = "East South East"
Qgis.CrsAxisDirection.SouthEast.__doc__ = "South East"
Qgis.CrsAxisDirection.SouthSouthEast.__doc__ = "South South East"
Qgis.CrsAxisDirection.South.__doc__ = "South"
Qgis.CrsAxisDirection.SouthSouthWest.__doc__ = "South South West"
Qgis.CrsAxisDirection.SouthWest.__doc__ = "South West"
Qgis.CrsAxisDirection.WestSouthWest.__doc__ = "West South West"
Qgis.CrsAxisDirection.West.__doc__ = "West"
Qgis.CrsAxisDirection.WestNorthWest.__doc__ = "West North West"
Qgis.CrsAxisDirection.NorthWest.__doc__ = "North West"
Qgis.CrsAxisDirection.NorthNorthWest.__doc__ = "North North West"
Qgis.CrsAxisDirection.GeocentricX.__doc__ = "Geocentric (X)"
Qgis.CrsAxisDirection.GeocentricY.__doc__ = "Geocentric (Y)"
Qgis.CrsAxisDirection.GeocentricZ.__doc__ = "Geocentric (Z)"
Qgis.CrsAxisDirection.Up.__doc__ = "Up"
Qgis.CrsAxisDirection.Down.__doc__ = "Down"
Qgis.CrsAxisDirection.Forward.__doc__ = "Forward"
Qgis.CrsAxisDirection.Aft.__doc__ = "Aft"
Qgis.CrsAxisDirection.Port.__doc__ = "Port"
Qgis.CrsAxisDirection.Starboard.__doc__ = "Starboard"
Qgis.CrsAxisDirection.Clockwise.__doc__ = "Clockwise"
Qgis.CrsAxisDirection.CounterClockwise.__doc__ = "Counter clockwise"
Qgis.CrsAxisDirection.ColumnPositive.__doc__ = "Column positive"
Qgis.CrsAxisDirection.ColumnNegative.__doc__ = "Column negative"
Qgis.CrsAxisDirection.RowPositive.__doc__ = "Row positive"
Qgis.CrsAxisDirection.RowNegative.__doc__ = "Row negative"
Qgis.CrsAxisDirection.DisplayRight.__doc__ = "Display right"
Qgis.CrsAxisDirection.DisplayLeft.__doc__ = "Display left"
Qgis.CrsAxisDirection.DisplayUp.__doc__ = "Display up"
Qgis.CrsAxisDirection.DisplayDown.__doc__ = "Display down"
Qgis.CrsAxisDirection.Future.__doc__ = "Future"
Qgis.CrsAxisDirection.Past.__doc__ = "Past"
Qgis.CrsAxisDirection.Towards.__doc__ = "Towards"
Qgis.CrsAxisDirection.AwayFrom.__doc__ = "Away from"
Qgis.CrsAxisDirection.Unspecified.__doc__ = "Unspecified"
Qgis.CrsAxisDirection.__doc__ = 'Coordinate reference system axis directions.\n\nFrom "Geographic information — Well-known text representation of coordinate reference systems", section 7.5.1.\n\n.. versionadded:: 3.26\n\n' + '* ``North``: ' + Qgis.CrsAxisDirection.North.__doc__ + '\n' + '* ``NorthNorthEast``: ' + Qgis.CrsAxisDirection.NorthNorthEast.__doc__ + '\n' + '* ``NorthEast``: ' + Qgis.CrsAxisDirection.NorthEast.__doc__ + '\n' + '* ``EastNorthEast``: ' + Qgis.CrsAxisDirection.EastNorthEast.__doc__ + '\n' + '* ``East``: ' + Qgis.CrsAxisDirection.East.__doc__ + '\n' + '* ``EastSouthEast``: ' + Qgis.CrsAxisDirection.EastSouthEast.__doc__ + '\n' + '* ``SouthEast``: ' + Qgis.CrsAxisDirection.SouthEast.__doc__ + '\n' + '* ``SouthSouthEast``: ' + Qgis.CrsAxisDirection.SouthSouthEast.__doc__ + '\n' + '* ``South``: ' + Qgis.CrsAxisDirection.South.__doc__ + '\n' + '* ``SouthSouthWest``: ' + Qgis.CrsAxisDirection.SouthSouthWest.__doc__ + '\n' + '* ``SouthWest``: ' + Qgis.CrsAxisDirection.SouthWest.__doc__ + '\n' + '* ``WestSouthWest``: ' + Qgis.CrsAxisDirection.WestSouthWest.__doc__ + '\n' + '* ``West``: ' + Qgis.CrsAxisDirection.West.__doc__ + '\n' + '* ``WestNorthWest``: ' + Qgis.CrsAxisDirection.WestNorthWest.__doc__ + '\n' + '* ``NorthWest``: ' + Qgis.CrsAxisDirection.NorthWest.__doc__ + '\n' + '* ``NorthNorthWest``: ' + Qgis.CrsAxisDirection.NorthNorthWest.__doc__ + '\n' + '* ``GeocentricX``: ' + Qgis.CrsAxisDirection.GeocentricX.__doc__ + '\n' + '* ``GeocentricY``: ' + Qgis.CrsAxisDirection.GeocentricY.__doc__ + '\n' + '* ``GeocentricZ``: ' + Qgis.CrsAxisDirection.GeocentricZ.__doc__ + '\n' + '* ``Up``: ' + Qgis.CrsAxisDirection.Up.__doc__ + '\n' + '* ``Down``: ' + Qgis.CrsAxisDirection.Down.__doc__ + '\n' + '* ``Forward``: ' + Qgis.CrsAxisDirection.Forward.__doc__ + '\n' + '* ``Aft``: ' + Qgis.CrsAxisDirection.Aft.__doc__ + '\n' + '* ``Port``: ' + Qgis.CrsAxisDirection.Port.__doc__ + '\n' + '* ``Starboard``: ' + Qgis.CrsAxisDirection.Starboard.__doc__ + '\n' + '* ``Clockwise``: ' + Qgis.CrsAxisDirection.Clockwise.__doc__ + '\n' + '* ``CounterClockwise``: ' + Qgis.CrsAxisDirection.CounterClockwise.__doc__ + '\n' + '* ``ColumnPositive``: ' + Qgis.CrsAxisDirection.ColumnPositive.__doc__ + '\n' + '* ``ColumnNegative``: ' + Qgis.CrsAxisDirection.ColumnNegative.__doc__ + '\n' + '* ``RowPositive``: ' + Qgis.CrsAxisDirection.RowPositive.__doc__ + '\n' + '* ``RowNegative``: ' + Qgis.CrsAxisDirection.RowNegative.__doc__ + '\n' + '* ``DisplayRight``: ' + Qgis.CrsAxisDirection.DisplayRight.__doc__ + '\n' + '* ``DisplayLeft``: ' + Qgis.CrsAxisDirection.DisplayLeft.__doc__ + '\n' + '* ``DisplayUp``: ' + Qgis.CrsAxisDirection.DisplayUp.__doc__ + '\n' + '* ``DisplayDown``: ' + Qgis.CrsAxisDirection.DisplayDown.__doc__ + '\n' + '* ``Future``: ' + Qgis.CrsAxisDirection.Future.__doc__ + '\n' + '* ``Past``: ' + Qgis.CrsAxisDirection.Past.__doc__ + '\n' + '* ``Towards``: ' + Qgis.CrsAxisDirection.Towards.__doc__ + '\n' + '* ``AwayFrom``: ' + Qgis.CrsAxisDirection.AwayFrom.__doc__ + '\n' + '* ``Unspecified``: ' + Qgis.CrsAxisDirection.Unspecified.__doc__
# --
Qgis.CrsAxisDirection.baseClass = Qgis
# monkey patching scoped based enum
Qgis.CoordinateOrder.Default.__doc__ = "Respect the default axis ordering for the CRS, as defined in the CRS's parameters"
Qgis.CoordinateOrder.XY.__doc__ = "Easting/Northing (or Longitude/Latitude for geographic CRS)"
Qgis.CoordinateOrder.YX.__doc__ = "Northing/Easting (or Latitude/Longitude for geographic CRS)"
Qgis.CoordinateOrder.__doc__ = 'Order of coordinates.\n\n.. versionadded:: 3.26\n\n' + '* ``Default``: ' + Qgis.CoordinateOrder.Default.__doc__ + '\n' + '* ``XY``: ' + Qgis.CoordinateOrder.XY.__doc__ + '\n' + '* ``YX``: ' + Qgis.CoordinateOrder.YX.__doc__
# --
Qgis.CoordinateOrder.baseClass = Qgis
# monkey patching scoped based enum
Qgis.AnnotationItemFlag.ScaleDependentBoundingBox.__doc__ = "Item's bounding box will vary depending on map scale"
Qgis.AnnotationItemFlag.__doc__ = 'Flags for annotation items.\n\n.. versionadded:: 3.22\n\n' + '* ``ScaleDependentBoundingBox``: ' + Qgis.AnnotationItemFlag.ScaleDependentBoundingBox.__doc__
# --
Qgis.AnnotationItemFlag.baseClass = Qgis
Qgis.AnnotationItemFlags.baseClass = Qgis
AnnotationItemFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.AnnotationItemGuiFlag.FlagNoCreationTools.__doc__ = "Do not show item creation tools for the item type"
Qgis.AnnotationItemGuiFlag.__doc__ = 'Flags for controlling how an annotation item behaves in the GUI.\n\n.. versionadded:: 3.22\n\n' + '* ``FlagNoCreationTools``: ' + Qgis.AnnotationItemGuiFlag.FlagNoCreationTools.__doc__
# --
Qgis.AnnotationItemGuiFlag.baseClass = Qgis
Qgis.AnnotationItemGuiFlags.baseClass = Qgis
AnnotationItemGuiFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.AnnotationItemNodeType.VertexHandle.__doc__ = "Node is a handle for manipulating vertices"
Qgis.AnnotationItemNodeType.__doc__ = 'Annotation item node types.\n\n.. versionadded:: 3.22\n\n' + '* ``VertexHandle``: ' + Qgis.AnnotationItemNodeType.VertexHandle.__doc__
# --
Qgis.AnnotationItemNodeType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.AnnotationItemEditOperationResult.Success.__doc__ = "Item was modified successfully"
Qgis.AnnotationItemEditOperationResult.Invalid.__doc__ = "Operation has invalid parameters for the item, no change occurred"
Qgis.AnnotationItemEditOperationResult.ItemCleared.__doc__ = "The operation results in the item being cleared, and the item should be removed from the layer as a result"
Qgis.AnnotationItemEditOperationResult.__doc__ = 'Results from an edit operation on an annotation item.\n\n.. versionadded:: 3.22\n\n' + '* ``Success``: ' + Qgis.AnnotationItemEditOperationResult.Success.__doc__ + '\n' + '* ``Invalid``: ' + Qgis.AnnotationItemEditOperationResult.Invalid.__doc__ + '\n' + '* ``ItemCleared``: ' + Qgis.AnnotationItemEditOperationResult.ItemCleared.__doc__
# --
Qgis.AnnotationItemEditOperationResult.baseClass = Qgis
QgsVectorLayerTemporalProperties.TemporalMode = Qgis.VectorTemporalMode
# monkey patching scoped based enum
QgsVectorLayerTemporalProperties.ModeFixedTemporalRange = Qgis.VectorTemporalMode.FixedTemporalRange
QgsVectorLayerTemporalProperties.ModeFixedTemporalRange.is_monkey_patched = True
QgsVectorLayerTemporalProperties.ModeFixedTemporalRange.__doc__ = "Mode when temporal properties have fixed start and end datetimes."
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeInstantFromField = Qgis.VectorTemporalMode.FeatureDateTimeInstantFromField
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeInstantFromField.is_monkey_patched = True
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeInstantFromField.__doc__ = "Mode when features have a datetime instant taken from a single field"
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndEndFromFields = Qgis.VectorTemporalMode.FeatureDateTimeStartAndEndFromFields
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndEndFromFields.is_monkey_patched = True
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndEndFromFields.__doc__ = "Mode when features have separate fields for start and end times"
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndDurationFromFields = Qgis.VectorTemporalMode.FeatureDateTimeStartAndDurationFromFields
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndDurationFromFields.is_monkey_patched = True
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndDurationFromFields.__doc__ = "Mode when features have a field for start time and a field for event duration"
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndEndFromExpressions = Qgis.VectorTemporalMode.FeatureDateTimeStartAndEndFromExpressions
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndEndFromExpressions.is_monkey_patched = True
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndEndFromExpressions.__doc__ = "Mode when features use expressions for start and end times"
QgsVectorLayerTemporalProperties.ModeRedrawLayerOnly = Qgis.VectorTemporalMode.RedrawLayerOnly
QgsVectorLayerTemporalProperties.ModeRedrawLayerOnly.is_monkey_patched = True
QgsVectorLayerTemporalProperties.ModeRedrawLayerOnly.__doc__ = "Redraw the layer when temporal range changes, but don't apply any filtering. Useful when symbology or rule based renderer expressions depend on the time range."
Qgis.VectorTemporalMode.__doc__ = 'Vector layer temporal feature modes\n\n.. versionadded:: 3.22\n\n' + '* ``ModeFixedTemporalRange``: ' + Qgis.VectorTemporalMode.FixedTemporalRange.__doc__ + '\n' + '* ``ModeFeatureDateTimeInstantFromField``: ' + Qgis.VectorTemporalMode.FeatureDateTimeInstantFromField.__doc__ + '\n' + '* ``ModeFeatureDateTimeStartAndEndFromFields``: ' + Qgis.VectorTemporalMode.FeatureDateTimeStartAndEndFromFields.__doc__ + '\n' + '* ``ModeFeatureDateTimeStartAndDurationFromFields``: ' + Qgis.VectorTemporalMode.FeatureDateTimeStartAndDurationFromFields.__doc__ + '\n' + '* ``ModeFeatureDateTimeStartAndEndFromExpressions``: ' + Qgis.VectorTemporalMode.FeatureDateTimeStartAndEndFromExpressions.__doc__ + '\n' + '* ``ModeRedrawLayerOnly``: ' + Qgis.VectorTemporalMode.RedrawLayerOnly.__doc__
# --
Qgis.VectorTemporalMode.baseClass = Qgis
# monkey patching scoped based enum
Qgis.VectorTemporalLimitMode.IncludeBeginExcludeEnd.__doc__ = "Default mode: include the Begin limit, but exclude the End limit"
Qgis.VectorTemporalLimitMode.IncludeBeginIncludeEnd.__doc__ = "Mode to include both limits of the filtering timeframe"
Qgis.VectorTemporalLimitMode.__doc__ = 'Mode for the handling of the limits of the filtering timeframe for vector features\n\n.. versionadded:: 3.22\n\n' + '* ``IncludeBeginExcludeEnd``: ' + Qgis.VectorTemporalLimitMode.IncludeBeginExcludeEnd.__doc__ + '\n' + '* ``IncludeBeginIncludeEnd``: ' + Qgis.VectorTemporalLimitMode.IncludeBeginIncludeEnd.__doc__
# --
Qgis.VectorTemporalLimitMode.baseClass = Qgis
QgsVectorDataProviderTemporalCapabilities.TemporalMode = Qgis.VectorDataProviderTemporalMode
# monkey patching scoped based enum
QgsVectorDataProviderTemporalCapabilities.ProviderHasFixedTemporalRange = Qgis.VectorDataProviderTemporalMode.HasFixedTemporalRange
QgsVectorDataProviderTemporalCapabilities.ProviderHasFixedTemporalRange.is_monkey_patched = True
QgsVectorDataProviderTemporalCapabilities.ProviderHasFixedTemporalRange.__doc__ = "Entire dataset from provider has a fixed start and end datetime."
QgsVectorDataProviderTemporalCapabilities.ProviderStoresFeatureDateTimeInstantInField = Qgis.VectorDataProviderTemporalMode.StoresFeatureDateTimeInstantInField
QgsVectorDataProviderTemporalCapabilities.ProviderStoresFeatureDateTimeInstantInField.is_monkey_patched = True
QgsVectorDataProviderTemporalCapabilities.ProviderStoresFeatureDateTimeInstantInField.__doc__ = "Dataset has feature datetime instants stored in a single field"
QgsVectorDataProviderTemporalCapabilities.ProviderStoresFeatureDateTimeStartAndEndInSeparateFields = Qgis.VectorDataProviderTemporalMode.StoresFeatureDateTimeStartAndEndInSeparateFields
QgsVectorDataProviderTemporalCapabilities.ProviderStoresFeatureDateTimeStartAndEndInSeparateFields.is_monkey_patched = True
QgsVectorDataProviderTemporalCapabilities.ProviderStoresFeatureDateTimeStartAndEndInSeparateFields.__doc__ = "Dataset stores feature start and end datetimes in separate fields"
Qgis.VectorDataProviderTemporalMode.__doc__ = 'Vector data provider temporal handling modes.\n\n.. versionadded:: 3.22\n\n' + '* ``ProviderHasFixedTemporalRange``: ' + Qgis.VectorDataProviderTemporalMode.HasFixedTemporalRange.__doc__ + '\n' + '* ``ProviderStoresFeatureDateTimeInstantInField``: ' + Qgis.VectorDataProviderTemporalMode.StoresFeatureDateTimeInstantInField.__doc__ + '\n' + '* ``ProviderStoresFeatureDateTimeStartAndEndInSeparateFields``: ' + Qgis.VectorDataProviderTemporalMode.StoresFeatureDateTimeStartAndEndInSeparateFields.__doc__
# --
Qgis.VectorDataProviderTemporalMode.baseClass = Qgis
QgsRasterLayerTemporalProperties.TemporalMode = Qgis.RasterTemporalMode
# monkey patching scoped based enum
QgsRasterLayerTemporalProperties.ModeFixedTemporalRange = Qgis.RasterTemporalMode.FixedTemporalRange
QgsRasterLayerTemporalProperties.ModeFixedTemporalRange.is_monkey_patched = True
QgsRasterLayerTemporalProperties.ModeFixedTemporalRange.__doc__ = "Mode when temporal properties have fixed start and end datetimes."
QgsRasterLayerTemporalProperties.ModeTemporalRangeFromDataProvider = Qgis.RasterTemporalMode.TemporalRangeFromDataProvider
QgsRasterLayerTemporalProperties.ModeTemporalRangeFromDataProvider.is_monkey_patched = True
QgsRasterLayerTemporalProperties.ModeTemporalRangeFromDataProvider.__doc__ = "Mode when raster layer delegates temporal range handling to the dataprovider."
QgsRasterLayerTemporalProperties.ModeRedrawLayerOnly = Qgis.RasterTemporalMode.RedrawLayerOnly
QgsRasterLayerTemporalProperties.ModeRedrawLayerOnly.is_monkey_patched = True
QgsRasterLayerTemporalProperties.ModeRedrawLayerOnly.__doc__ = "Redraw the layer when temporal range changes, but don't apply any filtering. Useful when raster symbology expressions depend on the time range. (since QGIS 3.22)"
Qgis.RasterTemporalMode.__doc__ = 'Raster layer temporal modes\n\n.. versionadded:: 3.22\n\n' + '* ``ModeFixedTemporalRange``: ' + Qgis.RasterTemporalMode.FixedTemporalRange.__doc__ + '\n' + '* ``ModeTemporalRangeFromDataProvider``: ' + Qgis.RasterTemporalMode.TemporalRangeFromDataProvider.__doc__ + '\n' + '* ``ModeRedrawLayerOnly``: ' + Qgis.RasterTemporalMode.RedrawLayerOnly.__doc__
# --
Qgis.RasterTemporalMode.baseClass = Qgis
QgsRasterDataProviderTemporalCapabilities.IntervalHandlingMethod = Qgis.TemporalIntervalMatchMethod
# monkey patching scoped based enum
QgsRasterDataProviderTemporalCapabilities.MatchUsingWholeRange = Qgis.TemporalIntervalMatchMethod.MatchUsingWholeRange
QgsRasterDataProviderTemporalCapabilities.MatchUsingWholeRange.is_monkey_patched = True
QgsRasterDataProviderTemporalCapabilities.MatchUsingWholeRange.__doc__ = "Use an exact match to the whole temporal range"
QgsRasterDataProviderTemporalCapabilities.MatchExactUsingStartOfRange = Qgis.TemporalIntervalMatchMethod.MatchExactUsingStartOfRange
QgsRasterDataProviderTemporalCapabilities.MatchExactUsingStartOfRange.is_monkey_patched = True
QgsRasterDataProviderTemporalCapabilities.MatchExactUsingStartOfRange.__doc__ = "Match the start of the temporal range to a corresponding layer or band, and only use exact matching results"
QgsRasterDataProviderTemporalCapabilities.MatchExactUsingEndOfRange = Qgis.TemporalIntervalMatchMethod.MatchExactUsingEndOfRange
QgsRasterDataProviderTemporalCapabilities.MatchExactUsingEndOfRange.is_monkey_patched = True
QgsRasterDataProviderTemporalCapabilities.MatchExactUsingEndOfRange.__doc__ = "Match the end of the temporal range to a corresponding layer or band, and only use exact matching results"
QgsRasterDataProviderTemporalCapabilities.FindClosestMatchToStartOfRange = Qgis.TemporalIntervalMatchMethod.FindClosestMatchToStartOfRange
QgsRasterDataProviderTemporalCapabilities.FindClosestMatchToStartOfRange.is_monkey_patched = True
QgsRasterDataProviderTemporalCapabilities.FindClosestMatchToStartOfRange.__doc__ = "Match the start of the temporal range to the least previous closest datetime."
QgsRasterDataProviderTemporalCapabilities.FindClosestMatchToEndOfRange = Qgis.TemporalIntervalMatchMethod.FindClosestMatchToEndOfRange
QgsRasterDataProviderTemporalCapabilities.FindClosestMatchToEndOfRange.is_monkey_patched = True
QgsRasterDataProviderTemporalCapabilities.FindClosestMatchToEndOfRange.__doc__ = "Match the end of the temporal range to the least previous closest datetime."
Qgis.TemporalIntervalMatchMethod.__doc__ = 'Method to use when resolving a temporal range to a data provider layer or band.\n\n.. versionadded:: 3.22\n\n' + '* ``MatchUsingWholeRange``: ' + Qgis.TemporalIntervalMatchMethod.MatchUsingWholeRange.__doc__ + '\n' + '* ``MatchExactUsingStartOfRange``: ' + Qgis.TemporalIntervalMatchMethod.MatchExactUsingStartOfRange.__doc__ + '\n' + '* ``MatchExactUsingEndOfRange``: ' + Qgis.TemporalIntervalMatchMethod.MatchExactUsingEndOfRange.__doc__ + '\n' + '* ``FindClosestMatchToStartOfRange``: ' + Qgis.TemporalIntervalMatchMethod.FindClosestMatchToStartOfRange.__doc__ + '\n' + '* ``FindClosestMatchToEndOfRange``: ' + Qgis.TemporalIntervalMatchMethod.FindClosestMatchToEndOfRange.__doc__
# --
Qgis.TemporalIntervalMatchMethod.baseClass = Qgis
# monkey patching scoped based enum
Qgis.RasterTemporalCapabilityFlag.RequestedTimesMustExactlyMatchAllAvailableTemporalRanges.__doc__ = "If present, indicates that the provider must only request temporal values which are exact matches for the values present in QgsRasterDataProviderTemporalCapabilities.allAvailableTemporalRanges()."
Qgis.RasterTemporalCapabilityFlag.__doc__ = 'Flags for raster layer temporal capabilities.\n\n.. versionadded:: 3.28\n\n' + '* ``RequestedTimesMustExactlyMatchAllAvailableTemporalRanges``: ' + Qgis.RasterTemporalCapabilityFlag.RequestedTimesMustExactlyMatchAllAvailableTemporalRanges.__doc__
# --
Qgis.RasterTemporalCapabilityFlag.baseClass = Qgis
Qgis.RasterTemporalCapabilityFlags.baseClass = Qgis
QgsCoordinateTransform.TransformDirection = Qgis.TransformDirection
# monkey patching scoped based enum
QgsCoordinateTransform.ForwardTransform = Qgis.TransformDirection.Forward
QgsCoordinateTransform.ForwardTransform.is_monkey_patched = True
QgsCoordinateTransform.ForwardTransform.__doc__ = "Forward transform (from source to destination)"
QgsCoordinateTransform.ReverseTransform = Qgis.TransformDirection.Reverse
QgsCoordinateTransform.ReverseTransform.is_monkey_patched = True
QgsCoordinateTransform.ReverseTransform.__doc__ = "Reverse/inverse transform (from destination to source)"
Qgis.TransformDirection.__doc__ = 'Indicates the direction (forward or inverse) of a transform.\n\n.. versionadded:: 3.22\n\n' + '* ``ForwardTransform``: ' + Qgis.TransformDirection.Forward.__doc__ + '\n' + '* ``ReverseTransform``: ' + Qgis.TransformDirection.Reverse.__doc__
# --
Qgis.TransformDirection.baseClass = Qgis
# monkey patching scoped based enum
Qgis.CoordinateTransformationFlag.BallparkTransformsAreAppropriate.__doc__ = "Indicates that approximate \"ballpark\" results are appropriate for this coordinate transform. See QgsCoordinateTransform.setBallparkTransformsAreAppropriate() for further details."
Qgis.CoordinateTransformationFlag.IgnoreImpossibleTransformations.__doc__ = "Indicates that impossible transformations (such as those which attempt to transform between two different celestial bodies) should be silently handled and marked as invalid. See QgsCoordinateTransform.isTransformationPossible() and QgsCoordinateTransform.isValid()."
Qgis.CoordinateTransformationFlag.__doc__ = 'Flags which adjust the coordinate transformations behave.\n\n.. versionadded:: 3.26\n\n' + '* ``BallparkTransformsAreAppropriate``: ' + Qgis.CoordinateTransformationFlag.BallparkTransformsAreAppropriate.__doc__ + '\n' + '* ``IgnoreImpossibleTransformations``: ' + Qgis.CoordinateTransformationFlag.IgnoreImpossibleTransformations.__doc__
# --
Qgis.CoordinateTransformationFlag.baseClass = Qgis
Qgis.CoordinateTransformationFlags.baseClass = Qgis
QgsMapSettings.Flag = Qgis.MapSettingsFlag
# monkey patching scoped based enum
QgsMapSettings.Antialiasing = Qgis.MapSettingsFlag.Antialiasing
QgsMapSettings.Antialiasing.is_monkey_patched = True
QgsMapSettings.Antialiasing.__doc__ = "Enable anti-aliasing for map rendering"
QgsMapSettings.DrawEditingInfo = Qgis.MapSettingsFlag.DrawEditingInfo
QgsMapSettings.DrawEditingInfo.is_monkey_patched = True
QgsMapSettings.DrawEditingInfo.__doc__ = "Enable drawing of vertex markers for layers in editing mode"
QgsMapSettings.ForceVectorOutput = Qgis.MapSettingsFlag.ForceVectorOutput
QgsMapSettings.ForceVectorOutput.is_monkey_patched = True
QgsMapSettings.ForceVectorOutput.__doc__ = "Vector graphics should not be cached and drawn as raster images"
QgsMapSettings.UseAdvancedEffects = Qgis.MapSettingsFlag.UseAdvancedEffects
QgsMapSettings.UseAdvancedEffects.is_monkey_patched = True
QgsMapSettings.UseAdvancedEffects.__doc__ = "Enable layer opacity and blending effects"
QgsMapSettings.DrawLabeling = Qgis.MapSettingsFlag.DrawLabeling
QgsMapSettings.DrawLabeling.is_monkey_patched = True
QgsMapSettings.DrawLabeling.__doc__ = "Enable drawing of labels on top of the map"
QgsMapSettings.UseRenderingOptimization = Qgis.MapSettingsFlag.UseRenderingOptimization
QgsMapSettings.UseRenderingOptimization.is_monkey_patched = True
QgsMapSettings.UseRenderingOptimization.__doc__ = "Enable vector simplification and other rendering optimizations"
QgsMapSettings.DrawSelection = Qgis.MapSettingsFlag.DrawSelection
QgsMapSettings.DrawSelection.is_monkey_patched = True
QgsMapSettings.DrawSelection.__doc__ = "Whether vector selections should be shown in the rendered map"
QgsMapSettings.DrawSymbolBounds = Qgis.MapSettingsFlag.DrawSymbolBounds
QgsMapSettings.DrawSymbolBounds.is_monkey_patched = True
QgsMapSettings.DrawSymbolBounds.__doc__ = "Draw bounds of symbols (for debugging/testing)"
QgsMapSettings.RenderMapTile = Qgis.MapSettingsFlag.RenderMapTile
QgsMapSettings.RenderMapTile.is_monkey_patched = True
QgsMapSettings.RenderMapTile.__doc__ = "Draw map such that there are no problems between adjacent tiles"
QgsMapSettings.RenderPartialOutput = Qgis.MapSettingsFlag.RenderPartialOutput
QgsMapSettings.RenderPartialOutput.is_monkey_patched = True
QgsMapSettings.RenderPartialOutput.__doc__ = "Whether to make extra effort to update map image with partially rendered layers (better for interactive map canvas). Added in QGIS 3.0"
QgsMapSettings.RenderPreviewJob = Qgis.MapSettingsFlag.RenderPreviewJob
QgsMapSettings.RenderPreviewJob.is_monkey_patched = True
QgsMapSettings.RenderPreviewJob.__doc__ = "Render is a 'canvas preview' render, and shortcuts should be taken to ensure fast rendering"
QgsMapSettings.RenderBlocking = Qgis.MapSettingsFlag.RenderBlocking
QgsMapSettings.RenderBlocking.is_monkey_patched = True
QgsMapSettings.RenderBlocking.__doc__ = "Render and load remote sources in the same thread to ensure rendering remote sources (svg and images). WARNING: this flag must NEVER be used from GUI based applications (like the main QGIS application) or crashes will result. Only for use in external scripts or QGIS server."
QgsMapSettings.LosslessImageRendering = Qgis.MapSettingsFlag.LosslessImageRendering
QgsMapSettings.LosslessImageRendering.is_monkey_patched = True
QgsMapSettings.LosslessImageRendering.__doc__ = "Render images losslessly whenever possible, instead of the default lossy jpeg rendering used for some destination devices (e.g. PDF). This flag only works with builds based on Qt 5.13 or later."
QgsMapSettings.Render3DMap = Qgis.MapSettingsFlag.Render3DMap
QgsMapSettings.Render3DMap.is_monkey_patched = True
QgsMapSettings.Render3DMap.__doc__ = "Render is for a 3D map"
QgsMapSettings.HighQualityImageTransforms = Qgis.MapSettingsFlag.HighQualityImageTransforms
QgsMapSettings.HighQualityImageTransforms.is_monkey_patched = True
QgsMapSettings.HighQualityImageTransforms.__doc__ = "Enable high quality image transformations, which results in better appearance of scaled or rotated raster components of a map (since QGIS 3.24)"
QgsMapSettings.SkipSymbolRendering = Qgis.MapSettingsFlag.SkipSymbolRendering
QgsMapSettings.SkipSymbolRendering.is_monkey_patched = True
QgsMapSettings.SkipSymbolRendering.__doc__ = "Disable symbol rendering while still drawing labels if enabled (since QGIS 3.24)"
QgsMapSettings.ForceRasterMasks = Qgis.MapSettingsFlag.ForceRasterMasks
QgsMapSettings.ForceRasterMasks.is_monkey_patched = True
QgsMapSettings.ForceRasterMasks.__doc__ = "Force symbol masking to be applied using a raster method. This is considerably faster when compared to the vector method, but results in a inferior quality output. (since QGIS 3.26.1)"
Qgis.MapSettingsFlag.__doc__ = 'Flags which adjust the way maps are rendered.\n\n.. versionadded:: 3.22\n\n' + '* ``Antialiasing``: ' + Qgis.MapSettingsFlag.Antialiasing.__doc__ + '\n' + '* ``DrawEditingInfo``: ' + Qgis.MapSettingsFlag.DrawEditingInfo.__doc__ + '\n' + '* ``ForceVectorOutput``: ' + Qgis.MapSettingsFlag.ForceVectorOutput.__doc__ + '\n' + '* ``UseAdvancedEffects``: ' + Qgis.MapSettingsFlag.UseAdvancedEffects.__doc__ + '\n' + '* ``DrawLabeling``: ' + Qgis.MapSettingsFlag.DrawLabeling.__doc__ + '\n' + '* ``UseRenderingOptimization``: ' + Qgis.MapSettingsFlag.UseRenderingOptimization.__doc__ + '\n' + '* ``DrawSelection``: ' + Qgis.MapSettingsFlag.DrawSelection.__doc__ + '\n' + '* ``DrawSymbolBounds``: ' + Qgis.MapSettingsFlag.DrawSymbolBounds.__doc__ + '\n' + '* ``RenderMapTile``: ' + Qgis.MapSettingsFlag.RenderMapTile.__doc__ + '\n' + '* ``RenderPartialOutput``: ' + Qgis.MapSettingsFlag.RenderPartialOutput.__doc__ + '\n' + '* ``RenderPreviewJob``: ' + Qgis.MapSettingsFlag.RenderPreviewJob.__doc__ + '\n' + '* ``RenderBlocking``: ' + Qgis.MapSettingsFlag.RenderBlocking.__doc__ + '\n' + '* ``LosslessImageRendering``: ' + Qgis.MapSettingsFlag.LosslessImageRendering.__doc__ + '\n' + '* ``Render3DMap``: ' + Qgis.MapSettingsFlag.Render3DMap.__doc__ + '\n' + '* ``HighQualityImageTransforms``: ' + Qgis.MapSettingsFlag.HighQualityImageTransforms.__doc__ + '\n' + '* ``SkipSymbolRendering``: ' + Qgis.MapSettingsFlag.SkipSymbolRendering.__doc__ + '\n' + '* ``ForceRasterMasks``: ' + Qgis.MapSettingsFlag.ForceRasterMasks.__doc__
# --
QgsMapSettings.Flags = Qgis.MapSettingsFlags
Qgis.MapSettingsFlag.baseClass = Qgis
Qgis.MapSettingsFlags.baseClass = Qgis
MapSettingsFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
QgsRenderContext.Flag = Qgis.RenderContextFlag
# monkey patching scoped based enum
QgsRenderContext.DrawEditingInfo = Qgis.RenderContextFlag.DrawEditingInfo
QgsRenderContext.DrawEditingInfo.is_monkey_patched = True
QgsRenderContext.DrawEditingInfo.__doc__ = "Enable drawing of vertex markers for layers in editing mode"
QgsRenderContext.ForceVectorOutput = Qgis.RenderContextFlag.ForceVectorOutput
QgsRenderContext.ForceVectorOutput.is_monkey_patched = True
QgsRenderContext.ForceVectorOutput.__doc__ = "Vector graphics should not be cached and drawn as raster images"
QgsRenderContext.UseAdvancedEffects = Qgis.RenderContextFlag.UseAdvancedEffects
QgsRenderContext.UseAdvancedEffects.is_monkey_patched = True
QgsRenderContext.UseAdvancedEffects.__doc__ = "Enable layer opacity and blending effects"
QgsRenderContext.UseRenderingOptimization = Qgis.RenderContextFlag.UseRenderingOptimization
QgsRenderContext.UseRenderingOptimization.is_monkey_patched = True
QgsRenderContext.UseRenderingOptimization.__doc__ = "Enable vector simplification and other rendering optimizations"
QgsRenderContext.DrawSelection = Qgis.RenderContextFlag.DrawSelection
QgsRenderContext.DrawSelection.is_monkey_patched = True
QgsRenderContext.DrawSelection.__doc__ = "Whether vector selections should be shown in the rendered map"
QgsRenderContext.DrawSymbolBounds = Qgis.RenderContextFlag.DrawSymbolBounds
QgsRenderContext.DrawSymbolBounds.is_monkey_patched = True
QgsRenderContext.DrawSymbolBounds.__doc__ = "Draw bounds of symbols (for debugging/testing)"
QgsRenderContext.RenderMapTile = Qgis.RenderContextFlag.RenderMapTile
QgsRenderContext.RenderMapTile.is_monkey_patched = True
QgsRenderContext.RenderMapTile.__doc__ = "Draw map such that there are no problems between adjacent tiles"
QgsRenderContext.Antialiasing = Qgis.RenderContextFlag.Antialiasing
QgsRenderContext.Antialiasing.is_monkey_patched = True
QgsRenderContext.Antialiasing.__doc__ = "Use antialiasing while drawing"
QgsRenderContext.RenderPartialOutput = Qgis.RenderContextFlag.RenderPartialOutput
QgsRenderContext.RenderPartialOutput.is_monkey_patched = True
QgsRenderContext.RenderPartialOutput.__doc__ = "Whether to make extra effort to update map image with partially rendered layers (better for interactive map canvas). Added in QGIS 3.0"
QgsRenderContext.RenderPreviewJob = Qgis.RenderContextFlag.RenderPreviewJob
QgsRenderContext.RenderPreviewJob.is_monkey_patched = True
QgsRenderContext.RenderPreviewJob.__doc__ = "Render is a 'canvas preview' render, and shortcuts should be taken to ensure fast rendering"
QgsRenderContext.RenderBlocking = Qgis.RenderContextFlag.RenderBlocking
QgsRenderContext.RenderBlocking.is_monkey_patched = True
QgsRenderContext.RenderBlocking.__doc__ = "Render and load remote sources in the same thread to ensure rendering remote sources (svg and images). WARNING: this flag must NEVER be used from GUI based applications (like the main QGIS application) or crashes will result. Only for use in external scripts or QGIS server."
QgsRenderContext.RenderSymbolPreview = Qgis.RenderContextFlag.RenderSymbolPreview
QgsRenderContext.RenderSymbolPreview.is_monkey_patched = True
QgsRenderContext.RenderSymbolPreview.__doc__ = "The render is for a symbol preview only and map based properties may not be available, so care should be taken to handle map unit based sizes in an appropriate way."
QgsRenderContext.LosslessImageRendering = Qgis.RenderContextFlag.LosslessImageRendering
QgsRenderContext.LosslessImageRendering.is_monkey_patched = True
QgsRenderContext.LosslessImageRendering.__doc__ = "Render images losslessly whenever possible, instead of the default lossy jpeg rendering used for some destination devices (e.g. PDF). This flag only works with builds based on Qt 5.13 or later."
QgsRenderContext.ApplyScalingWorkaroundForTextRendering = Qgis.RenderContextFlag.ApplyScalingWorkaroundForTextRendering
QgsRenderContext.ApplyScalingWorkaroundForTextRendering.is_monkey_patched = True
QgsRenderContext.ApplyScalingWorkaroundForTextRendering.__doc__ = "Whether a scaling workaround designed to stablise the rendering of small font sizes (or for painters scaled out by a large amount) when rendering text. Generally this is recommended, but it may incur some performance cost."
QgsRenderContext.Render3DMap = Qgis.RenderContextFlag.Render3DMap
QgsRenderContext.Render3DMap.is_monkey_patched = True
QgsRenderContext.Render3DMap.__doc__ = "Render is for a 3D map"
QgsRenderContext.ApplyClipAfterReprojection = Qgis.RenderContextFlag.ApplyClipAfterReprojection
QgsRenderContext.ApplyClipAfterReprojection.is_monkey_patched = True
QgsRenderContext.ApplyClipAfterReprojection.__doc__ = "Feature geometry clipping to mapExtent() must be performed after the geometries are transformed using coordinateTransform(). Usually feature geometry clipping occurs using the extent() in the layer's CRS prior to geometry transformation, but in some cases when extent() could not be accurately calculated it is necessary to clip geometries to mapExtent() AFTER transforming them using coordinateTransform()."
QgsRenderContext.RenderingSubSymbol = Qgis.RenderContextFlag.RenderingSubSymbol
QgsRenderContext.RenderingSubSymbol.is_monkey_patched = True
QgsRenderContext.RenderingSubSymbol.__doc__ = "Set whenever a sub-symbol of a parent symbol is currently being rendered. Can be used during symbol and symbol layer rendering to determine whether the symbol being rendered is a subsymbol. (Since QGIS 3.24)"
QgsRenderContext.HighQualityImageTransforms = Qgis.RenderContextFlag.HighQualityImageTransforms
QgsRenderContext.HighQualityImageTransforms.is_monkey_patched = True
QgsRenderContext.HighQualityImageTransforms.__doc__ = "Enable high quality image transformations, which results in better appearance of scaled or rotated raster components of a map (since QGIS 3.24)"
QgsRenderContext.SkipSymbolRendering = Qgis.RenderContextFlag.SkipSymbolRendering
QgsRenderContext.SkipSymbolRendering.is_monkey_patched = True
QgsRenderContext.SkipSymbolRendering.__doc__ = "Disable symbol rendering while still drawing labels if enabled (since QGIS 3.24)"
Qgis.RenderContextFlag.__doc__ = 'Flags which affect rendering operations.\n\n.. versionadded:: 3.22\n\n' + '* ``DrawEditingInfo``: ' + Qgis.RenderContextFlag.DrawEditingInfo.__doc__ + '\n' + '* ``ForceVectorOutput``: ' + Qgis.RenderContextFlag.ForceVectorOutput.__doc__ + '\n' + '* ``UseAdvancedEffects``: ' + Qgis.RenderContextFlag.UseAdvancedEffects.__doc__ + '\n' + '* ``UseRenderingOptimization``: ' + Qgis.RenderContextFlag.UseRenderingOptimization.__doc__ + '\n' + '* ``DrawSelection``: ' + Qgis.RenderContextFlag.DrawSelection.__doc__ + '\n' + '* ``DrawSymbolBounds``: ' + Qgis.RenderContextFlag.DrawSymbolBounds.__doc__ + '\n' + '* ``RenderMapTile``: ' + Qgis.RenderContextFlag.RenderMapTile.__doc__ + '\n' + '* ``Antialiasing``: ' + Qgis.RenderContextFlag.Antialiasing.__doc__ + '\n' + '* ``RenderPartialOutput``: ' + Qgis.RenderContextFlag.RenderPartialOutput.__doc__ + '\n' + '* ``RenderPreviewJob``: ' + Qgis.RenderContextFlag.RenderPreviewJob.__doc__ + '\n' + '* ``RenderBlocking``: ' + Qgis.RenderContextFlag.RenderBlocking.__doc__ + '\n' + '* ``RenderSymbolPreview``: ' + Qgis.RenderContextFlag.RenderSymbolPreview.__doc__ + '\n' + '* ``LosslessImageRendering``: ' + Qgis.RenderContextFlag.LosslessImageRendering.__doc__ + '\n' + '* ``ApplyScalingWorkaroundForTextRendering``: ' + Qgis.RenderContextFlag.ApplyScalingWorkaroundForTextRendering.__doc__ + '\n' + '* ``Render3DMap``: ' + Qgis.RenderContextFlag.Render3DMap.__doc__ + '\n' + '* ``ApplyClipAfterReprojection``: ' + Qgis.RenderContextFlag.ApplyClipAfterReprojection.__doc__ + '\n' + '* ``RenderingSubSymbol``: ' + Qgis.RenderContextFlag.RenderingSubSymbol.__doc__ + '\n' + '* ``HighQualityImageTransforms``: ' + Qgis.RenderContextFlag.HighQualityImageTransforms.__doc__ + '\n' + '* ``SkipSymbolRendering``: ' + Qgis.RenderContextFlag.SkipSymbolRendering.__doc__
# --
QgsRenderContext.Flags = Qgis.RenderContextFlags
Qgis.RenderContextFlag.baseClass = Qgis
Qgis.RenderContextFlags.baseClass = Qgis
RenderContextFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
QgsRenderContext.TextRenderFormat = Qgis.TextRenderFormat
# monkey patching scoped based enum
QgsRenderContext.TextFormatAlwaysOutlines = Qgis.TextRenderFormat.AlwaysOutlines
QgsRenderContext.TextFormatAlwaysOutlines.is_monkey_patched = True
QgsRenderContext.TextFormatAlwaysOutlines.__doc__ = "Always render text using path objects (AKA outlines/curves). This setting guarantees the best quality rendering, even when using a raster paint surface (where sub-pixel path based text rendering is superior to sub-pixel text-based rendering). The downside is that text is converted to paths only, so users cannot open created vector outputs for post-processing in other applications and retain text editability.  This setting also guarantees complete compatibility with the full range of formatting options available through QgsTextRenderer and QgsTextFormat, some of which may not be possible to reproduce when using a vector-based paint surface and TextFormatAlwaysText mode. A final benefit to this setting is that vector exports created using text as outlines do not require all users to have the original fonts installed in order to display the text in its original style."
QgsRenderContext.TextFormatAlwaysText = Qgis.TextRenderFormat.AlwaysText
QgsRenderContext.TextFormatAlwaysText.is_monkey_patched = True
QgsRenderContext.TextFormatAlwaysText.__doc__ = "Always render text as text objects. While this mode preserves text objects as text for post-processing in external vector editing applications, it can result in rendering artifacts or poor quality rendering, depending on the text format settings. Even with raster based paint devices, TextFormatAlwaysText can result in inferior rendering quality to TextFormatAlwaysOutlines. When rendering using TextFormatAlwaysText to a vector based device (e.g. PDF or SVG), care must be taken to ensure that the required fonts are available to users when opening the created files, or default fallback fonts will be used to display the output instead. (Although PDF exports MAY automatically embed some fonts when possible, depending on the user's platform)."
Qgis.TextRenderFormat.__doc__ = 'Options for rendering text.\n\n.. versionadded:: 3.22\n\n' + '* ``TextFormatAlwaysOutlines``: ' + Qgis.TextRenderFormat.AlwaysOutlines.__doc__ + '\n' + '* ``TextFormatAlwaysText``: ' + Qgis.TextRenderFormat.AlwaysText.__doc__
# --
Qgis.TextRenderFormat.baseClass = Qgis
# monkey patching scoped based enum
Qgis.RenderSubcomponentProperty.Generic.__doc__ = "Generic subcomponent property"
Qgis.RenderSubcomponentProperty.ShadowOffset.__doc__ = "Shadow offset"
Qgis.RenderSubcomponentProperty.BlurSize.__doc__ = "Blur size"
Qgis.RenderSubcomponentProperty.GlowSpread.__doc__ = "Glow spread size"
Qgis.RenderSubcomponentProperty.__doc__ = 'Rendering subcomponent properties.\n\n.. versionadded:: 3.22\n\n' + '* ``Generic``: ' + Qgis.RenderSubcomponentProperty.Generic.__doc__ + '\n' + '* ``ShadowOffset``: ' + Qgis.RenderSubcomponentProperty.ShadowOffset.__doc__ + '\n' + '* ``BlurSize``: ' + Qgis.RenderSubcomponentProperty.BlurSize.__doc__ + '\n' + '* ``GlowSpread``: ' + Qgis.RenderSubcomponentProperty.GlowSpread.__doc__
# --
Qgis.RenderSubcomponentProperty.baseClass = Qgis
QgsVertexId.VertexType = Qgis.VertexType
# monkey patching scoped based enum
QgsVertexId.SegmentVertex = Qgis.VertexType.Segment
QgsVertexId.SegmentVertex.is_monkey_patched = True
QgsVertexId.SegmentVertex.__doc__ = "The actual start or end point of a segment"
QgsVertexId.CurveVertex = Qgis.VertexType.Curve
QgsVertexId.CurveVertex.is_monkey_patched = True
QgsVertexId.CurveVertex.__doc__ = "An intermediate point on a segment defining the curvature of the segment"
Qgis.VertexType.__doc__ = 'Types of vertex.\n\n.. versionadded:: 3.22\n\n' + '* ``SegmentVertex``: ' + Qgis.VertexType.Segment.__doc__ + '\n' + '* ``CurveVertex``: ' + Qgis.VertexType.Curve.__doc__
# --
Qgis.VertexType.baseClass = Qgis
QgsSimpleMarkerSymbolLayerBase.Shape = Qgis.MarkerShape
# monkey patching scoped based enum
QgsSimpleMarkerSymbolLayerBase.Square = Qgis.MarkerShape.Square
QgsSimpleMarkerSymbolLayerBase.Square.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Square.__doc__ = "Square"
QgsSimpleMarkerSymbolLayerBase.Diamond = Qgis.MarkerShape.Diamond
QgsSimpleMarkerSymbolLayerBase.Diamond.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Diamond.__doc__ = "Diamond"
QgsSimpleMarkerSymbolLayerBase.Pentagon = Qgis.MarkerShape.Pentagon
QgsSimpleMarkerSymbolLayerBase.Pentagon.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Pentagon.__doc__ = "Pentagon"
QgsSimpleMarkerSymbolLayerBase.Hexagon = Qgis.MarkerShape.Hexagon
QgsSimpleMarkerSymbolLayerBase.Hexagon.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Hexagon.__doc__ = "Hexagon"
QgsSimpleMarkerSymbolLayerBase.Triangle = Qgis.MarkerShape.Triangle
QgsSimpleMarkerSymbolLayerBase.Triangle.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Triangle.__doc__ = "Triangle"
QgsSimpleMarkerSymbolLayerBase.EquilateralTriangle = Qgis.MarkerShape.EquilateralTriangle
QgsSimpleMarkerSymbolLayerBase.EquilateralTriangle.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.EquilateralTriangle.__doc__ = "Equilateral triangle"
QgsSimpleMarkerSymbolLayerBase.Star = Qgis.MarkerShape.Star
QgsSimpleMarkerSymbolLayerBase.Star.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Star.__doc__ = "Star"
QgsSimpleMarkerSymbolLayerBase.Arrow = Qgis.MarkerShape.Arrow
QgsSimpleMarkerSymbolLayerBase.Arrow.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Arrow.__doc__ = "Arrow"
QgsSimpleMarkerSymbolLayerBase.Circle = Qgis.MarkerShape.Circle
QgsSimpleMarkerSymbolLayerBase.Circle.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Circle.__doc__ = "Circle"
QgsSimpleMarkerSymbolLayerBase.Cross = Qgis.MarkerShape.Cross
QgsSimpleMarkerSymbolLayerBase.Cross.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Cross.__doc__ = "Cross (lines only)"
QgsSimpleMarkerSymbolLayerBase.CrossFill = Qgis.MarkerShape.CrossFill
QgsSimpleMarkerSymbolLayerBase.CrossFill.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.CrossFill.__doc__ = "Solid filled cross"
QgsSimpleMarkerSymbolLayerBase.Cross2 = Qgis.MarkerShape.Cross2
QgsSimpleMarkerSymbolLayerBase.Cross2.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Cross2.__doc__ = "Rotated cross (lines only), 'x' shape"
QgsSimpleMarkerSymbolLayerBase.Line = Qgis.MarkerShape.Line
QgsSimpleMarkerSymbolLayerBase.Line.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Line.__doc__ = "Vertical line"
QgsSimpleMarkerSymbolLayerBase.ArrowHead = Qgis.MarkerShape.ArrowHead
QgsSimpleMarkerSymbolLayerBase.ArrowHead.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.ArrowHead.__doc__ = "Right facing arrow head (unfilled, lines only)"
QgsSimpleMarkerSymbolLayerBase.ArrowHeadFilled = Qgis.MarkerShape.ArrowHeadFilled
QgsSimpleMarkerSymbolLayerBase.ArrowHeadFilled.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.ArrowHeadFilled.__doc__ = "Right facing filled arrow head"
QgsSimpleMarkerSymbolLayerBase.SemiCircle = Qgis.MarkerShape.SemiCircle
QgsSimpleMarkerSymbolLayerBase.SemiCircle.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.SemiCircle.__doc__ = "Semi circle (top half)"
QgsSimpleMarkerSymbolLayerBase.ThirdCircle = Qgis.MarkerShape.ThirdCircle
QgsSimpleMarkerSymbolLayerBase.ThirdCircle.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.ThirdCircle.__doc__ = "One third circle (top left third)"
QgsSimpleMarkerSymbolLayerBase.QuarterCircle = Qgis.MarkerShape.QuarterCircle
QgsSimpleMarkerSymbolLayerBase.QuarterCircle.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.QuarterCircle.__doc__ = "Quarter circle (top left quarter)"
QgsSimpleMarkerSymbolLayerBase.QuarterSquare = Qgis.MarkerShape.QuarterSquare
QgsSimpleMarkerSymbolLayerBase.QuarterSquare.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.QuarterSquare.__doc__ = "Quarter square (top left quarter)"
QgsSimpleMarkerSymbolLayerBase.HalfSquare = Qgis.MarkerShape.HalfSquare
QgsSimpleMarkerSymbolLayerBase.HalfSquare.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.HalfSquare.__doc__ = "Half square (left half)"
QgsSimpleMarkerSymbolLayerBase.DiagonalHalfSquare = Qgis.MarkerShape.DiagonalHalfSquare
QgsSimpleMarkerSymbolLayerBase.DiagonalHalfSquare.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.DiagonalHalfSquare.__doc__ = "Diagonal half square (bottom left half)"
QgsSimpleMarkerSymbolLayerBase.RightHalfTriangle = Qgis.MarkerShape.RightHalfTriangle
QgsSimpleMarkerSymbolLayerBase.RightHalfTriangle.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.RightHalfTriangle.__doc__ = "Right half of triangle"
QgsSimpleMarkerSymbolLayerBase.LeftHalfTriangle = Qgis.MarkerShape.LeftHalfTriangle
QgsSimpleMarkerSymbolLayerBase.LeftHalfTriangle.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.LeftHalfTriangle.__doc__ = "Left half of triangle"
QgsSimpleMarkerSymbolLayerBase.Octagon = Qgis.MarkerShape.Octagon
QgsSimpleMarkerSymbolLayerBase.Octagon.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Octagon.__doc__ = "Octagon (since QGIS 3.18)"
QgsSimpleMarkerSymbolLayerBase.SquareWithCorners = Qgis.MarkerShape.SquareWithCorners
QgsSimpleMarkerSymbolLayerBase.SquareWithCorners.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.SquareWithCorners.__doc__ = "A square with diagonal corners (since QGIS 3.18)"
QgsSimpleMarkerSymbolLayerBase.AsteriskFill = Qgis.MarkerShape.AsteriskFill
QgsSimpleMarkerSymbolLayerBase.AsteriskFill.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.AsteriskFill.__doc__ = "A filled asterisk shape (since QGIS 3.18)"
QgsSimpleMarkerSymbolLayerBase.HalfArc = Qgis.MarkerShape.HalfArc
QgsSimpleMarkerSymbolLayerBase.HalfArc.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.HalfArc.__doc__ = "A line-only half arc (since QGIS 3.20)"
QgsSimpleMarkerSymbolLayerBase.ThirdArc = Qgis.MarkerShape.ThirdArc
QgsSimpleMarkerSymbolLayerBase.ThirdArc.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.ThirdArc.__doc__ = "A line-only one third arc (since QGIS 3.20)"
QgsSimpleMarkerSymbolLayerBase.QuarterArc = Qgis.MarkerShape.QuarterArc
QgsSimpleMarkerSymbolLayerBase.QuarterArc.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.QuarterArc.__doc__ = "A line-only one quarter arc (since QGIS 3.20)"
QgsSimpleMarkerSymbolLayerBase.ParallelogramRight = Qgis.MarkerShape.ParallelogramRight
QgsSimpleMarkerSymbolLayerBase.ParallelogramRight.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.ParallelogramRight.__doc__ = "Parallelogram that slants right (since QGIS 3.28)"
QgsSimpleMarkerSymbolLayerBase.ParallelogramLeft = Qgis.MarkerShape.ParallelogramLeft
QgsSimpleMarkerSymbolLayerBase.ParallelogramLeft.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.ParallelogramLeft.__doc__ = "Parallelogram that slants left (since QGIS 3.28)"
QgsSimpleMarkerSymbolLayerBase.Trapezoid = Qgis.MarkerShape.Trapezoid
QgsSimpleMarkerSymbolLayerBase.Trapezoid.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Trapezoid.__doc__ = "Trapezoid (since QGIS 3.28)"
QgsSimpleMarkerSymbolLayerBase.Shield = Qgis.MarkerShape.Shield
QgsSimpleMarkerSymbolLayerBase.Shield.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Shield.__doc__ = "A shape consisting of a triangle attached to a rectangle (since QGIS 3.28)"
QgsSimpleMarkerSymbolLayerBase.DiamondStar = Qgis.MarkerShape.DiamondStar
QgsSimpleMarkerSymbolLayerBase.DiamondStar.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.DiamondStar.__doc__ = "A 4-sided star (since QGIS 3.28)"
QgsSimpleMarkerSymbolLayerBase.Heart = Qgis.MarkerShape.Heart
QgsSimpleMarkerSymbolLayerBase.Heart.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Heart.__doc__ = "Heart (since QGIS 3.28)"
QgsSimpleMarkerSymbolLayerBase.Decagon = Qgis.MarkerShape.Decagon
QgsSimpleMarkerSymbolLayerBase.Decagon.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.Decagon.__doc__ = "Decagon (since QGIS 3.28)"
QgsSimpleMarkerSymbolLayerBase.RoundedSquare = Qgis.MarkerShape.RoundedSquare
QgsSimpleMarkerSymbolLayerBase.RoundedSquare.is_monkey_patched = True
QgsSimpleMarkerSymbolLayerBase.RoundedSquare.__doc__ = "A square with rounded corners (since QGIS 3.28)"
Qgis.MarkerShape.__doc__ = 'Marker shapes.\n\n.. note::\n\n   Prior to QGIS 3.24 this was available as :py:class:`QgsSimpleMarkerSymbolLayerBase`.Shape\n\n.. versionadded:: 3.24\n\n' + '* ``Square``: ' + Qgis.MarkerShape.Square.__doc__ + '\n' + '* ``Diamond``: ' + Qgis.MarkerShape.Diamond.__doc__ + '\n' + '* ``Pentagon``: ' + Qgis.MarkerShape.Pentagon.__doc__ + '\n' + '* ``Hexagon``: ' + Qgis.MarkerShape.Hexagon.__doc__ + '\n' + '* ``Triangle``: ' + Qgis.MarkerShape.Triangle.__doc__ + '\n' + '* ``EquilateralTriangle``: ' + Qgis.MarkerShape.EquilateralTriangle.__doc__ + '\n' + '* ``Star``: ' + Qgis.MarkerShape.Star.__doc__ + '\n' + '* ``Arrow``: ' + Qgis.MarkerShape.Arrow.__doc__ + '\n' + '* ``Circle``: ' + Qgis.MarkerShape.Circle.__doc__ + '\n' + '* ``Cross``: ' + Qgis.MarkerShape.Cross.__doc__ + '\n' + '* ``CrossFill``: ' + Qgis.MarkerShape.CrossFill.__doc__ + '\n' + '* ``Cross2``: ' + Qgis.MarkerShape.Cross2.__doc__ + '\n' + '* ``Line``: ' + Qgis.MarkerShape.Line.__doc__ + '\n' + '* ``ArrowHead``: ' + Qgis.MarkerShape.ArrowHead.__doc__ + '\n' + '* ``ArrowHeadFilled``: ' + Qgis.MarkerShape.ArrowHeadFilled.__doc__ + '\n' + '* ``SemiCircle``: ' + Qgis.MarkerShape.SemiCircle.__doc__ + '\n' + '* ``ThirdCircle``: ' + Qgis.MarkerShape.ThirdCircle.__doc__ + '\n' + '* ``QuarterCircle``: ' + Qgis.MarkerShape.QuarterCircle.__doc__ + '\n' + '* ``QuarterSquare``: ' + Qgis.MarkerShape.QuarterSquare.__doc__ + '\n' + '* ``HalfSquare``: ' + Qgis.MarkerShape.HalfSquare.__doc__ + '\n' + '* ``DiagonalHalfSquare``: ' + Qgis.MarkerShape.DiagonalHalfSquare.__doc__ + '\n' + '* ``RightHalfTriangle``: ' + Qgis.MarkerShape.RightHalfTriangle.__doc__ + '\n' + '* ``LeftHalfTriangle``: ' + Qgis.MarkerShape.LeftHalfTriangle.__doc__ + '\n' + '* ``Octagon``: ' + Qgis.MarkerShape.Octagon.__doc__ + '\n' + '* ``SquareWithCorners``: ' + Qgis.MarkerShape.SquareWithCorners.__doc__ + '\n' + '* ``AsteriskFill``: ' + Qgis.MarkerShape.AsteriskFill.__doc__ + '\n' + '* ``HalfArc``: ' + Qgis.MarkerShape.HalfArc.__doc__ + '\n' + '* ``ThirdArc``: ' + Qgis.MarkerShape.ThirdArc.__doc__ + '\n' + '* ``QuarterArc``: ' + Qgis.MarkerShape.QuarterArc.__doc__ + '\n' + '* ``ParallelogramRight``: ' + Qgis.MarkerShape.ParallelogramRight.__doc__ + '\n' + '* ``ParallelogramLeft``: ' + Qgis.MarkerShape.ParallelogramLeft.__doc__ + '\n' + '* ``Trapezoid``: ' + Qgis.MarkerShape.Trapezoid.__doc__ + '\n' + '* ``Shield``: ' + Qgis.MarkerShape.Shield.__doc__ + '\n' + '* ``DiamondStar``: ' + Qgis.MarkerShape.DiamondStar.__doc__ + '\n' + '* ``Heart``: ' + Qgis.MarkerShape.Heart.__doc__ + '\n' + '* ``Decagon``: ' + Qgis.MarkerShape.Decagon.__doc__ + '\n' + '* ``RoundedSquare``: ' + Qgis.MarkerShape.RoundedSquare.__doc__
# --
Qgis.MarkerShape.baseClass = Qgis
QgsTemplatedLineSymbolLayerBase.Placement = Qgis.MarkerLinePlacement
# monkey patching scoped based enum
QgsTemplatedLineSymbolLayerBase.Interval = Qgis.MarkerLinePlacement.Interval
QgsTemplatedLineSymbolLayerBase.Interval.is_monkey_patched = True
QgsTemplatedLineSymbolLayerBase.Interval.__doc__ = "Place symbols at regular intervals"
QgsTemplatedLineSymbolLayerBase.Vertex = Qgis.MarkerLinePlacement.Vertex
QgsTemplatedLineSymbolLayerBase.Vertex.is_monkey_patched = True
QgsTemplatedLineSymbolLayerBase.Vertex.__doc__ = "Place symbols on every vertex in the line"
QgsTemplatedLineSymbolLayerBase.LastVertex = Qgis.MarkerLinePlacement.LastVertex
QgsTemplatedLineSymbolLayerBase.LastVertex.is_monkey_patched = True
QgsTemplatedLineSymbolLayerBase.LastVertex.__doc__ = "Place symbols on the last vertex in the line"
QgsTemplatedLineSymbolLayerBase.FirstVertex = Qgis.MarkerLinePlacement.FirstVertex
QgsTemplatedLineSymbolLayerBase.FirstVertex.is_monkey_patched = True
QgsTemplatedLineSymbolLayerBase.FirstVertex.__doc__ = "Place symbols on the first vertex in the line"
QgsTemplatedLineSymbolLayerBase.CentralPoint = Qgis.MarkerLinePlacement.CentralPoint
QgsTemplatedLineSymbolLayerBase.CentralPoint.is_monkey_patched = True
QgsTemplatedLineSymbolLayerBase.CentralPoint.__doc__ = "Place symbols at the mid point of the line"
QgsTemplatedLineSymbolLayerBase.CurvePoint = Qgis.MarkerLinePlacement.CurvePoint
QgsTemplatedLineSymbolLayerBase.CurvePoint.is_monkey_patched = True
QgsTemplatedLineSymbolLayerBase.CurvePoint.__doc__ = "Place symbols at every virtual curve point in the line (used when rendering curved geometry types only)"
QgsTemplatedLineSymbolLayerBase.SegmentCenter = Qgis.MarkerLinePlacement.SegmentCenter
QgsTemplatedLineSymbolLayerBase.SegmentCenter.is_monkey_patched = True
QgsTemplatedLineSymbolLayerBase.SegmentCenter.__doc__ = "Place symbols at the center of every line segment"
QgsTemplatedLineSymbolLayerBase.InnerVertices = Qgis.MarkerLinePlacement.InnerVertices
QgsTemplatedLineSymbolLayerBase.InnerVertices.is_monkey_patched = True
QgsTemplatedLineSymbolLayerBase.InnerVertices.__doc__ = "Inner vertices (i.e. all vertices except the first and last vertex) (since QGIS 3.24)"
Qgis.MarkerLinePlacement.__doc__ = 'Defines how/where the symbols should be placed on a line.\n\n.. note::\n\n   Prior to QGIS 3.24 this was available as :py:class:`QgsTemplatedLineSymbolLayerBase`.Placement\n\n.. versionadded:: 3.24\n\n' + '* ``Interval``: ' + Qgis.MarkerLinePlacement.Interval.__doc__ + '\n' + '* ``Vertex``: ' + Qgis.MarkerLinePlacement.Vertex.__doc__ + '\n' + '* ``LastVertex``: ' + Qgis.MarkerLinePlacement.LastVertex.__doc__ + '\n' + '* ``FirstVertex``: ' + Qgis.MarkerLinePlacement.FirstVertex.__doc__ + '\n' + '* ``CentralPoint``: ' + Qgis.MarkerLinePlacement.CentralPoint.__doc__ + '\n' + '* ``CurvePoint``: ' + Qgis.MarkerLinePlacement.CurvePoint.__doc__ + '\n' + '* ``SegmentCenter``: ' + Qgis.MarkerLinePlacement.SegmentCenter.__doc__ + '\n' + '* ``InnerVertices``: ' + Qgis.MarkerLinePlacement.InnerVertices.__doc__
# --
Qgis.MarkerLinePlacement.baseClass = Qgis
Qgis.MarkerLinePlacements.baseClass = Qgis
MarkerLinePlacements = Qgis  # dirty hack since SIP seems to introduce the flags in module
QgsGradientFillSymbolLayer.GradientColorType = Qgis.GradientColorSource
# monkey patching scoped based enum
QgsGradientFillSymbolLayer.SimpleTwoColor = Qgis.GradientColorSource.SimpleTwoColor
QgsGradientFillSymbolLayer.SimpleTwoColor.is_monkey_patched = True
QgsGradientFillSymbolLayer.SimpleTwoColor.__doc__ = "Simple two color gradient"
QgsGradientFillSymbolLayer.ColorRamp = Qgis.GradientColorSource.ColorRamp
QgsGradientFillSymbolLayer.ColorRamp.is_monkey_patched = True
QgsGradientFillSymbolLayer.ColorRamp.__doc__ = "Gradient color ramp"
Qgis.GradientColorSource.__doc__ = 'Gradient color sources.\n\n.. note::\n\n   Prior to QGIS 3.24 this was available as :py:class:`QgsGradientFillSymbolLayer`.GradientColorType\n\n.. versionadded:: 3.24\n\n' + '* ``SimpleTwoColor``: ' + Qgis.GradientColorSource.SimpleTwoColor.__doc__ + '\n' + '* ``ColorRamp``: ' + Qgis.GradientColorSource.ColorRamp.__doc__
# --
Qgis.GradientColorSource.baseClass = Qgis
QgsGradientFillSymbolLayer.GradientType = Qgis.GradientType
# monkey patching scoped based enum
QgsGradientFillSymbolLayer.Linear = Qgis.GradientType.Linear
QgsGradientFillSymbolLayer.Linear.is_monkey_patched = True
QgsGradientFillSymbolLayer.Linear.__doc__ = "Linear gradient"
QgsGradientFillSymbolLayer.Radial = Qgis.GradientType.Radial
QgsGradientFillSymbolLayer.Radial.is_monkey_patched = True
QgsGradientFillSymbolLayer.Radial.__doc__ = "Radial (circular) gradient"
QgsGradientFillSymbolLayer.Conical = Qgis.GradientType.Conical
QgsGradientFillSymbolLayer.Conical.is_monkey_patched = True
QgsGradientFillSymbolLayer.Conical.__doc__ = "Conical (polar) gradient"
Qgis.GradientType.__doc__ = 'Gradient types.\n\n.. note::\n\n   Prior to QGIS 3.24 this was available as :py:class:`QgsGradientFillSymbolLayer`.GradientType\n\n.. versionadded:: 3.24\n\n' + '* ``Linear``: ' + Qgis.GradientType.Linear.__doc__ + '\n' + '* ``Radial``: ' + Qgis.GradientType.Radial.__doc__ + '\n' + '* ``Conical``: ' + Qgis.GradientType.Conical.__doc__
# --
Qgis.GradientType.baseClass = Qgis
QgsGradientFillSymbolLayer.GradientCoordinateMode = Qgis.SymbolCoordinateReference
# monkey patching scoped based enum
QgsGradientFillSymbolLayer.Feature = Qgis.SymbolCoordinateReference.Feature
QgsGradientFillSymbolLayer.Feature.is_monkey_patched = True
QgsGradientFillSymbolLayer.Feature.__doc__ = "Relative to feature/shape being rendered"
QgsGradientFillSymbolLayer.Viewport = Qgis.SymbolCoordinateReference.Viewport
QgsGradientFillSymbolLayer.Viewport.is_monkey_patched = True
QgsGradientFillSymbolLayer.Viewport.__doc__ = "Relative to the whole viewport/output device"
Qgis.SymbolCoordinateReference.__doc__ = 'Symbol coordinate reference modes.\n\n.. note::\n\n   Prior to QGIS 3.24 this was available as :py:class:`QgsGradientFillSymbolLayer`.GradientCoordinateMode\n\n.. versionadded:: 3.24\n\n' + '* ``Feature``: ' + Qgis.SymbolCoordinateReference.Feature.__doc__ + '\n' + '* ``Viewport``: ' + Qgis.SymbolCoordinateReference.Viewport.__doc__
# --
Qgis.SymbolCoordinateReference.baseClass = Qgis
QgsGradientFillSymbolLayer.GradientSpread = Qgis.GradientSpread
# monkey patching scoped based enum
QgsGradientFillSymbolLayer.Pad = Qgis.GradientSpread.Pad
QgsGradientFillSymbolLayer.Pad.is_monkey_patched = True
QgsGradientFillSymbolLayer.Pad.__doc__ = "Pad out gradient using colors at endpoint of gradient"
QgsGradientFillSymbolLayer.Reflect = Qgis.GradientSpread.Reflect
QgsGradientFillSymbolLayer.Reflect.is_monkey_patched = True
QgsGradientFillSymbolLayer.Reflect.__doc__ = "Reflect gradient"
QgsGradientFillSymbolLayer.Repeat = Qgis.GradientSpread.Repeat
QgsGradientFillSymbolLayer.Repeat.is_monkey_patched = True
QgsGradientFillSymbolLayer.Repeat.__doc__ = "Repeat gradient"
Qgis.GradientSpread.__doc__ = 'Gradient spread options, which control how gradients are rendered outside of their\nstart and end points.\n\n.. note::\n\n   Prior to QGIS 3.24 this was available as :py:class:`QgsGradientFillSymbolLayer`.GradientSpread\n\n.. versionadded:: 3.24\n\n' + '* ``Pad``: ' + Qgis.GradientSpread.Pad.__doc__ + '\n' + '* ``Reflect``: ' + Qgis.GradientSpread.Reflect.__doc__ + '\n' + '* ``Repeat``: ' + Qgis.GradientSpread.Repeat.__doc__
# --
Qgis.GradientSpread.baseClass = Qgis
QgsRandomMarkerFillSymbolLayer.CountMethod = Qgis.PointCountMethod
# monkey patching scoped based enum
QgsRandomMarkerFillSymbolLayer.AbsoluteCount = Qgis.PointCountMethod.Absolute
QgsRandomMarkerFillSymbolLayer.AbsoluteCount.is_monkey_patched = True
QgsRandomMarkerFillSymbolLayer.AbsoluteCount.__doc__ = "The point count is used as an absolute count of markers"
QgsRandomMarkerFillSymbolLayer.DensityBasedCount = Qgis.PointCountMethod.DensityBased
QgsRandomMarkerFillSymbolLayer.DensityBasedCount.is_monkey_patched = True
QgsRandomMarkerFillSymbolLayer.DensityBasedCount.__doc__ = "The point count is part of a marker density count"
Qgis.PointCountMethod.__doc__ = 'Methods which define the number of points randomly filling a polygon.\n\n.. note::\n\n   Prior to QGIS 3.24 this was available as :py:class:`QgsRandomMarkerFillSymbolLayer`.CountMethod\n\n.. versionadded:: 3.24\n\n' + '* ``AbsoluteCount``: ' + Qgis.PointCountMethod.Absolute.__doc__ + '\n' + '* ``DensityBasedCount``: ' + Qgis.PointCountMethod.DensityBased.__doc__
# --
Qgis.PointCountMethod.baseClass = Qgis
# monkey patching scoped based enum
Qgis.MarkerClipMode.NoClipping.__doc__ = "No clipping, render complete markers"
Qgis.MarkerClipMode.Shape.__doc__ = "Clip to polygon shape"
Qgis.MarkerClipMode.CentroidWithin.__doc__ = "Render complete markers wherever their centroid falls within the polygon shape"
Qgis.MarkerClipMode.CompletelyWithin.__doc__ = "Render complete markers wherever the completely fall within the polygon shape"
Qgis.MarkerClipMode.__doc__ = 'Marker clipping modes.\n\n.. versionadded:: 3.24\n\n' + '* ``NoClipping``: ' + Qgis.MarkerClipMode.NoClipping.__doc__ + '\n' + '* ``Shape``: ' + Qgis.MarkerClipMode.Shape.__doc__ + '\n' + '* ``CentroidWithin``: ' + Qgis.MarkerClipMode.CentroidWithin.__doc__ + '\n' + '* ``CompletelyWithin``: ' + Qgis.MarkerClipMode.CompletelyWithin.__doc__
# --
Qgis.MarkerClipMode.baseClass = Qgis
# monkey patching scoped based enum
Qgis.LineClipMode.ClipPainterOnly.__doc__ = "Applying clipping on the painter only (i.e. line endpoints will coincide with polygon bounding box, but will not be part of the visible portion of the line)"
Qgis.LineClipMode.ClipToIntersection.__doc__ = "Clip lines to intersection with polygon shape (slower) (i.e. line endpoints will coincide with polygon exterior)"
Qgis.LineClipMode.NoClipping.__doc__ = "Lines are not clipped, will extend to shape's bounding box."
Qgis.LineClipMode.__doc__ = 'Line clipping modes.\n\n.. versionadded:: 3.24\n\n' + '* ``ClipPainterOnly``: ' + Qgis.LineClipMode.ClipPainterOnly.__doc__ + '\n' + '* ``ClipToIntersection``: ' + Qgis.LineClipMode.ClipToIntersection.__doc__ + '\n' + '* ``NoClipping``: ' + Qgis.LineClipMode.NoClipping.__doc__
# --
Qgis.LineClipMode.baseClass = Qgis
# monkey patching scoped based enum
Qgis.DashPatternLineEndingRule.NoRule.__doc__ = "No special rule"
Qgis.DashPatternLineEndingRule.FullDash.__doc__ = "Start or finish the pattern with a full dash"
Qgis.DashPatternLineEndingRule.HalfDash.__doc__ = "Start or finish the pattern with a half length dash"
Qgis.DashPatternLineEndingRule.FullGap.__doc__ = "Start or finish the pattern with a full gap"
Qgis.DashPatternLineEndingRule.HalfGap.__doc__ = "Start or finish the pattern with a half length gap"
Qgis.DashPatternLineEndingRule.__doc__ = 'Dash pattern line ending rules.\n\n.. versionadded:: 3.24\n\n' + '* ``NoRule``: ' + Qgis.DashPatternLineEndingRule.NoRule.__doc__ + '\n' + '* ``FullDash``: ' + Qgis.DashPatternLineEndingRule.FullDash.__doc__ + '\n' + '* ``HalfDash``: ' + Qgis.DashPatternLineEndingRule.HalfDash.__doc__ + '\n' + '* ``FullGap``: ' + Qgis.DashPatternLineEndingRule.FullGap.__doc__ + '\n' + '* ``HalfGap``: ' + Qgis.DashPatternLineEndingRule.HalfGap.__doc__
# --
Qgis.DashPatternLineEndingRule.baseClass = Qgis
# monkey patching scoped based enum
Qgis.DashPatternSizeAdjustment.ScaleBothDashAndGap.__doc__ = "Both the dash and gap lengths are adjusted equally"
Qgis.DashPatternSizeAdjustment.ScaleDashOnly.__doc__ = "Only dash lengths are adjusted"
Qgis.DashPatternSizeAdjustment.ScaleGapOnly.__doc__ = "Only gap lengths are adjusted"
Qgis.DashPatternSizeAdjustment.__doc__ = 'Dash pattern size adjustment options.\n\n.. versionadded:: 3.24\n\n' + '* ``ScaleBothDashAndGap``: ' + Qgis.DashPatternSizeAdjustment.ScaleBothDashAndGap.__doc__ + '\n' + '* ``ScaleDashOnly``: ' + Qgis.DashPatternSizeAdjustment.ScaleDashOnly.__doc__ + '\n' + '* ``ScaleGapOnly``: ' + Qgis.DashPatternSizeAdjustment.ScaleGapOnly.__doc__
# --
Qgis.DashPatternSizeAdjustment.baseClass = Qgis
QgsGraduatedSymbolRenderer.GraduatedMethod = Qgis.GraduatedMethod
# monkey patching scoped based enum
QgsGraduatedSymbolRenderer.GraduatedColor = Qgis.GraduatedMethod.Color
QgsGraduatedSymbolRenderer.GraduatedColor.is_monkey_patched = True
QgsGraduatedSymbolRenderer.GraduatedColor.__doc__ = "Alter color of symbols"
QgsGraduatedSymbolRenderer.GraduatedSize = Qgis.GraduatedMethod.Size
QgsGraduatedSymbolRenderer.GraduatedSize.is_monkey_patched = True
QgsGraduatedSymbolRenderer.GraduatedSize.__doc__ = "Alter size of symbols"
Qgis.GraduatedMethod.__doc__ = 'Methods for modifying symbols by range in a graduated symbol renderer.\n\n.. note::\n\n   Prior to QGIS 3.26 this was available as :py:class:`QgsGraduatedSymbolRenderer`.GraduatedMethod\n\n.. versionadded:: 3.26\n\n' + '* ``GraduatedColor``: ' + Qgis.GraduatedMethod.Color.__doc__ + '\n' + '* ``GraduatedSize``: ' + Qgis.GraduatedMethod.Size.__doc__
# --
Qgis.GraduatedMethod.baseClass = Qgis
# monkey patching scoped based enum
Qgis.DpiMode.All.__doc__ = "All"
Qgis.DpiMode.Off.__doc__ = "Off"
Qgis.DpiMode.QGIS.__doc__ = "QGIS"
Qgis.DpiMode.UMN.__doc__ = "UMN"
Qgis.DpiMode.GeoServer.__doc__ = "GeoServer"
Qgis.DpiMode.__doc__ = 'DpiMode enum\n\n.. versionadded:: 3.26\n\n' + '* ``All``: ' + Qgis.DpiMode.All.__doc__ + '\n' + '* ``Off``: ' + Qgis.DpiMode.Off.__doc__ + '\n' + '* ``QGIS``: ' + Qgis.DpiMode.QGIS.__doc__ + '\n' + '* ``UMN``: ' + Qgis.DpiMode.UMN.__doc__ + '\n' + '* ``GeoServer``: ' + Qgis.DpiMode.GeoServer.__doc__
# --
Qgis.DpiMode.baseClass = Qgis
QgsStringUtils.Capitalization = Qgis.Capitalization
# monkey patching scoped based enum
QgsStringUtils.MixedCase = Qgis.Capitalization.MixedCase
QgsStringUtils.MixedCase.is_monkey_patched = True
QgsStringUtils.MixedCase.__doc__ = "Mixed case, ie no change"
QgsStringUtils.AllUppercase = Qgis.Capitalization.AllUppercase
QgsStringUtils.AllUppercase.is_monkey_patched = True
QgsStringUtils.AllUppercase.__doc__ = "Convert all characters to uppercase"
QgsStringUtils.AllLowercase = Qgis.Capitalization.AllLowercase
QgsStringUtils.AllLowercase.is_monkey_patched = True
QgsStringUtils.AllLowercase.__doc__ = "Convert all characters to lowercase"
QgsStringUtils.ForceFirstLetterToCapital = Qgis.Capitalization.ForceFirstLetterToCapital
QgsStringUtils.ForceFirstLetterToCapital.is_monkey_patched = True
QgsStringUtils.ForceFirstLetterToCapital.__doc__ = "Convert just the first letter of each word to uppercase, leave the rest untouched"
QgsStringUtils.SmallCaps = Qgis.Capitalization.SmallCaps
QgsStringUtils.SmallCaps.is_monkey_patched = True
QgsStringUtils.SmallCaps.__doc__ = "Mixed case small caps (since QGIS 3.24)"
QgsStringUtils.TitleCase = Qgis.Capitalization.TitleCase
QgsStringUtils.TitleCase.is_monkey_patched = True
QgsStringUtils.TitleCase.__doc__ = "Simple title case conversion - does not fully grammatically parse the text and uses simple rules only. Note that this method does not convert any characters to lowercase, it only uppercases required letters. Callers must ensure that input strings are already lowercased."
QgsStringUtils.UpperCamelCase = Qgis.Capitalization.UpperCamelCase
QgsStringUtils.UpperCamelCase.is_monkey_patched = True
QgsStringUtils.UpperCamelCase.__doc__ = "Convert the string to upper camel case. Note that this method does not unaccent characters."
QgsStringUtils.AllSmallCaps = Qgis.Capitalization.AllSmallCaps
QgsStringUtils.AllSmallCaps.is_monkey_patched = True
QgsStringUtils.AllSmallCaps.__doc__ = "Force all characters to small caps (since QGIS 3.24)"
Qgis.Capitalization.__doc__ = 'String capitalization options.\n\n.. note::\n\n   Prior to QGIS 3.24 this was available as :py:class:`QgsStringUtils`.Capitalization\n\n.. versionadded:: 3.24\n\n' + '* ``MixedCase``: ' + Qgis.Capitalization.MixedCase.__doc__ + '\n' + '* ``AllUppercase``: ' + Qgis.Capitalization.AllUppercase.__doc__ + '\n' + '* ``AllLowercase``: ' + Qgis.Capitalization.AllLowercase.__doc__ + '\n' + '* ``ForceFirstLetterToCapital``: ' + Qgis.Capitalization.ForceFirstLetterToCapital.__doc__ + '\n' + '* ``SmallCaps``: ' + Qgis.Capitalization.SmallCaps.__doc__ + '\n' + '* ``TitleCase``: ' + Qgis.Capitalization.TitleCase.__doc__ + '\n' + '* ``UpperCamelCase``: ' + Qgis.Capitalization.UpperCamelCase.__doc__ + '\n' + '* ``AllSmallCaps``: ' + Qgis.Capitalization.AllSmallCaps.__doc__
# --
Qgis.Capitalization.baseClass = Qgis
# monkey patching scoped based enum
Qgis.TextRendererFlag.WrapLines.__doc__ = "Automatically wrap long lines of text"
Qgis.TextRendererFlag.__doc__ = 'Flags which control the behavior of rendering text.\n\n.. versionadded:: 3.24\n\n' + '* ``WrapLines``: ' + Qgis.TextRendererFlag.WrapLines.__doc__
# --
Qgis.TextRendererFlag.baseClass = Qgis
Qgis.TextRendererFlags.baseClass = Qgis
TextRendererFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.ScaleToTileZoomLevelMethod.MapBox.__doc__ = "Uses a scale doubling approach to account for hi-DPI tiles, and rounds to the nearest tile level for the map scale"
Qgis.ScaleToTileZoomLevelMethod.Esri.__doc__ = "No scale doubling, always rounds down when matching to available tile levels"
Qgis.ScaleToTileZoomLevelMethod.__doc__ = 'Available methods for converting map scales to tile zoom levels.\n\n.. versionadded:: 3.26\n\n' + '* ``MapBox``: ' + Qgis.ScaleToTileZoomLevelMethod.MapBox.__doc__ + '\n' + '* ``Esri``: ' + Qgis.ScaleToTileZoomLevelMethod.Esri.__doc__
# --
Qgis.ScaleToTileZoomLevelMethod.baseClass = Qgis
QgsCurve.Orientation = Qgis.AngularDirection
# monkey patching scoped based enum
QgsCurve.Clockwise = Qgis.AngularDirection.Clockwise
QgsCurve.Clockwise.is_monkey_patched = True
QgsCurve.Clockwise.__doc__ = "Clockwise direction"
QgsCurve.CounterClockwise = Qgis.AngularDirection.CounterClockwise
QgsCurve.CounterClockwise.is_monkey_patched = True
QgsCurve.CounterClockwise.__doc__ = "Counter-clockwise direction"
Qgis.AngularDirection.__doc__ = 'Angular directions.\n\n.. versionadded:: 3.24\n\n' + '* ``Clockwise``: ' + Qgis.AngularDirection.Clockwise.__doc__ + '\n' + '* ``CounterClockwise``: ' + Qgis.AngularDirection.CounterClockwise.__doc__
# --
Qgis.AngularDirection.baseClass = Qgis
# monkey patching scoped based enum
Qgis.RendererUsage.View.__doc__ = "Renderer used for displaying on screen"
Qgis.RendererUsage.Export.__doc__ = "Renderer used for printing or exporting to a file"
Qgis.RendererUsage.Unknown.__doc__ = "Renderer used for unknown usage"
Qgis.RendererUsage.__doc__ = 'Usage of the renderer.\n\n.. versionadded:: 3.24\n\n' + '* ``View``: ' + Qgis.RendererUsage.View.__doc__ + '\n' + '* ``Export``: ' + Qgis.RendererUsage.Export.__doc__ + '\n' + '* ``Unknown``: ' + Qgis.RendererUsage.Unknown.__doc__
# --
Qgis.RendererUsage.baseClass = Qgis
# monkey patching scoped based enum
Qgis.ViewSyncModeFlag.Sync3DTo2D.__doc__ = "Synchronize 3D view camera to the main map canvas extent"
Qgis.ViewSyncModeFlag.Sync2DTo3D.__doc__ = "Update the 2D main canvas extent to include the viewed area from the 3D view"
Qgis.ViewSyncModeFlag.__doc__ = 'Synchronization of 2D map canvas and 3D view\n\n.. versionadded:: 3.26\n\n' + '* ``Sync3DTo2D``: ' + Qgis.ViewSyncModeFlag.Sync3DTo2D.__doc__ + '\n' + '* ``Sync2DTo3D``: ' + Qgis.ViewSyncModeFlag.Sync2DTo3D.__doc__
# --
Qgis.ViewSyncModeFlag.baseClass = Qgis
# monkey patching scoped based enum
Qgis.HistoryProviderBackend.LocalProfile.__doc__ = "Local profile"
Qgis.HistoryProviderBackend.__doc__ = 'History provider backends.\n\n.. versionadded:: 3.24\n\n' + '* ``LocalProfile``: ' + Qgis.HistoryProviderBackend.LocalProfile.__doc__
# --
Qgis.HistoryProviderBackend.baseClass = Qgis
Qgis.HistoryProviderBackends.baseClass = Qgis
HistoryProviderBackends = Qgis  # dirty hack since SIP seems to introduce the flags in module
QgsCoordinateReferenceSystem.Format = Qgis.CrsDefinitionFormat
# monkey patching scoped based enum
QgsCoordinateReferenceSystem.FormatWkt = Qgis.CrsDefinitionFormat.Wkt
QgsCoordinateReferenceSystem.FormatWkt.is_monkey_patched = True
QgsCoordinateReferenceSystem.FormatWkt.__doc__ = "WKT format (always recommended over proj string format)"
QgsCoordinateReferenceSystem.FormatProj = Qgis.CrsDefinitionFormat.Proj
QgsCoordinateReferenceSystem.FormatProj.is_monkey_patched = True
QgsCoordinateReferenceSystem.FormatProj.__doc__ = "Proj string format"
Qgis.CrsDefinitionFormat.__doc__ = 'CRS definition formats.\n\n.. versionadded:: 3.24\n\n' + '* ``FormatWkt``: ' + Qgis.CrsDefinitionFormat.Wkt.__doc__ + '\n' + '* ``FormatProj``: ' + Qgis.CrsDefinitionFormat.Proj.__doc__
# --
Qgis.CrsDefinitionFormat.baseClass = Qgis
# monkey patching scoped based enum
Qgis.FieldDomainSplitPolicy.DefaultValue.__doc__ = "Use default field value"
Qgis.FieldDomainSplitPolicy.Duplicate.__doc__ = "Duplicate original value"
Qgis.FieldDomainSplitPolicy.GeometryRatio.__doc__ = "New values are computed by the ratio of their area/length compared to the area/length of the original feature"
Qgis.FieldDomainSplitPolicy.__doc__ = 'Split policy for field domains.\n\nWhen a feature is split into multiple parts, defines how the value of attributes\nfollowing the domain are computed.\n\n.. versionadded:: 3.26\n\n' + '* ``DefaultValue``: ' + Qgis.FieldDomainSplitPolicy.DefaultValue.__doc__ + '\n' + '* ``Duplicate``: ' + Qgis.FieldDomainSplitPolicy.Duplicate.__doc__ + '\n' + '* ``GeometryRatio``: ' + Qgis.FieldDomainSplitPolicy.GeometryRatio.__doc__
# --
Qgis.FieldDomainSplitPolicy.baseClass = Qgis
# monkey patching scoped based enum
Qgis.FieldDomainMergePolicy.DefaultValue.__doc__ = "Use default field value"
Qgis.FieldDomainMergePolicy.Sum.__doc__ = "Sum of values"
Qgis.FieldDomainMergePolicy.GeometryWeighted.__doc__ = "New values are computed as the weighted average of the source values"
Qgis.FieldDomainMergePolicy.__doc__ = 'Merge policy for field domains.\n\nWhen a feature is built by merging multiple features, defines how the value of\nattributes following the domain are computed.\n\n.. versionadded:: 3.26\n\n' + '* ``DefaultValue``: ' + Qgis.FieldDomainMergePolicy.DefaultValue.__doc__ + '\n' + '* ``Sum``: ' + Qgis.FieldDomainMergePolicy.Sum.__doc__ + '\n' + '* ``GeometryWeighted``: ' + Qgis.FieldDomainMergePolicy.GeometryWeighted.__doc__
# --
Qgis.FieldDomainMergePolicy.baseClass = Qgis
# monkey patching scoped based enum
Qgis.FieldDomainType.Coded.__doc__ = "Coded field domain"
Qgis.FieldDomainType.Range.__doc__ = "Numeric range field domain (min/max)"
Qgis.FieldDomainType.Glob.__doc__ = "Glob string pattern field domain"
Qgis.FieldDomainType.__doc__ = 'Types of field domain\n\n.. versionadded:: 3.26\n\n' + '* ``Coded``: ' + Qgis.FieldDomainType.Coded.__doc__ + '\n' + '* ``Range``: ' + Qgis.FieldDomainType.Range.__doc__ + '\n' + '* ``Glob``: ' + Qgis.FieldDomainType.Glob.__doc__
# --
Qgis.FieldDomainType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.TransactionMode.Disabled.__doc__ = "Edits are buffered locally and sent to the provider when toggling layer editing mode."
Qgis.TransactionMode.AutomaticGroups.__doc__ = "Automatic transactional editing means that on supported datasources (postgres and geopackage databases) the edit state of all tables that originate from the same database are synchronized and executed in a server side transaction."
Qgis.TransactionMode.BufferedGroups.__doc__ = "Buffered transactional editing means that all editable layers in the buffered transaction group are toggled synchronously and all edits are saved in a local edit buffer. Saving changes is executed within a single transaction on all layers (per provider)."
Qgis.TransactionMode.__doc__ = 'Transaction mode.\n\n.. versionadded:: 3.26\n\n' + '* ``Disabled``: ' + Qgis.TransactionMode.Disabled.__doc__ + '\n' + '* ``AutomaticGroups``: ' + Qgis.TransactionMode.AutomaticGroups.__doc__ + '\n' + '* ``BufferedGroups``: ' + Qgis.TransactionMode.BufferedGroups.__doc__
# --
Qgis.TransactionMode.baseClass = Qgis
# monkey patching scoped based enum
Qgis.AltitudeClamping.Absolute.__doc__ = "Elevation is taken directly from feature and is independent of terrain height (final elevation = feature elevation)"
Qgis.AltitudeClamping.Relative.__doc__ = "Elevation is relative to terrain height (final elevation = terrain elevation + feature elevation)"
Qgis.AltitudeClamping.Terrain.__doc__ = "Elevation is clamped to terrain (final elevation = terrain elevation)"
Qgis.AltitudeClamping.__doc__ = 'Altitude clamping.\n\n.. versionadded:: 3.26\n\n' + '* ``Absolute``: ' + Qgis.AltitudeClamping.Absolute.__doc__ + '\n' + '* ``Relative``: ' + Qgis.AltitudeClamping.Relative.__doc__ + '\n' + '* ``Terrain``: ' + Qgis.AltitudeClamping.Terrain.__doc__
# --
Qgis.AltitudeClamping.baseClass = Qgis
# monkey patching scoped based enum
Qgis.AltitudeBinding.Vertex.__doc__ = "Clamp every vertex of feature"
Qgis.AltitudeBinding.Centroid.__doc__ = "Clamp just centroid of feature"
Qgis.AltitudeBinding.__doc__ = 'Altitude binding.\n\n.. versionadded:: 3.26\n\n' + '* ``Vertex``: ' + Qgis.AltitudeBinding.Vertex.__doc__ + '\n' + '* ``Centroid``: ' + Qgis.AltitudeBinding.Centroid.__doc__
# --
Qgis.AltitudeBinding.baseClass = Qgis
# monkey patching scoped based enum
Qgis.NoConstraint = Qgis.BetweenLineConstraint.NoConstraint
Qgis.NoConstraint.is_monkey_patched = True
Qgis.BetweenLineConstraint.NoConstraint.__doc__ = "No additional constraint"
Qgis.Perpendicular = Qgis.BetweenLineConstraint.Perpendicular
Qgis.Perpendicular.is_monkey_patched = True
Qgis.BetweenLineConstraint.Perpendicular.__doc__ = "Perpendicular"
Qgis.Parallel = Qgis.BetweenLineConstraint.Parallel
Qgis.Parallel.is_monkey_patched = True
Qgis.BetweenLineConstraint.Parallel.__doc__ = "Parallel"
Qgis.BetweenLineConstraint.__doc__ = 'Between line constraints which can be enabled\n\n.. versionadded:: 3.26\n\n' + '* ``NoConstraint``: ' + Qgis.BetweenLineConstraint.NoConstraint.__doc__ + '\n' + '* ``Perpendicular``: ' + Qgis.BetweenLineConstraint.Perpendicular.__doc__ + '\n' + '* ``Parallel``: ' + Qgis.BetweenLineConstraint.Parallel.__doc__
# --
Qgis.BetweenLineConstraint.baseClass = Qgis
# monkey patching scoped based enum
Qgis.LineExtensionSide.BeforeVertex.__doc__ = "Lock to previous vertex"
Qgis.LineExtensionSide.AfterVertex.__doc__ = "Lock to next vertex"
Qgis.LineExtensionSide.NoVertex.__doc__ = "Don't lock to vertex"
Qgis.LineExtensionSide.__doc__ = 'Designates whether the line extension constraint is currently soft locked\nwith the previous or next vertex of the locked one.\n\n.. versionadded:: 3.26\n\n' + '* ``BeforeVertex``: ' + Qgis.LineExtensionSide.BeforeVertex.__doc__ + '\n' + '* ``AfterVertex``: ' + Qgis.LineExtensionSide.AfterVertex.__doc__ + '\n' + '* ``NoVertex``: ' + Qgis.LineExtensionSide.NoVertex.__doc__
# --
Qgis.LineExtensionSide.baseClass = Qgis
# monkey patching scoped based enum
Qgis.ProjectFlag.EvaluateDefaultValuesOnProviderSide.__doc__ = "If set, default values for fields will be evaluated on the provider side when features from the project are created instead of when they are committed."
Qgis.ProjectFlag.TrustStoredLayerStatistics.__doc__ = "If set, then layer statistics (such as the layer extent) will be read from values stored in the project instead of requesting updated values from the data provider. Additionally, when this flag is set, primary key unicity is not checked for views and materialized views with Postgres provider."
Qgis.ProjectFlag.RememberLayerEditStatusBetweenSessions.__doc__ = "If set, then any layers set to be editable will be stored in the project and immediately made editable whenever that project is restored"
Qgis.ProjectFlag.RememberAttributeTableWindowsBetweenSessions.__doc__ = "If set, then any open attribute tables will be stored in the project and immediately reopened when the project is restored"
Qgis.ProjectFlag.__doc__ = 'Flags which control the behavior of :py:class:`QgsProjects`.\n\n.. versionadded:: 3.26\n\n' + '* ``EvaluateDefaultValuesOnProviderSide``: ' + Qgis.ProjectFlag.EvaluateDefaultValuesOnProviderSide.__doc__ + '\n' + '* ``TrustStoredLayerStatistics``: ' + Qgis.ProjectFlag.TrustStoredLayerStatistics.__doc__ + '\n' + '* ``RememberLayerEditStatusBetweenSessions``: ' + Qgis.ProjectFlag.RememberLayerEditStatusBetweenSessions.__doc__ + '\n' + '* ``RememberAttributeTableWindowsBetweenSessions``: ' + Qgis.ProjectFlag.RememberAttributeTableWindowsBetweenSessions.__doc__
# --
Qgis.ProjectFlag.baseClass = Qgis
Qgis.ProjectFlags.baseClass = Qgis
ProjectFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.PlotToolFlag.ShowContextMenu.__doc__ = "Show a context menu when right-clicking with the tool."
Qgis.PlotToolFlag.__doc__ = 'Flags that control the way the :py:class:`QgsPlotTools` operate.\n\n.. versionadded:: 3.26\n\n' + '* ``ShowContextMenu``: ' + Qgis.PlotToolFlag.ShowContextMenu.__doc__
# --
Qgis.PlotToolFlag.baseClass = Qgis
Qgis.PlotToolFlags.baseClass = Qgis
PlotToolFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.LightSourceType.Point.__doc__ = "Point light source"
Qgis.LightSourceType.Directional.__doc__ = "Directional light source"
Qgis.LightSourceType.__doc__ = 'Light source types for 3D scenes.\n\n.. versionadded:: 3.26\n\n' + '* ``Point``: ' + Qgis.LightSourceType.Point.__doc__ + '\n' + '* ``Directional``: ' + Qgis.LightSourceType.Directional.__doc__
# --
Qgis.LightSourceType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.ProfileSurfaceSymbology.Line.__doc__ = "The elevation surface will be rendered using a line symbol"
Qgis.ProfileSurfaceSymbology.FillBelow.__doc__ = "The elevation surface will be rendered using a fill symbol below the surface level"
Qgis.ProfileSurfaceSymbology.__doc__ = 'Surface symbology type for elevation profile plots.\n\n.. versionadded:: 3.26\n\n' + '* ``Line``: ' + Qgis.ProfileSurfaceSymbology.Line.__doc__ + '\n' + '* ``FillBelow``: ' + Qgis.ProfileSurfaceSymbology.FillBelow.__doc__
# --
Qgis.ProfileSurfaceSymbology.baseClass = Qgis
# monkey patching scoped based enum
Qgis.VectorProfileType.IndividualFeatures.__doc__ = "Treat each feature as an individual object (eg buildings)"
Qgis.VectorProfileType.ContinuousSurface.__doc__ = "The features should be treated as representing values on a continuous surface (eg contour lines)"
Qgis.VectorProfileType.__doc__ = 'Types of elevation profiles to generate for vector sources.\n\n.. versionadded:: 3.26\n\n' + '* ``IndividualFeatures``: ' + Qgis.VectorProfileType.IndividualFeatures.__doc__ + '\n' + '* ``ContinuousSurface``: ' + Qgis.VectorProfileType.ContinuousSurface.__doc__
# --
Qgis.VectorProfileType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.ProfileGeneratorFlag.RespectsMaximumErrorMapUnit.__doc__ = "Generated profile respects the QgsProfileGenerationContext.maximumErrorMapUnits() property."
Qgis.ProfileGeneratorFlag.RespectsDistanceRange.__doc__ = "Generated profile respects the QgsProfileGenerationContext.distanceRange() property."
Qgis.ProfileGeneratorFlag.RespectsElevationRange.__doc__ = "Generated profile respects the QgsProfileGenerationContext.elevationRange() property."
Qgis.ProfileGeneratorFlag.__doc__ = 'Flags that control the way the :py:class:`QgsAbstractProfileGenerator` operate.\n\n.. versionadded:: 3.26\n\n' + '* ``RespectsMaximumErrorMapUnit``: ' + Qgis.ProfileGeneratorFlag.RespectsMaximumErrorMapUnit.__doc__ + '\n' + '* ``RespectsDistanceRange``: ' + Qgis.ProfileGeneratorFlag.RespectsDistanceRange.__doc__ + '\n' + '* ``RespectsElevationRange``: ' + Qgis.ProfileGeneratorFlag.RespectsElevationRange.__doc__
# --
Qgis.ProfileGeneratorFlag.baseClass = Qgis
Qgis.ProfileGeneratorFlags.baseClass = Qgis
ProfileGeneratorFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
QgsPointCloudRenderer.PointSymbol = Qgis.PointCloudSymbol
# monkey patching scoped based enum
QgsPointCloudRenderer.Square = Qgis.PointCloudSymbol.Square
QgsPointCloudRenderer.Square.is_monkey_patched = True
QgsPointCloudRenderer.Square.__doc__ = "Renders points as squares"
QgsPointCloudRenderer.Circle = Qgis.PointCloudSymbol.Circle
QgsPointCloudRenderer.Circle.is_monkey_patched = True
QgsPointCloudRenderer.Circle.__doc__ = "Renders points as circles"
Qgis.PointCloudSymbol.__doc__ = 'Rendering symbols for point cloud points.\n\n.. versionadded:: 3.26\n\n' + '* ``Square``: ' + Qgis.PointCloudSymbol.Square.__doc__ + '\n' + '* ``Circle``: ' + Qgis.PointCloudSymbol.Circle.__doc__
# --
Qgis.PointCloudSymbol.baseClass = Qgis
QgsPointCloudRenderer.DrawOrder = Qgis.PointCloudDrawOrder
# monkey patching scoped based enum
QgsPointCloudRenderer.Default = Qgis.PointCloudDrawOrder.Default
QgsPointCloudRenderer.Default.is_monkey_patched = True
QgsPointCloudRenderer.Default.__doc__ = "Draw points in the order they are stored"
QgsPointCloudRenderer.BottomToTop = Qgis.PointCloudDrawOrder.BottomToTop
QgsPointCloudRenderer.BottomToTop.is_monkey_patched = True
QgsPointCloudRenderer.BottomToTop.__doc__ = "Draw points with larger Z values last"
QgsPointCloudRenderer.TopToBottom = Qgis.PointCloudDrawOrder.TopToBottom
QgsPointCloudRenderer.TopToBottom.is_monkey_patched = True
QgsPointCloudRenderer.TopToBottom.__doc__ = "Draw points with larger Z values first"
Qgis.PointCloudDrawOrder.__doc__ = 'Pointcloud rendering order for 2d views\n\n/since QGIS 3.26\n\n' + '* ``Default``: ' + Qgis.PointCloudDrawOrder.Default.__doc__ + '\n' + '* ``BottomToTop``: ' + Qgis.PointCloudDrawOrder.BottomToTop.__doc__ + '\n' + '* ``TopToBottom``: ' + Qgis.PointCloudDrawOrder.TopToBottom.__doc__
# --
Qgis.PointCloudDrawOrder.baseClass = Qgis
QgsProject.AvoidIntersectionsMode = Qgis.AvoidIntersectionsMode
# monkey patching scoped based enum
QgsProject.AllowIntersections = Qgis.AvoidIntersectionsMode.AllowIntersections
QgsProject.AllowIntersections.is_monkey_patched = True
QgsProject.AllowIntersections.__doc__ = "Overlap with any feature allowed when digitizing new features"
QgsProject.AvoidIntersectionsCurrentLayer = Qgis.AvoidIntersectionsMode.AvoidIntersectionsCurrentLayer
QgsProject.AvoidIntersectionsCurrentLayer.is_monkey_patched = True
QgsProject.AvoidIntersectionsCurrentLayer.__doc__ = "Overlap with features from the active layer when digitizing new features not allowed"
QgsProject.AvoidIntersectionsLayers = Qgis.AvoidIntersectionsMode.AvoidIntersectionsLayers
QgsProject.AvoidIntersectionsLayers.is_monkey_patched = True
QgsProject.AvoidIntersectionsLayers.__doc__ = "Overlap with features from a specified list of layers when digitizing new features not allowed"
Qgis.AvoidIntersectionsMode.__doc__ = 'Flags which control how intersections of pre-existing feature are handled when digitizing new features.\n\n.. note::\n\n   Prior to QGIS 3.26 this was available as :py:class:`QgsProject`.AvoidIntersectionsMode\n\n.. versionadded:: 3.26\n\n' + '* ``AllowIntersections``: ' + Qgis.AvoidIntersectionsMode.AllowIntersections.__doc__ + '\n' + '* ``AvoidIntersectionsCurrentLayer``: ' + Qgis.AvoidIntersectionsMode.AvoidIntersectionsCurrentLayer.__doc__ + '\n' + '* ``AvoidIntersectionsLayers``: ' + Qgis.AvoidIntersectionsMode.AvoidIntersectionsLayers.__doc__
# --
Qgis.AvoidIntersectionsMode.baseClass = Qgis
QgsProject.FileFormat = Qgis.ProjectFileFormat
# monkey patching scoped based enum
QgsProject.Qgz = Qgis.ProjectFileFormat.Qgz
QgsProject.Qgz.is_monkey_patched = True
QgsProject.Qgz.__doc__ = "Archive file format, supports auxiliary data"
QgsProject.Qgs = Qgis.ProjectFileFormat.Qgs
QgsProject.Qgs.is_monkey_patched = True
QgsProject.Qgs.__doc__ = "Project saved in a clear text, does not support auxiliary data"
Qgis.ProjectFileFormat.__doc__ = 'Flags which control project read behavior.\n\n.. note::\n\n   Prior to QGIS 3.26 this was available as :py:class:`QgsProject`.FileFormat\n\n.. versionadded:: 3.26\n\n' + '* ``Qgz``: ' + Qgis.ProjectFileFormat.Qgz.__doc__ + '\n' + '* ``Qgs``: ' + Qgis.ProjectFileFormat.Qgs.__doc__
# --
Qgis.ProjectFileFormat.baseClass = Qgis
QgsProject.ReadFlag = Qgis.ProjectReadFlag
# monkey patching scoped based enum
QgsProject.FlagDontResolveLayers = Qgis.ProjectReadFlag.DontResolveLayers
QgsProject.FlagDontResolveLayers.is_monkey_patched = True
QgsProject.FlagDontResolveLayers.__doc__ = "Don't resolve layer paths (i.e. don't load any layer content). Dramatically improves project read time if the actual data from the layers is not required."
QgsProject.FlagDontLoadLayouts = Qgis.ProjectReadFlag.DontLoadLayouts
QgsProject.FlagDontLoadLayouts.is_monkey_patched = True
QgsProject.FlagDontLoadLayouts.__doc__ = "Don't load print layouts. Improves project read time if layouts are not required, and allows projects to be safely read in background threads (since print layouts are not thread safe)."
QgsProject.FlagTrustLayerMetadata = Qgis.ProjectReadFlag.TrustLayerMetadata
QgsProject.FlagTrustLayerMetadata.is_monkey_patched = True
QgsProject.FlagTrustLayerMetadata.__doc__ = "Trust layer metadata. Improves project read time. Do not use it if layers' extent is not fixed during the project's use by QGIS and QGIS Server."
QgsProject.FlagDontStoreOriginalStyles = Qgis.ProjectReadFlag.DontStoreOriginalStyles
QgsProject.FlagDontStoreOriginalStyles.is_monkey_patched = True
QgsProject.FlagDontStoreOriginalStyles.__doc__ = "Skip the initial XML style storage for layers. Useful for minimising project load times in non-interactive contexts."
QgsProject.FlagDontLoad3DViews = Qgis.ProjectReadFlag.DontLoad3DViews
QgsProject.FlagDontLoad3DViews.is_monkey_patched = True
QgsProject.FlagDontLoad3DViews.__doc__ = "Skip loading 3D views (since QGIS 3.26)"
QgsProject.DontLoadProjectStyles = Qgis.ProjectReadFlag.DontLoadProjectStyles
QgsProject.DontLoadProjectStyles.is_monkey_patched = True
QgsProject.DontLoadProjectStyles.__doc__ = "Skip loading project style databases (deprecated -- use ProjectCapability.ProjectStyles flag instead)"
Qgis.ProjectReadFlag.__doc__ = 'Flags which control project read behavior.\n\n.. note::\n\n   Prior to QGIS 3.26 this was available as :py:class:`QgsProject`.ReadFlag\n\n.. versionadded:: 3.26\n\n' + '* ``FlagDontResolveLayers``: ' + Qgis.ProjectReadFlag.DontResolveLayers.__doc__ + '\n' + '* ``FlagDontLoadLayouts``: ' + Qgis.ProjectReadFlag.DontLoadLayouts.__doc__ + '\n' + '* ``FlagTrustLayerMetadata``: ' + Qgis.ProjectReadFlag.TrustLayerMetadata.__doc__ + '\n' + '* ``FlagDontStoreOriginalStyles``: ' + Qgis.ProjectReadFlag.DontStoreOriginalStyles.__doc__ + '\n' + '* ``FlagDontLoad3DViews``: ' + Qgis.ProjectReadFlag.DontLoad3DViews.__doc__ + '\n' + '* ``DontLoadProjectStyles``: ' + Qgis.ProjectReadFlag.DontLoadProjectStyles.__doc__
# --
Qgis.ProjectReadFlag.baseClass = Qgis
QgsProject.ReadFlags = Qgis.ProjectReadFlags
Qgis.ProjectReadFlags.baseClass = Qgis
ProjectReadFlags = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.ProjectCapability.ProjectStyles.__doc__ = "Enable the project embedded style library. Enabling this flag can increase the time required to clear and load projects."
Qgis.ProjectCapability.__doc__ = 'Flags which control project capabilities.\n\nThese flags are specific upfront on creation of a :py:class:`QgsProject` object, and can\nbe used to selectively enable potentially costly functionality for the project.\n\n.. versionadded:: 3.26.1\n\n' + '* ``ProjectStyles``: ' + Qgis.ProjectCapability.ProjectStyles.__doc__
# --
Qgis.ProjectCapability.baseClass = Qgis
Qgis.ProjectCapabilities.baseClass = Qgis
ProjectCapabilities = Qgis  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
Qgis.MapBoxGlStyleSourceType.Vector.__doc__ = "Vector source"
Qgis.MapBoxGlStyleSourceType.Raster.__doc__ = "Raster source"
Qgis.MapBoxGlStyleSourceType.RasterDem.__doc__ = "Raster DEM source"
Qgis.MapBoxGlStyleSourceType.GeoJson.__doc__ = "GeoJSON source"
Qgis.MapBoxGlStyleSourceType.Image.__doc__ = "Image source"
Qgis.MapBoxGlStyleSourceType.Video.__doc__ = "Video source"
Qgis.MapBoxGlStyleSourceType.Unknown.__doc__ = "Other/unknown source type"
Qgis.MapBoxGlStyleSourceType.__doc__ = 'Available MapBox GL style source types.\n\n.. versionadded:: 3.28\n\n' + '* ``Vector``: ' + Qgis.MapBoxGlStyleSourceType.Vector.__doc__ + '\n' + '* ``Raster``: ' + Qgis.MapBoxGlStyleSourceType.Raster.__doc__ + '\n' + '* ``RasterDem``: ' + Qgis.MapBoxGlStyleSourceType.RasterDem.__doc__ + '\n' + '* ``GeoJson``: ' + Qgis.MapBoxGlStyleSourceType.GeoJson.__doc__ + '\n' + '* ``Image``: ' + Qgis.MapBoxGlStyleSourceType.Image.__doc__ + '\n' + '* ``Video``: ' + Qgis.MapBoxGlStyleSourceType.Video.__doc__ + '\n' + '* ``Unknown``: ' + Qgis.MapBoxGlStyleSourceType.Unknown.__doc__
# --
Qgis.MapBoxGlStyleSourceType.baseClass = Qgis
QgsArcGisPortalUtils.ItemType = Qgis.ArcGisRestServiceType
# monkey patching scoped based enum
QgsArcGisPortalUtils.FeatureService = Qgis.ArcGisRestServiceType.FeatureServer
QgsArcGisPortalUtils.FeatureService.is_monkey_patched = True
QgsArcGisPortalUtils.FeatureService.__doc__ = "FeatureServer"
QgsArcGisPortalUtils.MapService = Qgis.ArcGisRestServiceType.MapServer
QgsArcGisPortalUtils.MapService.is_monkey_patched = True
QgsArcGisPortalUtils.MapService.__doc__ = "MapServer"
QgsArcGisPortalUtils.ImageService = Qgis.ArcGisRestServiceType.ImageServer
QgsArcGisPortalUtils.ImageService.is_monkey_patched = True
QgsArcGisPortalUtils.ImageService.__doc__ = "ImageServer"
QgsArcGisPortalUtils.GlobeServer = Qgis.ArcGisRestServiceType.GlobeServer
QgsArcGisPortalUtils.GlobeServer.is_monkey_patched = True
QgsArcGisPortalUtils.GlobeServer.__doc__ = "GlobeServer"
QgsArcGisPortalUtils.GPServer = Qgis.ArcGisRestServiceType.GPServer
QgsArcGisPortalUtils.GPServer.is_monkey_patched = True
QgsArcGisPortalUtils.GPServer.__doc__ = "GPServer"
QgsArcGisPortalUtils.GeocodeServer = Qgis.ArcGisRestServiceType.GeocodeServer
QgsArcGisPortalUtils.GeocodeServer.is_monkey_patched = True
QgsArcGisPortalUtils.GeocodeServer.__doc__ = "GeocodeServer"
QgsArcGisPortalUtils.Unknown = Qgis.ArcGisRestServiceType.Unknown
QgsArcGisPortalUtils.Unknown.is_monkey_patched = True
QgsArcGisPortalUtils.Unknown.__doc__ = "Other unknown/unsupported type"
Qgis.ArcGisRestServiceType.__doc__ = 'Available ArcGIS REST service types.\n\n.. note::\n\n   Prior to QGIS 3.26 this was available as :py:class:`QgsArcGisPortalUtils`.ItemType.\n\n.. versionadded:: 3.28\n\n' + '* ``FeatureService``: ' + Qgis.ArcGisRestServiceType.FeatureServer.__doc__ + '\n' + '* ``MapService``: ' + Qgis.ArcGisRestServiceType.MapServer.__doc__ + '\n' + '* ``ImageService``: ' + Qgis.ArcGisRestServiceType.ImageServer.__doc__ + '\n' + '* ``GlobeServer``: ' + Qgis.ArcGisRestServiceType.GlobeServer.__doc__ + '\n' + '* ``GPServer``: ' + Qgis.ArcGisRestServiceType.GPServer.__doc__ + '\n' + '* ``GeocodeServer``: ' + Qgis.ArcGisRestServiceType.GeocodeServer.__doc__ + '\n' + '* ``Unknown``: ' + Qgis.ArcGisRestServiceType.Unknown.__doc__
# --
Qgis.ArcGisRestServiceType.baseClass = Qgis
QgsRelation.RelationType = Qgis.RelationshipType
# monkey patching scoped based enum
QgsRelation.Normal = Qgis.RelationshipType.Normal
QgsRelation.Normal.is_monkey_patched = True
QgsRelation.Normal.__doc__ = "A normal relation"
QgsRelation.Generated = Qgis.RelationshipType.Generated
QgsRelation.Generated.is_monkey_patched = True
QgsRelation.Generated.__doc__ = "A generated relation is a child of a polymorphic relation"
Qgis.RelationshipType.__doc__ = 'Relationship types.\n\n.. note::\n\n   Prior to QGIS 3.28 this was available as :py:class:`QgsRelation`.RelationType.\n\n.. versionadded:: 3.28\n\n' + '* ``Normal``: ' + Qgis.RelationshipType.Normal.__doc__ + '\n' + '* ``Generated``: ' + Qgis.RelationshipType.Generated.__doc__
# --
Qgis.RelationshipType.baseClass = Qgis
QgsRelation.RelationStrength = Qgis.RelationshipStrength
# monkey patching scoped based enum
QgsRelation.Association = Qgis.RelationshipStrength.Association
QgsRelation.Association.is_monkey_patched = True
QgsRelation.Association.__doc__ = "Loose relation, related elements are not part of the parent and a parent copy will not copy any children."
QgsRelation.Composition = Qgis.RelationshipStrength.Composition
QgsRelation.Composition.is_monkey_patched = True
QgsRelation.Composition.__doc__ = "Fix relation, related elements are part of the parent and a parent copy will copy any children or delete of parent will delete children"
Qgis.RelationshipStrength.__doc__ = 'Relationship strength.\n\n.. note::\n\n   Prior to QGIS 3.28 this was available as :py:class:`QgsRelation`.RelationStrength.\n\n.. versionadded:: 3.28\n\n' + '* ``Association``: ' + Qgis.RelationshipStrength.Association.__doc__ + '\n' + '* ``Composition``: ' + Qgis.RelationshipStrength.Composition.__doc__
# --
Qgis.RelationshipStrength.baseClass = Qgis
# monkey patching scoped based enum
Qgis.RelationshipCardinality.OneToOne.__doc__ = "One to one relationship"
Qgis.RelationshipCardinality.OneToMany.__doc__ = "One to many relationship"
Qgis.RelationshipCardinality.ManyToOne.__doc__ = "Many to one relationship"
Qgis.RelationshipCardinality.ManyToMany.__doc__ = "Many to many relationship"
Qgis.RelationshipCardinality.__doc__ = 'Relationship cardinality.\n\n.. versionadded:: 3.28\n\n' + '* ``OneToOne``: ' + Qgis.RelationshipCardinality.OneToOne.__doc__ + '\n' + '* ``OneToMany``: ' + Qgis.RelationshipCardinality.OneToMany.__doc__ + '\n' + '* ``ManyToOne``: ' + Qgis.RelationshipCardinality.ManyToOne.__doc__ + '\n' + '* ``ManyToMany``: ' + Qgis.RelationshipCardinality.ManyToMany.__doc__
# --
Qgis.RelationshipCardinality.baseClass = Qgis
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
# The following has been generated automatically from src/core/annotations/qgsannotationitemeditoperation.h
# monkey patching scoped based enum
QgsAbstractAnnotationItemEditOperation.Type.MoveNode.__doc__ = "Move a node"
QgsAbstractAnnotationItemEditOperation.Type.DeleteNode.__doc__ = "Delete a node"
QgsAbstractAnnotationItemEditOperation.Type.AddNode.__doc__ = "Add a node"
QgsAbstractAnnotationItemEditOperation.Type.TranslateItem.__doc__ = "Translate (move) an item"
QgsAbstractAnnotationItemEditOperation.Type.__doc__ = 'Operation type\n\n' + '* ``MoveNode``: ' + QgsAbstractAnnotationItemEditOperation.Type.MoveNode.__doc__ + '\n' + '* ``DeleteNode``: ' + QgsAbstractAnnotationItemEditOperation.Type.DeleteNode.__doc__ + '\n' + '* ``AddNode``: ' + QgsAbstractAnnotationItemEditOperation.Type.AddNode.__doc__ + '\n' + '* ``TranslateItem``: ' + QgsAbstractAnnotationItemEditOperation.Type.TranslateItem.__doc__
# --
# The following has been generated automatically from src/core/providers/arcgis/qgsarcgisrestutils.h
# monkey patching scoped based enum
QgsArcGisRestUtils.FeatureToJsonFlag.IncludeGeometry.__doc__ = "Whether to include the geometry definition"
QgsArcGisRestUtils.FeatureToJsonFlag.IncludeNonObjectIdAttributes.__doc__ = "Whether to include any non-objectId attributes"
QgsArcGisRestUtils.FeatureToJsonFlag.__doc__ = 'Flags which control the behavior of converting features to JSON.\n\n.. versionadded:: 3.28\n\n' + '* ``IncludeGeometry``: ' + QgsArcGisRestUtils.FeatureToJsonFlag.IncludeGeometry.__doc__ + '\n' + '* ``IncludeNonObjectIdAttributes``: ' + QgsArcGisRestUtils.FeatureToJsonFlag.IncludeNonObjectIdAttributes.__doc__
# --
QgsArcGisRestUtils.FeatureToJsonFlag.baseClass = QgsArcGisRestUtils
QgsArcGisRestUtils.FeatureToJsonFlags.baseClass = QgsArcGisRestUtils
FeatureToJsonFlags = QgsArcGisRestUtils  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/editform/qgsattributeeditorrelation.h
QgsAttributeEditorRelation.Button.baseClass = QgsAttributeEditorRelation
QgsAttributeEditorRelation.Buttons.baseClass = QgsAttributeEditorRelation
Buttons = QgsAttributeEditorRelation  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/auth/qgsauthmanager.h
QgsAuthManager.MessageLevel.baseClass = QgsAuthManager
# The following has been generated automatically from src/core/numericformats/qgscoordinatenumericformat.h
# monkey patching scoped based enum
QgsGeographicCoordinateNumericFormat.AngleFormat.DegreesMinutesSeconds.__doc__ = "Degrees, minutes and seconds, eg 30 degrees 45'30"
QgsGeographicCoordinateNumericFormat.AngleFormat.DegreesMinutes.__doc__ = "Degrees and decimal minutes, eg 30 degrees 45.55'"
QgsGeographicCoordinateNumericFormat.AngleFormat.DecimalDegrees.__doc__ = "Decimal degrees, eg 30.7555 degrees"
QgsGeographicCoordinateNumericFormat.AngleFormat.__doc__ = 'Angle format options.\n\n' + '* ``DegreesMinutesSeconds``: ' + QgsGeographicCoordinateNumericFormat.AngleFormat.DegreesMinutesSeconds.__doc__ + '\n' + '* ``DegreesMinutes``: ' + QgsGeographicCoordinateNumericFormat.AngleFormat.DegreesMinutes.__doc__ + '\n' + '* ``DecimalDegrees``: ' + QgsGeographicCoordinateNumericFormat.AngleFormat.DecimalDegrees.__doc__
# --
QgsGeographicCoordinateNumericFormat.AngleFormat.baseClass = QgsGeographicCoordinateNumericFormat
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
# The following has been generated automatically from src/core/qgsfeatureiterator.h
# monkey patching scoped based enum
QgsAbstractFeatureIterator.RequestToSourceCrsResult.Success.__doc__ = "Request was successfully updated to the source CRS, or no changes were required"
QgsAbstractFeatureIterator.RequestToSourceCrsResult.DistanceWithinMustBeCheckedManually.__doc__ = "The distance within request cannot be losslessly updated to the source CRS, and callers will need to take appropriate steps to handle the distance within requirement manually during feature iteration"
QgsAbstractFeatureIterator.RequestToSourceCrsResult.__doc__ = 'Possible results from the :py:func:`~QgsAbstractFeatureIterator.updateRequestToSourceCrs` method.\n\n.. versionadded:: 3.22\n\n' + '* ``Success``: ' + QgsAbstractFeatureIterator.RequestToSourceCrsResult.Success.__doc__ + '\n' + '* ``DistanceWithinMustBeCheckedManually``: ' + QgsAbstractFeatureIterator.RequestToSourceCrsResult.DistanceWithinMustBeCheckedManually.__doc__
# --
# The following has been generated automatically from src/core/qgsfieldproxymodel.h
QgsFieldProxyModel.Filters.baseClass = QgsFieldProxyModel
Filters = QgsFieldProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/geocoding/qgsgeocoder.h
# monkey patching scoped based enum
QgsGeocoderInterface.Flag.GeocodesStrings.__doc__ = "Can geocode string input values"
QgsGeocoderInterface.Flag.GeocodesFeatures.__doc__ = "Can geocode QgsFeature input values"
QgsGeocoderInterface.Flag.__doc__ = 'Capability flags for the geocoder.\n\n' + '* ``GeocodesStrings``: ' + QgsGeocoderInterface.Flag.GeocodesStrings.__doc__ + '\n' + '* ``GeocodesFeatures``: ' + QgsGeocoderInterface.Flag.GeocodesFeatures.__doc__
# --
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
QgsLabelLineSettings.DirectionSymbolPlacement.baseClass = QgsLabelLineSettings
# monkey patching scoped based enum
QgsLabelLineSettings.AnchorType.HintOnly.__doc__ = "Line anchor is a hint for preferred placement only, but other placements close to the hint are permitted"
QgsLabelLineSettings.AnchorType.Strict.__doc__ = "Line anchor is a strict placement, and other placements are not permitted"
QgsLabelLineSettings.AnchorType.__doc__ = 'Line anchor types\n\n' + '* ``HintOnly``: ' + QgsLabelLineSettings.AnchorType.HintOnly.__doc__ + '\n' + '* ``Strict``: ' + QgsLabelLineSettings.AnchorType.Strict.__doc__
# --
QgsLabelLineSettings.AnchorType.baseClass = QgsLabelLineSettings
# monkey patching scoped based enum
QgsLabelLineSettings.AnchorClipping.UseVisiblePartsOfLine.__doc__ = "Only visible parts of lines are considered when calculating the line anchor for labels"
QgsLabelLineSettings.AnchorClipping.UseEntireLine.__doc__ = "Entire original feature line geometry is used when calculating the line anchor for labels"
QgsLabelLineSettings.AnchorClipping.__doc__ = 'Clipping behavior for line anchor calculation.\n\n.. versionadded:: 3.20\n\n' + '* ``UseVisiblePartsOfLine``: ' + QgsLabelLineSettings.AnchorClipping.UseVisiblePartsOfLine.__doc__ + '\n' + '* ``UseEntireLine``: ' + QgsLabelLineSettings.AnchorClipping.UseEntireLine.__doc__
# --
QgsLabelLineSettings.AnchorClipping.baseClass = QgsLabelLineSettings
# monkey patching scoped based enum
QgsLabelLineSettings.AnchorTextPoint.StartOfText.__doc__ = "Anchor using start of text"
QgsLabelLineSettings.AnchorTextPoint.CenterOfText.__doc__ = "Anchor using center of text"
QgsLabelLineSettings.AnchorTextPoint.EndOfText.__doc__ = "Anchor using end of text"
QgsLabelLineSettings.AnchorTextPoint.FollowPlacement.__doc__ = "Automatically set the anchor point based on the lineAnchorPercent() value. Values <25% will use the start of text, values > 75% will use the end of text, and values in between will use the center of the text"
QgsLabelLineSettings.AnchorTextPoint.__doc__ = 'Anchor point of label text.\n\n.. versionadded:: 3.26\n\n' + '* ``StartOfText``: ' + QgsLabelLineSettings.AnchorTextPoint.StartOfText.__doc__ + '\n' + '* ``CenterOfText``: ' + QgsLabelLineSettings.AnchorTextPoint.CenterOfText.__doc__ + '\n' + '* ``EndOfText``: ' + QgsLabelLineSettings.AnchorTextPoint.EndOfText.__doc__ + '\n' + '* ``FollowPlacement``: ' + QgsLabelLineSettings.AnchorTextPoint.FollowPlacement.__doc__
# --
QgsLabelLineSettings.AnchorTextPoint.baseClass = QgsLabelLineSettings
# The following has been generated automatically from src/core/layout/qgslayoutmanager.h
QgsLayoutManagerProxyModel.Filters.baseClass = QgsLayoutManagerProxyModel
Filters = QgsLayoutManagerProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/locator/qgslocatorfilter.h
QgsLocatorFilter.Priority.baseClass = QgsLocatorFilter
QgsLocatorFilter.Flags.baseClass = QgsLocatorFilter
Flags = QgsLocatorFilter  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/vectortile/qgsmapboxglstyleconverter.h
# monkey patching scoped based enum
QgsMapBoxGlStyleConverter.PropertyType.Color.__doc__ = "Color property"
QgsMapBoxGlStyleConverter.PropertyType.Numeric.__doc__ = "Numeric property (e.g. line width, text size)"
QgsMapBoxGlStyleConverter.PropertyType.Opacity.__doc__ = "Opacity property"
QgsMapBoxGlStyleConverter.PropertyType.Point.__doc__ = "Point/offset property"
QgsMapBoxGlStyleConverter.PropertyType.__doc__ = 'Property types, for interpolated value conversion\n\n.. warning::\n\n   This is private API only, and may change in future QGIS versions\n\n' + '* ``Color``: ' + QgsMapBoxGlStyleConverter.PropertyType.Color.__doc__ + '\n' + '* ``Numeric``: ' + QgsMapBoxGlStyleConverter.PropertyType.Numeric.__doc__ + '\n' + '* ``Opacity``: ' + QgsMapBoxGlStyleConverter.PropertyType.Opacity.__doc__ + '\n' + '* ``Point``: ' + QgsMapBoxGlStyleConverter.PropertyType.Point.__doc__
# --
QgsMapBoxGlStyleConverter.PropertyType.baseClass = QgsMapBoxGlStyleConverter
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
# The following has been generated automatically from src/core/qgsmaplayerserverproperties.h
QgsServerWmsDimensionProperties.PredefinedWmsDimensionName.baseClass = QgsServerWmsDimensionProperties
# The following has been generated automatically from src/core/qgsmapsettingsutils.h
# monkey patching scoped based enum
QgsMapSettingsUtils.EffectsCheckFlag.IgnoreGeoPdfSupportedEffects.__doc__ = "Ignore advanced effects which are supported in GeoPDF exports"
QgsMapSettingsUtils.EffectsCheckFlag.__doc__ = 'Flags for controlling the behavior of :py:func:`~QgsMapSettingsUtils.containsAdvancedEffects`\n\n.. versionadded:: 3.14\n\n' + '* ``IgnoreGeoPdfSupportedEffects``: ' + QgsMapSettingsUtils.EffectsCheckFlag.IgnoreGeoPdfSupportedEffects.__doc__
# --
# The following has been generated automatically from src/core/numericformats/qgsnumericformat.h
# monkey patching scoped based enum
QgsNumericFormatContext.Interpretation.Generic.__doc__ = "Generic"
QgsNumericFormatContext.Interpretation.Latitude.__doc__ = "Latitude values"
QgsNumericFormatContext.Interpretation.Longitude.__doc__ = "Longitude values"
QgsNumericFormatContext.Interpretation.__doc__ = 'Interpretation of numeric values.\n\n.. versionadded:: 3.26\n\n' + '* ``Generic``: ' + QgsNumericFormatContext.Interpretation.Generic.__doc__ + '\n' + '* ``Latitude``: ' + QgsNumericFormatContext.Interpretation.Latitude.__doc__ + '\n' + '* ``Longitude``: ' + QgsNumericFormatContext.Interpretation.Longitude.__doc__
# --
QgsNumericFormatContext.Interpretation.baseClass = QgsNumericFormatContext
# The following has been generated automatically from src/core/pointcloud/qgspointcloudattributemodel.h
QgsPointCloudAttributeProxyModel.Filters.baseClass = QgsPointCloudAttributeProxyModel
Filters = QgsPointCloudAttributeProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/pointcloud/qgspointcloudlayer.h
# monkey patching scoped based enum
QgsPointCloudLayer.PointCloudStatisticsCalculationState.NotStarted.__doc__ = "The statistics calculation task has not been started"
QgsPointCloudLayer.PointCloudStatisticsCalculationState.Calculating.__doc__ = "The statistics calculation task is running"
QgsPointCloudLayer.PointCloudStatisticsCalculationState.Calculated.__doc__ = "The statistics calculation task is done and statistics are available"
QgsPointCloudLayer.PointCloudStatisticsCalculationState.__doc__ = 'Point cloud statistics calculation task\n\n.. versionadded:: 3.26\n\n' + '* ``NotStarted``: ' + QgsPointCloudLayer.PointCloudStatisticsCalculationState.NotStarted.__doc__ + '\n' + '* ``Calculating``: ' + QgsPointCloudLayer.PointCloudStatisticsCalculationState.Calculating.__doc__ + '\n' + '* ``Calculated``: ' + QgsPointCloudLayer.PointCloudStatisticsCalculationState.Calculated.__doc__
# --
QgsPointCloudLayer.PointCloudStatisticsCalculationState.baseClass = QgsPointCloudLayer
# The following has been generated automatically from src/core/processing/qgsprocessingcontext.h
# monkey patching scoped based enum
QgsProcessingContext.ProcessArgumentFlag.IncludeProjectPath.__doc__ = "Include the associated project path argument"
QgsProcessingContext.ProcessArgumentFlag.__doc__ = 'Flags controlling the results given by :py:func:`~QgsProcessingContext.asQgisProcessArguments`.\n\n.. versionadded:: 3.24\n\n' + '* ``IncludeProjectPath``: ' + QgsProcessingContext.ProcessArgumentFlag.IncludeProjectPath.__doc__
# --
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
QgsProcessingUtils.PointCloud = QgsProcessingUtils.LayerHint.PointCloud
QgsProcessingUtils.PointCloud.is_monkey_patched = True
QgsProcessingUtils.LayerHint.PointCloud.__doc__ = "Point cloud layer type, since QGIS 3.22"
QgsProcessingUtils.Annotation = QgsProcessingUtils.LayerHint.Annotation
QgsProcessingUtils.Annotation.is_monkey_patched = True
QgsProcessingUtils.LayerHint.Annotation.__doc__ = "Annotation layer type, since QGIS 3.22"
QgsProcessingUtils.LayerHint.__doc__ = 'Layer type hints.\n\n.. versionadded:: 3.4\n\n' + '* ``UnknownType``: ' + QgsProcessingUtils.LayerHint.UnknownType.__doc__ + '\n' + '* ``Vector``: ' + QgsProcessingUtils.LayerHint.Vector.__doc__ + '\n' + '* ``Raster``: ' + QgsProcessingUtils.LayerHint.Raster.__doc__ + '\n' + '* ``Mesh``: ' + QgsProcessingUtils.LayerHint.Mesh.__doc__ + '\n' + '* ``PointCloud``: ' + QgsProcessingUtils.LayerHint.PointCloud.__doc__ + '\n' + '* ``Annotation``: ' + QgsProcessingUtils.LayerHint.Annotation.__doc__
# --
# The following has been generated automatically from src/core/project/qgsprojectstylesettings.h
# monkey patching scoped based enum
QgsProjectStyleDatabaseProxyModel.Filter.FilterHideReadOnly.__doc__ = "Hide read-only style databases"
QgsProjectStyleDatabaseProxyModel.Filter.__doc__ = 'Available filter flags for filtering the model\n\n' + '* ``FilterHideReadOnly``: ' + QgsProjectStyleDatabaseProxyModel.Filter.FilterHideReadOnly.__doc__
# --
QgsProjectStyleDatabaseProxyModel.Filter.baseClass = QgsProjectStyleDatabaseProxyModel
QgsProjectStyleDatabaseProxyModel.Filters.baseClass = QgsProjectStyleDatabaseProxyModel
Filters = QgsProjectStyleDatabaseProxyModel  # dirty hack since SIP seems to introduce the flags in module
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
# The following has been generated automatically from src/core/providers/qgsprovidersublayermodel.h
# monkey patching scoped based enum
QgsProviderSublayerModel.Role.ProviderKey.__doc__ = "Provider key"
QgsProviderSublayerModel.Role.LayerType.__doc__ = "Layer type"
QgsProviderSublayerModel.Role.Uri.__doc__ = "Layer URI"
QgsProviderSublayerModel.Role.Name.__doc__ = "Layer name"
QgsProviderSublayerModel.Role.Description.__doc__ = "Layer description"
QgsProviderSublayerModel.Role.Path.__doc__ = "Layer path"
QgsProviderSublayerModel.Role.FeatureCount.__doc__ = "Feature count (for vector sublayers)"
QgsProviderSublayerModel.Role.WkbType.__doc__ = "WKB geometry type (for vector sublayers)"
QgsProviderSublayerModel.Role.GeometryColumnName.__doc__ = "Geometry column name (for vector sublayers)"
QgsProviderSublayerModel.Role.LayerNumber.__doc__ = "Layer number"
QgsProviderSublayerModel.Role.IsNonLayerItem.__doc__ = "``True`` if item is a non-sublayer item (e.g. an embedded project)"
QgsProviderSublayerModel.Role.NonLayerItemType.__doc__ = "Item type (for non-sublayer items)"
QgsProviderSublayerModel.Role.Flags.__doc__ = "Sublayer flags"
QgsProviderSublayerModel.Role.__doc__ = 'Custom model roles\n\n' + '* ``ProviderKey``: ' + QgsProviderSublayerModel.Role.ProviderKey.__doc__ + '\n' + '* ``LayerType``: ' + QgsProviderSublayerModel.Role.LayerType.__doc__ + '\n' + '* ``Uri``: ' + QgsProviderSublayerModel.Role.Uri.__doc__ + '\n' + '* ``Name``: ' + QgsProviderSublayerModel.Role.Name.__doc__ + '\n' + '* ``Description``: ' + QgsProviderSublayerModel.Role.Description.__doc__ + '\n' + '* ``Path``: ' + QgsProviderSublayerModel.Role.Path.__doc__ + '\n' + '* ``FeatureCount``: ' + QgsProviderSublayerModel.Role.FeatureCount.__doc__ + '\n' + '* ``WkbType``: ' + QgsProviderSublayerModel.Role.WkbType.__doc__ + '\n' + '* ``GeometryColumnName``: ' + QgsProviderSublayerModel.Role.GeometryColumnName.__doc__ + '\n' + '* ``LayerNumber``: ' + QgsProviderSublayerModel.Role.LayerNumber.__doc__ + '\n' + '* ``IsNonLayerItem``: ' + QgsProviderSublayerModel.Role.IsNonLayerItem.__doc__ + '\n' + '* ``NonLayerItemType``: ' + QgsProviderSublayerModel.Role.NonLayerItemType.__doc__ + '\n' + '* ``Flags``: ' + QgsProviderSublayerModel.Role.Flags.__doc__
# --
# monkey patching scoped based enum
QgsProviderSublayerModel.Column.Name.__doc__ = "Layer name"
QgsProviderSublayerModel.Column.Description.__doc__ = "Layer description"
QgsProviderSublayerModel.Column.__doc__ = 'Model columns\n\n' + '* ``Name``: ' + QgsProviderSublayerModel.Column.Name.__doc__ + '\n' + '* ``Description``: ' + QgsProviderSublayerModel.Column.Description.__doc__
# --
# The following has been generated automatically from src/core/providers/qgsproviderutils.h
# monkey patching scoped based enum
QgsProviderUtils.SublayerCompletenessFlag.IgnoreUnknownFeatureCount.__doc__ = "Indicates that an unknown feature count should not be considered as incomplete"
QgsProviderUtils.SublayerCompletenessFlag.IgnoreUnknownGeometryType.__doc__ = "Indicates that an unknown geometry type should not be considered as incomplete"
QgsProviderUtils.SublayerCompletenessFlag.__doc__ = 'Flags which control how :py:func:`QgsProviderUtils.sublayerDetailsAreIncomplete()` tests for completeness.\n\n' + '* ``IgnoreUnknownFeatureCount``: ' + QgsProviderUtils.SublayerCompletenessFlag.IgnoreUnknownFeatureCount.__doc__ + '\n' + '* ``IgnoreUnknownGeometryType``: ' + QgsProviderUtils.SublayerCompletenessFlag.IgnoreUnknownGeometryType.__doc__
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
# The following has been generated automatically from src/core/raster/qgsrasterprojector.h
QgsRasterProjector.Precision.baseClass = QgsRasterProjector
# The following has been generated automatically from src/core/qgsrenderchecker.h
# monkey patching scoped based enum
QgsRenderChecker.Flag.AvoidExportingRenderedImage.__doc__ = "Avoids exporting rendered images to reports"
QgsRenderChecker.Flag.__doc__ = 'Render checker flags.\n\n.. versionadded:: 3.28\n\n' + '* ``AvoidExportingRenderedImage``: ' + QgsRenderChecker.Flag.AvoidExportingRenderedImage.__doc__
# --
QgsRenderChecker.Flag.baseClass = QgsRenderChecker
QgsRenderChecker.Flags.baseClass = QgsRenderChecker
Flags = QgsRenderChecker  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/scalebar/qgsscalebarrenderer.h
# monkey patching scoped based enum
QgsScaleBarRenderer.Flag.FlagUsesLineSymbol.__doc__ = "Renderer utilizes the scalebar line symbol (see QgsScaleBarSettings.lineSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesFillSymbol.__doc__ = "Renderer utilizes the scalebar fill symbol (see QgsScaleBarSettings.fillSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesAlternateFillSymbol.__doc__ = "Renderer utilizes the alternate scalebar fill symbol (see QgsScaleBarSettings.alternateFillSymbol() )"
QgsScaleBarRenderer.Flag.FlagRespectsUnits.__doc__ = "Renderer respects the QgsScaleBarSettings.units() setting"
QgsScaleBarRenderer.Flag.FlagRespectsMapUnitsPerScaleBarUnit.__doc__ = "Renderer respects the QgsScaleBarSettings.mapUnitsPerScaleBarUnit() setting"
QgsScaleBarRenderer.Flag.FlagUsesUnitLabel.__doc__ = "Renderer uses the QgsScaleBarSettings.unitLabel() setting"
QgsScaleBarRenderer.Flag.FlagUsesSegments.__doc__ = "Renderer uses the scalebar segments"
QgsScaleBarRenderer.Flag.FlagUsesLabelBarSpace.__doc__ = "Renderer uses the QgsScaleBarSettings.labelBarSpace() setting"
QgsScaleBarRenderer.Flag.FlagUsesLabelVerticalPlacement.__doc__ = "Renderer uses the QgsScaleBarSettings.labelVerticalPlacement() setting"
QgsScaleBarRenderer.Flag.FlagUsesLabelHorizontalPlacement.__doc__ = "Renderer uses the QgsScaleBarSettings.labelHorizontalPlacement() setting"
QgsScaleBarRenderer.Flag.FlagUsesAlignment.__doc__ = "Renderer uses the QgsScaleBarSettings.alignment() setting"
QgsScaleBarRenderer.Flag.FlagUsesSubdivisions.__doc__ = "Renderer uses the scalebar subdivisions (see QgsScaleBarSettings.numberOfSubdivisions() )"
QgsScaleBarRenderer.Flag.FlagUsesDivisionSymbol.__doc__ = "Renderer utilizes the scalebar division symbol (see QgsScaleBarSettings.divisionLineSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesSubdivisionSymbol.__doc__ = "Renderer utilizes the scalebar subdivision symbol (see QgsScaleBarSettings.subdivisionLineSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesSubdivisionsHeight.__doc__ = "Renderer uses the scalebar subdivisions height (see QgsScaleBarSettings.subdivisionsHeight() )"
QgsScaleBarRenderer.Flag.__doc__ = 'Flags which control scalebar renderer behavior.\n\n.. versionadded:: 3.14\n\n' + '* ``FlagUsesLineSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesLineSymbol.__doc__ + '\n' + '* ``FlagUsesFillSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesFillSymbol.__doc__ + '\n' + '* ``FlagUsesAlternateFillSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesAlternateFillSymbol.__doc__ + '\n' + '* ``FlagRespectsUnits``: ' + QgsScaleBarRenderer.Flag.FlagRespectsUnits.__doc__ + '\n' + '* ``FlagRespectsMapUnitsPerScaleBarUnit``: ' + QgsScaleBarRenderer.Flag.FlagRespectsMapUnitsPerScaleBarUnit.__doc__ + '\n' + '* ``FlagUsesUnitLabel``: ' + QgsScaleBarRenderer.Flag.FlagUsesUnitLabel.__doc__ + '\n' + '* ``FlagUsesSegments``: ' + QgsScaleBarRenderer.Flag.FlagUsesSegments.__doc__ + '\n' + '* ``FlagUsesLabelBarSpace``: ' + QgsScaleBarRenderer.Flag.FlagUsesLabelBarSpace.__doc__ + '\n' + '* ``FlagUsesLabelVerticalPlacement``: ' + QgsScaleBarRenderer.Flag.FlagUsesLabelVerticalPlacement.__doc__ + '\n' + '* ``FlagUsesLabelHorizontalPlacement``: ' + QgsScaleBarRenderer.Flag.FlagUsesLabelHorizontalPlacement.__doc__ + '\n' + '* ``FlagUsesAlignment``: ' + QgsScaleBarRenderer.Flag.FlagUsesAlignment.__doc__ + '\n' + '* ``FlagUsesSubdivisions``: ' + QgsScaleBarRenderer.Flag.FlagUsesSubdivisions.__doc__ + '\n' + '* ``FlagUsesDivisionSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesDivisionSymbol.__doc__ + '\n' + '* ``FlagUsesSubdivisionSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesSubdivisionSymbol.__doc__ + '\n' + '* ``FlagUsesSubdivisionsHeight``: ' + QgsScaleBarRenderer.Flag.FlagUsesSubdivisionsHeight.__doc__
# --
# The following has been generated automatically from src/core/qgssnappingconfig.h
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
# The following has been generated automatically from src/core/qgsvectorsimplifymethod.h
QgsVectorSimplifyMethod.SimplifyHint.baseClass = QgsVectorSimplifyMethod
QgsVectorSimplifyMethod.SimplifyHints.baseClass = QgsVectorSimplifyMethod
SimplifyHints = QgsVectorSimplifyMethod  # dirty hack since SIP seems to introduce the flags in module
QgsVectorSimplifyMethod.SimplifyAlgorithm.baseClass = QgsVectorSimplifyMethod
# The following has been generated automatically from src/core/geometry/qgswkbtypes.h
QgsWkbTypes.Type.baseClass = QgsWkbTypes
QgsWkbTypes.GeometryType.baseClass = QgsWkbTypes
