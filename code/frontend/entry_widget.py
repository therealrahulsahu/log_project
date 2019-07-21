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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.le_phone = QtWidgets.QLineEdit(Form)
        self.le_phone.setStyleSheet("background-color:white;")
        self.le_phone.setObjectName("le_phone")
        self.gridLayout.addWidget(self.le_phone, 5, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.lb_emailico = QtWidgets.QLabel(Form)
        self.lb_emailico.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_emailico.setObjectName("lb_emailico")
        self.gridLayout.addWidget(self.lb_emailico, 3, 5, 1, 1)
        self.lb_addressico = QtWidgets.QLabel(Form)
        self.lb_addressico.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_addressico.setObjectName("lb_addressico")
        self.gridLayout.addWidget(self.lb_addressico, 7, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 1, 1, 1)
        self.le_email = QtWidgets.QLineEdit(Form)
        self.le_email.setStyleSheet("background-color:white;\n"
                                    "")
        self.le_email.setObjectName("le_email")
        self.gridLayout.addWidget(self.le_email, 3, 3, 1, 1)
        self.le_address = QtWidgets.QLineEdit(Form)
        self.le_address.setStyleSheet("background-color:white;")
        self.le_address.setObjectName("le_address")
        self.gridLayout.addWidget(self.le_address, 7, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 7, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 6, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 7, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 5, 6, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 1, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 1, 6, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 7, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 5, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 3, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 5, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 1, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 3, 2, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 5, 4, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 7, 2, 1, 1)
        self.le_name = QtWidgets.QLineEdit(Form)
        self.le_name.setStyleSheet("background-color:white;")
        self.le_name.setObjectName("le_name")
        self.gridLayout.addWidget(self.le_name, 1, 3, 1, 1)
        self.lb_phoneico = QtWidgets.QLabel(Form)
        self.lb_phoneico.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_phoneico.setObjectName("lb_phoneico")
        self.gridLayout.addWidget(self.lb_phoneico, 5, 5, 1, 1)
        self.lb_nameico = QtWidgets.QLabel(Form)
        self.lb_nameico.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_nameico.setObjectName("lb_nameico")
        self.gridLayout.addWidget(self.lb_nameico, 1, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem21, 6, 3, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem22, 4, 3, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem23, 8, 3, 1, 1)
        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 8)
        self.gridLayout.setColumnStretch(4, 2)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setColumnStretch(6, 6)
        self.gridLayout.setRowStretch(0, 5)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 3)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 3)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setRowStretch(7, 3)
        self.gridLayout.setRowStretch(8, 5)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem24)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem25)
        self.lb_warning = QtWidgets.QLabel(Form)
        self.lb_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_warning.setObjectName("lb_warning")
        self.horizontalLayout.addWidget(self.lb_warning)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem26)
        self.pushbt_reset = QtWidgets.QPushButton(Form)
        self.pushbt_reset.setStyleSheet("/*background-color: #f4511e;*/\n"
                                        "background-color: rgb(255, 104, 29);\n"
                                        "color: white;\n"
                                        "padding: 16px 32px;\n"
                                        "text-align: center;\n"
                                        "font-size: 16px;\n"
                                        "margin: 4px 2px;\n"
                                        "font-weight:bold;")
        self.pushbt_reset.setObjectName("pushbt_reset")
        self.horizontalLayout.addWidget(self.pushbt_reset)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem27)
        self.pushbt_okay = QtWidgets.QPushButton(Form)
        self.pushbt_okay.setStyleSheet("/*background-color: #f4511e;*/\n"
                                       "background-color: rgb(90, 255, 129);\n"
                                       "color: white;\n"
                                       "padding: 16px 32px;\n"
                                       "text-align: center;\n"
                                       "font-size: 16px;\n"
                                       "margin: 4px 2px;\n"
                                       "font-weight:bold;")
        self.pushbt_okay.setObjectName("pushbt_okay")
        self.horizontalLayout.addWidget(self.pushbt_okay)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem28)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 3)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 3)
        self.horizontalLayout.setStretch(6, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 8)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.myaction(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Make An Entry"))
        self.label_3.setText(_translate("Form", "Name"))
        self.lb_emailico.setText(_translate("Form", "T"))
        self.lb_addressico.setText(_translate("Form", "T"))
        self.label_6.setText(_translate("Form", "Address"))
        self.lb_phoneico.setText(_translate("Form", "T"))
        self.lb_nameico.setText(_translate("Form", "T"))
        self.label_4.setText(_translate("Form", "Email"))
        self.label_5.setText(_translate("Form", "Phone"))
        self.lb_warning.setText(_translate("Form", "Enter Details"))
        self.pushbt_reset.setText(_translate("Form", "Reset"))
        self.pushbt_okay.setText(_translate("Form", "Okay"))

    def myaction(self, Form):
        from code.images import im_enter
        self.lb_nameico.setPixmap(im_enter)
        self.lb_emailico.setPixmap(im_enter)
        self.lb_addressico.setPixmap(im_enter)
        self.lb_phoneico.setPixmap(im_enter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

