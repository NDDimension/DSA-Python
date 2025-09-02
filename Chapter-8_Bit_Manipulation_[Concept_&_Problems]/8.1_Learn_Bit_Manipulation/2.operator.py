"""
AND
-> all True = True
-> 1 false = False

"""


def logic_and(*args):
    return all(args)  # True only if all are True


"""
OR
-> 1 true = True
-> all false = False

"""


def logic_or(*args):
    return any(args)  # True if at least one is True


"""
XOR
-> no. of 1s odd -> 1
-> no. of 1s even -> 0

"""


def logic_xor(*args):
    return sum(args) % 2 == 1  # True if number of Trues is odd


"""
SHIFT R >>

n >> x
number n will fall over the cliff from behind x times

formula = n / 2^x

Example:

13 >> 1 -> 1101 -> 110  1
the last 1 will be removed and only 110 will be left as our answer

13 >> 2 -> 1101 -> 11  01
the last two digits 01 both will be removed and only 11 as our answer.
"""


def shift_right(n, x):
    return n // (2**x)  # Shift right x times: divide by 2^x


"""
SHIFT L <<

n << x 
number n will fall over the cliff from front x times

Example:

13 << 1 -> 1101 -> 1  1010
front 1 is removed and a zero added at last

Formula = n x 2^x
"""


def shift_left(n, x):
    return n * (2**x)  # Shift left x times: multiply by 2^x


"""
NOT
0 to 1 and 1 to 0
if -ve then 2s complement else not
"""
val = True

if val:
    result = False
else:
    result = True

print("NOT Result:", result)  # Output: False
