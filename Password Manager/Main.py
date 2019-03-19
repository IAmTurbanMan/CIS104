#Password manager

import random
import string

#declarations

passList = []
#user input for data to be saved
def newPassword():
    website = input ("Please enter website: ")
    user = input ("Please enter your username: ")
    password = input ("Please enter your password: ")
    if password == "random":
        digits = int(input("Please enter number of digits: "))
        randomPassword = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits ) for _ in range(digits))
        #print ("random password: {}".format (randomPassword))
        password = randomPassword
    else:
        pass

    # print (website)
    # print (user)
    # print (password)

    websiteEntry = dict([("website", website), ("username", user), ("password", password)])

    #print (websiteEntry)

    passList.append(websiteEntry)

    print(passList)

def showPassword():
    websiteSearch = input("for what website: ")
    for entry in passList:
        if websiteSearch == entry['website']:
            print (entry['username'])
            print (entry['password'])
            break
    print ("Website does not exist")

while True:
    
    print ('''
    Welcome to the password manager.
    new : create a new password
    show: look up password
    exit: exit the program
    ''')

    command = input('Please enter a command: ')
    if command == "new":
        newPassword()
    elif command == "exit":
        break
    elif command == "show":
        showPassword()
    else:
        print ("Please enter a valid command")