import json

aSong = {
    "Title": None,
    "Artist": None,
    "Album": None,
    "Track": None,
    "Year": None,
    "Genre": None
}

songList = []

def addSong():
    aSong["Title"] = input("Enter song title: ")
    aSong["Artist"] = input("Enter artist name: ")
    aSong["Album"] = input("Enter album title: ")
    aSong["Track"] = input("Enter track number: ")
    aSong["Year"] = input("Enter release year: ")
    aSong["Genre"] = input("Enter genre: ")

    #unsuccesful attempt at adding the dictionary to a list
    songList.append(aSong)

def saveSong():
    #successful attempt at writing each element in the list to the file
    if len(songList) > 0:
        with open("MusicDB.txt", "w") as f:
            for item in songList:
                f.write("{}\n".format (item))
    elif len(songList) == 0:
        print("You must add a song first!")

def listSong():
    count = 0
    f = open("MusicDB.txt", "r")
    for entry in f:
        emptyEntry = entry.replace('"', '').strip("{").strip("}").strip(",").split("}{")
    for s in emptyEntry:
        count = count + 1
        print("Song #{}: {}\n".format (count, s))

def menu():
    print("add : Add a new song to the database")
    print("list: List dong in the database")
    print("save: Save the database")
    print("help: Display this menu")
    print("exit: Exit the program")

