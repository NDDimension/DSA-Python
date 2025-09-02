"""
"Set the ith bit"

=> if ith 0 -> 1
"""


def setIth(n, i):
    return n | (1 << i)


result = setIth(9, 2)
print(bin(9))
print(result)
print(bin(result))
