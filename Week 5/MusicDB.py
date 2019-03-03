import json
import H5


H5.clearSong()
H5.menu()
dbCount = 0

while True:
    cmd = input("Enter a command from the lsit above: ")

    if cmd == "add":
        H5.addSong()
        dbCount = dbCount + 1
    
    elif cmd == "save" and dbCount <= 8:
        H5.saveSong()
    
    elif cmd == "save" and dbCount > 8:
        print("The database is full!")

    elif cmd == "list":
        H5.listSong()

    elif cmd == "help":
        H5.menu()

    elif cmd == "exit":
        break

    else:
        print("Please enter a valid command")
        continue