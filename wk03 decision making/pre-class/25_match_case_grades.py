# Example Program: Feedback based on Grade

grade = input("Enter the letter Grade: ")

match grade.upper():
    case "A":
        print("Excellent")
    case "B":
        print("Good job")
    case "C":
        print("Fair")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")

