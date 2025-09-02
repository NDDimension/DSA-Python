"""
"Toggle the ith bit"

=> Given n and i change the 0 -> 1 or 1 -> 0 on ith bit of n
"""


def toggleIth(n, i):
    return n ^ (1 << i)


bin(toggleIth(13, 1))
