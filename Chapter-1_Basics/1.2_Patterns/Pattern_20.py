"""
*               *
**           **
***       ***
****   ****
**********
****   ****
***       ***
**           **
*               *
"""


def pattern(n):
    spaces = 2 * n - 2
    for i in range(1, 2 * n):
        if i <= n:
            stars = i
        else:
            stars = 2 * n - i

        for _ in range(stars):
            print("8", end="")

        for _ in range(spaces):
            print("  ", end="")

        for _ in range(stars):
            print("8", end="")

        print()
        if i < n:
            spaces -= 2
        else:
            spaces += 2


n = int(input("Enter n: "))
pattern(n)
