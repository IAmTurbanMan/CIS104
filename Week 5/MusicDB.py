import json
import H5

songList = []

songList = H5.loadSong()
print (songList)
H5.menu()

while True:
    print ("\n")
    cmd = input("Enter a command: ")

    if cmd == "add":
        H5.addSong()
        print ("\n")
    
    elif cmd == "save" and len(H5.songList) <= 8:
        H5.saveSong()
        print("database saved\n")
    
    elif cmd == "save" and len(H5.songList) > 8:
        print("The database is full!")

    elif cmd == "list":
        print (*songList, sep = "\n")
        # H5.listSong()
        # print ("\n")

    elif cmd == "help":
        H5.menu()
        print ("\n")

    elif cmd == "sort":
        sortBy = input ("What do you want to sort by? title/artist/release: ")
        from operator import itemgetter
        if (sortBy == "title"):
            songList = sorted(songList, key = itemgetter('Title'))
        if (sortBy == "artist"):
            songList = sorted(songList, key = itemgetter('Artist'))
        if (sortBy == "release"):
            songList = sorted(songList, key = itemgetter('Year'))

    #https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary

    elif cmd == "exit":
        break

    else:
        print("Please enter a valid command")
        continue