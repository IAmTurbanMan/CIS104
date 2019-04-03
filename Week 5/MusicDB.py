import pickle
import json

def loadSong():
    #load songs into list from pickle file. No worryinh about how to get the text file
    #back in as a list. This handles all of that for you.
    unpickle = []       #need to initialize a new list to load the existing list into
    with open("MusicDB.pickle", "rb") as f:
        unpickle = pickle.load(f)
    return unpickle     #return the unpickled list

def menu():
    print("add : Add a new song to the database")
    print("list: List dong in the database")
    print("save: Save the database")
    print("sort: Sort the database by title/artist/release year")
    print("help: Display this menu")
    print("exit: Exit the program")

def saveSong():
    pickleOut = open("MusicDB.pickle", "wb")
    pickle.dump(songList, pickleOut)
    pickleOut.close()
    # saveSong()
    print("database saved\n")

songList = []           #initialize the actual list we will be using
songList = loadSong()   #load the unpickled list into the actual list we are using for this database
#print (songList)
menu()

while True:
    print ("\n")
    cmd = input("Enter a command: ")

    if cmd == "add":
        aSong = {}

        aSong["Title"] = input("Enter song title: ")
        aSong["Artist"] = input("Enter artist name: ")
        aSong["Album"] = input("Enter album title: ")
        aSong["Track"] = input("Enter track number: ")
        aSong["Year"] = input("Enter release year: ")
        aSong["Genre"] = input("Enter genre: ")

        songList.append(aSong)
    
    elif cmd == "save" and len(songList) <= 8:      #Alisa helped me find an really dumb error. I had "=<" instead of "<=".
        saveSong()
        #successful attempt at writing each element in the list to the file
        #pickles save lists and dictionaries as lists and dictionaries. Everything is stored in binary.
        #https://pythonprogramming.net/python-pickle-module-save-objects-serialization/

        # pickleOut = open("MusicDB.pickle", "wb")
        # pickle.dump(songList, pickleOut)
        # pickleOut.close()
        # # saveSong()
        # print("database saved\n")
    
    elif cmd == "save" and len(songList) > 8:
        print("The database is full!")

    elif cmd == "list":
        print (*songList, sep = "\n")

    elif cmd == "help":
        menu()
        print ("\n")

    elif cmd == "sort":
        sortBy = input ("What do you want to sort by? title/artist/year: ")
        from operator import itemgetter
        if (sortBy == "title"):
            songList = sorted(songList, key = itemgetter('Title'))
        if (sortBy == "artist"):
            songList = sorted(songList, key = itemgetter('Artist'))
        if (sortBy == "year"):
            songList = sorted(songList, key = itemgetter('Year'))

    #https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary

    elif cmd == "exit":
        break

    else:
        print("Please enter a valid command")
        continue