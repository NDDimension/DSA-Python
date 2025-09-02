"""
"Count the Number of Set bits"
"""


def countSetbits(n):
    return bin(n).count("1")


countSetbits(13)
