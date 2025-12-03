import pytest
from math_functions import square

def test_square_positive_integer():
    assert square(5) == 25

def test_square_zero():
    assert square(0) == 0

def test_square_negative_integer():
    assert square(-3) == 9

def test_square_positive_float():
    assert square(2.5) == 6.25


if __name__ == "__main__":
    # pytest.main([__file__])
    pytest.main([__file__, "-v"]) # verbose: more info