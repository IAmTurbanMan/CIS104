#CIS104 Lab 3: Calculator

#Shout out to Trey for helping me. I borrowed pretty heavily from his code.
#figured out how to use getch with Python from him.

#import calculator.py for functionality
import calculator as calc
#import msvcrt for getch function
import msvcrt

#initialize global variables
expressionIsDone = False
number = 1
num1Str = ""
num2Str = ""
print (">>", end='', flush = True)

#while loop to run calcuator
while (True):
    #wait for user input using getwch function
    pressedKey = msvcrt.getwch()
    #check if the key that was pressed was a number or .
    if (pressedKey == "1" or pressedKey == "2" or pressedKey == "3" or pressedKey == "4" or pressedKey == "5" or pressedKey == "6" or pressedKey == "7" or pressedKey == "8" or pressedKey == "9" or pressedKey == "0" or pressedKey == "."):
        print (pressedKey, end='', flush = True)
        
        #check if we are still on the first value and if the expression is completely done
        #add string of numbers to first value (num1) or second value (num2)
        if (number == 1 and expressionIsDone):
            num1Str = ''
            num1Str += pressedKey

        elif (number == 1):
            num1Str += pressedKey
        
        else:
            num2Str += pressedKey

    #check for operator
    if (pressedKey == "+" or pressedKey == "-" or pressedKey == "*" or pressedKey == "/" or pressedKey == "^"):
        if (number == 1):
            num1 = float (num1Str)
            number = 2
            num1Str = ""
            num2Str = ""
        
        oper = pressedKey
        print (pressedKey, end='', flush = True)

    #check for and execute calculator functions
    if (pressedKey == "I" or pressedKey == "i"):
        result = calc.invert (result)
        num1Str = str (result)
        print (result)
        print (">>", end='', flush = True)

    if (pressedKey == "C" or pressedKey == "c"):
        num1 = 0.0
        num2 = 0.0
        num1Str = ""
        num2Str = ""
        number = 1
        result = 0.0
        expressionIsDone = False
        print ("Calculator cleared")
        print (">>", end='', flush = True)

    if (pressedKey == "S" or pressedKey == "s"):
        calc.memStore (result)
        print ("{} saved".format(result))
        print (">>", end='', flush = True)

    if (pressedKey == "R" or pressedKey == "r"):
        result = calc.memRecall ()
        num1Str = str(result)
        print ("{} recalled".format (result))
        print (">>", end='', flush = True)

    if (pressedKey == "M" or pressedKey == "m"):
        calc.memClear()
        print ("memory cleared")
        print (">>", end='', flush = True)

    #check for enter key stroke
    #then run through operations
    if (pressedKey == chr(13)):
        if (num2Str != ""):
            num2 = float (num2Str)

            if (oper == "+"):
                result = calc.addition (num1,num2)
                print ("\n" + str(result))

            elif (oper == "-"):
                result = calc.subtraction (num1,num2)
                print ("\n" + str(result))
            
            elif (oper == "*"):
                result = calc.multiplication (num1,num2)
                print ("\n" + str(result))

            elif (oper == "/"):
                result = calc.divison (num1,num2)
                print ("\n" + str(result))

            elif (oper == "^"):
                result = calc.exponent (num1,num2)
                print ("\n" + str(result))

        print (">>", end='', flush = False)
        num1Str = str (result)
        num2Str = ""
        number = 1
        expressionIsDone = True

    #press X to exit
    if (pressedKey == "X" or pressedKey == "x"):
        print ("Goodbye!")
        break