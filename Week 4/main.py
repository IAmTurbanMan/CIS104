import calculator as calc
import math

print = ("select an operation")
print = ("+ Add")
print = ("- Subtract")
print = ("* Multiply")
print = ("/ Divide")
print = ("^ Power")
print = ("I/i Invert")
print = ("S/s Store memory")
print = ("R/r Recall memory")
print = ("M/m Clear memory")
print = ("C/c Clear calculator")
print = ("X/x Exit =")
num1 = float (input ("enter a number: "))
oper = (input ("enter an operation: "))
num2 = float ()

if (oper == "+"):
    currVal = calc.addition (num1,num2)
    num1 = currVal
    print (currVal)

elif (oper == "-"):
    currVal = calc.subtraction (num1,num2)
    num1 = currVal
    print (currVal)

elif (oper == "*"):
    currVal = calc.multiplication (num1,num2)
    num1 = currVal
    print (currVal)

elif (oper == "/"):
    currVal = calc.divison (num1,num2)
    num1 = currVal
    print (currVal)

elif (oper == "^"):
    currVal = calc.exponent (num1,num2)
    num1 = currVal
    print (currVal)

else:
    print ("please enter a valid operation")