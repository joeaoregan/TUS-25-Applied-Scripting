def is_valid_password_length(password, min_len=8, max_len=32):
    return min_len <= len(password) <= max_len