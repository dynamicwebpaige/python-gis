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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from buildertestdialog import BuilderTestDialog
import os.path


class BuilderTest:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'buildertest_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = BuilderTestDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/buildertest/icon.png"),
            u"Builder Test", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Builder Test", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Builder Test", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()

        layers = QgsMapLayerRegistry.instance().mapLayers().values()
        for layer in layers:
        	if layer.type() == QgsMapLayer.VectorLayer:
        		self.dlg.layerCombo.addItem(layer.name(), layer)
        # Run the dialog event loop 
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
        	index = self.dlg.layerCombo.currentIndex()
        	layer = self.dlg.layerCombo.itemData(index)
        	QMessageBox.information(self.iface.mainWindow(),"PyTexas 2014","The layer named %s has %d features." %(layer.name(),layer.featureCount()))
