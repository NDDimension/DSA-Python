"""
"Reverse Pairs in an array"

=> Given an array give the count of the total reverse pairs i.e.
    i < j and arr[i] > 2 * arr[j]
"""

"""
=> Brute Force:
    - Iterate and generate all pairs verify with the conditions.
    
=> Time Complexity : O(n^2)
=> Space Complexity : O(1)
"""


def reverse_pairs(arr):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j] * 2:
                count += 1

    return count


arr = [4, 1, 2, 3, 1]
print(reverse_pairs(arr))

"""
=> Optimal Approach:
    - using merge sort + count inversion logic with little tweak before 
       merge step

=> Time Complexity : O(2nlogn)
=> Space Complexity : O(n) [ with distortion of given input array ]
       
"""


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= right and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1

        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def reversePairsOptimal(arr, low, mid, high):
    right = mid + 1
    count = 0

    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1

        count += right - (mid + 1)

    return count


def mergeSort(arr, low, high):
    count = 0
    if low >= high:
        return count

    mid = (low + high) // 2
    count += mergeSort(arr, low, mid)
    count += mergeSort(arr, mid + 1, high)
    count += reversePairsOptimal(arr, low, mid, high)
    merge(arr, low, mid, high)

    return count


arr = [4, 1, 2, 3, 1]
reversePairsOptimal(arr, 0, len(arr) - 1, len(arr) - 1)
print(mergeSort(arr, 0, len(arr) - 1))
