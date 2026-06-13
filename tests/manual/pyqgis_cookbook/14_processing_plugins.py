# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/processing.html

import typing
from qgis.core import (
    QgsProcessingAlgorithm,
    QgsProcessingContext,
    QgsProcessingFeedback,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterNumber,
    QgsProcessingParameterFeatureSink,
    QgsFeatureSink,
)

_AnyDict = typing.Dict[str, typing.Any]


class BufferAlgorithm(QgsProcessingAlgorithm):

    # pylint: disable=missing-class-docstring

    INPUT = 'INPUT'
    DISTANCE = 'DISTANCE'
    OUTPUT = 'OUTPUT'

    def initAlgorithm(self, config: _AnyDict | None = None) -> None:
        _ = config

        self.addParameter(QgsProcessingParameterFeatureSource(
            self.INPUT, 'Input layer'))
        self.addParameter(QgsProcessingParameterNumber(
            self.DISTANCE, 'Buffer distance', defaultValue=100.0))
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT, 'Output layer'))

    def processAlgorithm(self, parameters: _AnyDict,
                         context: QgsProcessingContext,
                         feedback: QgsProcessingFeedback | None) -> _AnyDict:
        _ = feedback

        source = self.parameterAsSource(parameters, self.INPUT, context)
        distance = self.parameterAsDouble(parameters, self.DISTANCE, context)
        (sink, dest_id) = self.parameterAsSink(
            parameters, self.OUTPUT, context,
            source.fields(), source.wkbType(), source.sourceCrs())
        for f in source.getFeatures():
            f.setGeometry(f.geometry().buffer(distance, 5))
            sink.addFeature(f, QgsFeatureSink.Flag.FastInsert)

        return {self.OUTPUT: dest_id}

    def name(self) -> str:
        return 'buffer'

    def displayName(self) -> str:
        return 'Buffer Features'

    def group(self) -> str:
        return 'Examples'

    def groupId(self) -> str:
        return 'examples'

    def createInstance(self) -> QgsProcessingAlgorithm:
        return BufferAlgorithm()
