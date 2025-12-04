# P61 - Set Operations
#  len(s)           Return the number of elements in set s (cardinality of s).
#  x in s           Check if x is an element of the set s.
#  x not in s       Check if x is not an element of the set s.
#  s.copy()         Return a copy of the set s (i.e. a new set, not a reference to the set s).
#  s.add(elem)      Add element elem to the set s.
#  s.remove(elem)   Remove element elem from the set s. Raises KeyError if elem is not contained in the set.
#  s.discard(elem)  Remove element elem from the set s if it is present.
#  s.pop()          Remove and return an element from the set s. Raises KeyError if the set is empty.
#  s.clear()        Remove all elements from the set s

number_string = "6 3 9 6 6 5 9 3"
s = [int(num) for num in number_string.split()]
print(s)
s = set(s)
print(s)

x = 9
print(x in s)
print(4 in s)

print(2 not in s)
print(3 not in s)

s2 = s.copy()
print(s2)

s.add(4)
print(s)

s.remove(3)
print(s)

x = s.pop()
print(x)
print(s)

s.clear()
print(s)
