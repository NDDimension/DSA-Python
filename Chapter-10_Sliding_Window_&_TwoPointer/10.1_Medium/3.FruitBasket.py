"""
904. Fruit Into Baskets (LeetCode)

You are visiting a farm that has a row of fruit trees arranged in a line.
The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, there are restrictions:
  - You only have two baskets, and each basket can only hold a single type of fruit.
  - You can start picking from any tree of your choice, and must pick exactly one fruit from each tree (moving to the right) until you can’t pick anymore.
  - Once you encounter a third type of fruit, you must stop (you can’t remove fruit from the baskets).

Return the maximum number of fruits you can pick.

Args:
fruits (List[int]): A list of integers representing the type of fruit each tree produces.

Returns:
int: The maximum number of fruits you can pick under the given constraints.

Example:
--------
>>> totalFruit([1,2,1])
3

>>> totalFruit([0,1,2,2])
3

>>> totalFruit([1,2,3,2,2])
4

Optimal Approach:
-----------------
Use the sliding window technique to maintain a window that contains at most two distinct fruit types.
Expand the window to include more fruits as long as the constraint is satisfied.
Shrink the window from the left when a third fruit type is encountered, updating the maximum size along the way.

Time Complexity: O(n), where n is the number of trees (length of fruits).
Space Complexity: O(1), since the number of distinct fruit types is limited to at most 2 in the window.
"""

"""Brute Force
TC : O(n^2)
SC : O(3)"""


def FIB(arr):
    n = len(arr)
    maxlen = 0
    for i in range(n):
        sett = set()
        for j in range(i, n):
            sett.add(arr[j])
            if len(sett) <= 2:
                maxlen = max(maxlen, j - i + 1)
            else:
                break

    return maxlen


FIB([1, 2, 1])

"""Optimal Approach
TC : O(n)
SC : O(3)"""

from collections import defaultdict


def FruitBasket(nums):
    basket = defaultdict(int)
    n = len(nums)
    left = 0
    maxlen = 0

    for right in range(n):
        basket[nums[right]] += 1

        while len(basket) > 2:
            basket[nums[left]] -= 1
            if basket[nums[left]] == 0:
                del basket[nums[left]]

            left += 1

        maxlen = max(maxlen, right - left + 1)
    return maxlen


FruitBasket([1, 2, 1])
