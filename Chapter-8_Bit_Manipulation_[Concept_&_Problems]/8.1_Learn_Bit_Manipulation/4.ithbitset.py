"""
"Check if the ith bit is set or not"

=> if ith bit is 1 -> True else False
"""


# Left Shift
def ithSetL(n, i):
    return (n & (1 << i)) != 0


ithSetL(13, 1)
ithSetL(13, 2)


# Right Shift
def ithSetR(n, i):
    if ((n >> i) and 1) == 0:
        return False
    return True


ithSetR(13, 1)
ithSetR(13, 2)
