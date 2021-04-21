# Filename: max_music_ui.py

"""Max Music is a Music Player built using Python and PyQt5."""


from PyQt5.QtWidgets import QMainWindow
# from PyQt5 import uic
from main_window_ui import Ui_MainWindow

__version__ = '0.1.0'
__author__ = 'Junaid Siddiqui'


class MaxMusicUI(QMainWindow, Ui_MainWindow):
    """Max Music's View / User Interface (UI)"""

    def __init__(self):
        """Initialises the main window"""
        super().__init__()

        # [Use when UI is finalised]
        self.setupUi(self)

        # [Use when creating/editing UI]
        # uic.loadUi('resources/mainwindow.ui', self)

        # Map objectNames for Ui elements to variables
