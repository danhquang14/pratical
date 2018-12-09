''' Name: Quang Khai Nguyen (13410893)
 Assignment: 1
 Program details: In our project, I will divide it into 5 functions including function main, function listsong, function menu,
 function addnewsong and function learnsong. For function main, first of all, i wrote a code to open and read the csv file, organize it properly
 and also sort it to make it good-looking and smooth. After that, i declared a userchoice as string type and use loops to getting the correct choice
 Then, in the case the user choose exit, all of value inside a song variable will be saved on the CSV file. For menu function, it is just display the menu
 every time when user finish list song, add new song and complete song. For listsong function, i create a new variable equal to zero. Then, i used for loop
 and if-else to find out this song learned or still learn via last word ("y" or "n"). Then, learnedsong will equal to len(song) minus the new create variable to display the number
 of the song learn and the song still learn. For addnewsong function, i created a new list variable . After that , i used while loops, strip and try and execpt to get the tile,artist
 and years without any error and blanks. Next, we append all value (title ,artist and years) to the new list variable and return it to the main. For learnsong function, i create a
 input variable to get the number of the song they want to learn. If the song they choose has already learned, it will be noticed to the users to choose other songs to learn. If
 the song they choose has not learned yet, it will be notice to the users that they can learn this songs and change the last word to be 'n' means learned song and save it to the song.
Github link:
'''
'''
(pseudocode for load song)
def main()   
    datafile=open("song.csv","r")
    data=datafile.readlines()
    song=[]
    for n in data:
        values = n.strip().split(',')
        song.append(values)
    datafile.close()
    numbersong=len(song)
    Display "!!!Welcome to Khai programming world!!!"
    Display len(song)& "songs loaded\nMenu:L - List songs
A - Add new song
C - Complete a song
Q - Quit"
    inputuserchoice
    getuserchoice
    while:
	if userchoice.upper()!="Q" then:
		if userchoice.upper() !="C" then:
			if userchoice.upper() !="A" then:
				addsong=addnewsong()
				song.append(addsong)
				userchoice=menu()
			elif userchoice.upper()=="L" then:
				listsong(song)
				userchoice=menu()
			else:
				Display"invalid syntax,please! Choose L, A, C or Q"
				input userchoice
				get userchoice
		else:
			if 'n' in song[3] then:
    				Display"No more"
			else:
				 song=learnsong(song,numersong)
			userchoice=menu();
	else:
		Display len(song)&" songs saved to song.csv Have a nice day!"
		for y in range(len(song)):
			song[y][2]=str(song[y][2])
		out_file=open("song.csv","w")
		for x in song:
			Display"{},{}".format(x[0], ','.join(x[1:])), file=out_file
		out_file.close
'''
def main():
    datafile=open("songs.csv","r")
    data=datafile.readlines()
    song=[]
    for n in data:
        values = n.strip().split(',')
        song.append(values)
    datafile.close()
    numbersong=len(song)
    print("!!!Welcome to Khai programming world!!!")
    print('''{} songs loaded\nMenu:
L - List songs
A - Add new song
C - Complete a song
Q - Quit
'''.format(len(song)))
    userchoice=str(input("Choose your option:"))
    while userchoice.upper() != "Q":
        if userchoice.upper() !="C":
            if userchoice.upper()=="A":
                addsong=addnewsong()
                song.append(addsong)
                userchoice = menu()
            elif userchoice.upper() =="L":
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
                    song=learnsong(song,numbersong)
                    break;
            userchoice = menu();
    else:
        print("{} songs saved to songs.csv\nHave a nice day!".format(len(song)))
        for y in range(len(song)):
            song[y][2] = str(song[y][2])
        out_file = open("songs.csv", 'w')
        for x in song:
            print("{},{}".format(x[0], ','.join(x[1:])), file=out_file)
        out_file.close()
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
def menu():
    print('''Menu:
L - List songs
A - Add new song
C - Complete a song
Q - Quit
''')
    choice=str(input("Choose your option"))
    return choice
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
'''(psuedocode for complete a song)
def learnsong(song,numbersong) 
while True:
	try:
		Display "enter the number of a song to mark as learned:"
		input complete_song as interger
		get complete_song
		while:
		if complete_song<0 or complete_song >numbersong then:
		Display "Please enter a valid number"
		input complete_song as interger
		get coplete_song
		else:
			while:
			if "n" in song[complete_song][3] then:
				Display("OOPS!! you have already learned this song")
				input complete_song as interger
				get complete_song
	exept ValueError:
		Display"Please enter a number"
	song[complete_song][3]='n'
	Display song[complete_song][0]&"from"&song[complete_song][1]&"learned"
	return song
'''
def learnsong(song,numbersong):
    while True:
        try:
            complete_song=int(input("Enter the number of a song to mark as learned "))
            while complete_song <0 or complete_song > numbersong:
                print("please enter a valid number")
                complete_song = int(input("Enter the number of a song to mark as learned "))
            else:
                while 'n' in song[complete_song][3]:
                    print("OOPS!! you have already learned this song")
                    complete_song = int(input("Enter the number of a song to mark as learned "))
            break;
        except ValueError:
            print("Please enter a number")
    song[complete_song][3]='n'
    print("{} from {}learned".format(song[complete_song][0],song[complete_song][1]))
    return song
main()