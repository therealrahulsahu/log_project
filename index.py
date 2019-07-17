from PyQt5 import QtWidgets, QtGui
from code.frontend import login_widget, signup_widget
from code.backend import logincode, signupcode

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    Form1 = QtWidgets.QWidget()
    login_ui = login_widget.Ui_Form()
    login_ui.setupUi(Form1)
    logincode.run(login_ui)
    Form1.show()
    del Form1
    Form2 = QtWidgets.QWidget()
    signup_ui = signup_widget.Ui_Form()
    signup_ui.setupUi(Form2)
    signupcode.run(signup_ui)
    Form2.show()


    sys.exit(app.exec_())

