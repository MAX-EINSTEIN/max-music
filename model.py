# Filename: model.py

"""Max Music is a Music Player built using Python and PyQt5."""
import os
import pprint
from tinytag import TinyTag
from PyQt5.QtWidgets import QStyle


class MaxMusicModel():
    """Max Music's model"""

    def __init__(self) -> None:
        """Initialises MaxMusicModel"""
        self.printer = pprint.PrettyPrinter(indent=4)

        self._music_path = "D:/MAX_EINSTEIN/Music/Black Panther album/"

        all_files = os.listdir(self._music_path)
        self.all_song_files = [os.path.join(self._music_path, song) for song
                               in all_files if TinyTag.is_supported(song)]

    def list_all_songs(self) -> list:
        all_song_tags = [TinyTag.get(song) for song in self.all_song_files]

        all_songs = []
        for tag in all_song_tags:
            duration = tag.duration
            data = [tag.title, tag.artist, tag.album,
                    tag.year, self.format_duration(duration)]
            data = list(map(lambda x: "Unknown" if x is None else x, data))
            self.printer.pprint(data)   # [DEBUG]
            all_songs.append(data)

        return all_songs

    def format_duration(self, duration: str) -> str:
        dur = round(float(duration))
        mins = dur//60
        secs = dur % 60
        return (f'{mins:2d}:{secs:2d}').replace(' ', '0')
    
    def duration_in_seconds(self, duration:str) -> int:
        mins, secs = list(map(int, duration.split(':')))
        return mins*60 + secs
