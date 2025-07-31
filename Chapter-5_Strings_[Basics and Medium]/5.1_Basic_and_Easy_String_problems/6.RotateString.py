"""
"Check if one string is rotation of other"

=> Given two strings we need to check if we rotate other strings a number of times we get the first one.
"""


def is_rotation(s1, s2):
    if len(s1) == len(s2) and s2 in (s1 + s1):
        return True
    else:
        return False


print(is_rotation("waterbottle", "erbottlewat"))
