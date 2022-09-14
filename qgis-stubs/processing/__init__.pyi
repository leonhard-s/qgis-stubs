import typing

from ..core import QgsProcessingContext, QgsProcessingFeedback
from .algfactory import ProcessingAlgFactory

alg = ProcessingAlgFactory()

def run(name: str, parameters: typing.Dict[str, typing.Any],
        is_child_algorithm: bool = ..., context: QgsProcessingContext = ...,
        feedback: QgsProcessingFeedback = ...) -> typing.Dict[str, typing.Any]: ...
