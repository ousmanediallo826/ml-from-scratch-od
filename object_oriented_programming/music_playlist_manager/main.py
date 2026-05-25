from song import *
from playlist import *


playlist = SmartPlaylist("Top Rock", "Alice", rules={"genre": "Rock", "min_plays": 5})

s1 = Song("Bohemian Rhapsody", "Queen",        "A Night at the Opera", 355, "Rock")
s2 = Song("Hotel California",  "Eagles",       "Hotel California",     391, "Rock")
s3 = Song("Blinding Lights",   "The Weeknd",   "After Hours",          200, "Pop")
s4 = Song("Enter Sandman",     "Metallica",    "Metallica",            332, "Rock")
s5 = Song("Shape of You",      "Ed Sheeran",   "Divide",               234, "Pop")

# Play some songs
for _ in range(12): s1.play()
for _ in range(7):  s2.play()
for _ in range(3):  s3.play()
for _ in range(9):  s4.play()

# Add songs
playlist.add_song(s1).add_song(s2).add_song(s3).add_song(s4).add_song(s5)

# Magic methods
print(playlist)                          # __str__
print(len(playlist))                     # __len__
print("Hotel California" in playlist)   # __contains__
playlist += Song("Comfortably Numb", "Pink Floyd", "The Wall", 382, "Rock")

# Properties
print(playlist.total_duration_str)      # "25m" or "1h 25m"
print(playlist.most_played)             # Song with highest play_count
print(playlist.genres)                  # {"Rock", "Pop"}

# Iterate
for song in playlist:                   # __iter__
    print(song)

# SmartPlaylist
all_songs = [s1, s2, s3, s4, s5]
playlist.refresh(all_songs)             # only Rock songs with >= 5 plays
print(playlist.song_count)              # should be 2 (s1 and s2)

# Descriptor validation
Song("Bad", "Artist", "Album", 30)     # raises ValueError
Song("Bad", "Artist", "Album", 200, play_count=1)  # raises ValueError

# Filter methods
print(playlist.filter_by_genre("Rock"))
print(playlist.filter_by_artist("Queen"))