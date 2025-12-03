import pytest
from q1a import is_valid_password

# Q1(c)
def test_valid_password():
    assert is_valid_password("&Now4Something")
    assert not is_valid_password("4Ever!")
    assert not is_valid_password("2Good2Be4Gotten?")
    assert not is_valid_password("Secret123")
    assert not is_valid_password("OpenSesame!")
    assert not is_valid_password("open_sesame123")


if __name__ == "__main__":
    pytest.main([__file__, '-v'])