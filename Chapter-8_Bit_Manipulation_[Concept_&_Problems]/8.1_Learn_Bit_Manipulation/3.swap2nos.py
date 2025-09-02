"""
"Swap two numbers without using the 3rd variable"

1. a = a xor b
2. b = a xor b ( a xor b xor b) = a
3. a = a xor b (a xor b xor a) = b

done
"""


def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return (a, b)


swap(1, 2)
