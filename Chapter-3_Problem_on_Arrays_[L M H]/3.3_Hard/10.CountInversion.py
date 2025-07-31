"""
"Count the Inversion Pairs"

=> Given an array find all the inversion pairs
    where i < j and arr[i] > arr[j]
"""

"""
=> Brute Force:
    - Iterate and find all pairs

=> Time Complexity: O(n^2)
=> Space Complexity: O(1)    
"""


def countInversion(arr):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1

    return count


arr = [5, 4, 3, 2, 1]
countInversion(arr)

"""
=> Optimal Approach:
    - using merge sort algo + adding inversion logic while merging
    
=> Time Complexity: O(nlogn)
=> Space Complexity: O(n)    
"""
import math


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    count = 0

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1

        else:
            temp.append(arr[right])
            count += mid - left + 1
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return count


def mergeSort(arr, low, high):
    count = 0
    if low >= high:
        return count

    mid = math.floor((low + high) / 2)
    count += mergeSort(arr, low, mid)
    count += mergeSort(arr, mid + 1, high)
    count += merge(arr, low, mid, high)

    return count


def countInversionOptimal(arr):
    n = len(arr)
    return mergeSort(arr, 0, n - 1)


arr = [5, 4, 3, 2, 1]
countInversionOptimal(arr)
