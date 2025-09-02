"""
"Single Number"

=> Given a number array with repeating numbers except one number
    and we need to return the odd one out.
"""

# Brute Force
"""
Counting the count of each element basically frequency and returning
the one with freq = 1.

=> TC : O(n)
=> SC : O(n)
"""

from collections import Counter


def SingleNumber(nums):
    freq = Counter(nums)
    for num, count in freq.items():
        if count == 1:
            return num

    return 0


SingleNumber([1, 1, 2, 2, 4])

# Bit Manipulation
"""
XOR between all and same nos. become 0 leaving the single number.

=> TC : O(n)
=> SC : O(1)
"""

from functools import reduce


def singleNumber(nums):
    return reduce(lambda x, y: x ^ y, nums)


singleNumber([1, 1, 2, 2, 3])
