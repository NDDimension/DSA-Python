"""
"XOR the numbers in given range N"

=> We are given a number N and we need to perform XOR till N from 1.
"""

# Brute Force
"""
Looping and perform XOR

TC : O(n)
SC : O(1)
"""


def XORrange(n):
    ans = 0
    for i in range(1, n + 1):
        ans ^= i

    return ans


XORrange(4)

# Optimal
"""
Observing some patterns we get the answer.

TC : O(1)
SC :O(1)
"""


def XORrange(n):
    if n % 4 == 1:
        return 1

    elif n % 4 == 2:
        return n + 1

    elif n % 4 == 3:
        return 0

    else:
        return n


XORrange(4)

"""
Follow up question to this !

Find the XOR for range(L , R):

We will be calling the function calculating XOR from 1 to n
and for L we will call it for L-1 and for R we call it for R and then we
do a XOR between these two L-1 ^ R. 

TC : O(1)
SC : O(1)
"""


def XOR(l, r):
    return XORrange(l - 1) ^ XORrange(r)


XOR(4, 7)
