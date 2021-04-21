# Filename: model.py

"""Max Music is a Music Player built using Python and PyQt5."""
import os
import pprint
from tinytag import TinyTag
import pygame


class MaxMusicModel():
    """Max Music's model"""

    def __init__(self) -> None:
        """Initialises MaxMusicModel"""
        self._music_path = "D:/MAX_EINSTEIN/Music/Black Panther album/"
        self.printer = pprint.PrettyPrinter(indent=4)

        pygame.mixer.init()
        self.is_playing = False

        all_files = os.listdir(self._music_path)
        self.all_song_files = [os.path.join(self._music_path, song) for song
                               in all_files if TinyTag.is_supported(song)]

    def list_all_songs(self) -> list:
        all_song_tags = [TinyTag.get(song) for song in self.all_song_files]

        all_songs = []
        for tag in all_song_tags:
            data = [tag.title, tag.artist, tag.album,
                    tag.year, f'{tag.duration:.2f}']
            data = list(map(lambda x: "Unknown" if x is None else x, data))
            self.printer.pprint(data)   # [DEBUG]
            all_songs.append(data)

        return all_songs

    def playSong(self, index) -> None:
        song = self.all_song_files[index]

        if self.is_playing:
            print('Pause song:', song)
            pygame.mixer.music.pause()
            self.is_playing = False
        else:
            print('Playing song:', song)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)
            self.is_playing = True

    def adjustVolume(self, percent: float) -> None:
        pygame.mixer.music.set_volume(0.01 * percent)
