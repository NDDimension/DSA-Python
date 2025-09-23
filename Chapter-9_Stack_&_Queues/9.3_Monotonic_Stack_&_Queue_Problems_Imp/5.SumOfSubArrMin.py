"""
Sum Of the Subarray Minimums

Given an array of integers, return the sum of the minimum values of all subarrays of the given array.

A subarray is a contiguous part of an array.

Approach:
- A brute force solution would be to compute the minimum for every possible subarray, but this would be inefficient (O(n^2) time complexity).
- We can solve this problem more efficiently using a stack-based approach with a monotonic stack.
- For each element, we need to calculate how many subarrays it is the minimum for.
- The total sum can then be computed by considering each element's contribution to the sum as the minimum of some subarrays.
- This can be done in O(n) time by iterating over the array and using the stack to keep track of the indices of elements.

Example 1:
Input: arr = [3, 1, 2, 4]
Output: 17
Explanation: The subarray minimums are:
[3], [1], [2], [4], [3, 1], [1, 2], [2, 4], [3, 1, 2], [1, 2, 4], [3, 1, 2, 4]
Their sum is 17.

Example 2:
Input: arr = [11, 81, 94, 43, 3]
Output: 444
Explanation: The subarray minimums are:
[11], [81], [94], [43], [3], [11, 81], [81, 94], [94, 43], [43, 3], [11, 81, 94], [81, 94, 43], [94, 43, 3], [11, 81, 94, 43], [81, 94, 43, 3], [11, 81, 94, 43, 3]
Their sum is 444.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^9
"""

"""Brute Force
TC : O(n^2)
SC : O(1)"""


def SOSM(arr):
    summ = 0
    mod = 1e9 + 7
    for i in range(len(arr)):
        mini = arr[i]
        for j in range(i, len(arr)):
            mini = min(mini, arr[j])
            summ = (summ + mini) % mod

    return summ


SOSM([3, 1, 2, 4])

"""Optimal Approach
TC : O(5n)
SC : O(5n)"""


def findNSE(arr):
    n = len(arr)
    nse = [n] * n
    st = []
    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        if st:
            nse[i] = st[-1]
        st.append(i)
    return nse


def findPSE(arr):
    pse = [-1] * len(arr)
    st = []
    for i in range(len(arr)):
        while st and arr[st[-1]] > arr[i]:
            st.pop()
        if st:
            pse[i] = st[-1]
        st.append(i)
    return pse


def SOSMOpt(arr):
    n = len(arr)
    nse = findNSE(arr)
    pse = findPSE(arr)
    total = 0
    mod = int(1e9 + 7)

    for i in range(n):
        left = i - pse[i]
        right = nse[i] - i
        total = (total + (arr[i] * left * right) % mod) % mod

    return total


SOSMOpt([3, 1, 2, 4])
