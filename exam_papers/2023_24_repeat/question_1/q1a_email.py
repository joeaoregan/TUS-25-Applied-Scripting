# 2023/24 Repeat
# Q1(a)(i)
def generate_email(fullname, use_format=True):
    firstname,lastname = fullname.lower().split(" ")
    if use_format:
        return f"{firstname}.{lastname}@tus.ie"
    return f"{firstname[0]}{lastname}@tus.ie"

# print(generate_email("Sam Bloggs"))
# print(generate_email("Sam Bloggs", False))

def hyphenate_lastname(fullname):
    names = fullname.split(" ")
    firstname = names[0]
    lastname = "-".join(names[1:])
    return f"{firstname} {lastname}"

# print(hyphenate_lastname("Sam Mac Giolla Bloggs"))

if __name__ == "__main__":
    keep_going = True
    while(keep_going):
        fullname = input("Enter the name in the format firstname lastname: ")
        new_format = input("Use new email format, y/n? ")

        use_new_format = new_format.lower() == 'y'
        
        email = generate_email(fullname, use_new_format)
        print(f"Email address is: {email}")

        keep_going = input("Create another, y/n? ").lower() != 'n'

