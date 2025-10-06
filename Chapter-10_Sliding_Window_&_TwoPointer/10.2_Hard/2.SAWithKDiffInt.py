"""
"Sub Array with K Different Integers"

Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good subarray is defined as a contiguous subarray with exactly k distinct integers.

Parameters:
nums (List[int]): A list of integers.
k (int): The exact number of distinct integers required in each subarray.

Returns:
int: The number of subarrays with exactly k distinct integers.

Constraints:
- 1 <= len(nums) <= 10^5
- nums[i] is an integer in the range [1, 10^4]
- 1 <= k <= len(nums)

Example 1:
>>> subarrays_with_k_distinct([1,2,1,2,3], 2)
7
Explanation: The 7 subarrays are [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,3].

Example 2:
>>> subarrays_with_k_distinct([1,2,1,3,4], 3)
6
Explanation: The 6 subarrays are [1,2,1,3], [2,1,3], [1,3,4], [2,1,3,4], [1,2,1,3,4], [1,2,1,3].

Optimal Approach:
Use the sliding window technique to count the number of subarrays with at most k distinct integers,
and subtract the count of subarrays with at most (k - 1) distinct integers:

    exactly_k = at_most_k(k) - at_most_k(k - 1)

This avoids brute-force checking of all subarrays and yields optimal performance.

Time Complexity: O(n), where n is the length of the array.
Space Complexity: O(n), for the hash map tracking frequencies of elements.
"""

"""Brute Force
TC : O(n^2)
SC : O(n)"""
from collections import defaultdict


def funct(nums, k):
    count = 0
    n = len(nums)
    for i in range(n):
        mapp = defaultdict(int)
        for j in range(i, n):
            mapp[nums[j]] += 1
            if len(mapp) == k:
                count += 1
            elif len(mapp) > k:
                break

    return count


funct([1, 2, 1, 2, 3], 2)


def SAWKDI(nums, k):
    l, count = 0, 0
    mpp = defaultdict(int)

    for r in range(len(nums)):
        if mpp[nums[r]] == 0:
            k -= 1
        mpp[nums[r]] += 1

        while k < 0:
            mpp[nums[l]] -= 1
            if mpp[nums[l]] == 0:
                k += 1
                del mpp[nums[l]]
            l += 1

        count += r - l + 1
    return count


def helper(nums, k):
    exactly_k = SAWKDI(nums, k) - SAWKDI(nums, k - 1)
    return exactly_k


helper([1, 2, 1, 2, 3], 2)
