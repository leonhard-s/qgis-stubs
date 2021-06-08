"""A helper module for typing unknown runtime types."""


class sip:
    """Mock object containing key objects of the sip namespace.

    This only servers to appease the type checking system; this class
    and its members are dummies with no functionality whatsoever.
    """

    class Buffer:
        """Mock for sip-handled IO buffers."""

    class wrapper:
        """Mock for sip-generated runtime wrappers.

        These wrap C++ entities. Refer to the subclasses' type stubs
        for member information.
        """

    class simplewrapper:
        """Mock for sip-handled wrapper subclasses."""


class Qsci:
    """Mock object for the QScintilla portion of PyQt5.

    This can be installed via pip as "qscintilla", but the
    "PyQt5-stubs" package does not define stubs for it, so we have to
    use dummy objects.
    """

    class QsciScintilla:
        """Mock for QsciScintilla base class."""
