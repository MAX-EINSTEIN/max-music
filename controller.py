# Filename: controller.py

"""Max Music is a Music Player built using Python and PyQt5."""
from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QTableWidgetItem, QTableWidget,\
    QToolButton, QSlider, QStyle
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap

from max_music_ui import MaxMusicUI
from model import MaxMusicModel

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
        self.pp_btn.setIcon(
            self._view.style().standardIcon(QStyle.SP_MediaPlay))
        self.nxt_btn: QToolButton = self._view.next_btn
        self.loop_btn: QToolButton = self._view.repeat_btn
        self._index = 0
        self._loop = False
        self.pb_slider: QSlider = self._view.progress_bar_slider
        self.pb_slider.setMinimum(0)
        self.pb_slider.setMaximum(0)
        self.ct_label: QLabel = self._view.current_time_label
        self.ct_label.setText(self._model.format_duration('0'))
        self.et_label: QLabel = self._view.end_time_label

        # Volume
        self.vol_slider: QSlider = self._view.vol_slider
        self.vol_slider.setMinimum = 0
        self.vol_slider.setMaximum = 100
        self.vol_slider.setValue = 100
        self.vol_slider.setSliderPosition(100)

        # MediaPlayer
        self._player = QMediaPlayer()
        self._player_state: QMediaPlayer.State = QMediaPlayer.StoppedState

        # Song Details
        self.sn_lable: QLabel = self._view.song_name_label
        self.sa_lable: QLabel = self._view.song_artist_label
        self.si_lable: QLabel = self._view.song_icon_label

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

        # MediaPlayer
        self._player.positionChanged.connect(self.position_changed)
        self._player.durationChanged.connect(self.duration_changed)
        self.pb_slider.sliderMoved.connect(self.set_position)

    def shuffle(self):
        random.shuffle(self._model.all_song_files)
        self.populateSongsTable()
        self.play()

    def previous(self) -> None:
        if(self._index > 0):
            self._index -= 1
        elif self._loop and self._index == 0:
            self._index = len(self._model.all_song_files) - 1
        self.songs_tw.selectRow(self._index)
        self._player_state = QMediaPlayer.PausedState
        self.play()

    def play(self) -> None:
        self.ct_milli = 0
        self._index = self.songs_tw.currentRow()

        filename = self._model.all_song_files[self._index]
        self._player.setMedia(
            QMediaContent(QUrl.fromLocalFile(filename)))

        self.sn_lable.setText(self.songs_tw.item(self._index, 0).text())
        self.sa_lable.setText(self.songs_tw.item(self._index, 1).text())
        self.si_lable.setPixmap(QPixmap('resources/app-icon.png'))

        if self._player_state == QMediaPlayer.PlayingState:
            print(f'Pause: {self._index}')
            self._player.pause()
            self._player_state = QMediaPlayer.PausedState
        else:
            print(f'Play: {self._index}')
            self._player.play()
            self._player_state = QMediaPlayer.PlayingState

        self.mediastate_changed(self._player_state)

        self.et_label.setText(self.songs_tw.item(self._index, 4).text())

    def next(self) -> None:
        if(self._index < len(self._model.all_song_files) - 1):
            self._index += 1
        elif self._loop and self._index == len(self._model.all_song_files) - 1:
            self._index = 0
        self.songs_tw.selectRow(self._index)
        self._player_state = QMediaPlayer.PausedState
        self.play()

    def loop(self) -> None:
        self._loop = not self._loop
        print('Loop:', self._loop)

    def changeVolume(self, value: int) -> None:
        self._player.setVolume(value)

    def mediastate_changed(self, state: QMediaPlayer.State):
        if state == QMediaPlayer.PlayingState:
            self.pp_btn.setIcon(
                self._view.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.pp_btn.setIcon(
                self._view.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.pb_slider.setValue(position)
        time = self._model.format_duration(str(position/1000))
        self.ct_label.setText(time)

    def duration_changed(self, duration):
        self.pb_slider.setRange(0, duration)

    def set_position(self, position):
        self._player.setPosition(position)

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
