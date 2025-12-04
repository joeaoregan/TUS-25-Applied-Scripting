# Built-in Functions and Lists
# A number of Python’s built-in functions can be used for processing lists:
# print(values)     prints the list in standard format (with brackets and commas)
# len(values)       returns the number of items in the list
# sum(values)       returns the total of all numbers in the list (error if non-numeric item)
# min(values)       returns the smallest number, for strings, returns the first in alphabetical order
# max(values)       returns the largest number, for strings, returns the last in alphabetical order 
# sorted(values)    returns a new sorted copy of the list (the original list is unchanged)
# reversed(values)  returns an iterator to traverse the list in reverse order (original list is unchanged)
marks = [84, 68, 71, 88, 95, 88]
print(marks)

print(f"{marks=}")

print(len(marks))
print(sum(marks))
print(sorted(marks))
print(min(marks))
print(max(marks))
print(reversed(marks))
print(list(reversed(marks)))

users = ['root', 'apache', 'mysql', 'jbloggs']
print(len(users))
print(sorted(users))
print(min(users))
print(max(users))
print(reversed(users))
print(list(reversed(users)))
# print(sum(users)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# sorted()
marks = [84, 68, 71, 88, 95, 88]
print(sorted(marks))
print(marks)

users = ['root', 'apache', 'mysql', 'jbloggs']
print(sorted(users))
print(users)


users = ['root', 'apache', 'mysql', 'Jbloggs'] # Uppercase comes first
print(sorted(users))

# sorted reverse
marks = [84, 68, 71, 88, 95, 88]
print(sorted(marks))
print(sorted(marks, reverse=True))


users = ['root', 'apache', 'mysql', 'jbloggs']
print(sorted(users, reverse=True))

weather_log = [3, "sunny", 21.3, False, 18.7]
# print(weather_log.sort()) # TypeError: '<' not supported between instances of 'str' and 'int'

