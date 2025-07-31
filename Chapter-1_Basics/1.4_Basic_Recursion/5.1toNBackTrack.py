"""
Generates a list of natural numbers from 1 to n using backtracking.

Parameters:
i (int): Current number to process (starts from n and decreases to 1).
n (int): The upper limit of the range (used for initialization only).
result (list, optional): Accumulator list used to store results during recursion.

Returns:
list: A list of natural numbers from 1 to n in ascending order.
"""


def One_to_N_Backwards(i, n, result=[]):
    if result is None:
        result = []

    if i < 1:
        return result

    One_to_N_Backwards(i - 1, n, result)
    result.append(i)

    return result


One_to_N_Backwards(10, 10)
