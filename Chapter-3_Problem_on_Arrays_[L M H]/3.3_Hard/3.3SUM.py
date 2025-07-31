"""
"3 Sum Problem"

=> Given an array return unique sequences of arrays of size 3 summing up gives 0
where all three elements are different.

"""

"""
=> Brute Force:

    - 3 Loops and find the unique element triplet using set.

=> Time Complexity : O(n^3 x log(no. of unique triplets))
=> Space Complexity : O(2n)

"""


def threeSumBrute(nums):
    sett = set()
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    sett.add(tuple(temp))

    return sett


nums = [-1, 0, 1, 2, -1, -4]
print(threeSumBrute(nums))


"""
=> Better Approach:

    - 2 loops + 1 hash and using formula k = -(i + j)

=> Time Complexity : O(n^2 x log(size of set))
=> Space Complexity : O(2n)

"""


def threeSumBetter(nums):
    sett = set()
    n = len(nums)

    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            k = -(nums[i] + nums[j])

            if k in hashset:
                temp = [nums[i], nums[j], k]
                temp.sort()
                sett.add(tuple(temp))

            hashset.add(nums[j])

    ans = list(sett)
    return ans


nums = [-1, 0, 1, 2, -1, -4]
print(threeSumBetter(nums))

"""
=> Optimal Approach:

    - Using 2 pointer approach 

=> Time Complexity : O(n^2) + O(nlogn)
=> Space Complexity : O(no. of unique triplets)

"""


def threeSumOptimal(nums):
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n):
        if i != 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1

            elif total > 0:
                k -= 1

            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j - 1]:
                    j += 1

                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

    return ans


nums = [-1, 0, 1, 2, -1, -4]
print(threeSumOptimal(nums))
