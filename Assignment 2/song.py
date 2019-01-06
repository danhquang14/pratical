class Song:
    def __init__(self, name="", artist="", year=0, status=""):
        self.name = name
        self.artist = artist
        self.year = year
        self.status = status
    def __str__(self):
        return "{:15s}, {:15s},{},(learned)".format(self.name, self.artist, self.year)
    def mark_learned(self):
        if self.status=="y":
            print("song has been learned")
        else:
            self.status="y"
            return self.status