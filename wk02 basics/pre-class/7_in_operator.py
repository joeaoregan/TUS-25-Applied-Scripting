# The in operator
# The in operator is used to check if a substring is contained within a string:

message = "Hello World"
print("Hello" in message)  # True
print("Goodbye" in message)  # False
print("hello" in message)  # False (case-sensitive)

email = 'jo.bloggs@tus.ie'
print('@' in email)  # True