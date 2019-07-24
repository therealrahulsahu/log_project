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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.le_name = QtWidgets.QLineEdit(Form)
        self.le_name.setStyleSheet("background-color:white;\n"
                                   "")
        self.le_name.setMaxLength(32)
        self.le_name.setObjectName("le_name")
        self.horizontalLayout_2.addWidget(self.le_name)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
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
        self.horizontalLayout_2.addWidget(self.pushbt_fetch)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 5)
        self.horizontalLayout_2.setStretch(4, 1)
        self.horizontalLayout_2.setStretch(5, 2)
        self.horizontalLayout_2.setStretch(6, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.combo_name = QtWidgets.QComboBox(Form)
        self.combo_name.setStyleSheet("background-color:white;")
        self.combo_name.setMaxCount(1)
        self.combo_name.setObjectName("combo_name")
        self.horizontalLayout_3.addWidget(self.combo_name)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 8)
        self.horizontalLayout_3.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.lb_warning = QtWidgets.QLabel(Form)
        self.lb_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_warning.setObjectName("lb_warning")
        self.horizontalLayout_5.addWidget(self.lb_warning)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.pushbt_mark = QtWidgets.QPushButton(Form)
        self.pushbt_mark.setStyleSheet("/*background-color: #f4511e;*/\n"
                                       "background-color: rgb(90, 255, 129);\n"
                                       "color: white;\n"
                                       "padding: 16px 32px;\n"
                                       "text-align: center;\n"
                                       "font-size: 16px;\n"
                                       "margin: 4px 2px;\n"
                                       "font-weight:bold;")
        self.pushbt_mark.setObjectName("pushbt_mark")
        self.horizontalLayout_5.addWidget(self.pushbt_mark)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 5)
        self.horizontalLayout_5.setStretch(2, 1)
        self.horizontalLayout_5.setStretch(3, 1)
        self.horizontalLayout_5.setStretch(4, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.myaction(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Mark Exit"))
        self.label_2.setText(_translate("Form", "Enter Name (Name\'s RegEx)"))
        self.pushbt_fetch.setText(_translate("Form", "Fetch"))
        self.lb_warning.setText(_translate("Form", "Enter Details"))
        self.pushbt_mark.setText(_translate("Form", "Mark Exit"))

    def myaction(self, Form):
        self.pushbt_mark.setEnabled(False)
        self.combo_name.setMaxCount(5)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

