# Question 2
# There are a number of ways to initialise a dictionary.
# Which of the following is not the correct code to initialise a dictionary?

irish_dict = {1: "A haon", 2: "A dó", 3: "A trí"}
print(irish_dict)  # Output: {1: 'A haon', 2: 'A dó', 3: 'A trí'}
print(type(irish_dict))  # Output: <class 'dict'>

irish_dict = dict([(1,"A haon"), (2,"A dó"), (3,"A trí")])
print(irish_dict)  # Output: {1: 'A haon', 2: 'A dó', 3: 'A trí'}
print(type(irish_dict))  # Output: <class 'dict'>

# irish_dict = dict(1:"A haon", 2:"A dó", 3:"A trí")
# print(irish_dict)  # Output: {1: 'A haon', 2: 'A dó', 3: 'A trí'}
# print(type(irish_dict))  # Output: <class 'dict'>
