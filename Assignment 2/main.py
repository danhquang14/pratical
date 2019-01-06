"""
Name: Quang Khai Nguyen
Date: 21/12/2018
Brief Project Description: Our project is Song Application with using pop up that allows the users to observe the list of their song, they can click to the song to learn and also can click to the
button (add new song) to add a new song that they wanted ( i also used try and except value to avoid error). Moreover, users can find their song easily by clicking to the sort song button
and choose the sort song in name or artist or year. i also have created a clear function to clear the label text
GitHub URL:https://github.com/danhquang14/pratical
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from songlist import Songlist
#Using for sorted button
sorted_song={"list of song: (name)":1,"list of song: (artist)":2,"list of song: (year)":3}

class SongApp(App):
    # Using StringProperty to for 2 status label in the main screen and 1 status label for pop up screen
    # Using ListProperty for sorted song button
    status_text = StringProperty()
    status_text1 = StringProperty()
    status_text2 = StringProperty()
    current_song = StringProperty()
    song_codes = ListProperty()
    def __init__(self, **kwargs):
        super(SongApp, self).__init__(**kwargs)
        # open csv file:
        datafile = open("songs.csv", "r")
        data = datafile.readlines()
        newsongs = []
        for n in data:
            values = n.strip().split(',')
            newsongs.append(values)
        datafile.close()
        self.list_song=Songlist()
        # convert list of list into list of object
        self.list_song.convert_list(newsongs)

        self.song_list_data=self.list_song.print()
        # Sort a list of song button
    def press_sort_button(self,song_code):
        # sort song by name
        if song_code=="list of song: (name)":
            self.list_song.sort_name()
        # sort song by artist
        elif song_code=="list of song: (artist)":
            self.list_song.sort_artist()
        #sort song by year
        else:
            self.list_song.sort_year()
        self.root.ids.entries_box.clear_widgets()
        self.create_entry_buttons()
    def build(self):
        self.title = "Song Application"
        self.root = Builder.load_file('app.kv')
        self.create_entry_buttons()
        self.song_codes = sorted_song.keys()
        print(self.song_codes)
        self.current_song = self.song_codes[0]
        return self.root

    def create_entry_buttons(self):
        # display if the song is already learned and unlearned, they will display in different color and text
        for n in self.song_list_data:
            if n.status=="y":
                text='"{}" by {} ({}) (learned)'.format(n.name,n.artist,int(n.year))
                temp_button = Button(text=text, background_color=(0, 1, 0, 1))
                temp_button.bind(on_release=self.press_learned)
                self.root.ids.entries_box.add_widget(temp_button)
            else:
                id_song=n.name
                text = '"{}" by {} ({})'.format(n.name, n.artist, int(n.year))
                temp_button = Button(id=id_song,text=text,background_color=(1, 0, 0, 1))
                temp_button.bind(on_release=self.press_entry)
                self.root.ids.entries_box.add_widget(temp_button)

        self.songlabel = self.list_song.get_total_label()
        self.status_text1 = self.songlabel
    # this function is if the user lick the learned song, the status text will display to notice the user know this song is already learned
    def press_learned(self,instance):
        n = instance.text
        self.status_text2="You have already learned this song"
    def press_entry(self, instance):

        # update status text
        n = instance.text
        self.list_song.get_songs(instance.id).mark_learned()
        self.root.ids.entries_box.clear_widgets()
        self.create_entry_buttons()
        save_csv=self.list_song.get_song_list()
        datafile=open("songs.csv", "w")
        for n in save_csv:
            datafile.write("{},{},{},{}\n".format(n[0], n[1], n[2], n[3]))
        datafile.close()
    # function for clear the status
    def press_clear(self):
        for instance in self.root.ids.entries_box.children:
            instance.state = 'normal'
        self.status_text2 = ""
    def press_add(self):
        self.status_text = "Enter details for new Song entry"
        # this opens the popup
        self.root.ids.popup.open()
    # save the song when the user fill in all the information to the table and click save
    def press_save(self,added_name,added_number,added_artist):

        if self.root.ids.added_name.text=="" or self.root.ids.added_artist.text=="" or self.root.ids.added_number.text=="":
            self.status_text = "All fields must be completed"
        else:
            new_name = self.root.ids.added_name.text
            new_artist = self.root.ids.added_artist.text
            new_number = self.root.ids.added_number.text
            try:
                if float(new_number)<=0:
                    self.status_text="Please enter a valid number"
                else:
                    newsong=[]
                    newsong.append(new_name)
                    newsong.append(new_artist)
                    newsong.append(new_number)
                    newsong.append("n")
                    newsonglist=self.list_song.add_song(newsong)
                    self.root.ids.entries_box.clear_widgets()
                    self.create_entry_buttons()
                    # close popup
                    self.root.ids.popup.dismiss()
                    self.clear_fields()

            except ValueError:
                self.status_text="Please enter a valid number"
        save_csv=self.list_song.get_song_list()
        datafile=open("songs.csv", "w")
        for n in save_csv:
            datafile.write("{},{},{},{}\n".format(n[0], n[1], n[2], n[3]))
        datafile.close()
    def clear_fields(self):
        self.root.ids.added_name.text = ""
        self.root.ids.added_artist.text=""
        self.root.ids.added_number.text = ""

    def press_cancel(self):
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = ""


SongApp().run()
