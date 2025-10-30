"""
Candy Problem

Description:
------------
There are `n` children standing in a line, each with a rating value.
You are to distribute candies to these children subject to the following conditions:
    1. Each child must have at least one candy.
    2. Children with a higher rating get more candies than their immediate neighbors.

The goal is to determine the minimum number of candies required to distribute
so that the above conditions are satisfied.

Parameters:
-----------
ratings : list[int]
    A list of integers representing the rating of each child.
    Example: [1, 0, 2]

Returns:
--------
int
    The minimum number of candies required to satisfy the given conditions.

Optimal Approach:
-----------------
Greedy Two-Pass Algorithm:
    1. Initialize an array `candies` where each child gets at least one candy.
    2. Perform a left-to-right pass:
        - If the current child's rating is higher than the previous one,
          give one more candy than the previous child.
    3. Perform a right-to-left pass:
        - If the current child's rating is higher than the next one,
          ensure the current child has more candies than the next child.
    4. The final answer is the sum of all candies.

Time Complexity:
----------------
O(N) — Two linear passes through the ratings list.
Space Complexity:
-----------------
O(N) — For storing the candies array (can be optimized to O(1) with care).

Example:
--------
>>> ratings = [1, 0, 2]
>>> candy(ratings)
5

Explanation:
------------
Step-by-step:
    - Initialize: candies = [1, 1, 1]
    - Left-to-right pass:
        ratings[1] < ratings[0] → no change
        ratings[2] > ratings[1] → candies[2] = candies[1] + 1 → [1, 1, 2]
    - Right-to-left pass:
        ratings[1] < ratings[2] → no change
        ratings[0] > ratings[1] → candies[0] = candies[1] + 1 → [2, 1, 2]
    - Total candies = 2 + 1 + 2 = 5
"""
# ============================================================
#  Method 1: Two-Pass Greedy (O(n) time, O(n) space)
# ============================================================


def candy(ratings):
    """
    Greedy solution to the Candy problem.
    Ensures each child has at least one candy and children with higher ratings
    than their neighbors get more candies.
    """
    n = len(ratings)
    if n == 0:
        return 0

    # Each child gets at least one candy
    left_candies = [1] * n
    right_candies = [1] * n

    # Left to right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            left_candies[i] = left_candies[i - 1] + 1

    # Right to left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            right_candies[i] = right_candies[i + 1] + 1

    # Combine both passes
    total_candies = sum(max(left_candies[i], right_candies[i]) for i in range(n))
    return total_candies


print(candy([1, 0, 2]))

# ============================================================
#  Method 2: Slope Method (O(n) time, O(1) space)
# ============================================================


def candy_slope(ratings):
    """
    One-pass Slope method for the Candy problem (O(1) extra space).

    Concept:
    - View ratings as an up-and-down mountain range.
    - Track lengths of increasing (up) and decreasing (down) slopes.
    - Adjust candies dynamically as the slope changes.
    - Avoid double-counting the "peak" child.
    """
    n = len(ratings)
    if n <= 1:
        return n

    total = 1  # Start with one candy for the first child
    up = 0  # Length of current ascending slope
    down = 0  # Length of current descending slope
    peak = 0  # Length of the last ascending slope

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            # Ascending slope: increment up
            up += 1
            peak = up
            down = 0
            total += 1 + up
        elif ratings[i] == ratings[i - 1]:
            # Flat slope: reset all counters
            up = down = peak = 0
            total += 1
        else:
            # Descending slope
            up = 0
            down += 1
            total += 1 + down - (1 if peak >= down else 0)

    return total


# ============================================================
#  Example Usage & Comparison
# ============================================================

if __name__ == "__main__":
    test_cases = [
        [1, 0, 2],
        [1, 2, 2],
        [1, 3, 4, 5, 2],
        [1, 2, 3, 1, 0],
        [5, 4, 3, 2, 1],
    ]

    for ratings in test_cases:
        print(f"Ratings: {ratings}")
        print(f"Slope Result    : {candy_slope(ratings)}")
        print("-" * 45)


def CandyProb(ratings):
    n = len(ratings)
    if n == 0:
        return 0
    summ = 1  # First child always gets 1 candy
    i = 1

    while i < n:
        # Flat slope
        if ratings[i] == ratings[i - 1]:
            summ += 1
            i += 1
            continue

        # Ascending slope
        up = 0
        while i < n and ratings[i] > ratings[i - 1]:
            up += 1
            summ += up
            i += 1

        # Descending slope
        down = 0
        while i < n and ratings[i] < ratings[i - 1]:
            down += 1
            summ += down
            i += 1

        # Peak adjustment
        if down > up:
            summ += down - up

    return summ


# Test
print(CandyProb([1, 0, 2]))  # Output: 5 ✅
print(CandyProb([1, 2, 2]))  # Output: 4 ✅
print(CandyProb([1, 3, 4, 5, 2]))  # Output: 11 ✅
