import typing

from ..core import (QgsProcessingOutputDefinition, QgsProcessingParameterDefinition,
                    QgsProcessingAlgorithm,
                    QgsProcessingParameterString,
                    QgsProcessingParameterAuthConfig,
                    QgsProcessingParameterNumber,
                    QgsProcessingParameterDistance,
                    QgsProcessingParameterDuration,
                    QgsProcessingParameterFeatureSource,
                    QgsProcessingParameterFeatureSink,
                    QgsProcessingParameterFileDestination,
                    QgsProcessingParameterFolderDestination,
                    QgsProcessingParameterRasterDestination,
                    QgsProcessingParameterVectorDestination,
                    QgsProcessingParameterPointCloudDestination,
                    QgsProcessingParameterBand,
                    QgsProcessingParameterBoolean,
                    QgsProcessingParameterCrs,
                    QgsProcessingParameterEnum,
                    QgsProcessingParameterExpression,
                    QgsProcessingParameterExtent,
                    QgsProcessingParameterField,
                    QgsProcessingParameterFile,
                    QgsProcessingParameterMapLayer,
                    QgsProcessingParameterMatrix,
                    QgsProcessingParameterMultipleLayers,
                    QgsProcessingParameterPoint,
                    QgsProcessingParameterGeometry,
                    QgsProcessingParameterRange,
                    QgsProcessingParameterRasterLayer,
                    QgsProcessingParameterVectorLayer,
                    QgsProcessingParameterMeshLayer,
                    QgsProcessingParameterColor,
                    QgsProcessingParameterScale,
                    QgsProcessingParameterLayout,
                    QgsProcessingParameterLayoutItem,
                    QgsProcessingParameterDateTime,
                    QgsProcessingParameterMapTheme,
                    QgsProcessingParameterProviderConnection,
                    QgsProcessingParameterDatabaseSchema,
                    QgsProcessingParameterDatabaseTable,
                    QgsProcessingParameterCoordinateOperation,
                    QgsProcessingParameterPointCloudLayer,
                    QgsProcessingParameterAnnotationLayer,
                    QgsProcessingOutputString,
                    QgsProcessingOutputBoolean,
                    QgsProcessingOutputFile,
                    QgsProcessingOutputFolder,
                    QgsProcessingOutputHtml,
                    QgsProcessingOutputLayerDefinition,
                    QgsProcessingOutputMapLayer,
                    QgsProcessingOutputMultipleLayers,
                    QgsProcessingOutputNumber,
                    QgsProcessingOutputRasterLayer,
                    QgsProcessingOutputVectorLayer,
                    QgsProcessingOutputPointCloudLayer)

_CallableT = typing.TypeVar('_CallableT', bound=typing.Callable[..., typing.Any])


class ProcessingAlgFactoryException(Exception):
    """
    Exception raised when using @alg on a function.
    """

    def __init__(self, message: str) -> None: ...


