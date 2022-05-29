"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
"""


def isPalindrome(s: str) -> bool:
    s = s.lower()
    ascii_s = list(c for c in s if ord('a') <= ord(c) <= ord('z'))
    ascii_s_reverse = list(reversed(ascii_s))
    return ascii_s == ascii_s_reverse
