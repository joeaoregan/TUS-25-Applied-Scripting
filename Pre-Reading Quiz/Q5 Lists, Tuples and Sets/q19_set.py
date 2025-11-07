# The variable unique contains a set of single characters {"a", "e", "i", "o", "u"}

# What is the correct code to add the string "y" to unique?

unique = {"a", "e", "i", "o", "u"}

# a.
# unique += "y" # TypeError: unsupported operand type(s) for +=: 'set' and 'str'

# b.
unique.add("y") # ok

# c.
# unique.append("y") # AttributeError: 'set' object has no attribute 'append'

# d.
# unique.insert("y") # AttributeError: 'set' object has no attribute 'insert'

print(unique)