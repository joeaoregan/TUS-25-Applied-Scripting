# Program to determine whether or not a year is a leap year

# A year is a leap year 
# if it is evenly divisible by 400, e.g. 1600, 2000, 2400
# OR it is evenly divisible by 4 and not by 100, e.g. 2016, 2020, 2024
# Years such as 2021 are obviously leap years,
# but the centeary years 1900 and 210 are also not leap years

# Input the year
year = int(input("Enter the year: "))

# Check if it is a Leap Year
# The % is a "modulo operator" (also used in C/C++/Java)
# Modulo airthmetic involves dividing one number by another and getting the remainder
# For example 24 % 4 = 3 (23 divided by 4 goes 5 times, remainder 3)
# To check for "evenly divisible, check if the remainder is zero
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")