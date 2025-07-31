"""
"Leaders in an Array"

=> Given [1, 22, 12, 3, 0 , 6]
=> Leaders = [ 22, 12, 6] as after those all are small

=> Brute Force :

    - Iterate picking one ele and checking next are smaller or not

=> Time Complexity = O(n ^ 2)
=> Space Complexity = O(n)

=> Optimal Approach :

    - Pick one ele and check the remaining after it choose max out of them
    - Check if ele > max chosen then its a  leader

=> Time Complexity = O(n)
=> Space Complexity = O(n)
"""


def leader_brute(nums):
    lead = []
    for i in range(len(nums)):
        leader = True

        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                leader = False
                break

        if leader:
            lead.append(nums[i])

    return lead


def leader_optimal(nums):
    n = len(nums)
    leaders = []
    max_ele = nums[n - 1]
    leaders.append(nums[n - 1])

    for i in range(n - 2, -1, -1):
        if nums[i] > max_ele:
            leaders.append(nums[i])
            max_ele = nums[i]

    return leaders[::-1]


nums = [10, 22, 12, 3, 0, 6]
print(leader_optimal(nums))
