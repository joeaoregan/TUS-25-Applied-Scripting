def check_password_length(password, min_len=8, max_len=32):
    if min_len <= len(password) <= max_len:
        print("Password is correct length")
    else:
        print("Password is not the correct length")


if __name__=="__main__":
    # user_password = input('Enter your password: ')
    user_password = "password"

    check_password_length(user_password, 10, 20)

    check_password_length(password=user_password, min_len=10, max_len=20)

    check_password_length(user_password, max_len=12)