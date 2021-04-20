import sys
from PyQt5 import QtWidgets
from max_music_ui import MaxMusicUI


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    view = MaxMusicUI()
    view.show()
    sys.exit(app.exec_())
