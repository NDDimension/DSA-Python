"""
"Print all Subsequences / Power Set"

=> We need to print the power set i.e. all possible items of a given string S.
"""


# Using Bit Manipulation
# Time Complexity : O(2 ^ n * n)
# Space Complexity : O(1)
def PowerSet(s):
    n = len(s)
    power_set = []

    for num in range(2**n):  # from 0 to 2^n - 1 (inclusive)
        sub = ""
        for i in range(n):
            if num & (1 << i):  # check if i-th bit is set
                sub += s[i]
        power_set.append(sub)
        print(sub)

    return sorted(power_set)


# Example usage:
print(PowerSet("abc"))

# Using Recursion
# Time Complexity : O(2^n)
# Space Complexity : O(n)


def PowerSet_Recursion(i, s, f):
    if i == len(s):
        print(f, end=" ")
        return

    # include s[i]
    f += s[i]
    PowerSet_Recursion(i + 1, s, f)

    # backtrack -> remove last char (handled by not modifyinh f in-place)
    f = f[:-1]

    PowerSet_Recursion(i + 1, s, f)


PowerSet_Recursion(0, "abc", "")
