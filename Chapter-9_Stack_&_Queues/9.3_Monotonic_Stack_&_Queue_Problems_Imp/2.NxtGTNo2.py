"""
Problem:
Next Greater Element II

Given a circular array (the next element of the last element is the first element of the array),
return the next greater number for every element. The next greater number of a number x is the first
greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number.
If it doesn't exist, return -1 for this number.

Example:
Input: nums = [1,2,1]
Output: [2,-1,2]

Explanation:
    The first 1's next greater number is 2;
    The number 2 does not have a next greater number;
    The second 1's next greater number needs to wrap around and is 2.

Constraints:
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9

Approach:
- Use a monotonic decreasing stack to track indices of elements.
- Traverse the array twice (simulate circular behavior using modulo).
- For each element, pop from stack until a greater element is found.
- Store the result in a separate array initialized with -1.
- Time Complexity: O(n), where n is the length of the array.
"""


# Circular Array
# TC : O(n^2)
# SC : O(n)
def nge2(arr):
    nge = [-1] * len(arr)
    for i in range(len(arr)):
        for j in range(i + 1, i + len(arr)):
            ind = j % len(arr)
            if arr[ind] > arr[i]:
                nge[i] = arr[ind]
                break
    return nge


nge2([1, 2, 1])


# Monotonic Stack
# TC : O(4n)
# SC : O(2n) + O(n)
def nge2(arr):
    n = len(arr)
    nge = [-1] * n
    st = []

    for i in range(2 * n - 1, -1, -1):
        curr = arr[i % n]

        # Pop elements that are less than or equal to current
        while st and arr[st[-1]] <= curr:
            st.pop()

        if i < n:
            if st:
                nge[i] = arr[st[-1]]

        # Push current index
        st.append(i % n)

    return nge
