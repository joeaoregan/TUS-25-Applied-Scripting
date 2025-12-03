import pytest
from q1a_email import generate_email, hyphenate_lastname

# Q1(c)(i)
def test_generate_email():
    assert generate_email("Sam Bloggs", True) == "sam.bloggs@tus.ie"
    assert generate_email("Sam Bloggs", False) == "sbloggs@tus.ie"
    assert generate_email("Sam Bloggs") == "sam.bloggs@tus.ie"

# Q1(c)(ii)
def test_hyphenate_lastname():
    assert hyphenate_lastname("Sam Bloggs") == "Sam Bloggs"
    assert hyphenate_lastname("Sam Mac Bloggs") == "Sam Mac-Bloggs"
    assert hyphenate_lastname("Sam Mac Giolla Bloggs") == "Sam Mac-Giolla-Bloggs"

if __name__ == "__main__":
    # Q1(c)(iii) Include code which runs the unit tests from parts (c)(i) and (c)(ii) with verbosity enabled.
    pytest.main([__file__, "-v"])