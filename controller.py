# Filename: controller.py

"""Max Music is a Music Player built using Python and PyQt5."""
from PyQt5 import QtCore
from max_music_ui import MaxMusicUI
from model import MaxMusicModel
from PyQt5.QtWidgets import QProgressBar, QTableWidgetItem, QTableWidget, QToolButton, QSlider
import random


class MaxMusicController:
    """Max Music's Controller."""

    def __init__(self, model: MaxMusicModel, view: MaxMusicUI) -> None:
        """Controller initializer """
        self._model = model
        self._view = view

        # Songs Table Widget
        self.col_count = 5
        self.songs_tw: QTableWidget = self._view.songs_tv
        self.populateSongsTable()

        # Music Controls
        self.shuffle_btn: QToolButton = self._view.shuffle_btn
        self.prev_btn: QToolButton = self._view.previous_btn
        self.pp_btn: QToolButton = self._view.play_pause_btn
        self.nxt_btn: QToolButton = self._view.next_btn
        self.loop_btn: QToolButton = self._view.repeat_btn
        self._index = 0
        self._loop = False
        self.song_pb: QProgressBar = self._view.song_progress_bar
        self.song_pb.setMinimum(0)
        self.song_pb.setMaximum(0)

        # Volume
        self.vol_slider: QSlider = self._view.vol_slider
        self.vol_slider.setMinimum = 0
        self.vol_slider.setMaximum = 100

        # Connect signals and slots
        self._connectSignals()

    def _connectSignals(self) -> None:
        # Music Controls
        self.shuffle_btn.clicked.connect(lambda: self.shuffle())
        self.prev_btn.clicked.connect(lambda: self.previous())
        self.pp_btn.clicked.connect(lambda: self.play())
        self.nxt_btn.clicked.connect(lambda: self.next())
        self.loop_btn.clicked.connect(lambda: self.loop())

        # Volume
        self.vol_slider.valueChanged[int].connect(self.changeVolume)

    def shuffle(self):
        random.shuffle(self._model.all_song_files)
        self.populateSongsTable()
        self._model.is_playing = False
        self.play()

    def previous(self) -> None:
        if(self._index > 0):
            self._index -= 1
        elif self._loop and self._index == 0:
            self._index = len(self._model.all_song_files) - 1
        self.songs_tw.selectRow(self._index)
        self._model.is_playing = False
        self.play()

    def play(self) -> None:
        self._index = self.songs_tw.currentRow()
        self._model.playSong(self._index)

    def next(self) -> None:
        if(self._index < len(self._model.all_song_files) - 1):
            self._index += 1
        elif self._loop and self._index == len(self._model.all_song_files) - 1:
            self._index = 0
        self.songs_tw.selectRow(self._index)
        self._model.is_playing = False
        self.play()

    def loop(self) -> None:
        self._loop = not self._loop
        print('Loop:', self._loop)

    def changeVolume(self, value) -> None:
        self._model.adjustVolume(float(value))

    def populateSongsTable(self) -> None:
        data = self._model.list_all_songs()

        self.songs_tw.setRowCount(len(data))
        self.songs_tw.setColumnCount(self.col_count)

        self.songs_tw.setHorizontalHeaderLabels(
            ['Name', 'Artists', 'Albums', 'Year', 'Duration (s)'])

        for m in range(0, len(data)):
            for n in range(0, self.col_count):
                newitem = QTableWidgetItem(str(data[m][n]))
                newitem.setFlags(QtCore.Qt.ItemIsSelectable |
                                 QtCore.Qt.ItemIsEnabled)
                self.songs_tw.setItem(m, n, newitem)

        self.songs_tw.resizeColumnsToContents()
        self.songs_tw.resizeRowsToContents()

        self._index = 0
        self.songs_tw.selectRow(self._index)
