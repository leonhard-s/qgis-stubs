# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : May 2014
    Copyright            : (C) 2014 by Nathan Woodrow
    Email                : woodrow dot nathan at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Nathan Woodrow'
__date__ = 'May 2014'
__copyright__ = '(C) 2014, Nathan Woodrow'

from qgis.PyQt import QtCore

from qgis._analysis import *
"""
This folder is completed using sipify.pl script
It is not aimed to be manually edited
"""
# The following has been generated automatically from src/analysis/georeferencing/qgsgcptransformer.h
# monkey patching scoped based enum
QgsGcpTransformerInterface.TransformMethod.Linear.__doc__ = "Linear transform"
QgsGcpTransformerInterface.TransformMethod.Helmert.__doc__ = "Helmert transform"
QgsGcpTransformerInterface.TransformMethod.PolynomialOrder1.__doc__ = "Polynomial order 1"
QgsGcpTransformerInterface.TransformMethod.PolynomialOrder2.__doc__ = "Polyonmial order 2"
QgsGcpTransformerInterface.TransformMethod.PolynomialOrder3.__doc__ = "Polynomial order"
QgsGcpTransformerInterface.TransformMethod.ThinPlateSpline.__doc__ = "Thin plate splines"
QgsGcpTransformerInterface.TransformMethod.Projective.__doc__ = "Projective"
QgsGcpTransformerInterface.TransformMethod.InvalidTransform.__doc__ = "Invalid transform"
QgsGcpTransformerInterface.TransformMethod.__doc__ = 'Available transformation methods.\n\n' + '* ``Linear``: ' + QgsGcpTransformerInterface.TransformMethod.Linear.__doc__ + '\n' + '* ``Helmert``: ' + QgsGcpTransformerInterface.TransformMethod.Helmert.__doc__ + '\n' + '* ``PolynomialOrder1``: ' + QgsGcpTransformerInterface.TransformMethod.PolynomialOrder1.__doc__ + '\n' + '* ``PolynomialOrder2``: ' + QgsGcpTransformerInterface.TransformMethod.PolynomialOrder2.__doc__ + '\n' + '* ``PolynomialOrder3``: ' + QgsGcpTransformerInterface.TransformMethod.PolynomialOrder3.__doc__ + '\n' + '* ``ThinPlateSpline``: ' + QgsGcpTransformerInterface.TransformMethod.ThinPlateSpline.__doc__ + '\n' + '* ``Projective``: ' + QgsGcpTransformerInterface.TransformMethod.Projective.__doc__ + '\n' + '* ``InvalidTransform``: ' + QgsGcpTransformerInterface.TransformMethod.InvalidTransform.__doc__
# --
# The following has been generated automatically from src/analysis/vector/geometry_checker/qgsgeometrycheck.h
QgsGeometryCheck.Flags.baseClass = QgsGeometryCheck
Flags = QgsGeometryCheck  # dirty hack since SIP seems to introduce the flags in module
