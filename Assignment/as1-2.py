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
        print("Have a nice day!")
def menu():
    print('''Menu:
 L - List songs
 A - Add new song
 C - Complete a song
 Q - Quit
 ''')
    choice = str(input("Choose your option"))
    return choice

main()