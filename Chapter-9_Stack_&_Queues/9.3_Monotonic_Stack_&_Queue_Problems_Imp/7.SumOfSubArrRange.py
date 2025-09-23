"""
Calculates the sum of ranges of all subarrays in the input array.

The range of a subarray is defined as the difference between the maximum and minimum elements in the subarray.
The function returns the sum of all such ranges for every possible subarray of the input array.

Approach:
- Brute force would involve checking all subarrays and calculating min and max for each, which takes O(n^2) time.
- The optimal approach uses monotonic stacks to compute the contribution of each element as:
    - How many subarrays it is the minimum in.
    - How many subarrays it is the maximum in.
- For each element:
    - Calculate its total contribution to all subarrays where it is the maximum.
    - Subtract its total contribution to all subarrays where it is the minimum.
- This gives us the total sum of subarray ranges in O(n) time.

Time Complexity:
- O(n), where n is the length of the input array, using monotonic stacks for both min and max passes.

Space Complexity:
- O(n), for the stacks used in the computation.

Parameters:
nums (List[int]): The input array of integers.

Returns:
int: The sum of ranges of all subarrays.

Example:
Input:
nums = [1, 2, 3]

Output:
4

Explanation:
- Subarrays: [1], [2], [3], [1,2], [2,3], [1,2,3]
- Ranges:     0    0    0     1      1      2
- Sum = 0 + 0 + 0 + 1 + 1 + 2 = 4
"""

"""Brute Force
TC : O(n^2)
SC : O(1)"""


def SOSAR(arr):
    summ = 0
    n = len(arr)
    for i in range(n):
        l, s = arr[i], arr[i]
        for j in range(i + 1, n):
            l, s = max(l, arr[j]), min(s, arr[j])
            summ = summ + (l - s)

    return summ


SOSAR([1, 2, 3])

"""Optimal Approach
TC : O(n)
SC : O(n)"""
"""Optimal Approach
TC : O(n)
SC : O(n)
"""


def findNSG(arr):
    n = len(arr)
    nsg = [n] * n
    st = []
    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] <= arr[i]:
            st.pop()
        if st:
            nsg[i] = st[-1]
        st.append(i)
    return nsg


def findPSG(arr):
    psg = [-1] * len(arr)
    st = []
    for i in range(len(arr)):
        while st and arr[st[-1]] < arr[i]:
            st.pop()
        if st:
            psg[i] = st[-1]
        st.append(i)
    return psg


def sumMAX(arr):
    n = len(arr)
    nsg = findNSG(arr)
    psg = findPSG(arr)
    total = 0
    mod = int(1e9 + 7)

    for i in range(n):
        left = i - psg[i]
        right = nsg[i] - i
        total = (total + (arr[i] * left * right) % mod) % mod

    return total


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


def sumMIN(arr):
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


def SOSARopt(arr):
    return sumMAX(arr) - sumMIN(arr)


SOSARopt([1, 2, 3])
