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

from qgis._analysis import *
from qgis.core import Qgis as _Qgis

# preserve API compatibility following QgsExifTools moved to core
from qgis.core import QgsExifTools
# preserve API compatibility as QgsAlignRaster.Item moved to QgsAlignRasterData.RasterItem
from qgis.core import QgsAlignRasterData

QgsAlignRaster.Item = QgsAlignRasterData.RasterItem

QgsAlignRaster.ResampleAlg = _Qgis.GdalResampleAlgorithm
# monkey patching scoped based enum
QgsAlignRaster.RA_NearestNeighbour = _Qgis.GdalResampleAlgorithm.RA_NearestNeighbour
QgsAlignRaster.RA_NearestNeighbour.is_monkey_patched = True
QgsAlignRaster.RA_NearestNeighbour.__doc__ = "Nearest neighbour (select on one input pixel)"
QgsAlignRaster.RA_Bilinear = _Qgis.GdalResampleAlgorithm.RA_Bilinear
QgsAlignRaster.RA_Bilinear.is_monkey_patched = True
QgsAlignRaster.RA_Bilinear.__doc__ = "Bilinear (2x2 kernel)"
QgsAlignRaster.RA_Cubic = _Qgis.GdalResampleAlgorithm.RA_Cubic
QgsAlignRaster.RA_Cubic.is_monkey_patched = True
QgsAlignRaster.RA_Cubic.__doc__ = "Cubic Convolution Approximation (4x4 kernel)"
QgsAlignRaster.RA_CubicSpline = _Qgis.GdalResampleAlgorithm.RA_CubicSpline
QgsAlignRaster.RA_CubicSpline.is_monkey_patched = True
QgsAlignRaster.RA_CubicSpline.__doc__ = "Cubic B-Spline Approximation (4x4 kernel)"
QgsAlignRaster.RA_Lanczos = _Qgis.GdalResampleAlgorithm.RA_Lanczos
QgsAlignRaster.RA_Lanczos.is_monkey_patched = True
QgsAlignRaster.RA_Lanczos.__doc__ = "Lanczos windowed sinc interpolation (6x6 kernel)"
QgsAlignRaster.RA_Average = _Qgis.GdalResampleAlgorithm.RA_Average
QgsAlignRaster.RA_Average.is_monkey_patched = True
QgsAlignRaster.RA_Average.__doc__ = "Average (computes the average of all non-NODATA contributing pixels)"
QgsAlignRaster.RA_Mode = _Qgis.GdalResampleAlgorithm.RA_Mode
QgsAlignRaster.RA_Mode.is_monkey_patched = True
QgsAlignRaster.RA_Mode.__doc__ = "Mode (selects the value which appears most often of all the sampled points)"
QgsAlignRaster.RA_Max = _Qgis.GdalResampleAlgorithm.RA_Max
QgsAlignRaster.RA_Max.is_monkey_patched = True
QgsAlignRaster.RA_Max.__doc__ = "Maximum (selects the maximum of all non-NODATA contributing pixels)"
QgsAlignRaster.RA_Min = _Qgis.GdalResampleAlgorithm.RA_Min
QgsAlignRaster.RA_Min.is_monkey_patched = True
QgsAlignRaster.RA_Min.__doc__ = "Minimum (selects the minimum of all non-NODATA contributing pixels)"
QgsAlignRaster.RA_Median = _Qgis.GdalResampleAlgorithm.RA_Median
QgsAlignRaster.RA_Median.is_monkey_patched = True
QgsAlignRaster.RA_Median.__doc__ = "Median (selects the median of all non-NODATA contributing pixels)"
QgsAlignRaster.RA_Q1 = _Qgis.GdalResampleAlgorithm.RA_Q1
QgsAlignRaster.RA_Q1.is_monkey_patched = True
QgsAlignRaster.RA_Q1.__doc__ = "First quartile (selects the first quartile of all non-NODATA contributing pixels)"
QgsAlignRaster.RA_Q3 = _Qgis.GdalResampleAlgorithm.RA_Q3
QgsAlignRaster.RA_Q3.is_monkey_patched = True
QgsAlignRaster.RA_Q3.__doc__ = "Third quartile (selects the third quartile of all non-NODATA contributing pixels)"
_Qgis.GdalResampleAlgorithm.__doc__ = "Resampling algorithm to be used (equivalent to GDAL's enum GDALResampleAlg)\n\n.. note::\n\n   RA_Max, RA_Min, RA_Median, RA_Q1 and RA_Q3 are available on GDAL >= 2.0 builds only\n\n.. versionadded:: 3.34\n\n" + '* ``RA_NearestNeighbour``: ' + _Qgis.GdalResampleAlgorithm.RA_NearestNeighbour.__doc__ + '\n' + '* ``RA_Bilinear``: ' + _Qgis.GdalResampleAlgorithm.RA_Bilinear.__doc__ + '\n' + '* ``RA_Cubic``: ' + _Qgis.GdalResampleAlgorithm.RA_Cubic.__doc__ + '\n' + '* ``RA_CubicSpline``: ' + _Qgis.GdalResampleAlgorithm.RA_CubicSpline.__doc__ + '\n' + '* ``RA_Lanczos``: ' + _Qgis.GdalResampleAlgorithm.RA_Lanczos.__doc__ + '\n' + '* ``RA_Average``: ' + _Qgis.GdalResampleAlgorithm.RA_Average.__doc__ + '\n' + '* ``RA_Mode``: ' + _Qgis.GdalResampleAlgorithm.RA_Mode.__doc__ + '\n' + '* ``RA_Max``: ' + _Qgis.GdalResampleAlgorithm.RA_Max.__doc__ + '\n' + '* ``RA_Min``: ' + _Qgis.GdalResampleAlgorithm.RA_Min.__doc__ + '\n' + '* ``RA_Median``: ' + _Qgis.GdalResampleAlgorithm.RA_Median.__doc__ + '\n' + '* ``RA_Q1``: ' + _Qgis.GdalResampleAlgorithm.RA_Q1.__doc__ + '\n' + '* ``RA_Q3``: ' + _Qgis.GdalResampleAlgorithm.RA_Q3.__doc__
# --
_Qgis.GdalResampleAlgorithm.baseClass = _Qgis

