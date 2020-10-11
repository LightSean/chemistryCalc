# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalculatorBase.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 430)
        self.screen = QtWidgets.QLCDNumber(Dialog)
        self.screen.setEnabled(True)
        self.screen.setGeometry(QtCore.QRect(10, 30, 481, 111))
        font = QtGui.QFont()
        font.setFamily("Modern")
        font.setBold(True)
        font.setWeight(75)
        self.screen.setFont(font)
        self.screen.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.screen.setAutoFillBackground(False)
        self.screen.setStyleSheet("background-color: rgb(144, 154, 129);\n"
"\n"
"\n"
"")
        self.screen.setFrameShape(QtWidgets.QFrame.Box)
        self.screen.setFrameShadow(QtWidgets.QFrame.Plain)
        self.screen.setLineWidth(2)
        self.screen.setSmallDecimalPoint(True)
        self.screen.setDigitCount(12)
        self.screen.setProperty("value", 121.13485)
        self.screen.setObjectName("screen")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 150, 201, 31))
        self.label.setObjectName("label")
        self.molecule_line_edit = QtWidgets.QLineEdit(Dialog)
        self.molecule_line_edit.setGeometry(QtCore.QRect(220, 150, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.molecule_line_edit.setFont(font)
        self.molecule_line_edit.setText("")
        self.molecule_line_edit.setObjectName("molecule_line_edit")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 190, 481, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 271, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(290, 211, 201, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.input_asker = QtWidgets.QLabel(Dialog)
        self.input_asker.setGeometry(QtCore.QRect(10, 260, 271, 31))
        self.input_asker.setTextFormat(QtCore.Qt.AutoText)
        self.input_asker.setObjectName("input_asker")
        self.calc_param_line_edit = QtWidgets.QLineEdit(Dialog)
        self.calc_param_line_edit.setGeometry(QtCore.QRect(290, 260, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calc_param_line_edit.setFont(font)
        self.calc_param_line_edit.setText("")
        self.calc_param_line_edit.setObjectName("calc_param_line_edit")
        self.calculate_btn = QtWidgets.QPushButton(Dialog)
        self.calculate_btn.setGeometry(QtCore.QRect(160, 320, 75, 23))
        self.calculate_btn.setObjectName("calculate_btn")
        self.clear_btn = QtWidgets.QPushButton(Dialog)
        self.clear_btn.setGeometry(QtCore.QRect(260, 320, 75, 23))
        self.clear_btn.setObjectName("clear_btn")
        self.exit_btn = QtWidgets.QPushButton(Dialog)
        self.exit_btn.setGeometry(QtCore.QRect(-10, 390, 511, 41))
        self.exit_btn.setObjectName("exit_btn")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 360, 141, 16))
        self.label_3.setObjectName("label_3")
        self.showing_results_label = QtWidgets.QLabel(Dialog)
        self.showing_results_label.setGeometry(QtCore.QRect(10, 10, 481, 16))
        self.showing_results_label.setObjectName("showing_results_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Enter Molecule/Element</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">What do you want to calculate?!</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Dialog", "Moles (mole)"))
        self.comboBox.setItemText(1, _translate("Dialog", "Mass (gr)"))
        self.input_asker.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">How many grams do you have?</span></p></body></html>"))
        self.calculate_btn.setText(_translate("Dialog", "Calculate"))
        self.clear_btn.setText(_translate("Dialog", "Clear"))
        self.exit_btn.setText(_translate("Dialog", "Exit"))
        self.label_3.setText(_translate("Dialog", "Created by Sean & Benny (:"))
        self.showing_results_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">showing results for molecule : </p></body></html>"))
