"""
"Minimum number of days to make M bouquets"

=> Given "bloom Days" we need to find the min of day where we can have ample amount of flowers
    to make M bouquets having K flowers.

k = Adjacent Flowers
"""


def possible(bloom_days, day, m, k):
    cnt, no_of_bouquets = 0, 0
    for i in range(len(bloom_days)):
        if bloom_days[i] <= day:
            cnt += 1

        else:
            no_of_bouquets += cnt // k
            cnt = 0

    no_of_bouquets += cnt // k
    return no_of_bouquets >= m


# Brute Force
# TC : O((max - min + 1) x N)


def min_days(bloom_days, m, k):
    for i in range(min(bloom_days), max(bloom_days) + 1):
        if possible(bloom_days, i, m, k) == True:
            return i
    return -1


bloom_days = [1, 10, 3, 10, 2]
m = 3
k = 2
print(min_days(bloom_days, m, k))


# Binary Search
# TC : O(N x [max - min + 1])
def min_days_bs(bloom_days, m, k):
    if len(bloom_days) < m * k:
        return -1

    low = min(bloom_days)
    high = max(bloom_days)

    while low <= high:
        mid = (low + high) // 2

        if possible(bloom_days, mid, m, k) == True:
            high = mid - 1
        else:
            low = mid + 1

    return low


bloom_days = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2
print(min_days_bs(bloom_days, m, k))
