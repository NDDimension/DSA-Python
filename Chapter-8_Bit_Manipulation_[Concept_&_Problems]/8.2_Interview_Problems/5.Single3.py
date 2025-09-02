"""
"Single III"

=> Given an array having duplicates along with 2 distinct numbers occuring only 1 one time we need to return them.
"""

# Naive Approach
"""
Hashing and finding those 2 nos based on their frequency

TC : O(n)
SC : O(n)
"""

from collections import Counter


def Single3(nums):
    counts = Counter(nums)
    return [num for num, count in counts.items() if count == 1]


Single3([1, 1, 2, 2, 3, 3, 4, 5])

# Bit Manipulation
"""
We will be using the concept of `Buckets`
We are going to perform XOR between the nums and going to get a
number .

In that number we will be focusing on the rightmost set bit
after that we will be performing AND between that number and 
number - 1 following by a XOR with number.

Now two separate buckets having the distinct numbers in them 
based on the rightmost set bit and now just perform the XOR
in each bucket and we get our nums

TC : O(n)
SC : O(1)
"""


def Single3(nums):
    xor = 0
    for num in nums:
        xor ^= num

    diff = xor & -xor

    a, b = 0, 0
    for num in nums:
        if num & diff:
            a ^= num

        else:
            b ^= num

    return [a, b]


Single3([1, 1, 2, 2, 3, 3, 4, 5])
