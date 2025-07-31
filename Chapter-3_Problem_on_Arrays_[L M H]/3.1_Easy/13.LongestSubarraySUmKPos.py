"""
"Longest Subarray with Sum Equals to K"

=> Sub-Array -> A contiguous segment of an array

=> Brute Force :

    - Generate all possible sub-arrays
    - Check if sum equals K

=> Time Complexity => O(n^3) or O(n^2)
=> Space Complexity => O(1)

=> Better Approach:

    - Create a hashmap to store sum of sub-arrays ending at each index
    - For each sub-array, check if sum - K exists in hashmap
    - Use prefix sum array to find sum of sub-array from 0 to i

=> Time Complexity => O(n)
=> Space Complexity => O(n)

=> Optimal Approach:

    - Two pointers , move add , if increase trim from left

=> Time Complexity => O(2n)
=> Space Complexity => O(1)
"""


def longestSubarrayBrute(nums, k):
    max_length = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            summ = 0
            for g in range(i, j + 1):
                summ += nums[g]

            if summ == k:
                max_length = max(max_length, j - i + 1)

    return max_length


# Now to optimize the above code we can do :
def longestSubarrayBruteOpt(nums, k):
    max_length = 0
    for i in range(len(nums)):
        summ = 0
        for j in range(i, len(nums)):
            summ += nums[j]

            if summ == k:
                max_length = max(max_length, j - i + 1)

    return max_length


# Optimal for containing pos + neg numbers
def longestSubarrayBetter(nums, k):
    prefix_sum = 0
    prefix_map = {0: -1}
    max_length = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum - k in prefix_map:
            max_length = max(max_length, i - prefix_map[prefix_sum - k])

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_length


def longestSubarrayOpt(nums, k):
    left, right = 0
    summ = nums[0]
    max_length = 0

    while right < len(nums):
        while left <= right and summ > k:
            summ -= nums[left]
            left += 1

        if summ == k:
            max_length = max(max_length, right - left + 1)

        right += 1
        if right < len(nums):
            summ += nums[right]

    return max_length


arr = [1, 2, 3, 1, 1, 1, 1]
k = 3
print(longestSubarrayBetter(arr, k))
