"""
Countthe Number of Nice Sub Arrays

Given an array of integers nums and an integer k, return the number of "nice" subarrays.

A "nice" subarray is defined as a contiguous subarray containing exactly k odd numbers.

Approach:
    - Transform the problem into a binary array where 1 represents an odd number and 0 an even number.
    - Then, use the sliding window technique to count the number of subarrays with exactly k 1s.
    - This is equivalent to the classic "number of subarrays with sum equal to k" problem.
    - We use the formula:
        Exact(k) = AtMost(k) - AtMost(k - 1)

Time Complexity: O(n), where n is the length of nums.
Space Complexity: O(1), ignoring the input/output size.

Args:
    nums (List[int]): The input array of integers.
    k (int): The exact number of odd numbers required in the subarray.

Returns:
    int: The number of nice subarrays with exactly k odd numbers.

Example:
    >>> sol = Solution()
    >>> sol.numberOfSubarrays([1,1,2,1,1], 3)
    2
    # The two nice subarrays are:
    # [1,1,2,1], [1,2,1,1]
"""


def atMost(nums, k):
    if k < 0:
        return 0

    l = 0
    summ = 0
    count = 0

    for r in range(len(nums)):
        summ += nums[r] % 2

        while summ > k:
            summ -= nums[l] % 2
            l += 1

        count += r - l + 1

    return count


def CNNSA(nums, goal):
    return atMost(nums, goal) - atMost(nums, goal - 1)


CNNSA([1, 1, 2, 1, 1], 3)
