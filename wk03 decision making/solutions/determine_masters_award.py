# Program to Determine Masters Award
#Input mark
mark = int(input("Enter your overall mark: "))
#If mark is valid
if not 0 <= mark <= 100: # alternative to if mark < 0 or mark > 100 
    print("Invalid Mark")
elif mark >= 70:    
    print("First Class Honours")
elif mark >= 50:
        print("Second Class Honours")
elif (mark >= 40):
    print("Pass")
else:
    print("No Award")

    