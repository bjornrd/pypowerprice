import PySide6
from PySide6 import QtCore, QtWidgets, QtGui

from ui.ui_appmainwindow import Ui_MainWindow

class ApplicationMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)