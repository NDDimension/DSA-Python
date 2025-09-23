"""
Trapping Rainwater

Given n non-negative integers representing the height of walls at each index,
where the width of each wall is 1, compute how much water it can trap after raining.

The problem asks to calculate the total amount of water trapped between the walls.

Approach:
- We can solve this problem optimally using two pointers.
- Use two pointers, `left` and `right`, initialized at the beginning and end of the array.
- Maintain two variables, `left_max` and `right_max`, to store the maximum height encountered from both directions.
- At each step, move the pointer that points to the smaller height. Calculate the trapped water based on the height difference between the current pointer position and the respective maximum height.
- This ensures that we traverse the array once, resulting in O(n) time complexity and O(1) space complexity.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The trapped water is represented by the following diagram:
[0,1,0,2,1,0,1,3,2,1,2,1]
There are 6 units of water trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
Explanation: The trapped water is represented by the following diagram:
[4,2,0,3,2,5]
There are 9 units of water trapped.

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""


# TC : O(2n) + O(n)
# SC : O(2n)
def prefixMax(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(len(arr)):
        prefix[i] = max(prefix[i - 1], arr[i])
    return prefix


def suffixMax(arr):
    suffix = [0] * len(arr)
    suffix[len(arr) - 1] = arr[len(arr) - 1]
    for i in range(len(arr) - 2, -1, -1):
        suffix[i] = max(suffix[i + 1], arr[i])
    return suffix


def TrappingWater(arr):
    if not arr:
        return 0  # No water can be trapped if the array is empty

    prefix = prefixMax(arr)  # Get the prefix max array
    suffix = suffixMax(arr)  # Get the suffix max array
    total = 0

    for i in range(len(arr)):
        # Water trapped at position i = min(prefix[i], suffix[i]) - arr[i]
        total += min(prefix[i], suffix[i]) - arr[i]

    return total


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(TrappingWater(arr))  # Output: 6


# Two pointer
# TC : O(n)
# SC : O(1)
def TrapWater(arr):
    n = len(arr)
    lmax = rmax = total = 0
    l, r = 0, (n - 1)

    while l < r:
        if arr[l] <= arr[r]:
            if lmax > arr[l]:
                total += lmax - arr[l]
            else:
                lmax = arr[l]
            l += 1
        else:
            if rmax > arr[r]:
                total += rmax - arr[r]
            else:
                rmax = arr[r]
            r -= 1
    return total


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(TrapWater(arr))
