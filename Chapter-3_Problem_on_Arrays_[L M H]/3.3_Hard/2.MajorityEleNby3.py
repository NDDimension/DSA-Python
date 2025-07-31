"""
"Majority Element in the array appearing N / 3 times"

=> Given an array [1,1,1,3,3,2,2,2]
=> N = 8

then which integers are appearing more than N / 3 = 8 / 3 ~ 2  times

Answer => [1, 2]
also its answer will always be 2 numbers only.
"""

"""
=> Brute Force:
     - Iterate taking each element and count occurences

=> Time Complexity : O(n ^ 2)
=> Space Complexity : O(n)
"""


def majorityElementBrute(nums):
    n = len(nums)
    ans = []

    for i in range(n):
        if len(ans) == 0 or ans[0] != nums[i]:
            count = 0

            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1

            if count > n / 3:
                ans.append(nums[i])

        if len(ans) == 2:
            break

    return ans


nums = [1, 1, 1, 3, 3, 2, 2, 2]
majorityElementBrute(nums)

"""
=> Better Approach:

    - using hashmap 

=> Time Complexity : O(n)
=> Space Complexity : O(n)
"""
from collections import defaultdict


def majorityElementBetter(nums):
    ls = []
    count = defaultdict(int)
    minn = len(nums) // 3 + 1

    for i in range(len(nums)):
        count[nums[i]] += 1
        if count[nums[i]] == minn:
            ls.append(nums[i])

    return ls


nums = [1, 1, 1, 3, 3, 2, 2, 2]
majorityElementBetter(nums)

"""
=> Optimal Aprroach:

    - Cancel off logic to count the majority element

=> Time Complexity : O(n)
=> Space Complexity : O(1)
"""


def majorityElementOptimal(nums):
    n = len(nums)

    c1, c2 = 0, 0
    e1, e2 = float("-inf"), float("-inf")

    for i in range(n):
        if c1 == 0 and e2 != nums[i]:
            c1 = 1
            e1 = nums[i]

        elif c2 == 0 and e1 != nums[i]:
            c2 = 1
            e2 = nums[i]

        elif nums[i] == e1:
            c1 += 1

        elif nums[i] == e2:
            c2 += 1

        else:
            c1 -= 1
            c2 -= 1

    c1, c2 = 0, 0
    for i in range(n):
        if nums[i] == e1:
            c1 += 1
        if nums[i] == e2:
            c2 += 1

    minn = int(n / 3) + 1
    ls = []
    if c1 >= minn:
        ls.append(e1)
    if c2 >= minn:
        ls.append(e2)

    return ls


nums = [1, 1, 1, 3, 3, 2, 2, 2]
majorityElementOptimal(nums)
