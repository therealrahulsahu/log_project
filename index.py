from PyQt5 import QtWidgets
from code.frontend import (login_widget, signup_widget, forget_widget, entry_widget, exit_widget, show_widget)
from code.backend import (signupcode, forgetcode, logincode, entrycode, exitcode, showcode)
from code.images import ic_insert_table
from code.mongo_conn import myc
from code.backend import errors
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1120, 630)
        self.setWindowTitle('Entry LOG')
        self.setWindowIcon(ic_insert_table)
        self.myc = myc
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
        self.menu_bar.setVisible(True)

        form_feature = QtWidgets.QWidget()
        vbox = QtWidgets.QVBoxLayout()
        tab_widget = QtWidgets.QTabWidget()

        entry_tab = QtWidgets.QWidget()
        form1 = entry_widget.Ui_Form()
        form1.setupUi(entry_tab)
        entrycode.run(form1, self)

        exit_tab = QtWidgets.QWidget()
        form2 = exit_widget.Ui_Form()
        form2.setupUi(exit_tab)
        exitcode.run(form2, self)

        show_tab = QtWidgets.QWidget()
        form3 = show_widget.Ui_Form()
        form3.setupUi(show_tab)
        showcode.run(form3, self)

        tab_widget.addTab(entry_tab, 'Entry')
        tab_widget.addTab(exit_tab, 'Exit')
        tab_widget.addTab(show_tab, 'Show')

        vbox.addWidget(tab_widget)
        form_feature.setLayout(vbox)
        self.setCentralWidget(form_feature)

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






