# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1120, 630)
        Form.setStyleSheet("/*background-color:#59BAEA;*/\n"
                           "background-color:#8860D0;\n"
                           "")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.pushbt_fetch = QtWidgets.QPushButton(Form)
        self.pushbt_fetch.setStyleSheet("/*background-color: #f4511e;*/\n"
                                        "background-color: rgb(90, 255, 129);\n"
                                        "color: white;\n"
                                        "padding: 16px 32px;\n"
                                        "text-align: center;\n"
                                        "font-size: 16px;\n"
                                        "margin: 4px 2px;\n"
                                        "font-weight:bold;")
        self.pushbt_fetch.setObjectName("pushbt_fetch")
        self.gridLayout.addWidget(self.pushbt_fetch, 5, 4, 1, 1)
        self.le_nosdoc = QtWidgets.QLineEdit(Form)
        self.le_nosdoc.setStyleSheet("background-color:white;")
        self.le_nosdoc.setObjectName("le_nosdoc")
        self.gridLayout.addWidget(self.le_nosdoc, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        self.le_name = QtWidgets.QLineEdit(Form)
        self.le_name.setStyleSheet("background-color:white;\n"
                                   "")
        self.le_name.setObjectName("le_name")
        self.gridLayout.addWidget(self.le_name, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 6, 4, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 5)
        self.gridLayout.setColumnStretch(4, 2)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 5)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 5)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 5)
        self.gridLayout.setRowStretch(6, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tb_data = QtWidgets.QTextBrowser(Form)
        self.tb_data.setStyleSheet("background-color:white;")
        self.tb_data.setObjectName("tb_data")
        self.horizontalLayout.addWidget(self.tb_data)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 15)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.myaction(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushbt_fetch.setText(_translate("Form", "Fetch Data"))
        self.label.setText(_translate("Form", "Name (or Name\'s RegEx)"))
        self.label_2.setText(_translate("Form", "No. of Document "))

    def myaction(self, Form):
        onlyInt = QtGui.QIntValidator()
        self.le_nosdoc.setValidator(onlyInt)
        self.le_nosdoc.setText('5')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

