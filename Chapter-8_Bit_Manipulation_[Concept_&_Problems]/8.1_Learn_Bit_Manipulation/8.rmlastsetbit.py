"""
"Remove the Last set bit(rightmost)"

=> Given n remove the last 1 from rightmost to 0
"""


def remLastSetBit(n):
    return n & (n - 1)


bin(remLastSetBit(13))
