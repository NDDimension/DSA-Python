"""
"Find the Kth missing Integer"

=> Given an sorted array we need to find the kth missing integer.

Example:

arr = [2,3,4,7,11]
k = 5

original numbers => 1 2 3 4 5 6 7 8 9 10 11
-> 9 is appearing on 5th number in missing numbers (1,5,6,8,9,10)

Hence answer = 9
"""

# Naive Solution
# TC : O(n)
# SC : O(n)


def kth_missing(arr, k):
    n = len(arr)
    for i in range(n):
        if arr[i] <= k:
            k += 1

        else:
            break

    return k


arr = [2, 3, 4, 7, 11]
k = 5
kth_missing(arr, k)

# Binary Search
# TC : O(logn)
# SC : O(1)


def kth_missing_BS(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)

        if missing < k:
            low = mid + 1

        else:
            high = mid - 1

    return high + 1 + k


arr = [2, 3, 4, 7, 11]
k = 5
kth_missing_BS(arr, k)
