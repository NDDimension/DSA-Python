"""
"Isomorphic Strings"

=> Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

=> Example

Input: s = "egg", t = "add"
Output: true
why? -> e mapped to a , both g are mapped to d so its ok.

Input: s = "foo", t = "bar"
Output: false
why? -> f mapped to b , o mapped to a and o also mapped to r so its not ok.
"""


def transform(s):
    mapping = {}
    return list(map(lambda x: mapping.setdefault(x, len(mapping)), s))


def Isomorphic(s, t):
    return transform(s) == transform(t)


s = "egg"
t = "add"
print(Isomorphic(s, t))
