# Function: This program determines if a date entered by the user is valid.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

year = int(input("Enter a year: "))
month = int(input("Enter month: "))
day = int(input("Enter a day: "))



if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False



# endOfJob()
if validDate == True:
    # Output statement
    print(f"{month}/{day}/{year} is a valid date.")
else: 
    validDate == False
    # Output statement
    print(f"{month}/{day}/{year} is an invalid date.")
