import math

#initialize variables
#memVal to store memory

memVal = None

#mathematical functions
#addition
def addition (x,y):
    return x + y

#subtraction
def subtraction (x,y):
    return x - y

#multiplication
def multiplication (x,y):
    return x * y

#division
def divison (x,y):
    return x / y

#exponent: take x number to the y power
def exponent (x,y):
    return x ** y

#invert a number
def invert (x):
    return x * -1

#calculator functions
#store the last result in memory
def memStore (x):
    global memVal
    memVal = x
    return memVal

#recall the stored number
def memRecall ():
    return memVal

#clear the stored number
def memClear ():
    global memVal
    memVal = 0.0