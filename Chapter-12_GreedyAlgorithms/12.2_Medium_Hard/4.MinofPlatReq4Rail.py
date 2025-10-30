"""
"Minimum number of platforms required for a Railway"

Problem:
    Given two lists `arrival` and `departure`, each representing the arrival and
    departure times of trains at a station (in the same order), find the minimum
    number of platforms required so that no train has to wait for another to leave.

Approach (Two-Pointer / Sorting):
    1. Sort both `arrival` and `departure` arrays.
    2. Use two pointers `i` and `j` to traverse the lists:
        - If the next train arrives before or at the same time as the earliest
          departing train, increment the count of platforms (`plat_needed += 1`).
        - Otherwise, if a train departs before the next one arrives,
          decrement the count (`plat_needed -= 1`).
    3. Keep track of the maximum platforms needed at any point in time.

Time Complexity:
    O(n log n) — for sorting the arrival and departure times.
Space Complexity:
    O(1) — only a few extra variables used.

Example:
    >>> arrival = [900, 940, 950, 1100, 1500, 1800]
    >>> departure = [910, 1200, 1120, 1130, 1900, 2000]
    >>> minPlatforms(arrival, departure)
    3

    Explanation:
        - At 9:00 → 1 train
        - At 9:40 → 2 trains (since another train arrives before the first departs)
        - At 9:50 → 3 trains (one more arrives before any departure)
        - After 11:20 → trains start departing → platform count reduces
        - Maximum concurrent trains = 3, so 3 platforms are needed.
"""


def minPlatforms(arrival, departure):
    arrival.sort()
    departure.sort()
    n = len(arrival)

    plat_needed = 1
    result = 1
    i = 1
    j = 0

    while i < n and j < n:
        if arrival[i] <= departure[j]:
            plat_needed += 1
            i += 1
        else:
            plat_needed -= 1
            j += 1
        result = max(result, plat_needed)

    return result


def minPlatforms2(arrival, departure):
    """
    Problem:
        Given arrival and departure times of trains, find the minimum number of
        platforms required at a railway station so that no train has to wait.

    Approach (Brute Force, O(n²)):
        - For every train, check how many other trains overlap with its schedule.
        - Overlap condition:
              arrival[i] <= departure[j] and arrival[j] <= departure[i]
        - The maximum number of overlapping trains at any time equals the
          number of platforms required.

    Time Complexity:
        O(n²)
    Space Complexity:
        O(1)

    Example:
        >>> arrival = [900, 940, 950, 1100, 1500, 1800]
        >>> departure = [910, 1200, 1120, 1130, 1900, 2000]
        >>> minPlatforms2(arrival, departure)
        3
    """
    n = len(arrival)
    maxcount = 0

    for i in range(n):
        cnt = 1  # current train needs one platform
        for j in range(i + 1, n):
            # Check if train j overlaps with train i
            if arrival[i] <= departure[j] and arrival[j] <= departure[i]:
                cnt += 1
        maxcount = max(maxcount, cnt)

    return maxcount


# Example run
print(
    minPlatforms2(
        [900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]
    )
)
