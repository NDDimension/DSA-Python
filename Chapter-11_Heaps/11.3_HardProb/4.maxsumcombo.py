"""
Maximum Sum Combination

Given two integer arrays `nums1` and `nums2`, and an integer `k`,
return the k maximum valid sum combinations from all possible combinations
where each combination is formed by adding one element from `nums1` and one from `nums2`.

A valid sum combination is defined as:
    sum = nums1[i] + nums2[j], for any valid i and j.

Return the k largest such sums in non-increasing order.

Examples:

>>> Solution().maxCombinations([7, 3], [1, 6], 2)
[13, 9]
Explanation:
    7 + 6 = 13
    3 + 6 = 9

>>> Solution().maxCombinations([3, 4, 5], [2, 6, 3], 2)
[11, 10]
Explanation:
    5 + 6 = 11
    4 + 6 = 10

:param nums1: List[int] - First integer array
:param nums2: List[int] - Second integer array
:param k: int - Number of maximum combinations to return
:return: List[int] - k maximum sum combinations in non-increasing order
"""

"""
------------------------------------------------------------------------
Brute Force Approach:
---------------------
1. Generate all possible combinations of nums1[i] + nums2[j].
2. Store all combinations in a list.
3. Sort the list in descending order.
4. Return the first k elements.

Time Complexity: O(n * m * log(n * m)) where n = len(nums1), m = len(nums2)
Space Complexity: O(n * m)
"""


def maxCombinationss(nums1, nums2, k):
    allsums = []
    for a in nums1:
        for b in nums2:
            allsums.append(a + b)
    allsums.sort(reverse=True)
    return allsums[:k]


maxCombinationss([7, 3], [1, 6], 2)

"""
------------------------------------------------------------------------
Optimal Approach (Using Max Heap):
----------------------------------
1. Sort both arrays in descending order.
2. Use a max-heap to always get the next largest possible sum.
3. Track visited index pairs (i, j) to avoid recomputation.
4. At each step, push next two possible pairs: (i+1, j) and (i, j+1).
5. Repeat k times to extract top k sums.

Time Complexity: O(k * log k) (since heap operations are logarithmic and we do this k times)
Space Complexity: O(k + n) for heap and visited set
"""


def maxCombinations(nums1, nums2, k):
    import heapq

    n = len(nums1)
    nums1.sort(reverse=True)
    nums2.sort(reverse=True)

    maxheap = []
    visited = set()

    heapq.heappush(maxheap, (-(nums1[0] + nums2[0]), 0, 0))
    visited.add((0, 0))

    result = []

    while k > 0 and maxheap:
        currsum, i, j = heapq.heappop(maxheap)
        result.append(-currsum)
        k -= 1

        if i + 1 < n and (i + 1, j) not in visited:
            heapq.heappush(maxheap, (-(nums1[i + 1] + nums2[j]), i + 1, j))
            visited.add((i + 1, j))

        if j + 1 < n and (i, j + 1) not in visited:
            heapq.heappush(maxheap, (-(nums1[i] + nums2[j + 1]), i, j + 1))
            visited.add((i, j + 1))
    return result


maxCombinations([7, 3], [1, 6], 2)
