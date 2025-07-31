"""
"Best Time to Buy and Sell Stock"

=> Brute Force :
    - Iterate over each day
    - For each day, find the minimum price and maximum profit that can be made.
    - Keep track of the maximum profit
    - Return maximum profit

=> Time Complexity => O(n^2)
=> Space Complexity => O(1)

=> Optimal Approach :

    - Initialize min_price as first element of prices
    - Iterate over each day
    - If current price is less than min_price, update min_price
    - If current price is greater than min_price, update max_profit if max_profit is less than current price - min_price
    - Return max_profit

=> Time Complexity => O(n)
=> Space Complexity => O(1)
"""


def max_profit(prices):
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] > prices[i]:
                max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit


def max_profit_optimized(prices):
    max_profit = 0
    min_price = float("inf")

    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(max_profit_optimized(prices))
