from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QGuiApplication
import sys
temp = QGuiApplication(sys.argv)
im_correct = QPixmap("code\\images\\correct.ico").scaled(30, 30)
im_enter = QPixmap("code\\images\\enter.ico").scaled(30, 30)
ic_insert_table = QIcon("code\\images\\insert_table.ico")
im_wrong = QPixmap("code\\images\\wrong.ico").scaled(30, 30)
im_loading = QPixmap('code\\images\\hourglass.ico').scaled(30, 30)
# sys.exit(temp.exec_())
