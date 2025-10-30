"""
🍋 Problem: Lemonade Change

You're a lemonade seller. Each lemonade costs $5.

Customers pay with $5, $10, or $20 bills. You must provide the correct change
to each customer in the order they arrive, and you start with no money.

Return True if you can provide change to every customer, or False otherwise.

------------------------------------------------------------------------------------------------

Determines if it is possible to give correct change to every customer in order,
starting with no initial money.

Each lemonade costs $5, and customers pay with $5, $10, or $20 bills. The function
uses a greedy strategy to give change in the most optimal way by prioritizing higher
denomination bills when giving change for $20.

    Parameters:
    ----------
    bills : List[int]
        A list of integers representing the bills customers use to pay, in order.

    Returns:
    -------
    bool
        True if correct change can be given to every customer, False otherwise.

    Example:
    -------
    >>> lemonade_change([5, 5, 5, 10, 20])
    True

    >>> lemonade_change([5, 5, 10, 10, 20])
    False

    Greedy Strategy:
    ----------------
    - Keep track of how many $5 and $10 bills you have.
    - For a $10 bill, give one $5.
    - For a $20 bill, prefer to give one $10 + one $5 (instead of three $5s),
      to keep more $5 bills for future change.

    Time Complexity:
    ----------------
    O(n), where n is the number of customers.

    Space Complexity:
    -----------------
    O(1), only tracking two counters ($5 and $10 bills).

"""


def lemonade_change(bills):
    five, ten = 0, 0

    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:  # bill == 20
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

    return True


lemonade_change([5, 5, 5, 10, 20])
