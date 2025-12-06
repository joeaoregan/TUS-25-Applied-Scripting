import pytest
from q4a_regex import check_filename

def test_check_filename():
    assert check_filename("index.html") == "Valid Filename"
    assert check_filename("favion.ico") == "Valid Filename"
    assert check_filename("index-test.html") == "Valid Filename"
    assert check_filename("flask_web_app100.py") == "Valid Filename"
    assert check_filename("home page.htm") == "Not a valid Filename"
    assert check_filename("index") == "Not a valid Filename"
    assert check_filename("$special.png") == "Not a valid Filename"
    assert check_filename("special.pngde") == "Not a valid Filename"

    
if __name__=="__main__":
    pytest.main([__file__, "-v"])