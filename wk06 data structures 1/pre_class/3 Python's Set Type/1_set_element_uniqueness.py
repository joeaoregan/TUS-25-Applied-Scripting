# P58 Sets - Set Element Uniqueness

word = "accessible"
letters = list(word)
print(word)
print(letters)
print(set(word)) # unique letters

unique_letters = set(letters)
print(unique_letters)
unique_letters_list = list(set(letters))
print(unique_letters_list)

sorted_letters_list = sorted(list(set(letters)))
print(sorted_letters_list)