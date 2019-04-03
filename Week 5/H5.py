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
    #pickles save lists and dictionaries as lists and dictionaries. Everything is stored in binary.
    #https://pythonprogramming.net/python-pickle-module-save-objects-serialization/
    
    pickleOut = open("MusicDB.pickle", "wb")
    pickle.dump(songList, pickleOut)
    pickleOut.close()

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