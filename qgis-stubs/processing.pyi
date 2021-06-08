# -*- coding: utf-8 -*-

"""
***************************************************************************
    algfactory.py
    ---------------------
    Date                 : November 2018
    Copyright            : (C) 2018 by Nathan Woodrow
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
__date__ = 'November 2018'
__copyright__ = '(C) 2018, Nathan Woodrow'

from typing import Any, Callable, Dict, List, Literal, Optional, Union

from PyQt5.QtGui import QIcon

from .core import (QgsProcessingContext,
                   QgsProcessingFeedback,
                   QgsProcessingParameterDefinition,
                   QgsProcessingAlgorithm,
                   QgsProcessingOutputDefinition,
                   QgsProcessingParameters)

_ProcessingInput = Union[
    str,
    int,
    float,
    bool,
    Literal['NUMBER'],
    Literal['INT'],
    Literal['STRING'],
    Literal['DISTANCE'],
    Literal['SINK'],
    Literal['SOURCE'],
    Literal['FILE_DEST'],
    Literal['FOLDER_DEST'],
    Literal['RASTER_LAYER'],
    Literal['RASTER_LAYER_DEST'],
    Literal['VECTOR_LAYER_DEST'],
    Literal['BAND'],
    Literal['BOOL'],
    Literal['CRS'],
    Literal['ENUM'],
    Literal['EXPRESSION'],
    Literal['EXTENT'],
    Literal['FIELD'],
    Literal['FILE'],
    Literal['MAPLAYER'],
    Literal['MATRIX'],
    Literal['MULTILAYER'],
    Literal['POINT'],
    Literal['GEOMETRY'],
    Literal['RANGE'],
    Literal['VECTOR_LAYER'],
    Literal['AUTH_CFG'],
    Literal['MESH_LAYER'],
    Literal['SCALE'],
    Literal['LAYOUT'],
    Literal['LAYOUT_ITEM'],
    Literal['COLOR'],
    Literal['DATETIME'],
    Literal['MAP_THEME'],
    Literal['PROVIDER_CONNECTION'],
    Literal['DATABASE_SCHEMA'],
    Literal['DATABASE_TABLE'],
    Literal['COORDINATE_OPERATION']]

_ProcessingOutput = Union[
    str,
    int,
    float,
    Literal['NUMBER'],
    Literal['DISTANCE'],
    Literal['INT'],
    Literal['STRING'],
    Literal['FILE'],
    Literal['FOLDER'],
    Literal['HTML'],
    Literal['LAYERDEF'],
    Literal['MAPLAYER'],
    Literal['MULTILAYER'],
    Literal['RASTER_LAYER'],
    Literal['VECTOR_LAYER'],
    Literal['BOOL']]


class ProcessingAlgFactoryException(Exception):
    """
    Exception raised when using @alg on a function.
    """

    def __init__(self, message: Any) -> None: ...


class AlgWrapper(QgsProcessingAlgorithm):
    """
    Wrapper object used to create new processing algorithms from @alg.
    """

    def __init__(self, name: Optional[str] = ..., display: Optional[str] = ..., group: Optional[str] = ..., group_id: Optional[str] = ..., inputs: Optional[Dict[Any, Any]] = ..., outputs: Optional[Dict[Any, Any]] = ..., func: Optional[Callable[..., None]] = ..., help: Optional[str] = ..., icon: Optional[str] = ...) -> None: ...

    def define(self, name: str, label: str, group: Optional[str], group_label: Optional[str], help: Optional[str] = ..., icon: str = ...) -> None: ...

    def end(self) -> None:
        """
        Finalize the wrapper logic and check for any invalid config.
        """

    def add_output(self, type: QgsProcessingOutputDefinition, **kwargs: Any) -> None: ...
    def add_help(self, helpstring: str, *args: Any, **kwargs: Any) -> None: ...
    def add_input(self, type: QgsProcessingParameterDefinition, **kwargs: Any) -> None: ...
    @property
    def inputs(self) -> Dict[str, QgsProcessingParameterDefinition]: ...
    @property
    def outputs(self) -> Dict[str, QgsProcessingOutputDefinition]: ...
    def set_func(self, func: Callable[..., Any]) -> None: ...

    @property
    def has_outputs(self) -> bool:
        """
        True if this alg wrapper has outputs defined.
        """

    @property
    def has_inputs(self) -> bool:
        """
        True if this alg wrapper has outputs defined.
        """

    # Overloads
    def name(self) -> str: ...
    def displayName(self) -> str: ...
    def group(self) -> str: ...
    def groupId(self) -> str: ...
    def processAlgorithm(self, parameters: QgsProcessingParameters, context: QgsProcessingContext, feedback: QgsProcessingFeedback) -> Dict[str, Any]: ...
    def createInstance(self) -> AlgWrapper: ...
    def initAlgorithm(self, configuration: Optional[Dict[str, Any]] = ..., p_str: Optional[str] = ..., Any: Any = ..., *args: Any, **kwargs: Any) -> None: ...
    def shortHelpString(self) -> str: ...
    def icon(self) -> QIcon: ...


class ProcessingAlgFactory():
    STRING = "STRING",
    INT = "INT",
    NUMBER = "NUMBER",
    DISTANCE = "DISTANCE",
    SINK = "SINK"
    SOURCE = "SOURCE"
    FILE = "FILE",
    FOLDER = "FOLDER",
    HTML = "HTML",
    LAYERDEF = "LAYERDEF",
    MAPLAYER = "MAPLAYER",
    MULTILAYER = "MULTILAYER",
    RASTER_LAYER = "RASTER_LAYER",
    VECTOR_LAYER = "VECTOR_LAYER",
    MESH_LAYER = "MESH_LAYER",
    FILE_DEST = "FILE_DEST",
    FOLDER_DEST = "FOLDER_DEST",
    RASTER_LAYER_DEST = "RASTER_LAYER_DEST",
    VECTOR_LAYER_DEST = "VECTOR_LAYER_DEST",
    BAND = "BAND",
    BOOL = "BOOL",
    CRS = "CRS",
    ENUM = "ENUM",
    EXPRESSION = "EXPRESSION",
    EXTENT = "EXTENT",
    FIELD = "FIELD",
    MATRIX = "MATRIX",
    POINT = "POINT",
    GEOMETRY = "GEOMETRY",
    RANGE = "RANGE",
    AUTH_CFG = "AUTH_CFG"
    SCALE = "SCALE"
    COLOR = "COLOR"
    LAYOUT = "LAYOUT"
    LAYOUT_ITEM = "LAYOUT_ITEM"
    DATETIME = "DATETIME"
    MAP_THEME = "MAP_THEME"
    PROVIDER_CONNECTION = "PROVIDER_CONNECTION"
    DATABASE_SCHEMA = "DATABASE_SCHEMA"
    DATABASE_TABLE = "DATABASE_TABLE"
    COORDINATE_OPERATION = "COORDINATE_OPERATION"

    instances: List[QgsProcessingAlgorithm]

    def __init__(self) -> None: ...

    def tr(self, string: str) -> str:
        """
        Returns a translatable string with the self.tr() function.
        """

    @property
    def current(self) -> AlgWrapper: ...
    @property
    def current_defined(self) -> bool: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

    def output(self, type: _ProcessingInput, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        """
        Define a output parameter for this algorithm using @alg.output.
        Apart from `type` this method will take all arguments and pass them though to the correct `QgsProcessingOutputDefinition ` type.

        Types:
            str: QgsProcessingOutputString
            int: QgsProcessingOutputNumber
            float: QgsProcessingOutputNumber
            alg.NUMBER: QgsProcessingOutputNumber
            alg.DISTANCE: QgsProcessingOutputNumber
            alg.INT: QgsProcessingOutputNumber
            alg.STRING: QgsProcessingOutputString
            alg.FILE: QgsProcessingOutputFile
            alg.FOLDER: QgsProcessingOutputFolder
            alg.HTML: QgsProcessingOutputHtml
            alg.LAYERDEF:  QgsProcessingOutputLayerDefinition
            alg.MAPLAYER:  QgsProcessingOutputMapLayer
            alg.MULTILAYER:  QgsProcessingOutputMultipleLayers
            alg.RASTER_LAYER: QgsProcessingOutputRasterLayer
            alg.VECTOR_LAYER: QgsProcessingOutputVectorLayer
            alg.BOOL: QgsProcessingOutputBoolean

        :param type: The type of the input. This should be a type define on `alg` like alg.STRING, alg.DISTANCE
        :keyword label: The label of the output. Will convert into `description` arg.
        :keyword parent: The string ID of the parent parameter. Parent parameter must be defined before its here.
        """

    def help(self, helpstring: str, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        """
        Define the help for the algorithm using @alg.help. This method will
        be used instead of the doc string on the function as the help in the processing dialogs.

        :param helpstring: The help text. Use alg.tr() for translation support.
        """

    def input(self, type: _ProcessingInput, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        """
        Define a input parameter for this algorithm using @alg.input.
        Apart from `type` this method will take all arguments and pass them though to the correct `QgsProcessingParameterDefinition` type.

        Types:

            str: QgsProcessingParameterString
            int: QgsProcessingParameterNumber
            float: QgsProcessingParameterNumber
            bool: QgsProcessingParameterBoolean
            alg.NUMBER: QgsProcessingParameterNumber
            alg.INT: QgsProcessingParameterNumber
            alg.STRING: QgsProcessingParameterString
            alg.DISTANCE: QgsProcessingParameterDistance
            alg.SINK: QgsProcessingParameterFeatureSink
            alg.SOURCE: QgsProcessingParameterFeatureSource
            alg.FILE_DEST: QgsProcessingParameterFileDestination
            alg.FOLDER_DEST: QgsProcessingParameterFolderDestination
            alg.RASTER_LAYER: QgsProcessingParameterRasterLayer
            alg.RASTER_LAYER_DEST: QgsProcessingParameterRasterDestination
            alg.VECTOR_LAYER_DEST: QgsProcessingParameterVectorDestination
            alg.BAND: QgsProcessingParameterBand
            alg.BOOL: QgsProcessingParameterBoolean
            alg.CRS: QgsProcessingParameterCrs
            alg.ENUM: QgsProcessingParameterEnum
            alg.EXPRESSION: QgsProcessingParameterExpression
            alg.EXTENT: QgsProcessingParameterExtent
            alg.FIELD: QgsProcessingParameterField
            alg.FILE: QgsProcessingParameterFile
            alg.MAPLAYER: QgsProcessingParameterMapLayer
            alg.MATRIX: QgsProcessingParameterMatrix
            alg.MULTILAYER: QgsProcessingParameterMultipleLayers
            alg.POINT: QgsProcessingParameterPoint
            alg.GEOMETRY: QgsProcessingParameterGeometry
            alg.RANGE: QgsProcessingParameterRange
            alg.VECTOR_LAYER: QgsProcessingParameterVectorLayer
            alg.AUTH_CFG: QgsProcessingParameterAuthConfig
            alg.MESH_LAYER: QgsProcessingParameterMeshLayer
            alg.SCALE: QgsProcessingParameterScale
            alg.LAYOUT: QgsProcessingParameterLayout
            alg.LAYOUT_ITEM: QgsProcessingParameterLayoutItem
            alg.COLOR: QgsProcessingParameterColor
            alg.DATETIME: QgsProcessingParameterDateTime
            alg.MAP_THEME: QgsProcessingParameterMapTheme
            alg.PROVIDER_CONNECTION: QgsProcessingParameterProviderConnection
            alg.DATABASE_SCHEMA: QgsProcessingParameterDatabaseSchema
            alg.DATABASE_TABLE: QgsProcessingParameterDatabaseTable
            alg.COORDINATE_OPERATION: QgsProcessingParameterCoordinateOperation

        :param type: The type of the input. This should be a type define on `alg` like alg.STRING, alg.DISTANCE
        :keyword label: The label of the output. Translates into `description` arg.
        :keyword parent: The string ID of the parent parameter. Parent parameter must be defined before its here.
        :keyword default: The default value set for that parameter. Translates into `defaultValue` arg.
        """


input_type_mapping: Dict[_ProcessingInput, QgsProcessingParameterDefinition]
output_type_mapping: Dict[_ProcessingOutput, QgsProcessingOutputDefinition]

alg = ProcessingAlgFactory()


def run(name: str, parameters: Dict[str, Any], context: QgsProcessingContext, feedback: QgsProcessingFeedback, is_child_algorithm: bool = ...) -> Dict[str, Any]: ...
