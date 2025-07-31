"""
"Count the Subarrays with XOR = k"

=> Given an array we need to return the count of the subarrays having XOR as k

"""

"""
=> Brute Force:

    - Iterate , generate all subarrays and find XORs , keep a counter and return it.

=> Time Complexity ~ O(n^3)
=> Space Complexity ~ O(1)

"""


def CSXORK_brute(arr, target):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            xorr = 0
            for k in range(i, j + 1):
                xorr = xorr ^ arr[k]

            if xorr == target:
                count += 1

    return count


arr = [4, 2, 2, 6, 4]
target = 6
print(CSXORK_brute(arr, target))


"""
=> Better Approach:

    - Using two loops and iteratively doing XOR

=> Time Complexity ~ O(n^2)
=> Space Complexity ~ O(1)

"""


def CSXORK_better(arr, target):
    count = 0
    n = len(arr)

    for i in range(n):
        xorr = 0
        for j in range(i, n):
            xorr = xorr ^ arr[j]
            if xorr == target:
                count += 1

    return count


arr = [4, 2, 2, 6, 4]
target = 6
print(CSXORK_better(arr, target))


"""
=> Optimal Approach:

    -using hashing and backward check

=> Time Complexity ~ O(n)
=> Space Complexity ~ O(n)

"""
from collections import defaultdict


def CSXORK_optimal(arr, target):
    n = len(arr)
    count = 0
    xorr = 0
    mpp = defaultdict(int)
    mpp[xorr] = 1

    for i in range(n):
        xorr = xorr ^ arr[i]
        x = xorr ^ target

        count += mpp[x]
        mpp[xorr] += 1

    return count


arr = [4, 2, 2, 6, 4]
target = 6
print(CSXORK_optimal(arr, target))
