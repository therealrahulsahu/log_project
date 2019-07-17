from PyQt5 import QtWidgets, QtGui
from code.frontend import login_widget, signup_widget
from code.backend import logincode, signupcode
from code.images import ic_insert_table


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1120, 630)
        self.setWindowTitle('Entry LOG')
        self.setWindowIcon(ic_insert_table)

        self.start()

    def signup_wid(self):
        form = QtWidgets.QWidget()
        signup_ui = signup_widget.Ui_Form()
        signup_ui.setupUi(form)
        signupcode.run(signup_ui)
        self.setCentralWidget(form)

    def login_wid(self):
        form = QtWidgets.QWidget()
        login_ui = login_widget.Ui_Form()
        login_ui.setupUi(form)
        logincode.run(login_ui)
        self.setCentralWidget(form)

        login_ui.pushbt_signup.clicked.connect(self.signup_wid)

    def start(self):
        self.login_wid()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MW = MyWindow()
    MW.show()

    sys.exit(app.exec_())
