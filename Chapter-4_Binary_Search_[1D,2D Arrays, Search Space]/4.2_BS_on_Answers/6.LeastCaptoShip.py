"""
"Least Capacity to ship packages within D days"

=> Given packages and certain days we need to ship them within given deadline and for that
    we need to find the least capacity (for ship) to fill the ship with packages to complete the task.
"""

# Naive Approach
# TC : O((sum - max + 1) x N ) ~ O(n^2)
# SC : O(1)


def daysReq(packages, capacity):
    day = 1
    load = 0

    for i in range(len(packages)):
        if load + packages[i] > capacity:
            day += 1
            load = packages[i]

        else:
            load += packages[i]

    return day


def leastCapacity(packages, days):
    max_ele = max(packages)
    sum_packages = sum(packages)

    for capacity in range(max_ele, sum_packages + 1):
        days_Req = daysReq(packages, capacity)
        if days_Req <= days:
            return capacity


packages = [5, 4, 5, 2, 3, 4, 5, 6]
days = 5
print(leastCapacity(packages, days))

# Binary Search
# TC : O(log(sum - max + 1) x N )
# SC : O(1)


def min_capacity(packages, days):
    max_ele = max(packages)
    sum_packages = sum(packages)

    low = max_ele
    high = sum_packages

    while low <= high:
        mid = (low + high) // 2

        if daysReq(packages, mid) <= days:
            high = mid - 1

        else:
            low = mid + 1

    return low


packages = [5, 4, 5, 2, 3, 4, 5, 6]
days = 5
print(min_capacity(packages, days))
