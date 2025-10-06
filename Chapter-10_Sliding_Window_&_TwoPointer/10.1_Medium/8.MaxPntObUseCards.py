"""
Maximum Points You Can Obtain from Cards

You have several cards arranged in a row, and each card has an associated number of points.
You can take exactly k cards from the array, taking cards only from either the beginning or
the end of the row (not from the middle). You need to maximize the total number of points
you can obtain.

Given an integer array `cardPoints` and an integer `k`, return the maximum score you can
obtain by taking exactly `k` cards.

Parameters
----------
cardPoints : List[int]
    A list of integers representing the points on each card.
k : int
    The number of cards you must take.

Returns
-------
int
    The maximum score you can obtain.

Example
-------
>>> sol = Solution()
>>> sol.maxScore([1,2,3,4,5,6,1], 3)
12
# Explanation: Take the last three cards (6,1) and the first one (1) for a total of 1+6+5=12

>>> sol.maxScore([2,2,2], 2)
4

>>> sol.maxScore([9,7,7,9,7,7,9], 7)
55

Constraints
-----------
- 1 <= cardPoints.length <= 10^5
- 1 <= cardPoints[i] <= 10^4
- 1 <= k <= cardPoints.length

Optimal Method
--------------
Use sliding window to find the minimal sum of the subarray of length len(cardPoints) - k.
Subtract that from the total sum to get the maximum score.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def MPOUC(nums, k):
    lsum, rsum, maxSum = 0, 0, 0
    for i in range(k):
        lsum += nums[i]
        maxSum = lsum

    ridx = len(nums) - 1
    for i in range(k - 1, -1, -1):
        lsum -= nums[i]
        rsum += nums[ridx]
        ridx -= 1
        maxSum = max(maxSum, lsum + rsum)

    return maxSum


MPOUC([9, 7, 7, 9, 7, 7, 9], 7)
