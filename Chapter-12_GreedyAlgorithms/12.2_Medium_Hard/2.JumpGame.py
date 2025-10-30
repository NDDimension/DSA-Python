"""
Problem:
    Jump Game

Description:
    You are given an integer array `nums` where each element `nums[i]`
    represents the maximum jump length you can make from that position.
    Your goal is to determine if you can reach the last index starting from the first index.

Optimal Approach (Greedy Algorithm):
    1. Initialize a variable `max_reach` to 0 — it represents the farthest index
       that can be reached so far.
    2. Iterate through the array:
        - At each index `i`, if `i` is greater than `max_reach`, it means
          you cannot reach this position → return False.
        - Otherwise, update `max_reach = max(max_reach, i + nums[i])`.
    3. If the loop completes, it means all positions are reachable → return True.

    Intuition:
        Always track the farthest point you can reach while moving forward.
        If you ever encounter an index that is beyond this reach, you cannot proceed further.

    Time Complexity: O(N)
    Space Complexity: O(1)

Parameters:
    nums (List[int]): A list of non-negative integers representing the maximum jump length at each position.

Returns:
    bool: True if you can reach the last index, otherwise False.

Example:
    >>> nums = [2, 3, 1, 1, 4]
    >>> can_jump(nums)
    True
    Explanation:
        Start at index 0 → jump 1 step to index 1 (max reach = 4)
        From index 1 → can reach end (index 4)
        Hence, return True.

    >>> nums = [3, 2, 1, 0, 4]
    >>> can_jump(nums)
    False
    Explanation:
        You can reach only up to index 3, but nums[3] = 0 prevents moving further.
        Hence, cannot reach the end.
"""


def canJump(nums):
    max_reach = 0
    n = len(nums)

    for i in range(n):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
    return True


canJump([2, 3, 1, 1, 4])
canJump([3, 2, 1, 0, 4])
