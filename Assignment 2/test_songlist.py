"""
(incomplete) Tests for SongList class
"""
from songlist import Songlist
from song import Song

# test empty SongList
song_list1 = Songlist()
print(song_list1)
assert len(song_list1.song_lists) == 0

# test loading songs
datafile = open("songs.csv", "r")
data = datafile.readlines()
newsongs = []
for n in data:
    values = n.strip().split(',')
    newsongs.append(values)
datafile.close
print(newsongs)
assert len(newsongs) > 0  # assuming CSV file is not empty

# TODO: add tests below to show the various required methods work as expected
# test sorting songs
song_list1.sort_name()
print(song_list1.sort_name)
song_list1.sort_artist()
print(song_list1.sort_artist)
song_list1.sort_year()
print(song_list1.sort_year)
# test adding a new Song

# test get_song()

# test getting the number of required and learned songs (separately)

# test saving songs (check CSV file manually to see results)
