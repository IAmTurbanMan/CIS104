memVal = 0.0

def calcClear ():
    memVal = 0.0
    print ("calculator cleared")

def addition (x,y):
    return x + y

def subtraction (x,y):
    return x - y

def multiplication (x,y):
    return x * y

def divison (x,y):
    return x / y

def exponent (x,y):
    return x ** y

def invert (x):
    return x * -1

def memStore (x):
    memVal = x
    print ("{} stored".format (memVal))

def memRecall ():
    return memVal
    print ("{} recalled".format (memVal))

def memClear ():
    memVal = 0.0
    print ("memory cleared")