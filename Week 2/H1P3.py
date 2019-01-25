#input amount of change
pennies = int (input ("Pennies: "))
nickels = int (input ("Nickels: "))
dimes = int (input ("Dimes: "))
quarters = int (input ("Quarters: "))
half_dollar = int (input ("Half dollar coins: "))
dollar = int (input ("One dollar coins: "))

#if statements to determine whether plural
if pennies == 1:
    print ("You have {} penny.".format (pennies))
else:
    print ("You have {} pennies.".format (pennies))

if nickels == 1:
    print ("You have {} nickel.".format (nickels))
else:
    print ("You have {} nickels.".format (nickels))

if dimes == 1:
    print ("You have {} dime.".format (dimes))
else:
    print ("You have {} dimes.".format (dimes))

if quarters == 1:
    print ("You have {} quarter.".format (quarters))
else:
    print ("You have {} quarters.".format (quarters))

if half_dollar == 1:
    print ("You have {} half dollar coin.".format (half_dollar))
else:
    print ("You have {} half dollar coins.".format (half_dollar))

if dollar == 1:
    print ("You have {} one dollar coin.".format (dollar))
else:
    print ("You have {} one dollar coins.".format (dollar))


#determine actual value of coins
penny_value = float (pennies * .01)
nickel_value = float (nickels * .05)
dime_value = float (dimes * .10)
quarter_value = float (quarters * .25)
half_dollar_value = float (half_dollar * .50)

#sum value
total = (penny_value + nickel_value + dime_value + quarter_value + half_dollar_value + dollar)

#print total
print ("You have a total of ${:.2f}.".format (total))