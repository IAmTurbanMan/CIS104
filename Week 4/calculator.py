import math

#initialize variables
currVal = 0.0
memVal = 0.0

#function to clear calculator
def calcClear ():
    global memVal, currVal
    memVal = 0.0
    currVal = 0.0
    return print ("calculator cleared")

#function to add two numbers
def addition (x,y):
    global currVal
    currVal = x + y
    return print (currVal)

def subtraction (x,y):
    global currVal
    currVal = x - y
    return print (currVal)

def multiplication (x,y):
    global currVal
    currVal = x * y
    return print (currVal)

def divison (x,y):
    global currVal
    currVal = x / y
    return print (currVal)

def exponent (x,y):
    global currVal
    currVal = x ** y
    return print (currVal)

def invert (x):
    global currVal
    currVal = x * -1
    return print (currVal)

def memStore (x):
    global memVal
    memVal = x
    return print ("{} stored".format (memVal))

def memRecall ():
    currVal = memVal
    return print ("{} recalled".format (currVal))

def memClear ():
    global memVal
    memVal = 0.0
    print ("memory cleared")