QgsZonalStatistics.Statistic = _Qgis.ZonalStatistic
# monkey patching scoped based enum
QgsZonalStatistics.Count = _Qgis.ZonalStatistic.Count
QgsZonalStatistics.Count.is_monkey_patched = True
QgsZonalStatistics.Count.__doc__ = "Pixel count"
QgsZonalStatistics.Sum = _Qgis.ZonalStatistic.Sum
QgsZonalStatistics.Sum.is_monkey_patched = True
QgsZonalStatistics.Sum.__doc__ = "Sum of pixel values"
QgsZonalStatistics.Mean = _Qgis.ZonalStatistic.Mean
QgsZonalStatistics.Mean.is_monkey_patched = True
QgsZonalStatistics.Mean.__doc__ = "Mean of pixel values"
QgsZonalStatistics.Median = _Qgis.ZonalStatistic.Median
QgsZonalStatistics.Median.is_monkey_patched = True
QgsZonalStatistics.Median.__doc__ = "Median of pixel values"
QgsZonalStatistics.StDev = _Qgis.ZonalStatistic.StDev
QgsZonalStatistics.StDev.is_monkey_patched = True
QgsZonalStatistics.StDev.__doc__ = "Standard deviation of pixel values"
QgsZonalStatistics.Min = _Qgis.ZonalStatistic.Min
QgsZonalStatistics.Min.is_monkey_patched = True
QgsZonalStatistics.Min.__doc__ = "Min of pixel values"
QgsZonalStatistics.Max = _Qgis.ZonalStatistic.Max
QgsZonalStatistics.Max.is_monkey_patched = True
QgsZonalStatistics.Max.__doc__ = "Max of pixel values"
QgsZonalStatistics.Range = _Qgis.ZonalStatistic.Range
QgsZonalStatistics.Range.is_monkey_patched = True
QgsZonalStatistics.Range.__doc__ = "Range of pixel values (max - min)"
QgsZonalStatistics.Minority = _Qgis.ZonalStatistic.Minority
QgsZonalStatistics.Minority.is_monkey_patched = True
QgsZonalStatistics.Minority.__doc__ = "Minority of pixel values"
QgsZonalStatistics.Majority = _Qgis.ZonalStatistic.Majority
QgsZonalStatistics.Majority.is_monkey_patched = True
QgsZonalStatistics.Majority.__doc__ = "Majority of pixel values"
QgsZonalStatistics.Variety = _Qgis.ZonalStatistic.Variety
QgsZonalStatistics.Variety.is_monkey_patched = True
QgsZonalStatistics.Variety.__doc__ = "Variety (count of distinct) pixel values"
QgsZonalStatistics.Variance = _Qgis.ZonalStatistic.Variance
QgsZonalStatistics.Variance.is_monkey_patched = True
QgsZonalStatistics.Variance.__doc__ = "Variance of pixel values"
QgsZonalStatistics.All = _Qgis.ZonalStatistic.All
QgsZonalStatistics.All.is_monkey_patched = True
QgsZonalStatistics.All.__doc__ = "All statistics"
QgsZonalStatistics.Default = _Qgis.ZonalStatistic.Default
QgsZonalStatistics.Default.is_monkey_patched = True
QgsZonalStatistics.Default.__doc__ = "Default statistics"
_Qgis.ZonalStatistic.__doc__ = "Statistics to be calculated during a zonal statistics operation.\n\n.. versionadded:: 3.36.\n\n" + '* ``Count``: ' + _Qgis.ZonalStatistic.Count.__doc__ + '\n' + '* ``Sum``: ' + _Qgis.ZonalStatistic.Sum.__doc__ + '\n' + '* ``Mean``: ' + _Qgis.ZonalStatistic.Mean.__doc__ + '\n' + '* ``Median``: ' + _Qgis.ZonalStatistic.Median.__doc__ + '\n' + '* ``StDev``: ' + _Qgis.ZonalStatistic.StDev.__doc__ + '\n' + '* ``Min``: ' + _Qgis.ZonalStatistic.Min.__doc__ + '\n' + '* ``Max``: ' + _Qgis.ZonalStatistic.Max.__doc__ + '\n' + '* ``Range``: ' + _Qgis.ZonalStatistic.Range.__doc__ + '\n' + '* ``Minority``: ' + _Qgis.ZonalStatistic.Minority.__doc__ + '\n' + '* ``Majority``: ' + _Qgis.ZonalStatistic.Majority.__doc__ + '\n' + '* ``Variety``: ' + _Qgis.ZonalStatistic.Variety.__doc__ + '\n' + '* ``Variance``: ' + _Qgis.ZonalStatistic.Variance.__doc__ + '\n' + '* ``All``: ' + _Qgis.ZonalStatistic.All.__doc__ + '\n' + '* ``Default``: ' + _Qgis.ZonalStatistic.Default.__doc__
# --
_Qgis.ZonalStatistic.baseClass = _Qgis
QgsZonalStatistics.Statistics = _Qgis.ZonalStatistics
_Qgis.ZonalStatistics.baseClass = _Qgis
ZonalStatistics = _Qgis  # dirty hack since SIP seems to introduce the flags in module
QgsZonalStatistics.Result = _Qgis.ZonalStatisticResult
# monkey patching scoped based enum
QgsZonalStatistics.Success = _Qgis.ZonalStatisticResult.Success
QgsZonalStatistics.Success.is_monkey_patched = True
QgsZonalStatistics.Success.__doc__ = "Success"
QgsZonalStatistics.LayerTypeWrong = _Qgis.ZonalStatisticResult.LayerTypeWrong
QgsZonalStatistics.LayerTypeWrong.is_monkey_patched = True
QgsZonalStatistics.LayerTypeWrong.__doc__ = "Layer is not a polygon layer"
QgsZonalStatistics.LayerInvalid = _Qgis.ZonalStatisticResult.LayerInvalid
QgsZonalStatistics.LayerInvalid.is_monkey_patched = True
QgsZonalStatistics.LayerInvalid.__doc__ = "Layer is invalid"
QgsZonalStatistics.RasterInvalid = _Qgis.ZonalStatisticResult.RasterInvalid
QgsZonalStatistics.RasterInvalid.is_monkey_patched = True
QgsZonalStatistics.RasterInvalid.__doc__ = "Raster layer is invalid"
QgsZonalStatistics.RasterBandInvalid = _Qgis.ZonalStatisticResult.RasterBandInvalid
QgsZonalStatistics.RasterBandInvalid.is_monkey_patched = True
QgsZonalStatistics.RasterBandInvalid.__doc__ = "The raster band does not exist on the raster layer"
QgsZonalStatistics.FailedToCreateField = _Qgis.ZonalStatisticResult.FailedToCreateField
QgsZonalStatistics.FailedToCreateField.is_monkey_patched = True
QgsZonalStatistics.FailedToCreateField.__doc__ = "Output fields could not be created"
QgsZonalStatistics.Canceled = _Qgis.ZonalStatisticResult.Canceled
QgsZonalStatistics.Canceled.is_monkey_patched = True
QgsZonalStatistics.Canceled.__doc__ = "Algorithm was canceled"
_Qgis.ZonalStatisticResult.__doc__ = "Zonal statistics result codes.\n\n.. versionadded:: 3.36.\n\n" + '* ``Success``: ' + _Qgis.ZonalStatisticResult.Success.__doc__ + '\n' + '* ``LayerTypeWrong``: ' + _Qgis.ZonalStatisticResult.LayerTypeWrong.__doc__ + '\n' + '* ``LayerInvalid``: ' + _Qgis.ZonalStatisticResult.LayerInvalid.__doc__ + '\n' + '* ``RasterInvalid``: ' + _Qgis.ZonalStatisticResult.RasterInvalid.__doc__ + '\n' + '* ``RasterBandInvalid``: ' + _Qgis.ZonalStatisticResult.RasterBandInvalid.__doc__ + '\n' + '* ``FailedToCreateField``: ' + _Qgis.ZonalStatisticResult.FailedToCreateField.__doc__ + '\n' + '* ``Canceled``: ' + _Qgis.ZonalStatisticResult.Canceled.__doc__
# --
_Qgis.ZonalStatisticResult.baseClass = _Qgis

