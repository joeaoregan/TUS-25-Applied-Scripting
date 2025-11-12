# Program to Determine Masters Award
# Version 3: Using match-case with if guards

#Input mark
mark = int(input("Enter your overall mark: "))

# Determine and display the output
match mark:
    case mark if not 0 <= mark <= 100:
        print("Invalid mark")
    case mark if mark >= 70:    
        print("First Class Honours")
    case mark if mark >= 50:
            print("Second Class Honours")
    case mark if mark >= 40:
        print("Pass")
    case _:
        print("No Award")

