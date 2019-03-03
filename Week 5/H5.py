import json

aSong = 
{
    "Title": None,
    "Artist": None,
    "Album": None,
    "Track": None,
    "Year": None,
    "Genre": None,
}

def addSong():
    aSong["Title"] = input("Enter song title: ")
    aSong["Artist"] = input("Enter artist name: ")
    aSong["Album"] = input("Enter album title: ")
    aSong["Track"] = input("Enter track number: ")
    aSong["Year"] = input("Enter release year: ")
    aSong["Genre"] = input("Enter genre: ")

def saveSong():
    if aSong["Title"] != None:
        writefile = open("MusicDB.txt", "a")
        writefile.write(json.dumps(Song))
    elif aSong["Title"] == None:
        print("You must add a song first!")

def clearSong():
    file = open("MusicDB.txt", "w")
    file.truncate(0)

def listSong():
    count = 0
    f = open("MusicDB.txt", "r")
    for entry in f:
        empty = []
        emptyEntry = entry.replace('"', '').strip("{").strip("}").strip(",").split("}{")
    for s in emptyEntry:
        count = count + 1
        print("Song #{}: {}\n".format (count, s))

def menu():
    print("add : Add a new song to the database\n")
    print("list: List dong in the database\n")
    print("save: Save the database\n")
    print("help: Display this menu\n")
    print("exit: Exit the program\n")

