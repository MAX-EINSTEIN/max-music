# Filename: app.py

"""Max Music is a Music Player built using Python and PyQt5."""


import sys
from PyQt5 import QtWidgets
from max_music_ui import MaxMusicUI
from controller import MaxMusicController
from model import MaxMusicModel


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    with open("resources/darkeum.qss", 'r') as file:
        qss = file.read()
        app.setStyleSheet(qss)

    __view = MaxMusicUI()
    __model = MaxMusicModel()
    MaxMusicController(model=__model, view=__view)

    __view.show()

    sys.exit(app.exec_())
