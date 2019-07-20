from PyQt5 import QtWidgets
from code.frontend import login_widget, signup_widget, forget_widget
from code.backend import signupcode, forgetcode, logincode
from code.images import ic_insert_table
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1120, 630)
        self.setWindowTitle('Entry LOG')
        self.setWindowIcon(ic_insert_table)

        self.logged_user = ''

        self.mn_bar()
        self.start()

    def mn_bar(self):
        self.menu_bar = self.menuBar()

        quit_action = QtWidgets.QAction('&Quit Session', self)
        quit_action.setShortcut('Ctrl+Q')
        quit_action.triggered.connect(self.login_wid)

        self.file_menu = self.menu_bar.addMenu('&File')
        self.file_menu.addAction(quit_action)
        self.file_menu.addAction(quit_action)

    def forget_wid(self):
        form_forget = QtWidgets.QWidget()
        forget_ui = forget_widget.Ui_Form()
        forget_ui.setupUi(form_forget)
        forgetcode.run(forget_ui, self)
        self.setCentralWidget(form_forget)
        forget_ui.pushbt_back.clicked.connect(self.login_wid)

    def signup_wid(self):
        form_signup = QtWidgets.QWidget()
        signup_ui = signup_widget.Ui_Form()
        signup_ui.setupUi(form_signup)
        signupcode.run(signup_ui, self)
        self.setCentralWidget(form_signup)
        signup_ui.pushbt_back.clicked.connect(self.login_wid)

    def feature_wid(self):
        pass

    def login_wid(self):
        self.menu_bar.setVisible(False)
        self.logged_user = ''

        form_login = QtWidgets.QWidget()
        login_ui = login_widget.Ui_Form()
        login_ui.setupUi(form_login)
        logincode.run(login_ui, self)
        self.setCentralWidget(form_login)

        login_ui.pushbt_signup.clicked.connect(self.signup_wid)
        login_ui.pushbt_forget.clicked.connect(self.forget_wid)

    def start(self):
        self.login_wid()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    win = MyWindow()
    win.show()

    sys.exit(app.exec_())






