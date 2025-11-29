email = "       info@TUS.ie     "
print(email.strip().lower().endswith("tus.ie"))  # True

# string operations performed left to right from the variable

email.strip() # remove white space
email.strip().lower() # then converts to lower case
email.strip().lower().endswith("tus.ie") # then checks the ending