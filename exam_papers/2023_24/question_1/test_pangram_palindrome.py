import pytest
from q1_pangram import is_palindrome, is_pangram

# 1(c)(i)
def test_is_pangram():
    assert is_pangram("The quick brown fox jumps over a lazy dog")
    assert not is_pangram("The quick brown fox jumps over a dog")

# 1(c)(ii)
def test_is_palindrome():
    assert is_palindrome("Rats live on no evil star", True)
    assert not is_palindrome("A man, a plan, a canal - Panama!", True)
    assert is_palindrome("A man, a plan, a canal - Panama!", False)
    assert is_palindrome("A man, a plan, a canal - Panama!")


if __name__ == "__main__":
    # 1(c)(iii)
    pytest.main([__file__, "-v"])

