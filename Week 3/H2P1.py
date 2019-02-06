#H2P1: functions

#ask for and store age
age = int (input ("Enter your age: "))

#calculate and store age in 10 years
futureAge = int (age + 10)

#print greeting giving user a sense of impending doom
print ("You will be {} years old in ten years! You're getting old.".format (futureAge))

#ask for and store Fahrenheit
temperatureF = float (input ("Enter the current temperature in Fahrenheit: "))

#calculate and store Celcius
temperatureC = float ((temperatureF - 32.0) * (5.0 / 9.0))

#print temperature in Celcius
print ("It is {:.1f} degrees celcius.".format (temperatureC))

