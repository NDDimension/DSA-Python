"""
"Find the number that appears ONCE in array where other numbers appear twice"

=> Brute Force :

    - Iterate and count the frequency of each number

=> Time Complexity => O(n^2)
=> Space Complexity => O(1)

=> Better Approach :

    - use hash map to store the frequency of each number
    - Iterate -> hash map and return the number with frequency 1

=> Time Complexity => O(n)
=> Space Complexity => O(n)


"""


def find_single_number(nums):
    for num in nums:
        count = 0
        for j in nums:
            if j == num:
                count += 1
        if count == 1:
            return num


def find_single_number1(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num


from collections import Counter


def find_single_number2(nums):
    counter = Counter(nums)
    for num, freq in counter.items():
        if freq == 1:
            return num


def find_single_numberOpt(nums):
    from functools import reduce
    from operator import xor

    return reduce(xor, nums)


def find_single_number3Opt(nums):
    xor1 = 0
    for i in nums:
        xor1 ^= nums[i]

    return xor1


nums = [4, 3, 2, 4, 3, 2, -1]
print(find_single_number3Opt(nums))
