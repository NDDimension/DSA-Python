"""
Sliding Window Maximum

Given an integer array `nums`, there is a sliding window of size `k` which
moves from the very left to the very right. You can only see the `k` numbers
in the window. Each time the sliding window moves right by one position.

Return a list of the maximum value in each window.

Args:
    nums (List[int]): List of integers.
    k (int): Size of the sliding window.

Returns:
    List[int]: The maximum value in each sliding window.

Example:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation:
        Window position                Max
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
         1 [3  -1  -3] 5  3  6  7       3
         1  3 [-1  -3  5] 3  6  7       5
         1  3  -1 [-3  5  3] 6  7       5
         1  3  -1  -3 [5  3  6] 7       6
         1  3  -1  -3  5 [3  6  7]      7

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - 1 <= k <= nums.length

Optimal Approach:
    Use a deque (double-ended queue) to store indices of elements. The deque
    is maintained such that:
        1. The front of the deque is always the index of the maximum value
           in the current window.
        2. Elements smaller than the current number are removed from the back
           since they can't be the max as long as the current element is in
           the window.
        3. Remove elements from the front if they are out of the current window.

Time Complexity:
    O(n) - Each element is pushed and popped from the deque at most once.

Space Complexity:
    O(k) - For the deque used to store indices.
"""

"""Brute Force
TC : O(n-k) x O(k)
SC : O(n - k)"""


def SWM(nums, k):
    lst = []
    for i in range(len(nums) - k + 1):
        maxi = nums[i]
        for j in range(i, i + k):
            maxi = max(maxi, nums[j])
        lst.append(maxi)

    return lst


SWM([1, 3, -1, -3, 5, 3, 6, 7], 3)

"""Optimal Approach
TC : O(2n)
SC : O(n - k) + O(k) """
from collections import deque


def SWMM(nums, k):
    if not nums or k == 0:
        return []

    dq = deque()
    res = []

    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            res.append(nums[dq[0]])

    return res


SWMM([1, 3, -1, -3, 5, 3, 6, 7], 3)