"""
This folder is completed using sipify.py script
It is not aimed to be manually edited
"""
# The following has been generated automatically from src/analysis/processing/qgsalgorithmbatchgeocode.h
try:
    QgsBatchGeocodeAlgorithm.__overridden_methods__ = ['initParameters', 'tags', 'group', 'groupId', 'inputLayerTypes', 'supportInPlaceEdit', 'outputName', 'prepareAlgorithm', 'processFeature', 'outputCrs', 'outputFields', 'outputWkbType']
    QgsBatchGeocodeAlgorithm.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgsalignraster.h
try:
    QgsAlignRaster.suggestedWarpOutput = staticmethod(QgsAlignRaster.suggestedWarpOutput)
    QgsAlignRaster.__abstract_methods__ = ['progress']
    QgsAlignRaster.__group__ = ['raster']
except (NameError, AttributeError):
    pass
try:
    QgsAlignRaster.RasterInfo.__doc__ = """Utility class for gathering information about rasters"""
    QgsAlignRaster.RasterInfo.__group__ = ['raster']
except (NameError, AttributeError):
    pass
try:
    QgsAlignRaster.ProgressHandler.__doc__ = """Helper struct to be sub-classed for progress reporting"""
    QgsAlignRaster.ProgressHandler.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/qgsanalysis.h
try:
    QgsAnalysis.instance = staticmethod(QgsAnalysis.instance)
    QgsAnalysis.geometryCheckRegistry = staticmethod(QgsAnalysis.geometryCheckRegistry)
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgsaspectfilter.h
try:
    QgsAspectFilter.__overridden_methods__ = ['processNineCellWindow']
    QgsAspectFilter.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgsderivativefilter.h
try:
    QgsDerivativeFilter.__abstract_methods__ = ['processNineCellWindow']
    QgsDerivativeFilter.__overridden_methods__ = ['processNineCellWindow']
    QgsDerivativeFilter.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/vector/geometry_checker/qgsfeaturepool.h
try:
    QgsFeaturePool.__abstract_methods__ = ['updateFeature', 'deleteFeature']
    QgsFeaturePool.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/georeferencing/qgsgcpgeometrytransformer.h
