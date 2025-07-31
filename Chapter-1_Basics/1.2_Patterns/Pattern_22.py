"""
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
"""


def pattern(n):
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            top, left, right, bottom = i, j, (2 * n - 2) - j, (2 * n - 2) - i
            print(n - min(top, left, right, bottom), end=" ")

        print()


n = int(input("Enter n: "))
pattern(n)
