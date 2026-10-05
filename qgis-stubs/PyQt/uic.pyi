from os import PathLike
from typing import IO, Any, TypeVar, overload

from PyQt6.QtWidgets import QWidget

_W = TypeVar('_W', bound=QWidget)
_UiFile = str | PathLike[str] | IO[str] | IO[bytes]

# PyQt6-stubs has no uic module. The generated form classes and widgets are
# only known at runtime, so they are typed as Any.
def loadUiType(uifile: _UiFile) -> tuple[Any, Any]: ...

@overload
def loadUi(uifile: _UiFile, baseinstance: None = None, package: str = '') -> Any: ...
@overload
def loadUi(uifile: _UiFile, baseinstance: _W, package: str = '') -> _W: ...
