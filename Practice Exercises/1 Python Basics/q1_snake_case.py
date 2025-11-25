# A00258304
snake_case = input("Enter the variable name in snake_case: ")

camel_case = snake_case.replace("_", " ")

camel_case = camel_case.title()

camel_case = camel_case.replace(" ", "")

camel_case = camel_case[0].lower() + camel_case[1:]

print(f"The equivalent variable name in camelCase is: {camel_case}")