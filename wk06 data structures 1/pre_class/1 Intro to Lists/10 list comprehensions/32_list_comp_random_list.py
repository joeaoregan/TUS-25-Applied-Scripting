from random import randint
numbers = [randint(0,5) for i in range(10)]
print(f"{numbers=}")

# Example: Working with a list of Strings
sentence = "In a hole in the ground there lived a Hobbit"
words = sentence.split()
letters = [word[0] for word in words]
print(letters)

lengths = [len(word) for word in words]
print(lengths)