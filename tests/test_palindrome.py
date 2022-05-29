from problems import palindrome
import pytest

@pytest.mark.parametrize("s,excepted", [ ("A man, a plan, a canal: Panama", True),
                                         ("race a car", False),
                                         (" ", True)
                                           ])  
def test_palindrome(s, excepted):
    assert excepted == palindrome.isPalindrome(s)
    