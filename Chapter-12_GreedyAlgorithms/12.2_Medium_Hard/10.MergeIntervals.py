"""
Merge Intervals

Given a collection of intervals, merge all overlapping intervals
and return a list of the non-overlapping intervals that cover all
the intervals in the input.

The optimal approach sorts the intervals by their start time and
then iterates through them, merging overlapping intervals as needed.
Sorting ensures we can process intervals in linear order to detect
overlaps efficiently.

Approach:
    1. Sort intervals by their start time.
    2. Initialize an empty list `merged` to store merged intervals.
    3. For each interval:
        - If `merged` is empty or current interval does not overlap
          with the last merged interval, append it to `merged`.
        - Else, merge the current interval with the last one by updating
          the end time to be the maximum of both end times.
    4. Return `merged` after processing all intervals.

Time Complexity:
    O(n log n) — due to sorting (where n is the number of intervals).
Space Complexity:
    O(n) — for storing the merged output list.

Example:
    >>> intervals = [[1,3],[2,6],[8,10],[15,18]]
    >>> merge(intervals)
    [[1, 6], [8, 10], [15, 18]]

    >>> intervals = [[1,4],[4,5]]
    >>> merge(intervals)
    [[1, 5]]
"""


def merge(intervals):
    # Step 1: Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # Step 2: If no overlap, add the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Step 3: Merge overlapping intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


merge([[1, 3], [2, 6], [8, 10], [15, 18]])
