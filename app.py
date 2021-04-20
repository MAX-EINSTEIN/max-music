import sys
from PyQt5 import QtWidgets
from max_music_ui import MaxMusicUI


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    with open("resources/darkeum.qss", 'r') as file:
        qss = file.read()
        app.setStyleSheet(qss)

    view = MaxMusicUI()
    view.show()
    sys.exit(app.exec_())
