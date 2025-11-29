# The string module
# whitespace -- a string containing all ASCII whitespace
# ascii_lowercase -- a string containing all ASCII lowercase letters
# ascii_uppercase -- a string containing all ASCII uppercase letters
# ascii_letters -- a string containing all ASCII letters (lowercase + uppercase)
# digits -- a string containing all ASCII digits
# hexdigits -- a string containing all hexadecimal digits
# octdigits -- a string containing all octal digits
# punctuation -- a string containing all ASCII punctuation characters considered printable

import string

from random import choice

print(choice(string.ascii_letters))  # Random letter

print(choice(string.digits))  # Random digit

print(choice(string.punctuation)) # Random punctuation character