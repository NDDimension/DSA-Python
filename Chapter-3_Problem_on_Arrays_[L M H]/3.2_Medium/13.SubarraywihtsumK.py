"""
"Number of Sub-arrays with sum = K"

=> Given an array we need to return the number of subarrays whose sum = k

=> Brute Force:

    - Generate all subarray and check the sum and return the count

=> Time Complexity: O(n^3)
=> Space Complexity: O(1)

=> Better Approach:

    - Iterate and remove the third loop
    - Accumulate the sum going through the loop

=> Time Complexity: O(n^2)
=> Space Complexity: O(1)


=> Optimal Approach ;

    - Using prefix sum

=> Time Complexity: O(n)
=> Space Complexity: O(n)

"""


def subarray_sumBrute(arr, k):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            summ = 0
            for k in range(i, j + 1):
                summ += arr[k]

            if summ == k:
                count += 1

    return count


def subarray_sumBetter(arr, k):
    count = 0
    n = len(arr)

    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += arr[j]
            if summ == k:
                count += 1

    return count


from collections import defaultdict


def subarray_sumOptimal(arr, k):
    n = len(arr)
    mpp = defaultdict(int)
    prsum, count = 0, 0

    mpp[0] = 1

    for i in range(n):
        prsum += arr[i]
        remove = prsum - k
        count += mpp[remove]
        mpp[prsum] += 1

    return count


arr = [3, 1, 2, 4]
k = 6

print(subarray_sumOptimal(arr, k))
