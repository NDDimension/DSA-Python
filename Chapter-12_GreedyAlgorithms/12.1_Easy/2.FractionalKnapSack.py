"""
Fractional Knapsack - Greedy Algorithm Problem

Problem:
    Given the weights and values of `n` items, and the maximum capacity of a knapsack,
    determine the maximum total value that can be obtained by selecting items such that
    you can take any fraction of an item.

    Unlike the 0/1 Knapsack, you are allowed to break items and take fractions of them
    to fill the knapsack to its capacity.

Parameters:
    capacity (float): The total weight capacity of the knapsack.
    weights (List[float]): The list of weights for each item.
    values (List[float]): The list of values corresponding to each item.

Returns:
    float: The maximum value that can be obtained in the knapsack with fractional items.

Optimal Approach:
    - Calculate the value-to-weight ratio for each item.
    - Sort the items in descending order of this ratio.
    - Greedily pick items starting from the highest ratio:
        - If the whole item fits, take it completely.
        - If not, take the fraction that fits.
    - Stop when the knapsack is full.

Time Complexity:
    O(n log n), where n is the number of items (due to sorting by value/weight ratio).

Example:
    >>> fractionalKnapsack(50, [10, 20, 30], [60, 100, 120])
    240.0
    # Take all of item 0 (10kg, value 60),
    # all of item 1 (20kg, value 100),
    # and 2/3 of item 2 (20kg, value 80), total = 60 + 100 + 80 = 240.0
"""


def fractionalKnapsack(
    capacity: float, weights: list[float], values: list[float]
) -> float:
    n = len(weights)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    items.sort(reverse=True)  # Sort by value-to-weight ratio

    total_value = 0.0
    for ratio, weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break

    return total_value


fractionalKnapsack(50, [10, 20, 30], [60, 100, 120])
