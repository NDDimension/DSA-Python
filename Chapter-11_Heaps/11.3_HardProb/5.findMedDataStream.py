"""
Find Median from Data Stream

Design a data structure that supports adding numbers from a data stream and finding the median in efficient time.

Example:

>>> Input:
>>> ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
>>> [[], [1], [2], [], [3], []]

>>> Output:
>>> [None, None, None, 1.5, None, 2.0]

Explanation:
    - MedianFinder mf = new MedianFinder();
    - mf.addNum(1);    # arr = [1]
    - mf.addNum(2);    # arr = [1, 2]
    - mf.findMedian(); # return 1.5
    - mf.addNum(3);    # arr = [1, 2, 3]
    - mf.findMedian(); # return 2.0

"""

"""
Brute-force Approach:

>>> Idea:
Keep a list of all numbers. On findMedian(), sort the list and compute the median.

Time Complexity:
addNum(): O(1)
findMedian(): O(n log n) for sorting

Space Complexity: O(n)"""


class MedianFinder:
    def __init__(self) -> None:
        self.nums = []

    def addnum(self, num):
        self.nums.append(num)

    def findMedian(self):
        nums = sorted(self.nums)
        n = len(nums)
        mid = n // 2
        if n % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2

        else:
            return float(nums[mid])


mf = MedianFinder()
mf.addnum(1)
mf.addnum(2)
mf.findMedian()
mf.addnum(3)
mf.findMedian()


"""
Optimal Approach (Using Heaps):

>>> Idea:
Use two heaps:
    - A max-heap (low) to store the smaller half of numbers.
    - A min-heap (high) to store the larger half.

Ensure:
    - len(low) == len(high) or len(low) == len(high) + 1
    - Max of low ≤ Min of high

Median:
    - If even elements: average of tops of both heaps
    - If odd: top of low

Time Complexity:
addNum(): O(log n)
findMedian(): O(1)

Space Complexity: O(n)"""

import heapq


class Median:
    def __init__(self) -> None:
        self.low = []  # max heap
        self.high = []  # min heap

    def addNum(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))

        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self):
        if len(self.low) > len(self.high):
            return -self.low[0]

        return (-self.low[0] + self.high[0]) / 2


mf = Median()
mf.addNum(1)
mf.addNum(2)
mf.findMedian()
mf.addNum(3)
mf.findMedian()
