"""
Problem:
    Given an array of non-negative integers `nums`, where each element represents
    your maximum jump length from that position, return the minimum number of
    jumps required to reach the last index.

Optimal Approach (Greedy):
    - We iterate through the array while keeping track of:
        1. `farthest`: the farthest index that can be reached from the current range.
        2. `current_end`: the end of the current range (i.e., the farthest point
           reachable using the current number of jumps).
        3. `jumps`: the number of jumps made so far.

    - When the current index `i` reaches `current_end`, it means we’ve exhausted
      all possible jumps for the current range, so we increment `jumps` and
      update `current_end` to `farthest`.

    - This ensures we make the fewest number of jumps while covering as much
      distance as possible in each jump.

Time Complexity:
    O(n) — We traverse the array once.

Space Complexity:
    O(1) — We only use a few variables for tracking state.

Example:
    >>> jump([2, 3, 1, 1, 4])
    2
    Explanation:
        - Jump 1: from index 0 → index 1 (covering up to index 2)
        - Jump 2: from index 1 → index 4 (reaches the end)

    >>> jump([2, 3, 0, 1, 4])
    2
    Explanation:
        - Jump 1: from index 0 → index 1 (farthest = index 3)
        - Jump 2: from index 1 → index 4 (reaches the end)
"""


# Recursive Approach
# TC : O(n^n)
# SC : O(n)
def jumpRec(idx, arr, n, dp):
    """
    Recursive approach with memoization for Jump Game II.
    Returns the minimum number of jumps to reach the end.
    """
    if idx >= n - 1:
        return 0  # no more jumps needed

    if dp[idx] != -1:
        return dp[idx]

    mini = float("inf")
    for i in range(1, arr[idx] + 1):
        if idx + i < n:
            mini = min(mini, 1 + jumpRec(idx + i, arr, n, dp))

    dp[idx] = mini
    return dp[idx]


# Example usage
nums = [2, 3, 0, 1, 4]
n = len(nums)
dp = [-1] * n
print(jumpRec(0, nums, n, dp))  # Output: 2


def jump(nums):
    jumps = 0
    farthest = 0
    current_end = 0

    for i in range(len(nums) - 1):  # No need to jump from the last index
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps


# TC : O(n)
# SC : O(1)
def function(nums):
    jumps = 0
    l = r = 0
    n = len(nums)
    while r < n - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        jumps += 1
    return jumps


function([2, 3, 0, 1, 4])
