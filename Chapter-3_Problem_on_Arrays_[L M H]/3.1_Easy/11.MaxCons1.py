"""
"Maximum Consecutive Ones"

=> Time Complexity: O(n)
=> Space Complexity: O(1) [no extra space]

"""


def max_consecutive_ones(nums):
    count = 0
    max_count = 0

    for num in nums:
        count = count + 1 if num == 1 else 0
        max_count = max(max_count, count)

    return max_count


from itertools import groupby


def max_consecutive_ones(nums):
    return max((len(list(g)) for k, g in groupby(nums) if k == 1), default=0)


nums = [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
print(max_consecutive_ones(nums))
