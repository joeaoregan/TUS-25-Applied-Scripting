full_name = input("Enter your first and last names, separated by a space: ")

username = full_name.lower().split(" ")
username = username[0][0] + username[1]

print(f"Your username is: {username}")