"""
"4 Sum Problem"

=> Given an array return unique sequences of arrays of size 4 summing up gives 0
where all three elements are different.

"""

"""
=> Brute Force:

    - 4 Loops and find the unique element triplet using set.

=> Time Complexity : O(n^4)
=> Space Complexity : O(2n)

"""


def fourSumBrute(nums, target):
    sett = set()
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        sett.add(tuple(temp))

    return sett


nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
print(fourSumBrute(nums, 9))


"""
=> Better Approach:

    - 3 loops + 1 hash and using formula l = target -(i + j + k)

=> Time Complexity : O(n^3 x log(size of set))
=> Space Complexity : O(2(quads)) + O(n)


"""


def fourSumBetter(nums, target):
    sett = set()
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            hashset = set()
            for k in range(j + 1, n):
                l = target - (nums[i] + nums[j] + nums[k])
                if l in hashset:
                    temp = [nums[i], nums[j], nums[k], l]
                    temp.sort()
                    sett.add(tuple(temp))

                hashset.add(nums[k])

    ans = list(sett)
    return ans


nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
print(fourSumBetter(nums, 9))

"""
=> Optimal Approach:

    - Using pointer approach 

=> Time Complexity : O(n^3) + O(nlogn)
=> Space Complexity : O(no. of unique quads)

"""


def fourSumOptimal(nums, target):
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            k = j + 1
            l = n - 1

            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)

                    k += 1
                    l -= 1

                    while k < l and nums[k] == nums[k - 1]:
                        k += 1

                elif total < target:
                    k += 1
                else:
                    l -= 1

    return ans


nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
print(fourSumOptimal(nums, 9))
