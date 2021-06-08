# -*- coding: utf-8 -*-

"""
***************************************************************************
    user.py
    ---------------------
    Date                 : January 2015
    Copyright            : (C) 2015 by Nathan Woodrow
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
__date__ = 'January 2015'
__copyright__ = '(C) 2015, Nathan Woodrow'


def load_user_expressions(path: str) -> None:
    """
    Load all user expressions from the given paths
    """

userpythonhome: str
expressionspath: str

initfile: str 

template = """from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom', referenced_columns=[])
def my_sum(value1, value2, feature, parent):
    \"\"\"
    Calculates the sum of the two parameters value1 and value2.
    <h2>Example usage:</h2>
    <ul>
      <li>my_sum(5, 8) -> 13</li>
      <li>my_sum(\"field1\", \"field2\") -> 42</li>
    </ul>
    \"\"\"
    return value1 + value2
"""

default_expression_template = template
