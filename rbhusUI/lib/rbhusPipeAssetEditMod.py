# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbhusPipeAssetEditMod.ui'
#
# Created: Tue Nov  4 22:15:01 2014
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName(_fromUtf8("MainWindow"))
    MainWindow.setEnabled(True)
    MainWindow.resize(397, 200)
    self.centralwidget = QtGui.QWidget(MainWindow)
    self.centralwidget.setEnabled(True)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.gridLayout = QtGui.QGridLayout(self.centralwidget)
    self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.gridLayout.addItem(spacerItem, 11, 0, 1, 6)
    self.pushUsers = QtGui.QPushButton(self.centralwidget)
    self.pushUsers.setObjectName(_fromUtf8("pushUsers"))
    self.gridLayout.addWidget(self.pushUsers, 6, 5, 1, 1)
    self.line = QtGui.QFrame(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
    self.line.setSizePolicy(sizePolicy)
    self.line.setFrameShape(QtGui.QFrame.HLine)
    self.line.setFrameShadow(QtGui.QFrame.Sunken)
    self.line.setObjectName(_fromUtf8("line"))
    self.gridLayout.addWidget(self.line, 12, 0, 1, 6)
    self.checkDueDate = QtGui.QCheckBox(self.centralwidget)
    self.checkDueDate.setEnabled(True)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkDueDate.sizePolicy().hasHeightForWidth())
    self.checkDueDate.setSizePolicy(sizePolicy)
    self.checkDueDate.setText(_fromUtf8(""))
    self.checkDueDate.setChecked(False)
    self.checkDueDate.setObjectName(_fromUtf8("checkDueDate"))
    self.gridLayout.addWidget(self.checkDueDate, 4, 5, 1, 1)
    self.labelDesc = QtGui.QLabel(self.centralwidget)
    self.labelDesc.setObjectName(_fromUtf8("labelDesc"))
    self.gridLayout.addWidget(self.labelDesc, 7, 0, 1, 1)
    self.labelFRange = QtGui.QLabel(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelFRange.sizePolicy().hasHeightForWidth())
    self.labelFRange.setSizePolicy(sizePolicy)
    self.labelFRange.setObjectName(_fromUtf8("labelFRange"))
    self.gridLayout.addWidget(self.labelFRange, 2, 0, 1, 1)
    self.pushEdit = QtGui.QPushButton(self.centralwidget)
    self.pushEdit.setObjectName(_fromUtf8("pushEdit"))
    self.gridLayout.addWidget(self.pushEdit, 13, 0, 1, 6)
    self.pushTags = QtGui.QPushButton(self.centralwidget)
    self.pushTags.setObjectName(_fromUtf8("pushTags"))
    self.gridLayout.addWidget(self.pushTags, 10, 5, 1, 1)
    self.labelDue = QtGui.QLabel(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelDue.sizePolicy().hasHeightForWidth())
    self.labelDue.setSizePolicy(sizePolicy)
    self.labelDue.setObjectName(_fromUtf8("labelDue"))
    self.gridLayout.addWidget(self.labelDue, 4, 0, 1, 1)
    self.labelTags = QtGui.QLabel(self.centralwidget)
    self.labelTags.setObjectName(_fromUtf8("labelTags"))
    self.gridLayout.addWidget(self.labelTags, 10, 0, 1, 1)
    self.labelAssignTo = QtGui.QLabel(self.centralwidget)
    self.labelAssignTo.setObjectName(_fromUtf8("labelAssignTo"))
    self.gridLayout.addWidget(self.labelAssignTo, 6, 0, 1, 1)
    self.checkAssignSelf = QtGui.QCheckBox(self.centralwidget)
    self.checkAssignSelf.setChecked(False)
    self.checkAssignSelf.setObjectName(_fromUtf8("checkAssignSelf"))
    self.gridLayout.addWidget(self.checkAssignSelf, 6, 4, 1, 1)
    self.checkFRange = QtGui.QCheckBox(self.centralwidget)
    self.checkFRange.setEnabled(True)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkFRange.sizePolicy().hasHeightForWidth())
    self.checkFRange.setSizePolicy(sizePolicy)
    self.checkFRange.setText(_fromUtf8(""))
    self.checkFRange.setChecked(False)
    self.checkFRange.setObjectName(_fromUtf8("checkFRange"))
    self.gridLayout.addWidget(self.checkFRange, 2, 5, 1, 1)
    self.lineEditDesc = QtGui.QLineEdit(self.centralwidget)
    self.lineEditDesc.setEnabled(False)
    self.lineEditDesc.setText(_fromUtf8(""))
    self.lineEditDesc.setObjectName(_fromUtf8("lineEditDesc"))
    self.gridLayout.addWidget(self.lineEditDesc, 7, 1, 1, 4)
    self.lineEditTags = QtGui.QLineEdit(self.centralwidget)
    self.lineEditTags.setEnabled(False)
    self.lineEditTags.setObjectName(_fromUtf8("lineEditTags"))
    self.gridLayout.addWidget(self.lineEditTags, 10, 1, 1, 3)
    self.checkDesc = QtGui.QCheckBox(self.centralwidget)
    self.checkDesc.setEnabled(True)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkDesc.sizePolicy().hasHeightForWidth())
    self.checkDesc.setSizePolicy(sizePolicy)
    self.checkDesc.setText(_fromUtf8(""))
    self.checkDesc.setChecked(False)
    self.checkDesc.setObjectName(_fromUtf8("checkDesc"))
    self.gridLayout.addWidget(self.checkDesc, 7, 5, 1, 1)
    self.dateEditDue = QtGui.QDateTimeEdit(self.centralwidget)
    self.dateEditDue.setEnabled(False)
    self.dateEditDue.setCalendarPopup(True)
    self.dateEditDue.setObjectName(_fromUtf8("dateEditDue"))
    self.gridLayout.addWidget(self.dateEditDue, 4, 1, 1, 4)
    self.lineEditFRange = QtGui.QLineEdit(self.centralwidget)
    self.lineEditFRange.setEnabled(False)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEditFRange.sizePolicy().hasHeightForWidth())
    self.lineEditFRange.setSizePolicy(sizePolicy)
    self.lineEditFRange.setObjectName(_fromUtf8("lineEditFRange"))
    self.gridLayout.addWidget(self.lineEditFRange, 2, 1, 1, 4)
    self.checkTags = QtGui.QCheckBox(self.centralwidget)
    self.checkTags.setEnabled(True)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkTags.sizePolicy().hasHeightForWidth())
    self.checkTags.setSizePolicy(sizePolicy)
    self.checkTags.setText(_fromUtf8(""))
    self.checkTags.setChecked(False)
    self.checkTags.setObjectName(_fromUtf8("checkTags"))
    self.gridLayout.addWidget(self.checkTags, 10, 4, 1, 1)
    self.lineEditWorkers = QtGui.QLineEdit(self.centralwidget)
    self.lineEditWorkers.setEnabled(False)
    self.lineEditWorkers.setObjectName(_fromUtf8("lineEditWorkers"))
    self.gridLayout.addWidget(self.lineEditWorkers, 6, 1, 1, 2)
    self.checkAssign = QtGui.QCheckBox(self.centralwidget)
    self.checkAssign.setEnabled(True)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkAssign.sizePolicy().hasHeightForWidth())
    self.checkAssign.setSizePolicy(sizePolicy)
    self.checkAssign.setText(_fromUtf8(""))
    self.checkAssign.setChecked(False)
    self.checkAssign.setObjectName(_fromUtf8("checkAssign"))
    self.gridLayout.addWidget(self.checkAssign, 6, 3, 1, 1)
    MainWindow.setCentralWidget(self.centralwidget)
    self.statusBar = QtGui.QStatusBar(MainWindow)
    self.statusBar.setObjectName(_fromUtf8("statusBar"))
    MainWindow.setStatusBar(self.statusBar)

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(_translate("MainWindow", "Edit Asset", None))
    self.pushUsers.setText(_translate("MainWindow", "select", None))
    self.labelDesc.setToolTip(_translate("MainWindow", "group owner of the project directory", None))
    self.labelDesc.setText(_translate("MainWindow", "description", None))
    self.labelFRange.setText(_translate("MainWindow", "fRange", None))
    self.pushEdit.setText(_translate("MainWindow", "edit", None))
    self.pushTags.setText(_translate("MainWindow", "select", None))
    self.labelDue.setText(_translate("MainWindow", "due date", None))
    self.labelTags.setToolTip(_translate("MainWindow", "group owner of the project directory", None))
    self.labelTags.setText(_translate("MainWindow", "tags", None))
    self.labelAssignTo.setText(_translate("MainWindow", "assign to", None))
    self.checkAssignSelf.setText(_translate("MainWindow", "self", None))
    self.lineEditDesc.setToolTip(_translate("MainWindow", "group owner of the project directory", None))
    self.lineEditTags.setToolTip(_translate("MainWindow", "group owner of the project directory", None))
    self.lineEditTags.setText(_translate("MainWindow", "default", None))
    self.lineEditFRange.setText(_translate("MainWindow", "1", None))
    self.lineEditWorkers.setToolTip(_translate("MainWindow", "list of space separated usernames", None))

