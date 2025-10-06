"""
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive 1s in the array
if you can flip at most `k` 0s to 1s.

This problem is solved using the sliding window approach. We maintain a window [left, right]
such that the number of 0s in the window does not exceed `k`. If it does, we move the left pointer
to the right until the constraint is satisfied. At each step, we calculate the length of the window
and update the maximum length found.

Time Complexity: O(n), where n is the length of the array.
Space Complexity: O(1), constant space (only pointers and a counter).

Parameters:
----------
nums : List[int]
    A list of integers (0s and 1s) representing the binary array.

k : int
    The maximum number of 0s that can be flipped to 1s.

Returns:
-------
int
    The maximum number of consecutive 1s achievable after flipping at most `k` 0s.

Examples:
--------
>>> longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
6
# Flip two zeros at positions 4 and 5 to get the longest sequence of 1s: [1,1,1,0,0,1,1,1,1,1]

>>> longestOnes([0,0,1,1,1,0,0], 0)
3
# No flips allowed; longest run of 1s is [1,1,1]
"""

"""Brute Force
TC : O(n^2)
SC : O(1)"""


def MC1(a, k):
    n = len(a)
    maxlen = 0
    for i in range(n):
        zero = 0
        for j in range(i, n):
            if a[j] == 0:
                zero += 1

            if zero <= k:
                lenn = j - i + 1
                maxlen = max(maxlen, lenn)

            else:
                break

    return maxlen


MC1([0, 0, 1, 1, 1, 0, 0], 0)

"""Sliding Window
TC : O(n)
SC : O(1)"""


def MC1S(a, k):
    left = 0
    maxlen = 0
    zero = 0

    for right in range(len(a)):
        if a[right] == 0:
            zero += 1

        while zero > k:
            if a[left] == 0:
                zero -= 1

            left += 1

        maxlen = max(maxlen, right - left + 1)

    return maxlen


MC1S([0, 0, 1, 1, 1, 0, 0], 0)
