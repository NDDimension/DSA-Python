"""
"Clear the ith bit"

=> Given N and i we need to make 0 the ith bit in N
"""


def clearIth(n, i):
    return n & ~(1 << i)


bin(clearIth(15, 2))
