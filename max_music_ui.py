from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class MaxMusicUI(QMainWindow):
    """Max Music's View / User Interface (UI)"""

    def __init__(self):
        """Initialises the main window"""
        super().__init__()

        uic.loadUi('resources/mainwindow.ui', self)
