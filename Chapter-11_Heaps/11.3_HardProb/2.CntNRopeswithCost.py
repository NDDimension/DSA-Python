"""
Connect N ropes into one rope with the minimal total cost.

Each time you connect two ropes, the cost is equal to the sum of their lengths.
Your goal is to connect all the ropes with the minimum total cost.

Parameters:
-----------
ropes : List[int]
    A list of positive integers representing the lengths of the ropes.

Returns:
--------
int
    The minimum total cost to connect all ropes into one.


Example:
--------
>>> connectRopes([4, 3, 2, 6])
29
# Explanation:
# 1st: Connect 2 + 3 = 5  (cost: 5)
# 2nd: Connect 4 + 5 = 9  (cost: 9)
# 3rd: Connect 6 + 9 = 15 (cost: 15)
# Total cost = 5 + 9 + 15 = 29
"""

"""Brute Force"""


def connectRopes(ropes):
    def helper(ropes, totalCost):
        if len(ropes) == 1:
            return totalCost

        minTotal = float("inf")
        for i in range(len(ropes)):
            for j in range(i + 1, len(ropes)):
                # connect ropes[i] and ropes[j]
                newrope = ropes[i] + ropes[j]
                newlist = [ropes[k] for k in range(len(ropes)) if k != i and k != j]
                newlist.append(newrope)

                # Recurse with new list and updates cost
                cost = helper(newlist, totalCost + newrope)
                minTotal = min(minTotal, cost)
        return minTotal

    if not ropes or len(ropes) == 1:
        return 0

    return helper(ropes, 0)


connectRopes([4, 3, 2, 6])


"""Optimal Approach:
-----------------
Use a min-heap (priority queue) to always combine the two smallest ropes first.
This greedy approach ensures the least cost at each step, minimizing the overall cost.

Steps:
------
1. Convert the list into a min-heap.
2. While there is more than one rope:
    - Pop the two smallest ropes.
    - Combine them (cost = sum of both).
    - Add the cost to the total.
    - Push the combined rope back into the heap.
3. Return the total cost.

Time Complexity:
----------------
O(N log N), where N is the number of ropes.

Space Complexity:
-----------------
O(N), for the heap storage."""

import heapq


def connectRopesOptimal(ropes):
    if not ropes or len(ropes) == 1:
        return 0

    heapq.heapify(ropes)
    totalCost = 0

    while len(ropes) > 1:
        fst = heapq.heappop(ropes)
        snd = heapq.heappop(ropes)
        cost = fst + snd
        totalCost += cost
        heapq.heappush(ropes, cost)

    return totalCost


connectRopesOptimal([4, 3, 2, 6])
