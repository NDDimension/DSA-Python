"""
K Most Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example:
>>> Input: nums = [1,1,1,2,2,3], k = 2
>>> Output: [1,2]

Explanation:
    - 1 appears 3 times, 2 appears 2 times, 3 appears 1 time.
    - The top 2 frequent elements are [1, 2].
"""

"""
Brute-force Approach:

Idea:
>>> Count frequency of all elements using a hashmap.
>>> Sort elements by frequency.
>>> Return the top k.

Time Complexity: O(n log n) — sorting dominates
Space Complexity: O(n) — for frequency map"""


def kMostFrequent(nums, k):
    from collections import Counter

    freq = Counter(nums)
    sortednums = sorted(freq.items(), key=lambda x: -x[1])
    return [item[0] for item in sortednums[:k]]


kMostFrequent([1, 1, 1, 2, 2, 3], 2)

"""
Optimal Approach (Using Heap or Bucket Sort):

Option 1: Min-Heap (Priority Queue)
>>> Use a min-heap of size k to keep track of top k frequent elements.

Time Complexity: O(n log k)
Space Complexity: O(n)

Option 2: Bucket Sort (Best theoretical time)
>>> Use bucket sort since max frequency ≤ len(nums)

Time Complexity: O(n)
Space Complexity: O(n)
"""


def kMostFrequentHeap(nums, k):
    from collections import Counter
    import heapq

    freq = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]


kMostFrequentHeap([1, 1, 1, 2, 2, 3], 2)

from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        # Step 1: Frequency Map
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # Step 2: Bucket Sort by Frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        # Step 3: Collect k most frequent
        result = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result


sol = Solution()
sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
