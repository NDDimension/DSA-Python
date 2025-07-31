"""
"Find out how many times the array is rotated"

=> Same logic as finding minimum in sorted rotated array ; just need to return the index this time.
"""


def rotated_time(arr):
    n = len(arr)
    index = -1
    low, high = 0, n - 1
    ans = float("inf")

    while low <= high:
        mid = (low + high) // 2

        if arr[low] <= arr[high]:
            if arr[low] < ans:
                ans = arr[low]
                index = low
            break

        if arr[low] <= arr[mid]:
            if arr[low] < ans:
                index = low
                ans = arr[low]

            low = mid + 1

        else:
            high = mid - 1
            if arr[mid] < ans:
                index = mid
                ans = arr[mid]

    return ans, index


arr = [4, 5, 1, 2, 3]
print(rotated_time(arr))
