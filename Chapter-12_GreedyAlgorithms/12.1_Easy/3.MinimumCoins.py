"""
"Minimum Coins"

Given an integer array coins representing different denominations and an integer amount,
return the minimum number of coins required to make up that amount. If it is not possible
to make that amount with the given coins, return -1.
"""


def minCoins(amount):
    denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = 9
    coins = []
    for i in range(n - 1, -1, -1):
        while amount >= denominations[i]:
            amount -= denominations[i]
            coins.append(denominations[i])
    if amount != 0:
        return -1
    return coins


print(minCoins(100))
