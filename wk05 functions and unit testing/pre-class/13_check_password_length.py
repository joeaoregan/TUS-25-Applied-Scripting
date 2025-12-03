#  Example: Function to check is the length of a password is valid

def is_valid_password_length(password, min_len=8, max_len=32):
    return min_len <= len(password) <= max_len

if __name__=="__main__":
    password = input('Enter your password ')

    if is_valid_password_length(password):
        print("Password lenght is ok")
    else:
        print("Password is too short")