memVal = 0.0
currVal = 0.0

def calcClear ():
    currVal = 0.0
    memVal = 0.0
    print ("calculator cleared")

def addition (x,y):
    return x + y
    currVal = x + y

def subtraction (x,y):
    return x - y
    currVal = x - y

def multiplication (x,y):
    return x * y
    currVal = x * y

def divison (x,y):
    return x / y
    currVal = x / y

def exponent (x,y):
    return x ** y
    currVal = x ** y

def invert (x):
    return x * -1
    currVal = x * -1

def memStore ():
    memVal = currVal
    print ("{} stored".format (memVal))

def memRecall ():
    currVal = memVal
    print ("{} recalled".format (currVal))

def memClear ():
    memVal = 0.0
    print ("memory cleared")