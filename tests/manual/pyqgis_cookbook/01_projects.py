# Adapted from:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/loadproject.html#loading-projects

from qgis.core import QgsProject


def load_current_project() -> None:
    project = QgsProject.instance()
    assert project is not None
    print(project.fileName())


def open_project() -> None:
    project = QgsProject.instance()
    assert project is not None
    project.read('testdata/01_project.qgs')
    print(project.fileName())
