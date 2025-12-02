response = input("Do you want to continue, yes or no? ")

match response:
    case "y" | "Y" | "yes" | "Yes" | "YES":
        print("Proceeding")
    case "n" | "N" | "no" | "No" | "NO":
        print("Cancelling")
    case _:
        print("Invalid input")