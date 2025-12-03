import pytest
from q1_a_imo_number import chack_valid_imo_number

# Q1 (b) (i)
# Write PyTest unit tests for the function in Part (a)(i), 
# with the following inputs and expected outputs:

# Input     | Expected Output
# --------- | ---------------
# "9074729" | True
# "9074728" | False

import pytest
from q1_a_imo_number import check_imo_test_digit, chack_valid_imo_number

def test_imo_check_digit_is_correct():
    assert check_imo_test_digit("9074729")
    assert check_imo_test_digit("9074728") == False

# Q1 (b) (ii)
# Write PyTest unit tests for the function in Part (a)(ii), 
# with the following inputs and expected outputs:

# Input         | Expected Output
# ------------- | ---------------
# "IMO9074729"  | True
# "IMO9074728"  | False
# "IMO19074729" | False
# "INO9074729"  | False

def test_imo_number_is_correct():
    assert chack_valid_imo_number("IMO9074729")
    assert not chack_valid_imo_number("IMO9074728")
    assert not chack_valid_imo_number("IMO19074729")
    assert chack_valid_imo_number("INO9074729") == False # Works, but use not


if __name__ == "__main__":
    # Q1 (b) (iii) Include code which runs the unit tests from parts (c)(i) and (c)(ii) with verbosity enabled.
    pytest.main([__file__, "-v"])