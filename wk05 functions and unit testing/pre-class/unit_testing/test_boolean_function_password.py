import pytest
from password_functions import is_valid_password_length

def test_password_valid_length_default():
    assert is_valid_password_length("mypassword123")

def test_password_too_short():
    assert not is_valid_password_length("secret")

def test_password_too_long_default():
    long_password = "my very excellent password which is too long"
    assert not is_valid_password_length(long_password)

def test_password_at_min_length():
    assert is_valid_password_length("12345678")

def test_password_at_max_length():
    password = "a" * 32
    assert is_valid_password_length(password)

def test_password_custom_min_max_valid():
    password = "mypwd"
    assert is_valid_password_length(password, min_len=4, max_len=6)

def test_password_custom_min_max_invalid():
    password = "mypassword"
    assert not is_valid_password_length(password, min_len=4, max_len=6)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])