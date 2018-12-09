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
main()