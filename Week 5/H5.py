import json
import pickle

songList = []

def addSong():
    aSong = {}

    aSong["Title"] = input("Enter song title: ")
    aSong["Artist"] = input("Enter artist name: ")
    aSong["Album"] = input("Enter album title: ")
    aSong["Track"] = input("Enter track number: ")
    aSong["Year"] = input("Enter release year: ")
    aSong["Genre"] = input("Enter genre: ")

    #succesful attempt at adding the dictionary to a list!!!
    songList.append(aSong)

def saveSong():
    #successful attempt at writing each element in the list to the file

    pickleOut = open("MusicDB.pickle", "wb")
    pickle.dump(songList, pickleOut)
    pickleOut.close()

    # if len(songList) > 0:
    #     with open("MusicDB.txt", "w") as f:
    #         for item in songList:
    #             f.write("{}\n".format (item))
    # elif len(songList) == 0:
    #     print("You must add a song first!")

def listSong():
    print (*songList, sep = "\n")

def menu():
    print("add : Add a new song to the database")
    print("list: List dong in the database")
    print("save: Save the database")
    print("sort: Sort the database by title/artist/release year")
    print("help: Display this menu")
    print("exit: Exit the program")

def loadSong():
    unpickle = []
    with open("MusicDB.pickle", "rb") as f:
        unpickle = pickle.load(f)
    return unpickle