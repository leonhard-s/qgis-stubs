# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : October 2014
    Copyright            : (C) 2014 by Alessandro Pasotti
    Email                : elpaso at itopen dot it
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Alessandro Pasotti'
__date__ = 'October 2014'
__copyright__ = '(C) 2014, Alessandro Pasotti'

from PyQt5 import QtCore     # NOQA

from qgis._server import *  # NOQA
"""
This folder is completed using sipify.pl script
It is not aimed to be manually edited
"""
# The following has been generated automatically from src/server/qgsserverogcapi.h
QgsServerOgcApi.Rel.baseClass = QgsServerOgcApi
QgsServerOgcApi.ContentType.baseClass = QgsServerOgcApi
# The following has been generated automatically from src/server/qgsserverparameters.h
QgsServerParameter.Name.baseClass = QgsServerParameter
# The following has been generated automatically from src/server/qgsserverquerystringparameter.h
# monkey patching scoped based enum
QgsServerQueryStringParameter.Type.String.__doc__ = ""
QgsServerQueryStringParameter.Type.Integer.__doc__ = ""
QgsServerQueryStringParameter.Type.Double.__doc__ = ""
QgsServerQueryStringParameter.Type.Boolean.__doc__ = ""
QgsServerQueryStringParameter.Type.List.__doc__ = ""
QgsServerQueryStringParameter.Type.__doc__ = 'The Type enum represents the parameter type\n\n' + '* ``String``: ' + QgsServerQueryStringParameter.Type.String.__doc__ + '\n' + '* ``Integer``: ' + QgsServerQueryStringParameter.Type.Integer.__doc__ + '\n' + '* ``Double``: ' + QgsServerQueryStringParameter.Type.Double.__doc__ + '\n' + '* ``Boolean``: ' + QgsServerQueryStringParameter.Type.Boolean.__doc__ + '\n' + '* ``List``: ' + QgsServerQueryStringParameter.Type.List.__doc__
# --
QgsServerQueryStringParameter.Type.baseClass = QgsServerQueryStringParameter
# The following has been generated automatically from src/server/qgsserverrequest.h
QgsServerRequest.Method.baseClass = QgsServerRequest
QgsServerRequest.RequestHeader.baseClass = QgsServerRequest
# The following has been generated automatically from src/server/qgsserversettings.h
QgsServerSettingsEnv.Source.baseClass = QgsServerSettingsEnv
QgsServerSettingsEnv.EnvVar.baseClass = QgsServerSettingsEnv
