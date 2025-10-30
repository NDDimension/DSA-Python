"""
Job Sequencing Problem

Description:
------------
Given a set of jobs where each job has:
    - a deadline (the latest time by which it should be completed),
    - and a profit (earned if the job is completed before or on its deadline),
the goal is to find the maximum profit that can be earned by scheduling jobs
such that each job takes exactly one unit of time and only one job can be done at a time.

Objective:
-----------
Schedule jobs in a way that maximizes total profit while ensuring
that no two jobs overlap and each job is done before its deadline.

Parameters:
-----------
jobs : list of tuples
    Each tuple contains three elements: (job_id, deadline, profit)
    Example: [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]

Returns:
--------
tuple
    A tuple containing:
        - the list of selected job IDs in scheduled order
        - the maximum total profit earned

Optimal Approach:
-----------------
Greedy Algorithm:
    1. Sort all jobs in decreasing order of profit.
    2. Find the maximum deadline among all jobs.
    3. Create a time slot array to keep track of free slots.
    4. Iterate through each job in sorted order:
        - Try to schedule the job at its latest possible time slot (<= its deadline).
        - If the slot is available, assign the job to that slot.
    5. Calculate the total profit and return the job sequence.

Time Complexity:
----------------
O(N * M)
    where N = number of jobs, M = maximum deadline

Example:
--------
>>> jobs = [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
>>> job_sequencing(jobs)
(['a', 'c', 'e'], 142)

Explanation:
-------------
After sorting by profit: a(100), c(27), d(25), b(19), e(15)
- Job 'a' scheduled at slot 2
- Job 'c' scheduled at slot 1
- Job 'e' scheduled at slot 3
Total profit = 100 + 27 + 15 = 142
"""


def job_sequencing(jobs):
    # Sort jobs by profit in decreasing order
    jobs.sort(key=lambda job: job[2], reverse=True)

    # Find the maximum deadline among all jobs
    max_deadline = max([job[1] for job in jobs])

    # Time Slots
    slots = [None] * (max_deadline + 1)

    total_profit = 0
    job_sequence = []

    for jid, deadline, profit in jobs:
        for t in range(deadline, 0, -1):
            if slots[t] is None:
                slots[t] = jid
                total_profit += profit
                job_sequence.append(jid)
                break
    return (job_sequence, total_profit)


job_sequencing([("a", 2, 100), ("b", 1, 19), ("c", 2, 27), ("d", 1, 25), ("e", 3, 15)])
