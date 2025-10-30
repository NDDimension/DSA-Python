"""
Determines whether a given string containing '(', ')', and '*' characters is a valid parenthesis string.

A string is valid if:
- Every '(' has a corresponding ')'.
- Every ')' has a corresponding '('.
- The '*' character can represent either '(', ')' or an empty string.
- The string must be balanced after replacing '*' optimally.

Parameters:
----------
s : str
    The input string containing '(', ')', and '*' characters.

Returns:
-------
bool
    True if the string can be made valid, False otherwise.

Examples:
--------
>>> checkValidString("(*)")
True

>>> checkValidString("(*))")
True

>>> checkValidString("(*()")
True

Time Complexity:
----------------
O(n), where n is the length of the string.

Space Complexity:
-----------------
O(1), constant space greedy approach (optimized version).
"""

"""Brute Force Approach

TC : O(3^n)
SC : O(n)"""


def is_valid_parentheses(s, idx, cnt):
    if cnt < 0:
        return False

    if idx == len(s):
        return cnt == 0

    if s[idx] == "(":
        return is_valid_parentheses(s, idx + 1, cnt + 1)
    elif s[idx] == ")":
        return is_valid_parentheses(s, idx + 1, cnt - 1)
    elif s[idx] == "{":
        return is_valid_parentheses(s, idx + 1, cnt + 1)
    elif s[idx] == "}":
        return is_valid_parentheses(s, idx + 1, cnt - 1)
    elif s[idx] == "[":
        return is_valid_parentheses(s, idx + 1, cnt + 1)
    elif s[idx] == "]":
        return is_valid_parentheses(s, idx + 1, cnt - 1)
    return (
        is_valid_parentheses(s, idx + 1, cnt + 1)
        or is_valid_parentheses(s, idx + 1, cnt - 1)
        or is_valid_parentheses(s, idx + 1, cnt)
    )


is_valid_parentheses("()", 0, 0)

"""Optimal Approach

TC : O(n)
SC : O(1)"""


def checkValidString(s):
    min = max = 0
    n = len(s)
    for i in range(n):
        if s[i] == "(":
            min += 1
            max += 1
        elif s[i] == ")":
            min -= 1
            max -= 1
        else:
            min -= 1
            max += 1
        if min < 0:
            min = 0

        if max < 0:
            return False
    return min == 0


checkValidString("(*)")
