"""Custom typing pseudo-objects for typing sip and Qsci objects."""

__all__ = [
    'sip',
]

import typing


_SipWrapper =  typing.NewType('_SipWrapper', object)

class sip:
    """Dummy namespace for the untyped sip module."""

    Buffer: typing.ClassVar[typing.Any]

    class simplewrapper:
        ...

    class wrapper:
        ...


class Qsci:
    """Dummy namespace for the untyped PyQt5.Qsci module."""

    class QsciScintilla:
        ...
