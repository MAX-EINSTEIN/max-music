from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5 import QtGui
from PyQt5 import uic


class MaxMusicUI(QMainWindow):
    """Max Music's View / User Interface (UI)"""

    def __init__(self):
        """Initialises the main window"""
        super().__init__()

        uic.loadUi('resources/mainwindow.ui', self)

        # self.WINDOW_WIDTH = 1120
        # self.WINDOW_HEIGTH = 800

        # self.resize(self.WINDOW_WIDTH, self.WINDOW_HEIGTH)
        # self.setWindowTitle('Max Music')
        # self.setWindowIcon(QtGui.QIcon('resources/app-icon.png'))
        # # self.setStyleSheet("QWidget{background: #000000}")

        # self.generalLayout = QVBoxLayout()
        # self._centralWidget = QWidget(self)
        # self.setCentralWidget(self._centralWidget)
        # self._centralWidget.setLayout(self.generalLayout)
