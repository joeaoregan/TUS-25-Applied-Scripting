#  There are also string methods to count and search for substrings:

str = "test test test"
print(str.count("est"))      # 3
print(str.count("tes"))      # 3
print(str.find("est"))       # 2 (index of first occurrence)
print(str.find("tes"))       # 0 (index of first occurrence)
print(str.find("xyz"))       # -1 (not found)
print(str.index("est"))      # 2 (index of first occurrence)
print(str.index("tes"))      # 0 (index of first occurrence)
# print(str.index("xyz"))    # Raises ValueError (not found)    
print(str.rfind("est"))      # 10 (index of last occurrence)
print(str.rfind("tes"))      # 8  (index of last occurrence)
print(str.rindex("est"))     # 10 (index of last occurrence 
print(str.rindex("tes"))     # 8  (index of last occurrence
# print(str.rindex("xyz"))   # Raises ValueError (not found)
print()

email = "jo.bloggs@tus.ie"
print(email.count(".")) # 2
print(email.find("@"))  # 9
print(email.find("."))  # 2
print(email.find("+"))  # -1
print(email.rfind(".")) # 13
print(email.index("@")) # 9
# print(email.index("+")) # Raises ValueError
print()