import calculator as calc

currVal = 0.0

num1 = float (input ("enter a number: "))
num2 = float (input ("enter another number: "))
oper = (input ("enter an operation: "))

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