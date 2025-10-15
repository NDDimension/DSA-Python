"""
Replace each array element by its corresponding rank.

Given an integer array arr, transform it so that each element is replaced
by its rank when the array's unique values are sorted in ascending order.
Ranks start at 1. Equal elements share the same rank.

Optimal approach:
- Coordinate compression:
  1) Sort the unique values: uniq = sorted(set(arr))
  2) Assign ranks in order: rank[val] = idx + 1
  3) Map each original element to its rank using the dictionary.
This approach ensures duplicates receive the same rank, and distinct
values maintain their relative order.

Complexity:
- Time: O(n log n) due to sorting unique values (n = len(arr))
- Space: O(n) for the rank map and the output

Edge cases:
- Duplicates: equal values share the same rank
- Negative numbers and zeros are allowed
- Empty array returns []

Examples:
- Input:  arr = [40, 10, 20, 30]
  Output: [4, 1, 2, 3]
  Explanation:
    Unique sorted = [10, 20, 30, 40]
    Ranks: {10:1, 20:2, 30:3, 40:4}
    Map -> [4, 1, 2, 3]

- Input:  arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
  Output: [5, 3, 4, 2, 8, 6, 7, 1, 3]
  Explanation:
    Unique sorted = [5, 9, 12, 28, 37, 56, 80, 100]
    Ranks: {5:1, 9:2, 12:3, 28:4, 37:5, 56:6, 80:7, 100:8}

Args:
    arr: List of integers.

Returns:
    A new list where each element is replaced by its rank.
"""

"""Brute Force"""
"""
    Replace each array element by its corresponding rank (Brute Force).

    Brute-force approach (point-wise):
    - For each index i, compute rank = 1 + number of distinct values strictly less than arr[i] in the array.
    - Use a temporary set per i to avoid double-counting duplicates among the "less-than" values.
    - Assign the computed rank to result[i]. Equal elements naturally receive the same rank.

    Complexity:
    - Time: O(n^2) due to nested scanning for every element (n = len(arr)).
    - Space: O(n) for the output and a temporary set (up to n) per iteration.

    Examples:
    - Input:  [40, 10, 20, 30]
      Output: [4, 1, 2, 3]

    - Input:  [37, 12, 28, 9, 100, 56, 80, 5, 12]
      Output: [5, 3, 4, 2, 8, 6, 7, 1, 3]

    Args:
        arr: List of integers.

    Returns:
        A new list where each element is replaced by its rank.
"""


def arrayRank(arr):
    n = len(arr)
    res = [0] * n

    for i in range(n):
        ai = arr[i]
        seen = set()
        rank = 1

        for j in range(n):
            aj = arr[j]
            if aj < ai and aj not in seen:
                seen.add(aj)
                rank += 1

        res[i] = rank

    return res


arrayRank([40, 10, 20, 30])


def arrRank(arr):
    rank = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
    return [rank[v] for v in arr]


arrayRank([37, 12, 28, 9, 100, 56, 80, 5, 12])
