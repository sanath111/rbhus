# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbhusPipeSeqSceCreateMod.ui'
#
# Created: Tue Apr 29 22:22:36 2014
#      by: PyQt4 UI code generator 4.10.3
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
    MainWindow.resize(280, 285)
    self.centralwidget = QtGui.QWidget(MainWindow)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.gridLayout = QtGui.QGridLayout(self.centralwidget)
    self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    self.labelAdmin = QtGui.QLabel(self.centralwidget)
    self.labelAdmin.setObjectName(_fromUtf8("labelAdmin"))
    self.gridLayout.addWidget(self.labelAdmin, 8, 0, 1, 1)
    self.lineEditSequenceName = QtGui.QLineEdit(self.centralwidget)
    self.lineEditSequenceName.setEnabled(True)
    self.lineEditSequenceName.setObjectName(_fromUtf8("lineEditSequenceName"))
    self.gridLayout.addWidget(self.lineEditSequenceName, 1, 1, 1, 1)
    self.labelProjName = QtGui.QLabel(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelProjName.sizePolicy().hasHeightForWidth())
    self.labelProjName.setSizePolicy(sizePolicy)
    self.labelProjName.setObjectName(_fromUtf8("labelProjName"))
    self.gridLayout.addWidget(self.labelProjName, 0, 0, 1, 1)
    self.labelStartFrame = QtGui.QLabel(self.centralwidget)
    self.labelStartFrame.setObjectName(_fromUtf8("labelStartFrame"))
    self.gridLayout.addWidget(self.labelStartFrame, 4, 0, 1, 1)
    self.labelDesc = QtGui.QLabel(self.centralwidget)
    self.labelDesc.setObjectName(_fromUtf8("labelDesc"))
    self.gridLayout.addWidget(self.labelDesc, 9, 0, 1, 1)
    self.labelDue = QtGui.QLabel(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelDue.sizePolicy().hasHeightForWidth())
    self.labelDue.setSizePolicy(sizePolicy)
    self.labelDue.setObjectName(_fromUtf8("labelDue"))
    self.gridLayout.addWidget(self.labelDue, 7, 0, 1, 1)
    self.labelEndFrame = QtGui.QLabel(self.centralwidget)
    self.labelEndFrame.setObjectName(_fromUtf8("labelEndFrame"))
    self.gridLayout.addWidget(self.labelEndFrame, 6, 0, 1, 1)
    self.labelProjName_3 = QtGui.QLabel(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelProjName_3.sizePolicy().hasHeightForWidth())
    self.labelProjName_3.setSizePolicy(sizePolicy)
    self.labelProjName_3.setObjectName(_fromUtf8("labelProjName_3"))
    self.gridLayout.addWidget(self.labelProjName_3, 2, 0, 1, 1)
    self.labelProjName_2 = QtGui.QLabel(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelProjName_2.sizePolicy().hasHeightForWidth())
    self.labelProjName_2.setSizePolicy(sizePolicy)
    self.labelProjName_2.setObjectName(_fromUtf8("labelProjName_2"))
    self.gridLayout.addWidget(self.labelProjName_2, 1, 0, 1, 1)
    self.pushSelectSeq = QtGui.QPushButton(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushSelectSeq.sizePolicy().hasHeightForWidth())
    self.pushSelectSeq.setSizePolicy(sizePolicy)
    self.pushSelectSeq.setObjectName(_fromUtf8("pushSelectSeq"))
    self.gridLayout.addWidget(self.pushSelectSeq, 1, 2, 1, 1)
    self.lineEditProjName = QtGui.QLineEdit(self.centralwidget)
    self.lineEditProjName.setEnabled(False)
    self.lineEditProjName.setObjectName(_fromUtf8("lineEditProjName"))
    self.gridLayout.addWidget(self.lineEditProjName, 0, 1, 1, 2)
    self.lineEditSceneName = QtGui.QLineEdit(self.centralwidget)
    self.lineEditSceneName.setEnabled(True)
    self.lineEditSceneName.setObjectName(_fromUtf8("lineEditSceneName"))
    self.gridLayout.addWidget(self.lineEditSceneName, 2, 1, 1, 2)
    self.spinStartFrame = QtGui.QSpinBox(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.spinStartFrame.sizePolicy().hasHeightForWidth())
    self.spinStartFrame.setSizePolicy(sizePolicy)
    self.spinStartFrame.setMinimum(1)
    self.spinStartFrame.setMaximum(999999999)
    self.spinStartFrame.setObjectName(_fromUtf8("spinStartFrame"))
    self.gridLayout.addWidget(self.spinStartFrame, 4, 1, 1, 2)
    self.spinEndFrame = QtGui.QSpinBox(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.spinEndFrame.sizePolicy().hasHeightForWidth())
    self.spinEndFrame.setSizePolicy(sizePolicy)
    self.spinEndFrame.setMinimum(1)
    self.spinEndFrame.setMaximum(999999999)
    self.spinEndFrame.setObjectName(_fromUtf8("spinEndFrame"))
    self.gridLayout.addWidget(self.spinEndFrame, 6, 1, 1, 2)
    self.dateEditDue = QtGui.QDateTimeEdit(self.centralwidget)
    self.dateEditDue.setCalendarPopup(True)
    self.dateEditDue.setObjectName(_fromUtf8("dateEditDue"))
    self.gridLayout.addWidget(self.dateEditDue, 7, 1, 1, 2)
    self.lineEditAdmins = QtGui.QLineEdit(self.centralwidget)
    self.lineEditAdmins.setObjectName(_fromUtf8("lineEditAdmins"))
    self.gridLayout.addWidget(self.lineEditAdmins, 8, 1, 1, 2)
    self.lineEditDesc = QtGui.QLineEdit(self.centralwidget)
    self.lineEditDesc.setText(_fromUtf8(""))
    self.lineEditDesc.setObjectName(_fromUtf8("lineEditDesc"))
    self.gridLayout.addWidget(self.lineEditDesc, 9, 1, 1, 2)
    self.line = QtGui.QFrame(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
    self.line.setSizePolicy(sizePolicy)
    self.line.setFrameShape(QtGui.QFrame.HLine)
    self.line.setFrameShadow(QtGui.QFrame.Sunken)
    self.line.setObjectName(_fromUtf8("line"))
    self.gridLayout.addWidget(self.line, 12, 0, 1, 3)
    self.pushCreate = QtGui.QPushButton(self.centralwidget)
    self.pushCreate.setObjectName(_fromUtf8("pushCreate"))
    self.gridLayout.addWidget(self.pushCreate, 13, 0, 1, 3)
    spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.gridLayout.addItem(spacerItem, 11, 0, 1, 3)
    MainWindow.setCentralWidget(self.centralwidget)
    self.statusBar = QtGui.QStatusBar(MainWindow)
    self.statusBar.setObjectName(_fromUtf8("statusBar"))
    MainWindow.setStatusBar(self.statusBar)

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
    self.labelAdmin.setText(_translate("MainWindow", "admins", None))
    self.labelProjName.setText(_translate("MainWindow", "projName", None))
    self.labelStartFrame.setToolTip(_translate("MainWindow", "group owner of the project directory", None))
    self.labelStartFrame.setText(_translate("MainWindow", "startFrame", None))
    self.labelDesc.setToolTip(_translate("MainWindow", "group owner of the project directory", None))
    self.labelDesc.setText(_translate("MainWindow", "description", None))
    self.labelDue.setText(_translate("MainWindow", "due date", None))
    self.labelEndFrame.setToolTip(_translate("MainWindow", "group owner of the project directory", None))
    self.labelEndFrame.setText(_translate("MainWindow", "endFrame", None))
    self.labelProjName_3.setText(_translate("MainWindow", "sceneName", None))
    self.labelProjName_2.setText(_translate("MainWindow", "sequenceName", None))
    self.pushSelectSeq.setText(_translate("MainWindow", "select", None))
    self.lineEditAdmins.setToolTip(_translate("MainWindow", "list of space separated usernames", None))
    self.lineEditDesc.setToolTip(_translate("MainWindow", "description of the seq/sce", None))
    self.pushCreate.setText(_translate("MainWindow", "create", None))