try:
    QgsGcpGeometryTransformer.__overridden_methods__ = ['transformPoint']
    QgsGcpGeometryTransformer.__group__ = ['georeferencing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/georeferencing/qgsgcppoint.h
# monkey patching scoped based enum
QgsGcpPoint.PointType.Source.__doc__ = "Source point"
QgsGcpPoint.PointType.Destination.__doc__ = "Destination point"
QgsGcpPoint.PointType.__doc__ = """Coordinate point types

* ``Source``: Source point
* ``Destination``: Destination point

"""
# --
try:
    QgsGcpPoint.__group__ = ['georeferencing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/georeferencing/qgsgcptransformer.h
# monkey patching scoped based enum
QgsGcpTransformerInterface.TransformMethod.Linear.__doc__ = "Linear transform"
QgsGcpTransformerInterface.TransformMethod.Helmert.__doc__ = "Helmert transform"
QgsGcpTransformerInterface.TransformMethod.PolynomialOrder1.__doc__ = "Polynomial order 1"
QgsGcpTransformerInterface.TransformMethod.PolynomialOrder2.__doc__ = "Polyonmial order 2"
QgsGcpTransformerInterface.TransformMethod.PolynomialOrder3.__doc__ = "Polynomial order"
QgsGcpTransformerInterface.TransformMethod.ThinPlateSpline.__doc__ = "Thin plate splines"
QgsGcpTransformerInterface.TransformMethod.Projective.__doc__ = "Projective"
QgsGcpTransformerInterface.TransformMethod.InvalidTransform.__doc__ = "Invalid transform"
QgsGcpTransformerInterface.TransformMethod.__doc__ = """Available transformation methods.

* ``Linear``: Linear transform
* ``Helmert``: Helmert transform
* ``PolynomialOrder1``: Polynomial order 1
* ``PolynomialOrder2``: Polyonmial order 2
* ``PolynomialOrder3``: Polynomial order
* ``ThinPlateSpline``: Thin plate splines
* ``Projective``: Projective
* ``InvalidTransform``: Invalid transform

"""
# --
QgsGcpTransformerInterface.TransformMethod.baseClass = QgsGcpTransformerInterface
try:
    QgsGcpTransformerInterface.methodToString = staticmethod(QgsGcpTransformerInterface.methodToString)
    QgsGcpTransformerInterface.create = staticmethod(QgsGcpTransformerInterface.create)
    QgsGcpTransformerInterface.createFromParameters = staticmethod(QgsGcpTransformerInterface.createFromParameters)
    QgsGcpTransformerInterface.__abstract_methods__ = ['clone', 'updateParametersFromGcps', 'minimumGcpCount', 'method']
    QgsGcpTransformerInterface.__group__ = ['georeferencing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/vector/geometry_checker/qgsgeometrycheck.h
# monkey patching scoped based enum
QgsGeometryCheck.Result.Success.__doc__ = "Operation completed successfully"
QgsGeometryCheck.Result.Canceled.__doc__ = "User canceled calculation"
QgsGeometryCheck.Result.DuplicatedUniqueId.__doc__ = "Found duplicated unique ID value"
QgsGeometryCheck.Result.InvalidReferenceLayer.__doc__ = "Missed or invalid reference layer"
QgsGeometryCheck.Result.GeometryOverlayError.__doc__ = "Error performing geometry overlay operation"
QgsGeometryCheck.Result.__doc__ = """
.. versionadded:: 4.0

* ``Success``: Operation completed successfully
* ``Canceled``: User canceled calculation
* ``DuplicatedUniqueId``: Found duplicated unique ID value
* ``InvalidReferenceLayer``: Missed or invalid reference layer
* ``GeometryOverlayError``: Error performing geometry overlay operation

"""
# --
QgsGeometryCheck.Flags.baseClass = QgsGeometryCheck
Flags = QgsGeometryCheck  # dirty hack since SIP seems to introduce the flags in module
try:
    QgsGeometryCheck.Change.__attribute_docs__ = {'what': 'What level this change affects.', 'type': 'What action this change performs.', 'vidx': 'The index of the part / ring / vertex, depending on :py:func:`what`.'}
    QgsGeometryCheck.Change.__annotations__ = {'what': 'QgsGeometryCheck.ChangeWhat', 'type': 'QgsGeometryCheck.ChangeType', 'vidx': 'QgsVertexId'}
    QgsGeometryCheck.Change.__doc__ = """Descripts a change to fix a geometry.

.. versionadded:: 3.4"""
    QgsGeometryCheck.Change.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
try:
    QgsGeometryCheck.__virtual_methods__ = ['prepare', 'isCompatible', 'flags', 'collectErrors', 'availableResolutionMethods', 'resolutionMethods']
    QgsGeometryCheck.__abstract_methods__ = ['compatibleGeometryTypes', 'description', 'id', 'checkType']
    QgsGeometryCheck.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
try:
    QgsGeometryCheck.LayerFeatureIds.__doc__ = """A list of layers and feature ids for each of these layers.
In C++, the member `ids` can be accessed directly.
In Python some accessor methods will need to be written.

.. versionadded:: 3.4"""
    QgsGeometryCheck.LayerFeatureIds.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/vector/geometry_checker/qgsgeometrycheckcontext.h
try:
    QgsGeometryCheckContext.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/vector/geometry_checker/qgsgeometrycheckerror.h
try:
    QgsGeometryCheckError.__virtual_methods__ = ['contextBoundingBox', 'affectedAreaBBox', 'description', 'isEqual', 'closeMatch', 'update', 'icon']
    QgsGeometryCheckError.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/vector/geometry_checker/qgsgeometrycheckerutils.h
try:
    QgsGeometryCheckerUtils.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
try:
    QgsGeometryCheckerUtils.LayerFeature.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
try:
    QgsGeometryCheckerUtils.LayerFeatures.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/vector/geometry_checker/qgsgeometrycheckfactory.h
try:
    QgsGeometryCheckFactory.__abstract_methods__ = ['createGeometryCheck', 'id', 'description', 'isCompatible', 'flags', 'checkType']
    QgsGeometryCheckFactory.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
try:
    QgsGeometryCheckFactoryT.__overridden_methods__ = ['createGeometryCheck', 'description', 'id', 'isCompatible', 'flags', 'checkType']
    QgsGeometryCheckFactoryT.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/vector/geometry_checker/qgsgeometrycheckregistry.h
try:
    QgsGeometryCheckRegistry.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/vector/geometry_checker/qgsgeometrycheckresolutionmethod.h
try:
    QgsGeometryCheckResolutionMethod.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/vector/qgsgeometrysnapper.h
try:
    QgsGeometrySnapper.__attribute_docs__ = {'featureSnapped': 'Emitted each time a feature has been processed when calling\n:py:func:`~QgsGeometrySnapper.snapFeatures`\n'}
    QgsGeometrySnapper.__group__ = ['vector']
except (NameError, AttributeError):
    pass
try:
    QgsInternalGeometrySnapper.__group__ = ['vector']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/vector/qgsgeometrysnappersinglesource.h
try:
    QgsGeometrySnapperSingleSource.run = staticmethod(QgsGeometrySnapperSingleSource.run)
    QgsGeometrySnapperSingleSource.__group__ = ['vector']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/network/qgsgraph.h
try:
    QgsGraphEdge.__group__ = ['network']
except (NameError, AttributeError):
    pass
try:
    QgsGraphVertex.__group__ = ['network']
except (NameError, AttributeError):
    pass
try:
    QgsGraph.__group__ = ['network']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/network/qgsgraphanalyzer.h
try:
    QgsGraphAnalyzer.dijkstra = staticmethod(QgsGraphAnalyzer.dijkstra)
    QgsGraphAnalyzer.shortestTree = staticmethod(QgsGraphAnalyzer.shortestTree)
    QgsGraphAnalyzer.__group__ = ['network']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/network/qgsgraphbuilder.h
try:
    QgsGraphBuilder.__overridden_methods__ = ['addVertex', 'addEdge']
    QgsGraphBuilder.__group__ = ['network']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/network/qgsgraphbuilderinterface.h
try:
    QgsGraphBuilderInterface.__virtual_methods__ = ['addVertex', 'addEdge']
    QgsGraphBuilderInterface.__group__ = ['network']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/network/qgsgraphdirector.h
try:
    QgsGraphDirector.__virtual_methods__ = ['makeGraph']
    QgsGraphDirector.__abstract_methods__ = ['name']
    QgsGraphDirector.__group__ = ['network']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/interpolation/qgsgridfilewriter.h
try:
    QgsGridFileWriter.__group__ = ['interpolation']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgshillshadefilter.h
try:
    QgsHillshadeFilter.__overridden_methods__ = ['processNineCellWindow']
    QgsHillshadeFilter.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/interpolation/qgsidwinterpolator.h
try:
    QgsIDWInterpolator.__overridden_methods__ = ['interpolatePoint']
    QgsIDWInterpolator.__group__ = ['interpolation']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/interpolation/qgsinterpolator.h
# monkey patching scoped based enum
QgsInterpolator.SourcePoints = QgsInterpolator.SourceType.Points
QgsInterpolator.SourceType.SourcePoints = QgsInterpolator.SourceType.Points
QgsInterpolator.SourcePoints.is_monkey_patched = True
QgsInterpolator.SourcePoints.__doc__ = "Point source"
QgsInterpolator.SourceStructureLines = QgsInterpolator.SourceType.StructureLines
QgsInterpolator.SourceType.SourceStructureLines = QgsInterpolator.SourceType.StructureLines
QgsInterpolator.SourceStructureLines.is_monkey_patched = True
QgsInterpolator.SourceStructureLines.__doc__ = "Structure lines"
QgsInterpolator.SourceBreakLines = QgsInterpolator.SourceType.BreakLines
QgsInterpolator.SourceType.SourceBreakLines = QgsInterpolator.SourceType.BreakLines
QgsInterpolator.SourceBreakLines.is_monkey_patched = True
QgsInterpolator.SourceBreakLines.__doc__ = "Break lines"
QgsInterpolator.SourceType.__doc__ = """Describes the type of input data

* ``Points``: Point source

  Available as ``QgsInterpolator.SourcePoints`` in older QGIS releases.

* ``StructureLines``: Structure lines

  Available as ``QgsInterpolator.SourceStructureLines`` in older QGIS releases.

* ``BreakLines``: Break lines

  Available as ``QgsInterpolator.SourceBreakLines`` in older QGIS releases.


"""
# --
# monkey patching scoped based enum
QgsInterpolator.ValueAttribute = QgsInterpolator.ValueSource.Attribute
QgsInterpolator.ValueSource.ValueAttribute = QgsInterpolator.ValueSource.Attribute
QgsInterpolator.ValueAttribute.is_monkey_patched = True
QgsInterpolator.ValueAttribute.__doc__ = "Take value from feature's attribute"
QgsInterpolator.ValueZ = QgsInterpolator.ValueSource.Z
QgsInterpolator.ValueSource.ValueZ = QgsInterpolator.ValueSource.Z
QgsInterpolator.ValueZ.is_monkey_patched = True
QgsInterpolator.ValueZ.__doc__ = "Use feature's geometry Z values for interpolation"
QgsInterpolator.ValueM = QgsInterpolator.ValueSource.M
QgsInterpolator.ValueSource.ValueM = QgsInterpolator.ValueSource.M
QgsInterpolator.ValueM.is_monkey_patched = True
QgsInterpolator.ValueM.__doc__ = "Use feature's geometry M values for interpolation"
QgsInterpolator.ValueSource.__doc__ = """Source for interpolated values from features

* ``Attribute``: Take value from feature's attribute

  Available as ``QgsInterpolator.ValueAttribute`` in older QGIS releases.

* ``Z``: Use feature's geometry Z values for interpolation

  Available as ``QgsInterpolator.ValueZ`` in older QGIS releases.

* ``M``: Use feature's geometry M values for interpolation

  Available as ``QgsInterpolator.ValueM`` in older QGIS releases.


"""
# --
# monkey patching scoped based enum
QgsInterpolator.Result.Success.__doc__ = "Operation was successful"
QgsInterpolator.Result.Canceled.__doc__ = "Operation was manually canceled"
QgsInterpolator.Result.InvalidSource.__doc__ = "Operation failed due to invalid source"
QgsInterpolator.Result.FeatureGeometryError.__doc__ = "Operation failed due to invalid feature geometry"
QgsInterpolator.Result.__doc__ = """Result of an interpolation operation

* ``Success``: Operation was successful
* ``Canceled``: Operation was manually canceled
* ``InvalidSource``: Operation failed due to invalid source
* ``FeatureGeometryError``: Operation failed due to invalid feature geometry

"""
# --
try:
    QgsInterpolatorVertexData.__attribute_docs__ = {'x': 'X-coordinate', 'y': 'Y-coordinate', 'z': 'Z-coordinate'}
    QgsInterpolatorVertexData.__annotations__ = {'x': float, 'y': float, 'z': float}
    QgsInterpolatorVertexData.__doc__ = """Interpolation data for an individual source vertex."""
    QgsInterpolatorVertexData.__group__ = ['interpolation']
except (NameError, AttributeError):
    pass
try:
    QgsInterpolator.LayerData.__attribute_docs__ = {'source': 'Feature source', 'valueSource': 'Source for feature values to interpolate', 'interpolationAttribute': 'Index of feature attribute to use for interpolation', 'sourceType': 'Source type', 'transformContext': 'Coordinate transform context.\n\n.. versionadded:: 3.10.1'}
    QgsInterpolator.LayerData.__annotations__ = {'source': 'QgsFeatureSource', 'valueSource': 'QgsInterpolator.ValueSource', 'interpolationAttribute': int, 'sourceType': 'QgsInterpolator.SourceType', 'transformContext': 'QgsCoordinateTransformContext'}
    QgsInterpolator.LayerData.__doc__ = """A source together with the information about interpolation attribute / z-coordinate interpolation and the type (point, structure line, breakline)"""
    QgsInterpolator.LayerData.__group__ = ['interpolation']
except (NameError, AttributeError):
    pass
try:
    QgsInterpolator.__abstract_methods__ = ['interpolatePoint']
    QgsInterpolator.__group__ = ['interpolation']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgskde.h
# monkey patching scoped based enum
QgsKernelDensityEstimation.KernelQuartic = QgsKernelDensityEstimation.KernelShape.Quartic
QgsKernelDensityEstimation.KernelShape.KernelQuartic = QgsKernelDensityEstimation.KernelShape.Quartic
QgsKernelDensityEstimation.KernelQuartic.is_monkey_patched = True
QgsKernelDensityEstimation.KernelQuartic.__doc__ = "Quartic kernel"
QgsKernelDensityEstimation.KernelTriangular = QgsKernelDensityEstimation.KernelShape.Triangular
QgsKernelDensityEstimation.KernelShape.KernelTriangular = QgsKernelDensityEstimation.KernelShape.Triangular
QgsKernelDensityEstimation.KernelTriangular.is_monkey_patched = True
QgsKernelDensityEstimation.KernelTriangular.__doc__ = "Triangular kernel"
QgsKernelDensityEstimation.KernelUniform = QgsKernelDensityEstimation.KernelShape.Uniform
QgsKernelDensityEstimation.KernelShape.KernelUniform = QgsKernelDensityEstimation.KernelShape.Uniform
QgsKernelDensityEstimation.KernelUniform.is_monkey_patched = True
QgsKernelDensityEstimation.KernelUniform.__doc__ = "Uniform (flat) kernel"
QgsKernelDensityEstimation.KernelTriweight = QgsKernelDensityEstimation.KernelShape.Triweight
QgsKernelDensityEstimation.KernelShape.KernelTriweight = QgsKernelDensityEstimation.KernelShape.Triweight
QgsKernelDensityEstimation.KernelTriweight.is_monkey_patched = True
QgsKernelDensityEstimation.KernelTriweight.__doc__ = "Triweight kernel"
QgsKernelDensityEstimation.KernelEpanechnikov = QgsKernelDensityEstimation.KernelShape.Epanechnikov
QgsKernelDensityEstimation.KernelShape.KernelEpanechnikov = QgsKernelDensityEstimation.KernelShape.Epanechnikov
QgsKernelDensityEstimation.KernelEpanechnikov.is_monkey_patched = True
QgsKernelDensityEstimation.KernelEpanechnikov.__doc__ = "Epanechnikov kernel"
QgsKernelDensityEstimation.KernelShape.__doc__ = """Kernel shape type

* ``Quartic``: Quartic kernel

  Available as ``QgsKernelDensityEstimation.KernelQuartic`` in older QGIS releases.

* ``Triangular``: Triangular kernel

  Available as ``QgsKernelDensityEstimation.KernelTriangular`` in older QGIS releases.

* ``Uniform``: Uniform (flat) kernel

  Available as ``QgsKernelDensityEstimation.KernelUniform`` in older QGIS releases.

* ``Triweight``: Triweight kernel

  Available as ``QgsKernelDensityEstimation.KernelTriweight`` in older QGIS releases.

* ``Epanechnikov``: Epanechnikov kernel

  Available as ``QgsKernelDensityEstimation.KernelEpanechnikov`` in older QGIS releases.


"""
# --
# monkey patching scoped based enum
QgsKernelDensityEstimation.OutputRaw = QgsKernelDensityEstimation.OutputValues.Raw
QgsKernelDensityEstimation.OutputValues.OutputRaw = QgsKernelDensityEstimation.OutputValues.Raw
QgsKernelDensityEstimation.OutputRaw.is_monkey_patched = True
QgsKernelDensityEstimation.OutputRaw.__doc__ = "Output the raw KDE values"
QgsKernelDensityEstimation.OutputScaled = QgsKernelDensityEstimation.OutputValues.Scaled
QgsKernelDensityEstimation.OutputValues.OutputScaled = QgsKernelDensityEstimation.OutputValues.Scaled
QgsKernelDensityEstimation.OutputScaled.is_monkey_patched = True
QgsKernelDensityEstimation.OutputScaled.__doc__ = "Output mathematically correct scaled values"
QgsKernelDensityEstimation.OutputValues.__doc__ = """Output values type

* ``Raw``: Output the raw KDE values

  Available as ``QgsKernelDensityEstimation.OutputRaw`` in older QGIS releases.

* ``Scaled``: Output mathematically correct scaled values

  Available as ``QgsKernelDensityEstimation.OutputScaled`` in older QGIS releases.


"""
# --
# monkey patching scoped based enum
QgsKernelDensityEstimation.Success = QgsKernelDensityEstimation.Result.Success
QgsKernelDensityEstimation.Success.is_monkey_patched = True
QgsKernelDensityEstimation.Success.__doc__ = "Operation completed successfully"
QgsKernelDensityEstimation.DriverError = QgsKernelDensityEstimation.Result.DriverError
QgsKernelDensityEstimation.DriverError.is_monkey_patched = True
QgsKernelDensityEstimation.DriverError.__doc__ = "Could not open the driver for the specified format"
QgsKernelDensityEstimation.InvalidParameters = QgsKernelDensityEstimation.Result.InvalidParameters
QgsKernelDensityEstimation.InvalidParameters.is_monkey_patched = True
QgsKernelDensityEstimation.InvalidParameters.__doc__ = "Input parameters were not valid"
QgsKernelDensityEstimation.FileCreationError = QgsKernelDensityEstimation.Result.FileCreationError
QgsKernelDensityEstimation.FileCreationError.is_monkey_patched = True
QgsKernelDensityEstimation.FileCreationError.__doc__ = "Error creating output file"
QgsKernelDensityEstimation.RasterIoError = QgsKernelDensityEstimation.Result.RasterIoError
QgsKernelDensityEstimation.RasterIoError.is_monkey_patched = True
QgsKernelDensityEstimation.RasterIoError.__doc__ = "Error writing to raster"
QgsKernelDensityEstimation.Result.__doc__ = """Result of operation

* ``Success``: Operation completed successfully
* ``DriverError``: Could not open the driver for the specified format
* ``InvalidParameters``: Input parameters were not valid
* ``FileCreationError``: Error creating output file
* ``RasterIoError``: Error writing to raster

"""
# --
try:
    QgsKernelDensityEstimation.Parameters.__attribute_docs__ = {'source': 'Point feature source', 'radius': 'Fixed radius, in map units', 'radiusField': 'Field for radius, or empty if using a fixed radius', 'weightField': 'Field name for weighting field, or empty if not using weights', 'pixelSize': 'Size of pixel in output file', 'shape': 'Kernel shape', 'decayRatio': 'Decay ratio (Triangular kernels only)', 'outputValues': 'Type of output value'}
    QgsKernelDensityEstimation.Parameters.__annotations__ = {'source': 'QgsFeatureSource', 'radius': float, 'radiusField': str, 'weightField': str, 'pixelSize': float, 'shape': 'QgsKernelDensityEstimation.KernelShape', 'decayRatio': float, 'outputValues': 'QgsKernelDensityEstimation.OutputValues'}
    QgsKernelDensityEstimation.Parameters.__doc__ = """KDE parameters"""
    QgsKernelDensityEstimation.Parameters.__group__ = ['raster']
except (NameError, AttributeError):
    pass
try:
    QgsKernelDensityEstimation.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/mesh/qgsmeshcontours.h
try:
    QgsMeshContours.__group__ = ['mesh']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/mesh/qgsmeshtriangulation.h
try:
    QgsMeshZValueDatasetGroup.__overridden_methods__ = ['initialize', 'datasetMetadata', 'datasetCount', 'dataset', 'type', 'writeXml']
    QgsMeshZValueDatasetGroup.__group__ = ['mesh']
except (NameError, AttributeError):
    pass
try:
    QgsMeshEditingDelaunayTriangulation.__overridden_methods__ = ['text']
    QgsMeshEditingDelaunayTriangulation.__group__ = ['mesh']
except (NameError, AttributeError):
    pass
try:
    QgsMeshTriangulation.__group__ = ['mesh']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/processing/qgsnativealgorithms.h
try:
    QgsNativeAlgorithms.__overridden_methods__ = ['icon', 'svgIconPath', 'id', 'helpId', 'name', 'supportsNonFileBasedOutput', 'flags', 'loadAlgorithms']
    QgsNativeAlgorithms.__group__ = ['processing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/network/qgsnetworkdistancestrategy.h
try:
    QgsNetworkDistanceStrategy.__overridden_methods__ = ['cost']
    QgsNetworkDistanceStrategy.__group__ = ['network']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/network/qgsnetworkspeedstrategy.h
try:
    QgsNetworkSpeedStrategy.__overridden_methods__ = ['cost', 'requiredAttributes']
    QgsNetworkSpeedStrategy.__group__ = ['network']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/network/qgsnetworkstrategy.h
try:
    QgsNetworkStrategy.__virtual_methods__ = ['requiredAttributes']
    QgsNetworkStrategy.__abstract_methods__ = ['cost']
    QgsNetworkStrategy.__group__ = ['network']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgsninecellfilter.h
# monkey patching scoped based enum
QgsNineCellFilter.Result.Success.__doc__ = "Operation completed successfully"
QgsNineCellFilter.Result.InputLayerError.__doc__ = "Error reading input file"
QgsNineCellFilter.Result.DriverError.__doc__ = "Could not open the driver for the specified format"
QgsNineCellFilter.Result.CreateOutputError.__doc__ = "Error creating output file"
QgsNineCellFilter.Result.InputBandError.__doc__ = "Error reading input raster band"
QgsNineCellFilter.Result.OutputBandError.__doc__ = "Error reading output raster band"
QgsNineCellFilter.Result.RasterSizeError.__doc__ = "Raster height is too small (need at least 3 rows)"
QgsNineCellFilter.Result.Canceled.__doc__ = "User canceled calculation"
QgsNineCellFilter.Result.__doc__ = """
.. versionadded:: 3.44

* ``Success``: Operation completed successfully
* ``InputLayerError``: Error reading input file
* ``DriverError``: Could not open the driver for the specified format
* ``CreateOutputError``: Error creating output file
* ``InputBandError``: Error reading input raster band
* ``OutputBandError``: Error reading output raster band
* ``RasterSizeError``: Raster height is too small (need at least 3 rows)
* ``Canceled``: User canceled calculation

"""
# --
try:
    QgsNineCellFilter.__abstract_methods__ = ['processNineCellWindow']
    QgsNineCellFilter.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/processing/pdal/qgspdalalgorithms.h
try:
    QgsPdalAlgorithms.__overridden_methods__ = ['icon', 'svgIconPath', 'id', 'helpId', 'name', 'supportsNonFileBasedOutput', 'supportedOutputVectorLayerExtensions', 'supportedOutputRasterLayerExtensions', 'supportedOutputPointCloudLayerExtensions', 'loadAlgorithms']
    QgsPdalAlgorithms.__group__ = ['processing', 'pdal']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgsrastercalcnode.h
try:
    QgsRasterCalcNode.parseRasterCalcString = staticmethod(QgsRasterCalcNode.parseRasterCalcString)
    QgsRasterCalcNode.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgsrastercalculator.h
# monkey patching scoped based enum
QgsRasterCalculator.Success = QgsRasterCalculator.Result.Success
QgsRasterCalculator.Success.is_monkey_patched = True
QgsRasterCalculator.Success.__doc__ = "Calculation successful"
QgsRasterCalculator.CreateOutputError = QgsRasterCalculator.Result.CreateOutputError
QgsRasterCalculator.CreateOutputError.is_monkey_patched = True
QgsRasterCalculator.CreateOutputError.__doc__ = "Error creating output data file"
QgsRasterCalculator.InputLayerError = QgsRasterCalculator.Result.InputLayerError
QgsRasterCalculator.InputLayerError.is_monkey_patched = True
QgsRasterCalculator.InputLayerError.__doc__ = "Error reading input layer"
QgsRasterCalculator.Canceled = QgsRasterCalculator.Result.Canceled
QgsRasterCalculator.Canceled.is_monkey_patched = True
QgsRasterCalculator.Canceled.__doc__ = "User canceled calculation"
QgsRasterCalculator.ParserError = QgsRasterCalculator.Result.ParserError
QgsRasterCalculator.ParserError.is_monkey_patched = True
QgsRasterCalculator.ParserError.__doc__ = "Error parsing formula"
QgsRasterCalculator.MemoryError = QgsRasterCalculator.Result.MemoryError
QgsRasterCalculator.MemoryError.is_monkey_patched = True
QgsRasterCalculator.MemoryError.__doc__ = "Error allocating memory for result"
QgsRasterCalculator.BandError = QgsRasterCalculator.Result.BandError
QgsRasterCalculator.BandError.is_monkey_patched = True
QgsRasterCalculator.BandError.__doc__ = "Invalid band number for input"
QgsRasterCalculator.CalculationError = QgsRasterCalculator.Result.CalculationError
QgsRasterCalculator.CalculationError.is_monkey_patched = True
QgsRasterCalculator.CalculationError.__doc__ = "Error occurred while performing calculation"
QgsRasterCalculator.OpenCLKernelBuildError = QgsRasterCalculator.Result.OpenCLKernelBuildError
QgsRasterCalculator.OpenCLKernelBuildError.is_monkey_patched = True
QgsRasterCalculator.OpenCLKernelBuildError.__doc__ = "Error building OpenCL kernel"
QgsRasterCalculator.Result.__doc__ = """Result of the calculation

* ``Success``: Calculation successful
* ``CreateOutputError``: Error creating output data file
* ``InputLayerError``: Error reading input layer
* ``Canceled``: User canceled calculation
* ``ParserError``: Error parsing formula
* ``MemoryError``: Error allocating memory for result
* ``BandError``: Invalid band number for input
* ``CalculationError``: Error occurred while performing calculation
* ``OpenCLKernelBuildError``: Error building OpenCL kernel

"""
# --
try:
    QgsRasterCalculatorEntry.__attribute_docs__ = {'ref': 'Name of entry.', 'raster': 'Raster layer associated with entry.', 'bandNumber': 'Band number for entry. Numbering for bands usually starts at 1 for the first band, not 0.'}
    QgsRasterCalculatorEntry.__annotations__ = {'ref': str, 'raster': 'QgsRasterLayer', 'bandNumber': int}
    QgsRasterCalculatorEntry.rasterEntries = staticmethod(QgsRasterCalculatorEntry.rasterEntries)
    QgsRasterCalculatorEntry.__group__ = ['raster']
except (NameError, AttributeError):
    pass
try:
    QgsRasterCalculator.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgsrastermatrix.h
try:
    QgsRasterMatrix.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgsrelief.h
try:
    QgsRelief.__group__ = ['raster']
except (NameError, AttributeError):
    pass
try:
    QgsRelief.ReliefColor.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgsruggednessfilter.h
try:
    QgsRuggednessFilter.__overridden_methods__ = ['processNineCellWindow']
    QgsRuggednessFilter.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/vector/geometry_checker/qgssinglegeometrycheck.h
try:
    QgsSingleGeometryCheckError.__virtual_methods__ = ['update', 'isEqual', 'description']
    QgsSingleGeometryCheckError.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
try:
    QgsSingleGeometryCheck.__virtual_methods__ = ['collectErrors']
    QgsSingleGeometryCheck.__abstract_methods__ = ['processGeometry']
    QgsSingleGeometryCheck.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
try:
    QgsGeometryCheckErrorSingle.__group__ = ['vector', 'geometry_checker']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgsslopefilter.h
try:
    QgsSlopeFilter.__overridden_methods__ = ['processNineCellWindow']
    QgsSlopeFilter.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/interpolation/qgstininterpolator.h
# monkey patching scoped based enum
QgsTinInterpolator.Linear = QgsTinInterpolator.TinInterpolation.Linear
QgsTinInterpolator.Linear.is_monkey_patched = True
QgsTinInterpolator.Linear.__doc__ = "Linear interpolation"
QgsTinInterpolator.CloughTocher = QgsTinInterpolator.TinInterpolation.CloughTocher
QgsTinInterpolator.CloughTocher.is_monkey_patched = True
QgsTinInterpolator.CloughTocher.__doc__ = "Clough-Tocher interpolation"
QgsTinInterpolator.TinInterpolation.__doc__ = """Indicates the type of interpolation to be performed

* ``Linear``: Linear interpolation
* ``CloughTocher``: Clough-Tocher interpolation

"""
# --
try:
    QgsTinInterpolator.triangulationFields = staticmethod(QgsTinInterpolator.triangulationFields)
    QgsTinInterpolator.__overridden_methods__ = ['interpolatePoint']
    QgsTinInterpolator.__group__ = ['interpolation']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/raster/qgstotalcurvaturefilter.h
try:
    QgsTotalCurvatureFilter.__overridden_methods__ = ['processNineCellWindow']
    QgsTotalCurvatureFilter.__group__ = ['raster']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/network/qgsvectorlayerdirector.h
try:
    QgsVectorLayerDirector.__overridden_methods__ = ['makeGraph', 'name']
    QgsVectorLayerDirector.__group__ = ['network']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/georeferencing/qgsvectorwarper.h
# monkey patching scoped based enum
QgsVectorWarperTask.Result.Success.__doc__ = "Warping completed successfully"
QgsVectorWarperTask.Result.Canceled.__doc__ = "Task was canceled before completion"
QgsVectorWarperTask.Result.Error.__doc__ = "An error occurred while warping"
QgsVectorWarperTask.Result.__doc__ = """Task results

* ``Success``: Warping completed successfully
* ``Canceled``: Task was canceled before completion
* ``Error``: An error occurred while warping

"""
# --
try:
    QgsVectorWarperTask.__overridden_methods__ = ['cancel', 'run']
    QgsVectorWarperTask.__group__ = ['georeferencing']
except (NameError, AttributeError):
    pass
try:
    QgsVectorWarper.__group__ = ['georeferencing']
except (NameError, AttributeError):
    pass
# The following has been generated automatically from src/analysis/vector/qgszonalstatistics.h
try:
    QgsZonalStatistics.displayName = staticmethod(QgsZonalStatistics.displayName)
    QgsZonalStatistics.shortName = staticmethod(QgsZonalStatistics.shortName)
    QgsZonalStatistics.__group__ = ['vector']
except (NameError, AttributeError):
    pass

