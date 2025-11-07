# What is the correct code to increase by 1 the value in the frequencies list at an index specified by the variable index?

frequencies = [1, 1, 1, 1, 1]
index = 2

# a.
frequencies[index] += 1 # this

# b.
# frequencies[index]++ # SyntaxError: invalid syntax

# c.
# frequencies[index] =+ 1 # assigns the value +1 to the index

# d.
# frequencies[index] = 1 # assigns the value +1 to the index

print(frequencies)