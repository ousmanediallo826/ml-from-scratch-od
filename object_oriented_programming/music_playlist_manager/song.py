from dataclasses import dataclass
from descriptors import *
@dataclass
class Song:
    title: str
    artist: str
    album: str
    duration: float
    genre: str = "Unknown"
    play_count: int = 0


    duration = SongDuration()
    play_count = PlayCount()


    def __post_init__(self):
        self.duration = self.duration
        self.play_count = self.play_count


    @property
    def is_popular(self) -> bool:
        if self.play_count >= 10:
            return True
        return False

    @property
    def play(self):
        self.play_count += 1
        return self

    def __str__(self):
        return f"{self.artist} - {self.title} - ({self.duration}) ▶ {self.play_count} plays."