import calculator as calc
import math
import msvcrt

res = 0.0
num1 = 0.0
num2 = 0.0
oper = ""


print (">>")

while (True):
    if (num1 == 0.0 and res == 0.0):
        print ("+|-|*|/|^|I|C|S|R|M|X")
        print ("Press H for help")
        oper = input ("choose a function from above: ")

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

        if (oper == "+" or oper == "-" or oper == "*" or oper == "/" or oper == "^"):
            num1 = float (input ("first number: "))
            num2 = float (input ("second number: "))

            if (oper == "+"):
                res = calc.addition (num1,num2)
                num1 = res
                print (res)
                break

            if (oper == "-"):
                res = calc.subtraction (num1,num2)
                num1 = res
                print (res)
                break
            
            if (oper == "*"):
                res = calc.multiplication (num1,num2)
                num1 = res
                print (res)
                break

            if (oper == "/"):
                res = calc.divison (num1,num2)
                num1 = res
                print (res)
                break

            if (oper == "^"):
                res = calc.exponent (num1,num2)
                num1 = res
                print (res)
                break


        elif (oper == "X" or oper == "x"):
            break
                
