"""
Same as the previous one just a little change of
appending the value of "i" before function call.
"""


def N_to_One_backwards(i, n, result=[]):
    if result is None:
        result = []

    if i < 1:
        return result

    result.append(i)
    N_to_One_backwards(i - 1, n, result)

    return result


N_to_One_backwards(10, 10)
