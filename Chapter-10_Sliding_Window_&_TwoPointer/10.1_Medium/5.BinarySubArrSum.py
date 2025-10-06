"""
Binary SubArray with Sum

Given a binary array nums and an integer goal, return the number of non-empty subarrays
with a sum equal to goal.

A subarray is a contiguous part of the array.

Approach:
    - Use prefix sum and a hashmap to count the number of times a certain sum occurs.
    - For each prefix sum `curr_sum`, if there exists a previous prefix sum `curr_sum - goal`,
      then there is a subarray ending at the current index with the required sum.
    - We maintain a hashmap `prefix_counts` where key is the prefix sum and value is the count
      of times this sum has occurred.

Time Complexity: O(n), where n is the length of nums.
Space Complexity: O(n), due to the hashmap.

Args:
    nums (List[int]): Binary array of integers (0 or 1).
    goal (int): The desired subarray sum.

Returns:
    int: The number of non-empty subarrays with sum equal to goal.

Example:
    >>> sol = Solution()
    >>> sol.numSubarraysWithSum([1,0,1,0,1], 2)
    4
    # The 4 subarrays are:
    # [1,0,1], [0,1,0,1], [1,0,1], and [1,0,1]
"""


def atMost(nums, k):
    if k < 0:
        return 0

    l = 0
    summ = 0
    count = 0

    for r in range(len(nums)):
        summ += nums[r]

        while summ > k:
            summ -= nums[l]
            l += 1

        count += r - l + 1

    return count


def numSubarraysWithSum(nums, goal):
    """
    Uses the sliding window approach to count the number of subarrays with sum exactly equal to goal.
    This is done by calculating the difference between:
    - Number of subarrays with sum at most goal
    - Number of subarrays with sum at most (goal - 1)

    Time: O(n)
    Space: O(1)
    """
    return atMost(nums, goal) - atMost(nums, goal - 1)


numSubarraysWithSum([1, 0, 1, 0, 1], 2)
