# Example: Managing a List of Names
print("User management program")

users = []

while True:
    # menu of choices
    choice = input("[A]dd [R]emove [D]isplay [C]lear [Q]uit? ")

    # process the user's choice - check the first character of their choice
    match choice[0].lower():
        case "q": # quit
            break
        case "a": # add
            name = input("Enter name of new user: ")
            users.append(name)
            print(f"Added user {name}")
        case "r": # remove
            name = input("Enter name of user to remove: ")
            if name in users:
                users.remove(name)
                print(f"Remvoed user {name}")
            else:
                print(f"No such user {name}")
        case "d": # display
            print(f"Number of users: {len(users)}")
            users.sort() # sor the names in order and in place
            for user in users:
                print(user)
        case "c": # clear the list
            response = input("Remove all users from the list? (y/n) ")
            if response.lower() == "y":
                users.clear()
        case _:
            print("Invalid choice")
        
