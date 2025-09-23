"""
"Next Smaller Number"

=> Opposite of Next Greater Number
"""


def nge(arr):
    nge = [-1] * len(arr)
    stack = []

    for i in range(len(arr) - 1, -1, -1):  # iterate from end to start
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            nge[i] = stack[-1]

        # If stack is empty, nge[i] is already -1 (from initialization)
        stack.append(arr[i])

    return nge


nge([10, 9, 8, 7])
