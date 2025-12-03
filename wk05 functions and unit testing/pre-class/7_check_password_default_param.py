def check_password_length(password, minlen=8, maxlen=32):
    if minlen <= len(password) <= maxlen:
        print("Password is correct length")
    else:
        print("Password is not the correct length")

password = "Secret12"

check_password_length(password)
check_password_length(password, 10)
check_password_length(password, 10, 20)