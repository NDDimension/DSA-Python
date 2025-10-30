"""
Problem:
    N Meetings in One Room

Description:
    You are given two arrays, `start[]` and `end[]`, each of size N.
    The `start[i]` and `end[i]` represent the start and end times of the i-th meeting.
    You need to find the maximum number of meetings that can be scheduled in one room
    such that no two meetings overlap. The room can hold only one meeting at a time.

Optimal Approach (Greedy Algorithm):
    1. Pair up each meeting's start and end time as (start[i], end[i]).
    2. Sort the meetings by their end time in ascending order.
       - The key intuition is that finishing earlier leaves more room for subsequent meetings.
    3. Iterate through the sorted list:
       - Always pick the next meeting whose start time is greater than the end time of the last selected meeting.
    4. Count how many meetings can be selected this way.

    Time Complexity: O(N log N) — due to sorting
    Space Complexity: O(N) — for storing meeting pairs

Parameters:
    start (List[int]): A list of start times of meetings.
    end (List[int]): A list of end times of meetings.

Returns:
    int: The maximum number of meetings that can be scheduled in the room.

Example:
    >>> start = [1, 3, 0, 5, 8, 5]
    >>> end = [2, 4, 6, 7, 9, 9]
    >>> max_meetings(start, end)
    4

    Explanation:
        After sorting by end times:
            Meetings = [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
        Select meetings in this order:
            (1,2) → (3,4) → (5,7) → (8,9)
        Hence, the maximum number of meetings = 4.
"""


def maxMeetings(start, end):
    meetings = [(end[i], start[i], i + 1) for i in range(len(start))]
    meetings.sort()

    result = []
    lastend = -1

    for end, start, idx in meetings:
        if start > lastend:
            result.append(idx)
            lastend = end

    ans = print(
        f"Meetings : {meetings}\nTotal Meetings can be done: {len(result)}\nOrder of Meeetings : {result}"
    )
    return ans


maxMeetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9])
