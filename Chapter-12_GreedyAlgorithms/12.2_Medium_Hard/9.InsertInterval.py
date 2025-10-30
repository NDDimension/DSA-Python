"""
Insert a new interval into a list of non-overlapping, sorted intervals
and merge any overlapping intervals if necessary.

The intervals are initially sorted based on their start times.
The goal is to insert the new interval into the list while maintaining
order and ensuring that overlapping intervals are merged into a single interval.

Parameters
----------
intervals : list[list[int]]
    A list of non-overlapping intervals sorted by start time.
    Each interval is represented as [start, end].
new_interval : list[int]
    The interval to insert, represented as [start, end].

Returns
-------
list[list[int]]
    A new list of merged intervals after inserting the new one.

Optimal Approach
----------------
1. Iterate through the existing intervals.
2. Add all intervals that end before the new interval starts.
3. Merge all intervals that overlap with the new interval:
    - new_start = min(current_start, new_interval_start)
    - new_end   = max(current_end, new_interval_end)
4. Add all intervals that start after the new interval ends.
5. This ensures all intervals remain sorted and merged.

Time Complexity: O(n)
    - Each interval is visited at most once.

Space Complexity: O(n)
    - Result list to store merged intervals.

Example
-------
>>> intervals = [[1, 3], [6, 9]]
>>> new_interval = [2, 5]
>>> insert_interval(intervals, new_interval)
[[1, 5], [6, 9]]

Explanation
-----------
- Existing intervals: [1, 3], [6, 9]
- New interval: [2, 5]
- [1, 3] and [2, 5] overlap → merge to [1, 5]
- Final result: [[1, 5], [6, 9]]
"""


def insert_interval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] < new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    while i < n:
        result.append(intervals[i])
        i += 1
    return result


insert_interval([[1, 3], [6, 9]], [2, 5])
