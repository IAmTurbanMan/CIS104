#H2P2: Book learnin'

#input and store book information
bookName = input ("What is your favorite book? ")
bookAuthor = input ("Who wrote the book? ")
bookPublishYear = int (input ("What year was the book published? "))
bookPages = int (input ("How many pages does the book have? "))

#get current year and store
#found this code @ https://stackoverflow.com/questions/30071886/how-to-get-current-time-in-python-and-break-up-into-year-month-day-hour-minu
#modified to suit my needs
import datetime
now = datetime.datetime.now ()

#calculate and store age of book
bookAge = (now.year - bookPublishYear)

#conditional statements for age
if (bookAge < 10):
    print ("This book is younger than ten years.")
else:
    print ("This book is at least ten years old.")

#conditional statements for length
if (bookPages < 100):
    print ("This is a short book.")
elif (bookPages >= 100 and bookPages < 300):
    print ("This is an average book.")
else:
    print ("This is a long book.")
