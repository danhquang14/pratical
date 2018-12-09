def main():
    datafile=open("songs.csv","r")
    data=datafile.readlines()
    song=[]
    for n in data:
        values = n.strip().split(',')
        song.append(values)
    datafile.close()
    print("!!!Welcome to Khai programming world!!!")
    print('''{} songs loaded\nMenu:
    L - List songs
    A - Add new song
    C - Complete a song
    Q - Quit
    '''.format(len(song)))
    userchoice = str(input("Choose your option:"))
    while userchoice.upper() != "Q":
        if userchoice.upper() != "C":
            if userchoice.upper() == "A":
                addsong = addnewsong()
                song.append(addsong)
                userchoice = menu()
            elif userchoice.upper() == "L":
                listsong(song)
                userchoice = menu()
            else:
                print("invalid syntax, please! Choose L, A, C or Q")
                userchoice = str(input("Choose again:"))
        else:
            for l in range(len(song)):
                if "n" in song[l][3]:
                    print("no more song to learn")
                    break;
                else:
                    song = learnsong(song, numbersong)
                    break;
            userchoice = menu();
    else:
        print("{} songs saved to songs.csv\nHave a nice day!".format(len(song)))
def menu():
    print('''Menu:
 L - List songs
 A - Add new song
 C - Complete a song
 Q - Quit
 ''')
    choice = str(input("Choose your option"))
    return choice
def listsong(song):
    unlearnedsong=0
    for i in range(len(song)):
        if song[i][3]=="y":
            print("{:2}. * {:30} - {:4} ({})".format(i, song[i][0], song[i][1], song[i][2]))
            unlearnedsong+= 1
        else:
            print("{:2}.   {:30} - {:4} ({})".format(i, song[i][0], song[i][1], song[i][2]))
        learnedsong = len(song) - unlearnedsong
    print("{} songs learned, {} songs still to learn".format(learnedsong, unlearnedsong))
def addnewsong():
    updatesong=[]
    nameofnewsong=str(input("Title of a new song:"))
    while not nameofnewsong.strip():
        print("Input cannot be blank or any space at the beginning of the sentence in the head! please try again")
        nameofnewsong = str(input("Title of a new song:"))
    artistofnewsong=str(input("Artist of a new song:"))
    while not artistofnewsong.strip():
        print("Input cannot be blank or any space at the beginning of the sentence in the head! please try again")
        artistofnewsong = str(input("Artist of a new song:"))
    while True:
        try:
            yearofnewsong=int(input("Year:"))
            while yearofnewsong <=0:
                print("Number must be >=0")
                yearofnewsong = int(input("Year:"))
            break;
        except ValueError:
            print("Invalid input; enter a valid number")
    print('{} by {} ({}) added to song list'.format(nameofnewsong,artistofnewsong,yearofnewsong))
    updatesong.append(nameofnewsong)
    updatesong.append(artistofnewsong)
    updatesong.append(yearofnewsong)
    updatesong.append("y")
    return updatesong

main()