numbers = []
divisibleNumbers = []

for i in range(1, 1001):
        numbers.append(i)

for x in numbers:
        if (x%7 == 0):
                divisibleNumbers.append(x)

count = len(divisibleNumbers)

print("The number of integers that are divisible by 7 within the range 1-1000 is: {}".format (count))