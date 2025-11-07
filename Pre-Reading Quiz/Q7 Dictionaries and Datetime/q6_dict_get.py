# Question 6
# For the irish_dict above, what's the result of irish_dict.get(4, "Unknown")?

irish_dict = {1: "A haon", 2: "A dó", 3: "A trí"}
print(irish_dict.get(4, "Unknown"))  # Output: Unknown

test = irish_dict.get(4, "Unknown")
print(type(test))