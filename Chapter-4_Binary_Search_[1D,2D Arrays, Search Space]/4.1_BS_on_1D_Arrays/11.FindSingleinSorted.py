"""
"Find the element which is single in sorted array"

=> Given a sorted array we need to find out the element that occurs only once.

Example :
arr = [1, 1, 2, 3, 3, 4, 4]

Ans -> 2
"""

"""
=> Naive Approach using Linear Search.
"""


def linear_single(arr):
    n = len(arr)
    if n == 1:
        return arr[0]

    else:
        for i in range(n):
            if i == 0:
                if arr[i] != arr[i + 1]:
                    return arr[i]

            elif i == n - 1:
                if arr[i] != arr[i - 1]:
                    return arr[i]

            else:
                if arr[i] != arr[i + 1] and arr[i] != arr[i - 1]:
                    return arr[i]


arr = [1, 1, 2, 3, 3, 4, 4]
linear_single(arr)

"""
=> Using Binary Search.

- Mid will help us find it :
    if mid encounters (even , odd) index pair and same elements then eliminate right half
    if mid encounters (odd, even) index pair and different elements then eliminate left half
    
=> Time Complexity : O(log n)
=> Space Complexity : O(1)    
"""


def binary_single(arr):
    n = len(arr)
    if n == 1:
        return arr[0]

    if arr[0] != arr[1]:
        return arr[0]

    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]

    low = 1
    high = n - 2

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]

        # Left half
        if (mid % 2 == 1 and arr[mid - 1] == arr[mid]) or (
            mid % 2 == 0 and arr[mid] == arr[mid + 1]
        ):
            # eliminate left half
            low = mid + 1

        else:
            # eliminate right half
            high = mid - 1

    return -1


arr = [1, 1, 2, 3, 3, 4, 4]
binary_single(arr)
