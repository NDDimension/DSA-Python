"""
"Count the occurences of X for first and last time"

=> It is the same concept as first and last occurence question but here we need to apply
    raw binary search two times ; no concept of Lower & Upper bound.

=> Count how many time X occurs.

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

    return last - first + 1


arr = [2, 4, 6, 8, 8, 8, 8, 8, 11, 13]
target = 14
print(countOcc(arr, target))
