import math

#initialize variables
currVal = 0.0
memVal = 0.0

#function to clear calculator
def calcClear (memVal, currVal):
    memVal = 0.0
    currVal = 0.0
    return print ("calculator cleared")

#function to add two numbers
def addition (x,y):
    currVal = x + y
    return print (currVal)

def subtraction (x,y):
    currVal = x - y
    return print (currVal)

def multiplication (x,y):
    currVal = x * y
    return print (currVal)

def divison (x,y):
    currVal = x / y
    return print (currVal)

def exponent (x,y):
    currVal = x ** y
    return print (currVal)

def invert (x):
    currVal = x * -1
    return print (currVal)

def memStore (memVal, currVal):
    memVal = currVal
    return print ("{} stored".format (memVal))

def memRecall (currVal, memVal):
    currVal = memVal
    return print ("{} recalled".format (currVal))

def memClear (memVal):
    memVal = 0.0
    print ("memory cleared")