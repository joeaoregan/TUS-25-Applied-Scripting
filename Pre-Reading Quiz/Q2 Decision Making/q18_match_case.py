# A00258304

# Which of the following statements about the match-case structure is correct?
# a. The subject can be any expression, and patterns can include literals, variables, sequence patterns, or wildcards # True
# b. The subject can only be a variable, and patterns cannot include multiple alternatives
# c. The subject must always be an integer, and patterns can only be integer literals
# d. The subject can be any expression, but patterns must always be simple constants

greeting = "hello"
match greeting:
    case "hi":
        print("Hi")
    case "Hello":
        print("Hello")
    case "HELLO":
        print("HELLO")
    case _: # catch all
        print("Other")

number = 5
match number:
    case number if number < 5:
        print("Number less than 5")
    case number if number == 5:
        print("Number equal 5")
    case number if number > 5:
        print("Number greater than 5")