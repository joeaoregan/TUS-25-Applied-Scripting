# Input firstname
firstname = input("Enter user's firstname: ")
lastname = input("Enter user's lasntname: ")

# Generate username
username = firstname[0] + lastname

# Convert to lowercase
username = username.lower()

# Print the username
print(f"Username: {username}")