import json
import H5

H5.menu()

while True:
    print ("\n")
    cmd = input("Enter a command from the list above: ")

    if cmd == "add":
        H5.addSong()
        print ("\n")
    
    elif cmd == "save" and len(H5.songList) <= 8:
        H5.saveSong()
        print("database saved\n")
    
    elif cmd == "save" and len(H5.songList) > 8:
        print("The database is full!")

    elif cmd == "list":
        H5.listSong()
        print ("\n")

    elif cmd == "help":
        H5.menu()
        print ("\n")

    elif cmd == "exit":
        break

    else:
        print("Please enter a valid command")
        continue