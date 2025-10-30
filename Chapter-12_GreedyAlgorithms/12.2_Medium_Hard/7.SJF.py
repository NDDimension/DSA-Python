"""
Compute the average waiting time for a set of processes using the
Shortest Job First (SJF) CPU scheduling algorithm (non-preemptive version).

Shortest Job First (SJF) is a scheduling algorithm that selects the process
with the smallest burst time (execution time) to execute next. It minimizes
the average waiting time for a set of jobs.

Parameters
----------
jobs : list of tuples
    Each tuple represents a job in the form (arrival_time, burst_time).
    - arrival_time : int
        The time at which the job arrives.
    - burst_time : int
        The total execution time required by the job.

Returns
-------
float
    The average waiting time for all jobs.

Example
-------
>>> jobs = [(0, 6), (2, 8), (4, 7), (5, 3)]
>>> shortest_job_first(jobs)
6.5

Explanation
-----------
Jobs:
    J1: arrival=0, burst=6
    J2: arrival=2, burst=8
    J3: arrival=4, burst=7
    J4: arrival=5, burst=3

Order of execution (SJF): J1 → J4 → J3 → J2
Waiting times: [0, 15, 7, 1]
Average waiting time = (0 + 15 + 7 + 1) / 4 = 5.75

⚙️ Optimal Approach

Approach: Non-Preemptive Shortest Job First (SJF)

1. Sort jobs by arrival time.
2. Maintain a min-heap (priority queue) based on burst time.
3. Iterate through time:
    - Add all jobs that have arrived by the current time into the heap.
    - Select the job with the smallest burst time from the heap.
    - Update the current time and calculate waiting times.

4. Repeat until all jobs are completed.

Time Complexity:
Sorting: O(n log n)
Heap operations: O(n log n)
➡️ Overall: O(n log n)

This is the most efficient way to simulate SJF scheduling.
"""


def SJF(jobs):
    t = wait_time = 0
    jobs.sort()
    for i in range(len(jobs)):
        wait_time += t
        t += jobs[i]

    return int(wait_time / len(jobs))


SJF([4, 3, 7, 1, 2])
