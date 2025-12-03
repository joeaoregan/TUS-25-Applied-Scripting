import pytest
from q1_a import is_valid_username

def test_valid_username():
    assert is_valid_username("jbloggs")
    assert is_valid_username("Bloggs2022")
    assert is_valid_username("Joe_Bloggs1990")
    assert not is_valid_username("MyAdmin")
    assert not is_valid_username("Oscar_Fingal_OFlahertie_Wills_Wilde")
    assert not is_valid_username("Grace_O'Malley")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])