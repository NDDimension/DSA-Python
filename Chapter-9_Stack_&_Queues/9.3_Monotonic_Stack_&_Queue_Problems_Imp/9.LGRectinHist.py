"""
Given a list of integers representing the heights of bars in a histogram,
return the area of the largest rectangle that can be formed within the bounds
of the histogram.

The width of each bar is 1.

Parameters:
heights (List[int]): A list of non-negative integers representing the heights of histogram bars.

Returns:
int: The area of the largest rectangle that can be formed in the histogram.

Constraints:
- 1 <= len(heights) <= 10^5
- 0 <= heights[i] <= 10^4

Example:
--------
>>> largestRectangleArea([2,1,5,6,2,3])
10
Explanation: The largest rectangle has area 10 (between indices 2 and 3, heights 5 and 6).

>>> largestRectangleArea([2,4])
4

Optimal Approach:
-----------------
Use a stack to maintain indices of increasing bar heights. For each bar, pop from the stack
until the bar at the top of the stack is less than the current one. For each popped bar,
calculate the area with it as the smallest height. This ensures all rectangles are checked
in O(n) time using a monotonic stack.
"""

"""Brute Force
-> TC : 2 x O(2n) + O(n)
-> SC : O(2n) + O(2n) """


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


def LRAIH(arr):
    nse = findNSE(arr)
    pse = findPSE(arr)
    maxi = 0
    for i in range(len(arr)):
        maxi = max(maxi, (arr[i] * (nse[i] - pse[i] - 1)))
    return maxi


LRAIH([2, 1, 5, 6, 2, 3])

"""Optimal Approach
TC : O(2n)
SC : O(n)"""


def LAIH(arr):
    st = []
    maxArea = 0
    for i in range(len(arr)):
        while st and arr[st[-1]] > arr[i]:
            ele = st[-1]
            st.pop()
            nse = i
            if st:
                pse = st[-1]
            else:
                pse = -1

            maxArea = max(maxArea, arr[ele] * (nse - pse - 1))
        st.append(i)

    while st:
        nse = len(arr)
        ele = st[-1]
        st.pop()
        if st:
            pse = st[-1]
        else:
            pse = -1

        maxArea = max(maxArea, (nse - pse - 1) * arr[ele])
    return maxArea


LAIH([2, 1, 5, 6, 2, 3])