class ProcessingAlgFactory():
    STRING = 'STRING'
    INT = 'INT'
    NUMBER = 'NUMBER'
    DISTANCE = 'DISTANCE'
    SINK = 'SINK'
    SOURCE = 'SOURCE'
    FILE = 'FILE'
    FOLDER = 'FOLDER'
    HTML = 'HTML'
    LAYERDEF = 'LAYERDEF'
    MAPLAYER = 'MAPLAYER'
    MULTILAYER = 'MULTILAYER'
    RASTER_LAYER = 'RASTER_LAYER'
    VECTOR_LAYER = 'VECTOR_LAYER'
    MESH_LAYER = 'MESH_LAYER'
    POINT_CLOUD_LAYER = 'POINT_CLOUD_LAYER'
    FILE_DEST = 'FILE_DEST'
    FOLDER_DEST = 'FOLDER_DEST'
    RASTER_LAYER_DEST = 'RASTER_LAYER_DEST'
    VECTOR_LAYER_DEST = 'VECTOR_LAYER_DEST'
    POINTCLOUD_LAYER_DEST = 'POINTCLOUD_LAYER_DEST'
    BAND = 'BAND'
    BOOL = 'BOOL'
    CRS = 'CRS'
    ENUM = 'ENUM'
    EXPRESSION = 'EXPRESSION'
    EXTENT = 'EXTENT'
    FIELD = 'FIELD'
    MATRIX = 'MATRIX'
    POINT = 'POINT'
    GEOMETRY = 'GEOMETRY'
    RANGE = 'RANGE'
    AUTH_CFG = 'AUTH_CFG'
    SCALE = 'SCALE'
    COLOR = 'COLOR'
    LAYOUT = 'LAYOUT'
    LAYOUT_ITEM = 'LAYOUT_ITEM'
    DATETIME = 'DATETIME'
    MAP_THEME = 'MAP_THEME'
    PROVIDER_CONNECTION = 'PROVIDER_CONNECTION'
    DATABASE_SCHEMA = 'DATABASE_SCHEMA'
    DATABASE_TABLE = 'DATABASE_TABLE'
    COORDINATE_OPERATION = 'COORDINATE_OPERATION'
    POINTCLOUD_LAYER = 'POINTCLOUD_LAYER'
    ANNOTATION_LAYER = 'ANNOTATION_LAYER'

    def __init__(self) -> None: ...

    def tr(self, string: str) -> str:
        """Returns a translatable string with the self.tr() function."""
        ...

    @property
    def current(self) -> typing.Optional[QgsProcessingAlgorithm]: ...

    @property
    def current_defined(self) -> bool: ...

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Callable[[_CallableT], _CallableT]: ...

    def output(self, type: typing.Type[QgsProcessingOutputDefinition], *args: typing.Any, **kwargs: typing.Any,
    ) -> typing.Callable[[_CallableT], _CallableT]:
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
            alg.POINTCLOUD_LAYER: QgsProcessingOutputPointCloudLayer
            alg.BOOL: QgsProcessingOutputBoolean

        :param type: The type of the input. This should be a type define on `alg` like alg.STRING, alg.DISTANCE
        :keyword label: The label of the output. Will convert into `description` arg.
        :keyword parent: The string ID of the parent parameter. Parent parameter must be defined before its here.
        """
        ...
    
    def help(self, helpstring: str, *args: typing.Any, **kwargs: typing.Any) -> typing.Callable[[_CallableT], _CallableT]:
        """
        Define the help for the algorithm using @alg.help. This method will
        be used instead of the doc string on the function as the help in the processing dialogs.

        :param helpstring: The help text. Use alg.tr() for translation support.
        """
        ...

    def input(self, type: QgsProcessingParameterDefinition, *args: typing.Any, **kwargs: typing.Any) -> typing.Callable[[_CallableT], _CallableT]: 
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
            alg.POINTCLOUD_LAYER_DEST: QgsProcessingParameterPointCloudDestination
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
            alg.POINTCLOUD_LAYER: QgsProcessingParameterPointCloudLayer
            alg.ANNOTATION_LAYER: QgsProcessingParameterAnnotationLayer

        :param type: The type of the input. This should be a type define on `alg` like alg.STRING, alg.DISTANCE
        :keyword label: The label of the output. Translates into `description` arg.
        :keyword parent: The string ID of the parent parameter. Parent parameter must be defined before its here.
        :keyword default: The default value set for that parameter. Translates into `defaultValue` arg.
        """
        ...


