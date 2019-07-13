from PyQt5 import QtWidgets
from code.backend.procode import run
from code.frontend.ui_datainput import Ui_MainWindow


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    run(ui)    # my code function
    MainWindow.show()
    sys.exit(app.exec_())

