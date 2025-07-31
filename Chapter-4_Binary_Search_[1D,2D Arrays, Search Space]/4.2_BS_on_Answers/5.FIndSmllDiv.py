"""
"Find the Smallest Divisor given a Threshold"

=> Given an array and a threshold, we need to return the smallest divisor ;
    which on dividing by the array elements giving ceil values and upon summing those
    values we must get number <= thresold.

Example:

arr = [1,2,5,9]
threshold = 6

divisor = 5
(1/5 + 2/5 + 3/5 + 9/5) <= 6
"""

import math

# Brute Force:
# TC : O(max x N)
# SC : O(1)


def smallestDivisor(arr, threshold):
    for divisor in range(1, max(arr) + 1):
        summ = 0
        for j in range(len(arr)):
            summ += math.ceil(arr[j] / divisor)

        if summ <= threshold:
            return divisor

    return -1


arr = [1, 2, 5, 9]
threshold = 6
print(smallestDivisor(arr, threshold))


# Binary Search
# TC : O(log(max) x N)
# SC : O(1)


def smallestDivisor_BS(arr, threshold):
    low = 1
    high = max(arr)

    while low <= high:
        mid = (low + high) // 2
        summ = 0

        for j in range(len(arr)):
            summ += math.ceil(float(arr[j]) / mid)

        if summ <= threshold:
            high = mid - 1
        else:
            low = mid + 1

    return low


arr = [1, 2, 5, 9]
threshold = 6
print(smallestDivisor_BS(arr, threshold))
