# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : January 2007
    Copyright            : (C) 2007 by Martin Dobias
    Email                : wonder dot sk at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Martin Dobias'
__date__ = 'January 2007'
__copyright__ = '(C) 2007, Martin Dobias'

from . import analysis, core, gui, processing, server, user, utils

__all__ = [
    'analysis',
    'core',
    'gui',
    'processing',
    'server',
    'user',
    'utils'
]


def setupenv() -> None:
    """
    Set the environment for Windows based on the .vars files from the
    OSGeo4W package format.
    """
