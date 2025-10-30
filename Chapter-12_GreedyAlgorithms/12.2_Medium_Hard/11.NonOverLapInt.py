"""
Non-overlapping Intervals

Given an array of intervals where intervals[i] = [start_i, end_i],
find the minimum number of intervals you need to remove to make
the rest of the intervals non-overlapping.

The goal is to remove as few intervals as possible so that no two
intervals overlap.

Optimal Approach (Greedy):
    1. Sort intervals based on their end time.
    2. Use a greedy approach to keep intervals with the smallest
       possible end times (since they leave the most room for
       future intervals).
    3. Initialize `end` as the end time of the first interval and
       a counter `count` for removals.
    4. For each subsequent interval:
        - If the current interval's start < `end`, it overlaps → remove it
          (increment `count`).
        - Otherwise, update `end` to the current interval’s end.
    5. Return `count`.

Time Complexity:
    O(n log n) — for sorting the intervals by end time.
Space Complexity:
    O(1) — only uses constant extra space.

Example:
    >>> intervals = [[1,2],[2,3],[3,4],[1,3]]
    >>> erase_overlap_intervals(intervals)
    1
    # Explanation: Removing [1,3] makes the rest non-overlapping.

    >>> intervals = [[1,2],[1,2],[1,2]]
    >>> erase_overlap_intervals(intervals)
    2
    # Explanation: Keep one [1,2], remove the other two.

    >>> intervals = [[1,2],[2,3]]
    >>> erase_overlap_intervals(intervals)
    0
    # Explanation: Already non-overlapping.
"""


def erase_overlap_intervals(intervals):
    if not intervals:
        return 0

    # Step 1: Sort by end time
    intervals.sort(key=lambda x: x[1])

    end = intervals[0][1]
    count = 0  # Number of intervals to remove

    # Step 2: Iterate and apply greedy choice
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            # Overlapping → remove one
            count += 1
        else:
            # Non-overlapping → update end
            end = intervals[i][1]

    return count