input_type_mapping = {
    str: QgsProcessingParameterString,
    int: QgsProcessingParameterNumber,
    float: QgsProcessingParameterNumber,
    bool: QgsProcessingParameterBoolean,
    ProcessingAlgFactory.NUMBER: QgsProcessingParameterNumber,
    ProcessingAlgFactory.INT: QgsProcessingParameterNumber,
    ProcessingAlgFactory.STRING: QgsProcessingParameterString,
    ProcessingAlgFactory.DISTANCE: QgsProcessingParameterDistance,
    ProcessingAlgFactory.SINK: QgsProcessingParameterFeatureSink,
    ProcessingAlgFactory.SOURCE: QgsProcessingParameterFeatureSource,
    ProcessingAlgFactory.FILE_DEST: QgsProcessingParameterFileDestination,
    ProcessingAlgFactory.FOLDER_DEST: QgsProcessingParameterFolderDestination,
    ProcessingAlgFactory.RASTER_LAYER: QgsProcessingParameterRasterLayer,
    ProcessingAlgFactory.RASTER_LAYER_DEST: QgsProcessingParameterRasterDestination,
    ProcessingAlgFactory.VECTOR_LAYER_DEST: QgsProcessingParameterVectorDestination,
    ProcessingAlgFactory.POINTCLOUD_LAYER_DEST: QgsProcessingParameterPointCloudDestination,
    ProcessingAlgFactory.BAND: QgsProcessingParameterBand,
    ProcessingAlgFactory.BOOL: QgsProcessingParameterBoolean,
    ProcessingAlgFactory.CRS: QgsProcessingParameterCrs,
    ProcessingAlgFactory.ENUM: QgsProcessingParameterEnum,
    ProcessingAlgFactory.EXPRESSION: QgsProcessingParameterExpression,
    ProcessingAlgFactory.EXTENT: QgsProcessingParameterExtent,
    ProcessingAlgFactory.FIELD: QgsProcessingParameterField,
    ProcessingAlgFactory.FILE: QgsProcessingParameterFile,
    ProcessingAlgFactory.MAPLAYER: QgsProcessingParameterMapLayer,
    ProcessingAlgFactory.MATRIX: QgsProcessingParameterMatrix,
    ProcessingAlgFactory.MULTILAYER: QgsProcessingParameterMultipleLayers,
    ProcessingAlgFactory.POINT: QgsProcessingParameterPoint,
    ProcessingAlgFactory.GEOMETRY: QgsProcessingParameterGeometry,
    ProcessingAlgFactory.RANGE: QgsProcessingParameterRange,
    ProcessingAlgFactory.VECTOR_LAYER: QgsProcessingParameterVectorLayer,
    ProcessingAlgFactory.AUTH_CFG: QgsProcessingParameterAuthConfig,
    ProcessingAlgFactory.MESH_LAYER: QgsProcessingParameterMeshLayer,
    ProcessingAlgFactory.SCALE: QgsProcessingParameterScale,
    ProcessingAlgFactory.LAYOUT: QgsProcessingParameterLayout,
    ProcessingAlgFactory.LAYOUT_ITEM: QgsProcessingParameterLayoutItem,
    ProcessingAlgFactory.COLOR: QgsProcessingParameterColor,
    ProcessingAlgFactory.DATETIME: QgsProcessingParameterDateTime,
    ProcessingAlgFactory.MAP_THEME: QgsProcessingParameterMapTheme,
    ProcessingAlgFactory.PROVIDER_CONNECTION: QgsProcessingParameterProviderConnection,
    ProcessingAlgFactory.DATABASE_SCHEMA: QgsProcessingParameterDatabaseSchema,
    ProcessingAlgFactory.DATABASE_TABLE: QgsProcessingParameterDatabaseTable,
    ProcessingAlgFactory.COORDINATE_OPERATION: QgsProcessingParameterCoordinateOperation,
    ProcessingAlgFactory.POINTCLOUD_LAYER: QgsProcessingParameterPointCloudLayer,
    ProcessingAlgFactory.ANNOTATION_LAYER: QgsProcessingParameterAnnotationLayer
}

output_type_mapping = {
    str: QgsProcessingOutputString,
    int: QgsProcessingOutputNumber,
    float: QgsProcessingOutputNumber,
    ProcessingAlgFactory.NUMBER: QgsProcessingOutputNumber,
    ProcessingAlgFactory.DISTANCE: QgsProcessingOutputNumber,
    ProcessingAlgFactory.INT: QgsProcessingOutputNumber,
    ProcessingAlgFactory.STRING: QgsProcessingOutputString,
    ProcessingAlgFactory.FILE: QgsProcessingOutputFile,
    ProcessingAlgFactory.FOLDER: QgsProcessingOutputFolder,
    ProcessingAlgFactory.HTML: QgsProcessingOutputHtml,
    ProcessingAlgFactory.LAYERDEF: QgsProcessingOutputLayerDefinition,
    ProcessingAlgFactory.MAPLAYER: QgsProcessingOutputMapLayer,
    ProcessingAlgFactory.MULTILAYER: QgsProcessingOutputMultipleLayers,
    ProcessingAlgFactory.RASTER_LAYER: QgsProcessingOutputRasterLayer,
    ProcessingAlgFactory.VECTOR_LAYER: QgsProcessingOutputVectorLayer,
    ProcessingAlgFactory.POINTCLOUD_LAYER: QgsProcessingOutputPointCloudLayer,
    ProcessingAlgFactory.BOOL: QgsProcessingOutputBoolean,
}
