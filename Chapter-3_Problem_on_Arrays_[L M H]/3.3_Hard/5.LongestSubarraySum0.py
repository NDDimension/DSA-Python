"""
"Largest Sub-Array with sum = 0"

=> Given an array we need to return the sub-array which is largest and sums upto 0.

"""

"""
=> Brute Force:

    - Using two loop and generating all sub-arrays.

=> Time Complexity : O(n^2)
=> Space Complexity : O(1)

"""


def largestSubArrayBrute(arr):
    n = len(arr)
    maxx = 0

    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += arr[j]
            if summ == 0:
                maxx = max(maxx, j - i + 1)

    return maxx


arr = [9, -3, 3, -1, 6, -5]
print(largestSubArrayBrute(arr))

"""
=> Optimal Approach:

    - using prefix sum method

=> Time Complexity : O(n)
=> Space Complexity : O(n)


"""


def largestSubArrayOptimal(arr):
    mpp = {}
    maxi = 0
    summ = 0
    n = len(arr)

    for i in range(n):
        summ += arr[i]
        if summ == 0:
            maxi = i + 1

        else:
            if summ in mpp:
                maxi = max(maxi, i - mpp[summ])

            else:
                mpp[summ] = i

    return maxi


arr = [9, -3, 3, -1, 6, -5]
print(largestSubArrayOptimal(arr))
