import math

#initialize variables
#memVal to store memory

memVal = None

#mathematical functions
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

#calculator functions
def memStore (x):
    global memVal
    memVal = x
    return memVal

def memRecall ():
    return memVal

def memClear ():
    global memVal
    memVal = 0.0