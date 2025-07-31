"""
"Aggressive Cows"

=> Given stall cordinates we need to find the max(min distance between any two cows) to place them.
"""

# Naive approach
# TC : O((max -  min) x N)
# SC : O(1)


def can_we_place(stalls, cows, min_sep):
    countCows = 1
    last_coordinate = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_coordinate >= min_sep:
            countCows += 1
            last_coordinate = stalls[i]

    if countCows >= cows:
        return True
    else:
        return False


def aggressiveCows(stalls, cows):
    stalls.sort()

    for i in range(1, (max(stalls) - min(stalls))):
        if can_we_place(stalls, cows, i) == True:
            continue

        else:
            return i - 1

    return -1


stalls = [0, 3, 4, 7, 10, 9]
cows = 4

aggressiveCows(stalls, cows)

# Binaray Search
# TC : O(NlogN) + O([logn(max - min) x O(N)])
#


def aggressiveCows_BS(stalls, cows):
    stalls.sort()
    low = 0
    high = max(stalls) - min(stalls)

    while low <= high:
        mid = (low + high) // 2

        if can_we_place(stalls, cows, mid) == True:
            low = mid + 1

        else:
            high = mid - 1

    return low - 1


stalls = [0, 3, 4, 7, 10, 9]
cows = 4

aggressiveCows_BS(stalls, cows)
