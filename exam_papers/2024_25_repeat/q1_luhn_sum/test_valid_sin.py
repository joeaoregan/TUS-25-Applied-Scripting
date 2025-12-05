import pytest
from q1_a_luhn_sum import is_valid_sin, luhn_sum

# Q1(c)(i)
def test_luhn_sum():
    assert luhn_sum("046454286") == 50
    assert luhn_sum("130692544") == 40

# Q1(c)(ii)
def test_valid_sin():
    assert is_valid_sin("046454286")
    assert not is_valid_sin("046454287")
    assert not is_valid_sin("13069254403")
    assert not is_valid_sin("X46454286")


if __name__ == "__main__":
    # Q1(c)(iii)
    pytest.main([__file__, "-v"])