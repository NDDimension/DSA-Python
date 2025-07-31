"""
"Check whether the given strings are anagram"

Anagram -> String having same words in different order.
"""

from collections import Counter


def is_Anagram(s1, s2):
    if Counter(s1) == Counter(s2):
        return True
    return False


s1, s2 = "anagram", "nagaram"
print(is_Anagram(s1, s2))
