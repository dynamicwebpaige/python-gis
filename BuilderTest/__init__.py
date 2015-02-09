# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BuilderTest
                                 A QGIS plugin
 Python plugin that gives a feature count for any given displayed layer. (PyTexas 2014)
                             -------------------
        begin                : 2014-10-04
        copyright            : (C) 2014 by Paige Bailey
        email                : paige.bailey@alumni.rice.edu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load BuilderTest class from file BuilderTest
    from buildertest import BuilderTest
    return BuilderTest(iface)
