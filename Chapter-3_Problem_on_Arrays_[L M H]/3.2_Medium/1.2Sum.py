"""
"Two Sum Problem"

=> Given [2,6,5,8,11]

Type 1 => Target = 14 is it possible? Yes or No

Type 2 => Find the two numbers that add up to 14 => [6,8] at index [1,3]

=> Brute Force :

    - Iterate over each element in array
    - Check if target - current element exists in the remaining array

=> Time Complexity => O(n^2)
=> Space Complexity => O(1)

=> Better Approach :

    - Hashmap {key: value}
    - Iterate over each element in array
    - If target - current element exists in hashmap,
       return True and indices.

=> Time Complexity => O(n)
=> Space Complexity => O(n)

=> Optimal Approach :

    - Sort the array
    - Two pointers, move add , if increase trim from left
    - If sum is less than target, move left pointer
    - If sum is more than target, move right pointer

=> Time Complexity => O(n log n) + O(n)
=> Space Complexity => O(1)

"""


def twoSumbrute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j], True
            else:
                return False


def twoSumbetter(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i], True
        hashmap[num] = i
    return False


def twoSumoptimal(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        summ = nums[left] + nums[right]
        if summ == target:
            return True
        elif summ < target:
            left += 1
        else:
            right -= 1


nums = [2, 6, 5, 8, 11]
target = 14
print(twoSumoptimal(nums, target))
