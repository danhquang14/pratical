"""(Incomplete) Tests for Song class."""
from song import Song

# test empty song (defaults)
song = Song()
print(song)
assert song.artist == ""
assert song.name == ""
assert song.year == 0
assert song.status==""

# test initial-value song
song2 = Song("Amazing Grace", "John Newton", 1779,"y")
# TODO: write tests to show this initialisation works
assert song2.artist == "John Newton"
assert song2.name == "Amazing Grace"
assert song2.year == 1779
assert song2.status=="y"
print(song2)
# test mark_learned()
# TODO: write tests to show the mark_learned() method works
song2.mark_learned()
assert (song2.status == "y")