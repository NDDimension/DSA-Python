"""
"Find the Minimum element in the Rotated Sorted Array"

=> Given a rotated sorted array we need to return the element which is minimum.

- Using the logic of eliminating either right or left we can achieve this
- as the point of rotation might be holding the minimum element.

Trick here is ? -> We look for the sorted half and find its minimum until the search space is exhausted.

=> Time Complexity : O(logn)
=> Space Complexity : O(1)
"""


def find_min(arr):
    n = len(arr)

    low, high = 0, n - 1
    ans = float("inf")

    while low <= high:
        mid = (low + high) // 2

        if arr[low] <= arr[high]:
            ans = min(ans, arr[low])
            break

        if arr[low] <= arr[mid]:
            ans = min(ans, arr[low])
            low = mid + 1

        else:
            ans = min(ans, arr[mid])
            high = mid - 1

    return ans


arr = [4, 5, 1, 2, 3]
find_min(arr)
