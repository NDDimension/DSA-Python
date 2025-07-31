"""
"Find the First and Last Occuring Index of X"

=> Given an array we need to return the first occurence of it and last occurence of it in pairs of index.

- if element not present return {-1,-1}
- if present one time -> 1st and last index are same.
"""

"""
=> Using Linear Search 

=> Time Complexity: O(n)
=> Space Complexity: O(1)
"""


def FirstLastInd(arr, target):
    n = len(arr)
    first, last = -1, -1

    for i in range(n):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i

    return [first, last]


arr = [2, 4, 6, 8, 8, 8, 11, 13]
target = 14
print(FirstLastInd(arr, target))

"""
=> Using Binary Search : 
    - Lower bound : first occurence
    - Upper bound - 1 : last occurence

=> Time Complexity: O(logn)
=> Space Complexity: O(1)
"""


def lowerBound(arr, target):
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= target:
            high = mid - 1

        else:
            low = mid + 1

    return low


def upperBound(arr, target):
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return high


def FirstLastIndBS(arr, target):
    lb = lowerBound(arr, target)
    if lb == len(arr) or arr[lb] != target:
        return [-1, -1]

    ub = upperBound(arr, target)
    return [lb, ub]


arr = [2, 4, 6, 8, 8, 8, 11, 13]
target = 8
FirstLastIndBS(arr, target)

"""
"Count the occurences of X for first and last time"

=> It is the same concept as first and last occurence question but here we need to apply
    raw binary search two times ; no concept of Lower & Upper bound.

=> Time Complexity : 2O(logn)
=> Space Complexity : O(1)
"""


def countOcc(arr, target):
    n = len(arr)
    lowf, highf = 0, n - 1
    first = 0

    while lowf <= highf:
        midf = (lowf + highf) // 2

        if arr[midf] == target:
            first = midf
            highf = midf - 1

        elif arr[midf] < target:
            lowf = midf + 1

        else:
            highf = midf - 1
    if first == -1:
        return -1

    lowl, highl = 0, n - 1
    last = -1

    while lowl <= highl:
        midl = (lowl + highl) // 2

        if arr[midl] == target:
            last = midl
            lowl = midl + 1

        elif arr[midl] < target:
            lowl = midl + 1

        else:
            highl = midl - 1

    return [first, last]


arr = [2, 4, 6, 8, 8, 8, 8, 8, 11, 13]
target = 14
print(countOcc(arr, target))
