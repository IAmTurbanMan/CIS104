#CIS104 Lab 3: Calculator

#import calculator.py for functionality
import calculator as calc

#initialize global variables
res = 0.0
num1 = 0.0
num2 = 0.0
oper = ""

#while loop to run calcuator
while (True):
    #ask user to choose function
    if (num1 == 0.0 and res == 0.0):
        print ("+|-|*|/|^|I|C|S|R|M|X")
        print ("Press H for help")
        oper = input ("choose a function from above: ")
        print ("\n")

        #help option for operation
        if (oper == "H" or oper == "h"):
            print ("+ addition")
            print ("Press H for help")
            print ("- subtract")
            print ("* multiply")
            print ("/ divide")
            print ("^ exponent")
            print ("I/i invert")
            print ("C/c clear calculator")
            print ("S/s store memory")
            print ("R/r recall memory")
            print ("M/m clear memory")
            print ("X/x exit calculator")
            print ("\n")
        
        #if statements for calculator funtions
        if (oper == "I" or oper == "i"):
            if (num1 != 0.0):
                res = calc.invert (num1)
                num1 = res
                print ("\n")
            else:
                num1 = float (input ("number to invert: "))
                res = calc.invert (num1)
                num1 = res
                print ("\n")
        
        if (oper == "C" or oper == "c"):
            res = 0.0
            num1 = 0.0
            num2 = 0.0
            calc.memVal = 0.0
            print ("calculator has been cleared")
            print ("\n")

        if (oper == "S" or oper == "s"):
            calc.memStore (num1)
            print ("{} stored".format(calc.memVal))
            print ("\n")

        if (oper == "R" or oper == "r"):
            res = calc.memRecall ()
            num1 = res
            print ("{} recalled".format(calc.memVal))

        if (oper == "M" or oper == "m"):
            res = calc.memClear
            num1 = res
            print ("memory cleared")
            print ("\n")

        #if statements for clculator operations
        if (oper == "+" or oper == "-" or oper == "*" or oper == "/" or oper == "^"):
            num1 = float (input ("first number: "))
            num2 = float (input ("second number: "))

            if (oper == "+"):
                res = calc.addition (num1,num2)
                num1 = res
                print (res)
                print ("\n")

            if (oper == "-"):
                res = calc.subtraction (num1,num2)
                num1 = res
                print (res)
                print ("\n")
            
            if (oper == "*"):
                res = calc.multiplication (num1,num2)
                num1 = res
                print (res)
                print ("\n")

            if (oper == "/"):
                res = calc.divison (num1,num2)
                num1 = res
                print (res)
                print ("\n")

            if (oper == "^"):
                res = calc.exponent (num1,num2)
                num1 = res
                print (res)
                print ("\n")


        elif (oper == "X" or oper == "x"):
            print ("Goodbye.")
            break
    #Calculator will continue to run and store the result in num1
    #this block expects num1 to != 0 and will run through the whole thing again
    elif (num1 != 0.0 and res != 0.0):
        print ("+|-|*|/|^|I|C|S|R|M|X")
        print ("Press H for help")
        oper = input ("choose a function from above: ")
        print ("\n")

        if (oper == "H" or oper == "h"):
            print ("+ addition")
            print ("Press H for help")
            print ("- subtract")
            print ("* multiply")
            print ("/ divide")
            print ("^ exponent")
            print ("I/i invert")
            print ("C/c clear calculator")
            print ("S/s store memory")
            print ("R/r recall memory")
            print ("M/m clear memory")
            print ("X/x exit calculator")
            print ("\n")

        if (oper == "I" or oper == "i"):
            if (num1 != 0.0):
                res = calc.invert (num1)
                num1 = res
                print (res)
                print ("\n")
            else:
                num1 = float (input ("number to invert: "))
                res = calc.invert (num1)
                num1 = res
                print (res)
                print ("\n")
        
        if (oper == "C" or oper == "c"):
            res = 0.0
            num1 = 0.0
            num2 = 0.0
            calc.memVal = 0.0
            print ("calculator has been cleared")
            print ("\n")

        if (oper == "S" or oper == "s"):
            calc.memStore (num1)
            print ("{} stored".format(calc.memVal))
            print ("\n")

        if (oper == "R" or oper == "r"):
            res = calc.memRecall ()
            num1 = res
            print ("{} recalled".format(calc.memVal))
            print ("\n")

        if (oper == "M" or oper == "m"):
            res = calc.memClear
            num1 = res
            print ("memory cleared")
            print ("\n")

        if (oper == "+" or oper == "-" or oper == "*" or oper == "/" or oper == "^"):
            print ("{} is the first number".format (num1))
            num2 = float (input ("second number: "))

            if (oper == "+"):
                res = calc.addition (num1,num2)
                num1 = res
                print (res)
                print ("\n")

            if (oper == "-"):
                res = calc.subtraction (num1,num2)
                num1 = res
                print (res)
                print ("\n")
            
            if (oper == "*"):
                res = calc.multiplication (num1,num2)
                num1 = res
                print (res)
                print ("\n")

            if (oper == "/"):
                res = calc.divison (num1,num2)
                num1 = res
                print (res)
                print ("\n")

            if (oper == "^"):
                res = calc.exponent (num1,num2)
                num1 = res
                print (res)
                print ("\n")


        elif (oper == "X" or oper == "x"):
            print ("Goodbye.")
            break