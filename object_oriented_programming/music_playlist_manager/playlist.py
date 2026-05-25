from typing import Iterator

from song import *

class Playlist:
    platform = "SoundBox"
    _total_playlists = 0


    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.songs = []


    @property
    def total_duration(self) -> float:
        return sum(song.duration for song in self.songs)

    @property
    def total_duration_str(self):
       total_seconds = int(self.total_duration)
       hour = total_seconds // 3600
       minutes = total_seconds % 3600 // 60
       if hour > 0:
           return f"{hour:02}:{minutes:02}"
       return f"{minutes:02}"

    @property
    def song_count(self) -> int:
        return len(self.songs)

    @property
    def most_played(self):
        if not self.songs:
            return None
        return max(self.songs, key=lambda x: x.song_count)

    @property
    def genres(self) -> set:
        return {song.genre for song in self.songs}


    def __str__(self) -> str:
        return f"{Playlist.platform} | {Song.genre} by {self.owner} | {Playlist._total_playlists}"

    def __len__(self) -> int:
        return len(self.songs)

    def __contains__(self, song: Song) -> bool:
        return song in self.songs

    def __iter__(self) -> Iterator[Song]:
        return iter(self.songs)

    def __iadd__(self, song: Song):
        Playlist._total_playlists += song



    def add_song(self, song: Song):
        self.songs.append(song)
        return self

    def remove_song(self, song: Song):
        if song.title not in self.songs:
            raise ValueError(
                f"Song {song.title} not found in playlist"
            )
        self.songs.remove(song)

    def filter_by_genres(self, gen: str) -> list:
        return [gen for gen in self.songs if gen.genre.lower() == gen.lower() ]

    def filter_by_artist(self, art: str) -> list:
        return [art for art in self.songs if art.artist.lower() == art.lower() ]



class SmartPlaylist(Playlist):
    auto_label = "⚡ Auto"

    def __init__(self, name: str, owner: str, rules: dict = None):
        super().__init__(name, owner)
        self.rules = rules if rules is not None else {}

    def apply_rules(self, songs: list) -> list:
        result = songs

        if "genre" in self.rules:
            result = [s for s in result if s.genre.lower() == self.rules["genre"].lower()]

        if "min_plays" in self.rules:
            result = [s for s in result if s.play_count >= self.rules["min_plays"]]

        if "artist" in self.rules:
            result = [s for s in result if s.artist.lower() == self.rules["artist"].lower()]

        return result

    def refresh(self, songs: list):
        self._songs = []
        for song in self.apply_rules(songs):
            self.add_song(song)

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | {self.auto_label} | {len(self.rules)} rules"

