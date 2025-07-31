"""
"Find the Missing Number from the array"

=> Brute Force:

    - Iterate from 1 to n
    - Check if number exists in array

=> Time Complexity => O(n^2)  [Hypothetical situation]
=> Space Complexity => O(1)

=> Better Approach:

    - Iterate from 1 to n and create hashmap
    - Iterate over hasmap check for 0

=> Time Complexity => O(2n)
=> Space Complexity => O(n)

=> Optimal Approach:

    - Use XOR operation to find missing number
    - Sum all 1 to n - Sum of array

=> Time Complexity => O(n)
=> Space Complexity => O(1)
"""


def MissingBrute(arr):
    for i in range(1, len(arr) + 1):
        flag = 0
        for j in range(len(arr)):
            if arr[j] == i:
                flag = 1
                break

        if flag == 0:
            return i


from collections import Counter


def MissingBetter(arr):
    hasmap = Counter(arr)
    for i in range(1, len(arr) + 1):
        if hasmap[i] == 0:
            return i


def MissingOptSum(arr, n):
    originalsum = (n * (n + 1)) // 2
    return originalsum - sum(arr)


from functools import reduce
import operator


def MissingOptXOR(arr, n):
    return reduce(operator.xor, arr + list(range(1, n + 1)))


n = 7
arr = [1, 2, 4, 5, 6, 7]
print(f"{MissingOptXOR(arr, n)} is missing")
