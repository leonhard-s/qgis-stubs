import types
import typing

from . import QgsMapLayer, QgsProject, QgsReadWriteContext


class edit:
    def __init__(self, layer: QgsMapLayer) -> None: ...
    def __enter__(self) -> QgsMapLayer: ...
    def __exit__(self, ex_type: typing.Type[BaseException],
                 ex_value: BaseException, traceback: types.TracebackType) -> bool: ...


class ProjectDirtyBlocker():
    """
    Context manager used to block project setDirty calls.

    .. code-block:: python

        project = QgsProject.instance()
        with QgsProject.blockDirtying(project):
            # do something

    .. versionadded:: 3.2
    """

    def __init__(self, project: QgsProject) -> None: ...
    def __enter__(self) -> QgsProject: ...
    def __exit__(self, ex_type: typing.Type[BaseException],
                 ex_value: BaseException, traceback: types.TracebackType) -> bool: ...


class ReadWriteContextEnterCategory:
    """
    Push a category to the stack

    .. code-block:: python

        context = QgsReadWriteContext()
        with QgsReadWriteContext.enterCategory(context, category, details):
            # do something

    .. versionadded:: 3.2
    """

    def __init__(self, context: QgsReadWriteContext,
                 category_name: str, details: typing.Any = ...) -> None: ...

    def __enter__(self) -> QgsReadWriteContext: ...
    def __exit__(self, ex_type: typing.Type[BaseException],
                 ex_value: BaseException, traceback: types.TracebackType) -> bool: ...


class ScopedRuntimeProfileContextManager():
    """
    Context manager used to profile blocks of code in the QgsApplication.profiler() registry.

    .. code-block:: python

        with QgsRuntimeProfiler.profile('My operation'):
            # do something

    .. versionadded:: 3.14
    """

    def __init__(
        self, operation: typing.Callable[..., typing.Any]) -> None: ...

    def __enter__(self) -> typing.Callable[..., typing.Any]: ...

    def __exit__(self, ex_type: typing.Type[BaseException],
                 ex_value: BaseException, traceback: types.TracebackType) -> bool: ...
