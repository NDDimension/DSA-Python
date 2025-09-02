"""
"Power Set"

=> Given an array we need to return all the subsets of it.

=> TC : O(N x 2^n)
=> SC : O(2^n x N )
"""


def PowerSet(nums):
    n = len(nums)
    results = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(nums[j])
        results.append(subset)
    return results


PowerSet([1, 2, 3])
