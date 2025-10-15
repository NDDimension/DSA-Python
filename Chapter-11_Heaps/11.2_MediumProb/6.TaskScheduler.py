"""
Task Scheduler (LeetCode 621)

Given a list of tasks (uppercase letters) and a non-negative cooldown n,
return the least number of intervals needed to finish all tasks such that
the same task appears at least n intervals apart.

Edge cases:
- n = 0 -> answer is len(tasks)
- Many tasks tied for max frequency
- Empty tasks -> 0

Examples:
- tasks = ["A","A","A","B","B","B"], n = 2
  -> 8
  One valid schedule: A B idle A B idle A B

- tasks = ["A","C","A","B","D","B"], n = 1
  -> 6
  One valid schedule: A B C A B D

- tasks = ["A","A","A","A","B","C","D","E","F","G"], n = 2
  -> 10
  One valid schedule: A B C A D E A F G A

- tasks = ["A","A","A","B","B","B"], n = 50
  -> 104  (idles dominate)
"""

"""  1) Brute Force (Greedy Simulation with Max-Heap + Cooldown Queue)
       - Count frequencies of tasks.
       - Use a max-heap to always schedule the task with the highest remaining count.
       - Use a queue to keep tasks that are cooling down with their "available time".
       - Each time unit:
         - Release any task whose cooldown expired back to the heap.
         - If heap not empty, schedule one task (decrement count); if it remains, put it into cooldown with next available time t + n + 1.
         - If heap empty but cooldown not, it's an idle.
       - Time: O(T log K), where T = len(tasks), K = number of distinct tasks (≤ 26)
       - Space: O(K)
"""


def TaskScheduler(tasks, n):
    import heapq
    from collections import Counter, deque

    if not tasks:
        return 0

    freq = Counter(tasks)
    max_heap = [-c for c in freq.values()]
    heapq.heapify(max_heap)

    time = 0
    cooldown = deque()

    while max_heap or cooldown:
        time += 1

        while cooldown and cooldown[0][0] <= time:
            _, neg_count = cooldown.popleft()
            heapq.heappush(max_heap, neg_count)

        if max_heap:
            neg_count = heapq.heappop(max_heap) + 1
            if neg_count != 0:
                cooldown.append((time + n + 1, neg_count))
    return time


TaskScheduler(["A", "A", "A", "B", "B", "B"], 2)

"""    2) Optimal (Math / Bucket Fill)
       - Let f_max = max frequency of any task.
       - Let c_max = number of tasks that occur f_max times.
       - Arrange the most frequent tasks into (f_max - 1) full frames of size (n + 1),
         then place the c_max tasks in the last frame.
       - Answer = max(len(tasks), (f_max - 1) * (n + 1) + c_max)
       - Time: O(T) to count and scan; Space: O(K)
"""


def taskScheduler(tasks, n):
    from collections import Counter

    freq = Counter(tasks)
    if not freq:
        return 0

    fmax = max(freq.values())
    cmax = sum(1 for v in freq.values() if v == fmax)
    return max(len(tasks), (fmax - 1) * (n + 1) + cmax)


taskScheduler(["A", "A", "A", "B", "B", "B"], 2)
