import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from my_windows.main_window import Ui_MainWindow
import qdarkstyle    


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_win=MyWindow()
    my_win.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    my_win.show()
    sys.exit(app.exec_())