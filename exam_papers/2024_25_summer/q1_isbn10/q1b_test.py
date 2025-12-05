from q1a_isbn10 import calculated_check_character, check_valid_isbn10

import pytest

# Q1(b)
# (i)
def test_calculated_check_character():
    assert calculated_check_character("030640615") == "2"
    assert calculated_check_character("567725696") == "X"
    assert calculated_check_character("134524298") == "0"

# (ii)
def test_check_valid_isbn10():
    assert check_valid_isbn10("0306406152") == True
    assert check_valid_isbn10("10306406152") == False
    assert check_valid_isbn10("567725696Y") == False

if __name__=="__main__":
    # (iii)
    pytest.main([__file__, "-v"])