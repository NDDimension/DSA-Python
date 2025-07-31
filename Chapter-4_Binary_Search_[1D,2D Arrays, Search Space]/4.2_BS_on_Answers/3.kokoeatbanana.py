"""
"Koko Eating Bananas"

=> Given piles of bananas we need to return "minimum K" such that koko can eat all bananas in given "H hours".

K -> bananas/hr
"""

# Linear Approach
# TC : O(max(arr) x N) ->  time limit exceeded error
# SC : O(1)

import math


def calc_time(piles, hourly):
    total_hrs = 0
    for pile in piles:
        total_hrs += math.ceil(pile / hourly)

    return total_hrs


def minEatingSpeed(piles, h):
    max_pile = max(piles)

    for i in range(1, max_pile + 1):
        req_time = calc_time(piles, i)
        if req_time <= h:
            return i

    return -1


piles, h = [3, 6, 7, 11], 8
print(minEatingSpeed(piles, h))


# Binary Search
# TC : O(N x log(max(element)))
# SC : O(1)


def minEatingSpeed_bs(piles, h):
    max_pile = max(piles)
    low = 1
    high = max_pile
    ans = float("inf")

    while low <= high:
        mid = (low + high) // 2
        total_hrs = calc_time(piles, mid)

        if total_hrs <= h:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    return ans


piles, h = [3, 6, 7, 11], 8
print(minEatingSpeed_bs(piles, h))
