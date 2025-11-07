# The variable paragraph contains a long piece of text, e.g. in a triple-quoted string:
# paragraph = '''In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.'''

# Which of the following is the correct code to create a list contents containing the unique characters in paragraph?

paragraph = '''In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.'''

# a.
contents = list(set(paragraph)) # ok

# b.
# contents = set(list(paragraph)) # <class 'set'>

# c.
# contents = list(paragraph) # all characters

# d.
# contents = set(paragraph) # <class 'set'>

print(sorted(contents))
print(type(contents))