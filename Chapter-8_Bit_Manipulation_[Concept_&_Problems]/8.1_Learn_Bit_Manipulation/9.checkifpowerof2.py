"""
"Check if the given number is power of 2 or not"

=> Given N tell its power of 2 or not
"""


def powerOf2(n):
    return n & (n - 1) == 0


powerOf2(3)
