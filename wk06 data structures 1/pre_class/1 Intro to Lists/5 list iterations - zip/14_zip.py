letters = "abc"
numbers = [1,2,3]
print(zip(letters,numbers))

for pair in zip(letters, numbers):
    print(pair)

print()

# Tuple assignment
for letter, number in zip(letters, numbers):
    print(f"{letter=} {number=}")

print()

#  When using zip(), if the two sequences are not the same length, the resulting zip has the length of the shorter one:
vowels = ['a', 'e', 'i', 'o', 'u']
numbers = [1,2,3]
for vowel, number in zip(vowels, numbers):
    print(f"{vowel=} {number=}")