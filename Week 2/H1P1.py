first_name = input ("Enter your first name: ")
last_name = input ("Enter your last name: ")
age = int (input ("Enter your age: "))
confidence = int (input ("How confident are you in programmers (0 - 100)?: "))
dog_years = age * 7
percent = confidence / 100

print ("Hello {} {}, nice to meet you!".format (first_name, last_name))
print ("You may be {} in human years. But in dog years, you are {} years old!".format (age, dog_years))
if percent < .50:
    print ("I agree, programmers cannot be trusted.")
else:
    print ("Programming is hard work.")