import calculator as calc

num1 = float (input ("enter a number: "))
num2 = float (input ("enter another number: "))
oper = (input ("enter an operation: "))

if (oper == "+"):
    calc.addition (num1,num2)
    print (calc.currVal)

elif (oper == "-"):
    calc.subtraction (num1,num2)
    print (calc.currVal)

elif (oper == "*"):
    calc.multiplication (num1,num2)
    print (calc.currVal)

elif (oper == "/"):
    calcVal = calc.divison (num1,num2)
    print (calc.currVal)

elif (oper == "^"):
    calc.exponent (num1,num2)
    print (calc.currVal)

else:
    print ("please enter a valid operation")