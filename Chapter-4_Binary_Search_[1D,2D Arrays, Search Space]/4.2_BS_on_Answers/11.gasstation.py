"""
"Minimize the max distance to gas stations"

=> Given a sorted array of gas station we need to place k new gas stations such that the max distance between them is minimum.
"""

# Brute Force
# TC : O(k x n) + O(n)
# SC : O(n)


def GasStation(gas_stations, k):
    n = len(gas_stations) - 1  # Number of segments
    howmany = [0] * n  # Track how many extra stations per segment

    for _ in range(k):
        maxVal, maxInd = -1, -1
        for j in range(n):
            diff = gas_stations[j + 1] - gas_stations[j]
            section_length = diff / (howmany[j] + 1)
            if section_length > maxVal:
                maxVal = section_length
                maxInd = j
        howmany[maxInd] += 1

    maxAns = -1
    for i in range(n):
        section_length = (gas_stations[i + 1] - gas_stations[i]) / (howmany[i] + 1)
        maxAns = max(maxAns, section_length)

    return maxAns


gas_stations = [1, 13, 17, 23]
k = 5
print(GasStation(gas_stations, k))

# Using HEAP
# TC : O(n log n) + O(k log n)
# SC : O(n)

import heapq


def minMaxDist(arr, k):
    n = len(arr)
    howMany = [0] * (n - 1)
    pq = []

    for i in range(n - 1):
        heapq.heappush(pq, ((-1) * (arr[i + 1] - arr[i]), i))

    for gasStations in range(1, k + 1):
        tp = heapq.heappop(pq)
        secInd = tp[1]

        howMany[secInd] += 1
        inidiff = arr[secInd + 1] - arr[secInd]
        newSection = inidiff / (howMany[secInd] + 1)

        heapq.heappush(pq, (newSection * (-1), secInd))

    return pq[0][0] * (-1)


arr = [1, 13, 17, 23]
k = 5
print(minMaxDist(arr, k))


# Using Binary Search
# TC : O(n log n) + O(n)
# SC : O(1)


def no_of_GasStation_req(dist, arr):
    n = len(arr)
    count = 0

    for i in range(1, n):
        no_in_between = (arr[i] - arr[i - 1]) / dist
        if (arr[i] - arr[i - 1]) == (dist * no_in_between):
            no_in_between -= 1
        count += no_in_between
    return count


def min_max_dist(arr, k):
    n = len(arr)
    low, high = 0, 0
    for i in range(n - 1):
        high = max(high, arr[i + 1] - arr[i])

    diff = 1e-6
    while high - low > diff:
        mid = (low + high) / 2.0
        count = no_of_GasStation_req(mid, arr)

        if count > k:
            low = mid

        else:
            high = mid
    return high


arr = [1, 2, 3, 4, 5]
k = 4
print(min_max_dist(arr, k))
