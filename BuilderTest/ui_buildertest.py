# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_buildertest.ui'
#
# Created: Sat Oct  4 07:29:34 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BuilderTest(object):
    def setupUi(self, BuilderTest):
        BuilderTest.setObjectName(_fromUtf8("BuilderTest"))
        BuilderTest.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(BuilderTest)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layerCombo = QtGui.QComboBox(BuilderTest)
        self.layerCombo.setGeometry(QtCore.QRect(80, 110, 261, 41))
        self.layerCombo.setObjectName(_fromUtf8("layerCombo"))

        self.retranslateUi(BuilderTest)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), BuilderTest.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), BuilderTest.reject)
        QtCore.QMetaObject.connectSlotsByName(BuilderTest)

    def retranslateUi(self, BuilderTest):
        BuilderTest.setWindowTitle(_translate("BuilderTest", "BuilderTest", None))

