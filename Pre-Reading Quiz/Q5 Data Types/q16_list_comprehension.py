# The variable paragraph contains a long piece of text, e.g. in a triple-quoted string:
# paragraph = '''In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, 
# filled with the ends of worms and an oozy smell, nor yet a dry, bare, 
# sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.'''

# Which of the following is the correct code to create a list of the frequencies of each letter in the alphabet in the text contained in paragraph, 
# using a list comprehension? (i.e. ignoring case, count the numbers of a's, the number of b's and so on).

from string import ascii_lowercase

paragraph = '''In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.'''

# a.
# print([paragraph.count(x) for x in ascii_lowercase]) # works only for lowercase letters

# b.
print([paragraph.lower().count(x) for x in ascii_lowercase]) # works for all letters

# c.
# print([x for x in ascii_lowercase]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# d.
# print([ascii_lowercase.count(x) for x in paragraph]) # opposite counting