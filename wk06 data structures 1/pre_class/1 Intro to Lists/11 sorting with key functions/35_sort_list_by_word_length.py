# Example: Sort a list of words by word-length 

sentence = "In a hole in the ground there lived a Hobbit"
words = sentence.split()
words.sort(key=len)
print(words)