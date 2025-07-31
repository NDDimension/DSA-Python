"""
"Maximum Subarray Sum"

=> Brute Force :
    - Generate all possible sub-arrays
    - Check if sum equals K
    - Keep track of maximum sum
    - Return maximum sum

=> Time Complexity => O(n^3)
=> Space Complexity => O(1)

=> Better Approach:

    - Two loops and done the same as brute force

=> Time Complexity => O(n^2)
=> Space Complexity => O(1)

=> Opitmal Approach:

    - Using Kadane's Algorithm
    - take max ~ -infinity and sum == first element
    - sum gets carried if +ve else will be 0 and also max is updated

=> Time Complexity => O(n)
=> Space Complexity => O(1)
"""


def maxSubArraySum(arr):
    maxi = float("-inf")

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            summ = 0
            for k in range(i, j + 1):
                summ += arr[k]

            maxi = max(maxi, summ)

    return maxi


def maxSubArraySumBetter(arr):
    maxi = float("-inf")

    for i in range(len(arr)):
        summ = 0
        for j in range(i, len(arr)):
            summ += arr[j]
            maxi = max(maxi, summ)

    return maxi


def maxSubArraySumKadane(arr):
    maxi = float("-inf")
    summ = 0

    start = 0
    ansStart, ansEnd = -1, -1  # fixed typo here

    for i in range(len(arr)):
        if summ == 0:
            start = i

        summ += arr[i]

        if summ > maxi:
            maxi = summ
            ansStart, ansEnd = start, i

        if summ < 0:
            summ = 0

    if maxi < 0:
        print("No positive subarray found.")
        return 0

    print("Maximum subarray:", arr[ansStart : ansEnd + 1])  # cleaner subarray output
    return maxi


# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum sum:", maxSubArraySumKadane(arr))
