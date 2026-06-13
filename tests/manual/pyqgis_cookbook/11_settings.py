# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/settings.html

from qgis.core import QgsProject


def settings() -> None:
    proj = QgsProject.instance()
    assert proj is not None

    # store values
    proj.writeEntry("myplugin", "mytext", "hello world")
    proj.writeEntry("myplugin", "myint", 10)
    proj.writeEntryDouble("myplugin", "mydouble", 0.01)
    proj.writeEntryBool("myplugin", "mybool", True)

    # read values (returns a tuple with the value, and a status boolean
    # which communicates whether the value retrieved could be converted to
    # its type, in these cases a string, an integer, a double and a boolean
    # respectively)

    mytext, type_conversion_ok = proj.readEntry("myplugin",
                                                "mytext",
                                                "default text")
    myint, type_conversion_ok = proj.readNumEntry("myplugin",
                                                "myint",
                                                123)
    mydouble, type_conversion_ok = proj.readDoubleEntry("myplugin",
                                                        "mydouble",
                                                        123)
    mybool, type_conversion_ok = proj.readBoolEntry("myplugin",
                                                    "mybool",
                                                    False)

    _ = mytext, myint, mydouble, mybool, type_conversion_ok
