import pytest
from q1_a_i_and_ii import check_valid_check_digit, check_valid_imo

def test_valid_check_digit():
    assert(check_valid_check_digit("9074729"))
    assert(not check_valid_check_digit("9074728"))

def test_valid_imo():
    assert(check_valid_imo("IMO9074729"))
    assert(not check_valid_imo("IMO9074728"))
    assert(not check_valid_imo("IMO19074729"))
    assert(not check_valid_imo("INO9074729"))

if __name__ == "__main__":
    pytest.main([__file__, "-v"])