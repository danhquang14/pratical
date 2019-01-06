from song import Song
from operator import attrgetter
class Songlist:
    def __init__(self):
        # Create a empty list to put song in
        self.song_lists = []
    def convert_list(self, newsongs):
        for n in newsongs:
            song = Song(n[0], n[1], float(n[2]), n[3])
            self.song_lists.append(song)
    def get_song_list(self):
        save_list=[]
        for n in self.song_lists:
            final_lists=[]
            final_lists.append(n.name)
            final_lists.append(n.artist)
            final_lists.append(n.year)
            final_lists.append(n.status)
            save_list.append(final_lists)
        return save_list
    def get_songs(self, get_title=""):
        for song in self.song_lists:
            if song.name == get_title:
                return song
    def print(self):
        return self.song_lists
    def add_song(self,newsong):
        song=Song(newsong[0],newsong[1],float(newsong[2]),newsong[3])
        self.song_lists.append(song)
        return self.song_lists
    def sort_name(self):
        self.song_lists.sort(key=attrgetter("name"))
    def sort_artist(self):
        self.song_lists.sort(key=attrgetter("artist"))
    def sort_year(self):
        self.song_lists.sort(key=attrgetter("year"))
    def get_total_label(self):
        unlearnedsong = 0
        for n in self.song_lists:
            if n.status == "n":
                unlearnedsong += 1
            learnedsong = len(self.song_lists) - unlearnedsong
        self.label='To learn {}. Learned {}'.format(unlearnedsong,learnedsong)
        return self.label
