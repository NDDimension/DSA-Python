"""
"Next Greater Number [Monotonic Stack]"

=> When elements are stored in particular fashion in stack then its a Monotonic Stack.
"""

"""
LeetCode Problem: Next Greater Element

Description:
Given an array `nums`, for each element, find the next greater element to its right.
If there is no next greater element, output -1 for that position.

The Next Greater Element for an element x is the first greater element on the right side of x in the array.
If no such element exists, output -1.

Variants:
- Next Greater Element I: Given two arrays where one is a subset of the other.
- Next Greater Element II: The array is circular; the search continues from the beginning after reaching the end.

Function Signature:
    def nextGreaterElements(nums: List[int]) -> List[int]:

Parameters:
    nums (List[int]): A list of integers.

Returns:
    List[int]: A list where each element corresponds to the next greater number of the input element, or -1 if it does not exist.

Constraints:
    - 1 <= len(nums) <= 10^4
    - -10^9 <= nums[i] <= 10^9

Example:
    Input: nums = [2, 1, 2, 4, 3]
    Output: [4, 2, 4, -1, -1]

Approach:
    A monotonic decreasing stack is used to keep track of indices of elements for which the next greater element hasn't been found yet.
    We iterate through the array and update the result array whenever a next greater element is found.
"""
# Basic Approach
"""
TC : O(n^2)
SC : O(n)
"""


def NGE(arr):
    nge = [-1] * len(arr)

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                nge[i] = arr[j]
                break

    return nge


NGE([2, 1, 2, 4, 3])


# Monotonic Stack Approach
# TC : O(2n)
# SC : O(n) + O(n)
def nge(arr):
    nge = [-1] * len(arr)
    stack = []

    for i in range(len(arr) - 1, -1, -1):  # iterate from end to start
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            nge[i] = stack[-1]

        # If stack is empty, nge[i] is already -1 (from initialization)
        stack.append(arr[i])

    return nge


# Test
print(nge([2, 1, 2, 4, 3]))  # Output: [4, 2, 4, -1, -1]
