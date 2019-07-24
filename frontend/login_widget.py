from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1120, 630)
        Form.setStyleSheet("background-color:#59BAEA;\n"
                           "/*background-color:#8860D0;*/\n"
                           "")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.le_username = QtWidgets.QLineEdit(Form)
        self.le_username.setStyleSheet("background-color:white;")
        self.le_username.setMaxLength(32)
        self.le_username.setObjectName("le_username")
        self.horizontalLayout.addWidget(self.le_username)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 10)
        self.horizontalLayout.setStretch(4, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.le_password = QtWidgets.QLineEdit(Form)
        self.le_password.setStyleSheet("background-color:white;")
        self.le_password.setMaxLength(32)
        self.le_password.setObjectName("le_password")
        self.horizontalLayout_2.addWidget(self.le_password)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 10)
        self.horizontalLayout_2.setStretch(4, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.pushbt_login = QtWidgets.QPushButton(Form)
        self.pushbt_login.setMouseTracking(True)
        self.pushbt_login.setToolTip("")
        self.pushbt_login.setStyleSheet("background-color: #f4511e;\n"
                                        "color: white;\n"
                                        "padding: 16px 32px;\n"
                                        "text-align: center;\n"
                                        "font-size: 16px;\n"
                                        "margin: 4px 2px;\n"
                                        "font-weight:bold;")
        self.pushbt_login.setObjectName("pushbt_login")
        self.horizontalLayout_5.addWidget(self.pushbt_login)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.lb_loginico = QtWidgets.QLabel(Form)
        self.lb_loginico.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_loginico.setObjectName("lb_loginico")
        self.horizontalLayout_5.addWidget(self.lb_loginico)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.horizontalLayout_5.setStretch(0, 22)
        self.horizontalLayout_5.setStretch(1, 8)
        self.horizontalLayout_5.setStretch(2, 3)
        self.horizontalLayout_5.setStretch(3, 1)
        self.horizontalLayout_5.setStretch(4, 7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.pushbt_forget = QtWidgets.QPushButton(Form)
        self.pushbt_forget.setStyleSheet("background-color: #f4511e;\n"
                                         "color: white;\n"
                                         "padding: 16px 32px;\n"
                                         "text-align: center;\n"
                                         "font-size: 16px;\n"
                                         "margin: 4px 2px;\n"
                                         "font-weight:bold;")
        self.pushbt_forget.setObjectName("pushbt_forget")
        self.horizontalLayout_3.addWidget(self.pushbt_forget)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.pushbt_signup = QtWidgets.QPushButton(Form)
        self.pushbt_signup.setStyleSheet("background-color: #f4511e;\n"
                                         "color: white;\n"
                                         "padding: 16px 32px;\n"
                                         "text-align: center;\n"
                                         "font-size: 16px;\n"
                                         "margin: 4px 2px;\n"
                                         "font-weight:bold;")
        self.pushbt_signup.setObjectName("pushbt_signup")
        self.horizontalLayout_3.addWidget(self.pushbt_signup)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 15)
        self.horizontalLayout_3.setStretch(2, 30)
        self.horizontalLayout_3.setStretch(3, 10)
        self.horizontalLayout_3.setStretch(4, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(0, 20)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 20)
        self.verticalLayout_2.setStretch(5, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.myaction(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "User Login"))
        self.label.setText(_translate("Form", "Username"))
        self.label_2.setText(_translate("Form", "Password"))
        self.pushbt_login.setText(_translate("Form", "Login"))
        self.lb_loginico.setText(_translate("Form", "T"))
        self.pushbt_forget.setText(_translate("Form", "Forget Password or Username"))
        self.pushbt_signup.setText(_translate("Form", "Sign Up"))

    def myaction(self, Form):
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

