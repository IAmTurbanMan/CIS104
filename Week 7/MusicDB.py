import pickle
import json
import os

songList = []
#initialize the actual list we will be using

def loadSong():
    #load songs into list from pickle file. No worrying about how to get the text file
    #back in as a list. This handles all of that for you.
    unpickle = []
    #need to initialize a new list to load the existing list into
    if os.path.exists("MusicDB.pickle"):
        #search for pickle file
        with open("MusicDB.pickle", "rb") as f:
            unpickle = pickle.load(f)
            #load pickle file into list if the pickle file exists
        return unpickle
        #return the unpickled list
    else:
        return unpickle
        #return empty list

def addSong():
    aSong = {}
    aSong["Title"] = input("Enter song title: ")
    aSong["Artist"] = input("Enter artist name: ")
    aSong["Album"] = input("Enter album title: ")
    aSong["Track"] = input("Enter track number: ")
    aSong["Year"] = input("Enter release year: ")
    aSong["Genre"] = input("Enter genre: ")
    songList.append(aSong)

def listSong():
    print (*songList, sep = "\n")

def saveSong():
    pickleOut = open("MusicDB.pickle", "wb")
    pickle.dump(songList, pickleOut)
    pickleOut.close()
    print("database saved")
    #successful attempt at writing each element in the list to the file
    #pickles save lists and dictionaries as lists and dictionaries. Everything is stored in binary.
    #https://pythonprogramming.net/python-pickle-module-save-objects-serialization/

def findSong():
    searchBy = input("Song title: ")
    print("\n")
    searchBy = searchBy.lower()
    song = next((song for song in songList if song['Title'].lower() == searchBy), None)
    if song is not None:
        print(song)
    else:
        print("This song is not in the database.")
        pass
    #https://stackoverflow.com/questions/26447309/search-a-list-of-dictionary-in-python
    #Second answer


def clearSong():
    yesOrNo = input("Are you sure you want to clear the database? y/n: ")
    if yesOrNo.lower() == "y":
        songList.clear()
        if os.path.exists("MusicDB.pickle"):
            os.remove("MusicDB.pickle")
            print("Database has been cleared.")
        else:
            print("This file does not exist.")
    if yesOrNo.lower() == "n":
        pass

def menu():
    print("add  : Add a new song to the database")
    print("list : List dong in the database")
    print("save : Save the database")
    print("sort : Sort the database by title/artist/release year")
    print("find : Search for a song by title")
    print("clear: Clear the database")
    print("help : Display this menu")
    print("exit : Exit the program")

songList = loadSong()
#load the unpickled list into the actual list we are using for this database
menu()
print("\n")

while True:
    cmd = input("Enter a command: ")
    cmd = cmd.lower()
    print("\n")

    if cmd == "add":
        addSong()
        print("\n")

    elif cmd == "list":
        listSong()
        print("\n")

    elif cmd == "save":
        saveSong()
        print("\n")

    elif cmd == "sort":
        sortBy = input ("What do you want to sort by? title/artist/year: ")
        #sortBy = sortBy.lower()
        from operator import itemgetter
        if (sortBy == "title"):
            songList = sorted(songList, key = itemgetter('Title'))
        if (sortBy == "artist"):
            songList = sorted(songList, key = itemgetter('Artist'))
        if (sortBy == "year"):
            songList = sorted(songList, key = itemgetter('Year'))
        #not sure why, but this function will not work if I put it at the top of the code and define it as a function up there
        #I get an error that says I'm calling my songList list before I initialize it.
        #https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
        listSong()
        print("\n")

    elif cmd == "find":
        findSong()
        print("\n")

    elif cmd == "clear":
        clearSong()
        print("\n")

    elif cmd == "help":
        menu()
        print ("\n")

    elif cmd == "exit":
        break

    else:
        print("Please enter a valid command")
        continue