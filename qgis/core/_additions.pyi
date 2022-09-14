import typing

from . import (QgsAbstractValidityCheck, QgsExpressionFunction,
               QgsSettingsEntryBase, Qgis)

from ._context_managers import (edit, ProjectDirtyBlocker,
                                ReadWriteContextEnterCategory,
                                ScopedRuntimeProfileContextManager)

# NOTE: Some monkey-patched methods have been typed directly into their
# respective classes:
#
# - QgsTask.fromFunction()


class QgsEditError(Exception):
    def __init__(self, value: typing.Any) -> None: ...
    def __str__(self) -> str: ...


def register_function(
        function: typing.Callable[..., typing.Any], arg_count: typing.Union[str, int], group: str, usesgeometry: bool = ...,
        referenced_columns: typing.List[str] = ..., handlesnull: bool = ..., **kwargs: typing.Any) -> QgsExpressionFunction:
    """
    Register a Python function to be used as a expression function.

    Functions should take (values, feature, parent) as args:

    Example:
        def myfunc(values, feature, parent):
            pass

    They can also shortcut naming feature and parent args by using *args
    if they are not needed in the function.

    Example:
        def myfunc(values, *args):
            pass

    Functions should return a value compatible with QVariant

    Eval errors can be raised using parent.setEvalErrorString("Error message")

    :param function:
    :param arg_count:
    :param group:
    :param usesgeometry:
    :param handlesnull: Needs to be set to True if this function does not always return NULL if any parameter is NULL. Default False.
    :return:
    """
    ...


def qgsfunction(args: typing.Union[int, str] = ..., group: str = ..., **kwargs: typing.Any,
                ) -> typing.Callable[[typing.Callable[..., typing.Any]], typing.Callable[..., typing.Any]]:
    r"""
    Decorator function used to define a user expression function.

    :param args: Number of parameters, set to 'auto' to accept a variable length of parameters.
    :param group: The expression group to which this expression should be added.
    :param \**kwargs:
        See below

    :Keyword Arguments:
        * *referenced_columns* (``list``) --
          An array of field names on which this expression works. Can be set to ``[QgsFeatureRequest.ALL_ATTRIBUTES]``. By default empty.
        * *usesgeometry* (``bool``) --
          Defines if this expression requires the geometry. By default False.
        * *handlesnull* (``bool``) --
          Defines if this expression has custom handling for NULL values. If False, the result will always be NULL as soon as any parameter is NULL. False by default.

    Example:
      @qgsfunction(2, 'test'):
      def add(values, feature, parent):
        pass

    Will create and register a function in QgsExpression called 'add' in the
    'test' group that takes two arguments.

    or not using feature and parent:

    Example:
      @qgsfunction(2, 'test'):
      def add(values, *args):
        pass
    """
    ...


class PyQgsSettingsEntryEnumFlag(QgsSettingsEntryBase):
    """
    class PyQgsSettingsEntryEnumFlag
    An enum settings entry.
    since QGIS 3.20
    """

    def __init__(self, key: str, pluginName: str, defaultValue: typing.Any, description: str = ..., options: Qgis.SettingsOptions = ...) -> None:
        """
        Constructor for PyQgsSettingsEntryEnumFlag.
        :param key: argument specifies the final part of the settings key.
        :param pluginName: argument is inserted in the key after the section.
        :param defaultValue: argument specifies the default value for the settings entry.
        :param description: argument specifies a description for the settings entry.
        """
        ...

    def value(self, dynamicKeyPart: typing.Optional[str] = ...) -> typing.Any:
        """
        Get settings value.
        :param dynamicKeyPart: argument specifies the dynamic part of the settings key.
        """
        ...

    def valueWithDefaultOverride(self, defaultValueOverride: typing.Any, dynamicKeyPart: typing.Optional[str] = ...) -> typing.Any:
        """
        Get settings value with a default value override.
        :param defaultValueOverride: argument if valid is used instead of the normal default value.
        :param dynamicKeyPart: argument specifies the dynamic part of the settings key.
        """
        ...

    def defaultValue(self) -> typing.Any:
        """
        Get settings default value.
        """
        ...

    def setValue(self, value: typing.Any, dynamicKeyPart: typing.Union[typing.List[str], str, None] = ...) -> bool:
        """
        Set settings value.
        :param value: the value to set for the setting.
        :param dynamicKeyPart: argument specifies the dynamic part of the settings key (a single one a string, or several as a list)
        """
        ...

    def settingsType(self) -> Qgis.SettingsType:
        """
        Get the settings entry type.
        """
        ...


class check:
    """Constructs QgsAbstractValidityChecks using a decorator.

    To use, Python based checks should use the decorator syntax:

    .. code-block:: python
        @check.register(type=QgsAbstractValidityCheck.TypeLayoutCheck)
        def my_layout_check(context, feedback):
            results = ...
            return results

    """

    def __init__(self) -> None: ...

    def register(self, type: QgsAbstractValidityCheck.Type, *args: typing.Any, **kwargs: typing.Any) -> typing.Callable[[typing.Callable[..., typing.Any]], None]:
        """Implements a decorator for registering Python based checks.

        :param type: check type, e.g. QgsAbstractValidityCheck.Type.TypeLayoutCheck
        """
        ...
