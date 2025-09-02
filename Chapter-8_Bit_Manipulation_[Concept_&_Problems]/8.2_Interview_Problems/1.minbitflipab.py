"""
"Minimum bit flip to convert a number"

=> We are given a start we need to get to goal by changing bits.
"""

"""
We will be using XOR between start and goal to get the number having 1s where we need to do the change.
And the no. of set bits is our answer.

=> TC : O(log m)
=> SC : O(log m)
"""


def changeNumber(start, goal):
    ans = start ^ goal
    return bin(ans).count("1")


changeNumber(3, 4)
