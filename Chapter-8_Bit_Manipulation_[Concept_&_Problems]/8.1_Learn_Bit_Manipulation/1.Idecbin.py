"""
Decimal to Binary

TC : O(log_2 n)
SC : O(log_2 n)
"""


def dec2bin(n):
    res = ""
    while n > 0:
        if n % 2 == 1:
            res += "1"
        else:
            res += "0"
        n //= 2
    res = res[::-1]
    return res


print(dec2bin(13))


def dec2bin_concise(n):
    return bin(n)[2:]


dec2bin_concise(13)

"""
Binary to Decimal

TC : O(len)
SC : O(1)
"""


def bin2dec_concise(b):
    return int(b, 2)


bin2dec_concise("1101")


def bin2dec(b):
    p2 = 1
    num = 0
    for i in range(len(b) - 1, -1, -1):
        if b[i] == "1":
            num += p2
        p2 *= 2
    return num


bin2dec("1101")
