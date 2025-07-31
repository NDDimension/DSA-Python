"""
1                   1
1 2             2 1
1 2 3       3 2 1
1 2 3 4 4 3 2 1
"""


def pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")

        space = 4 * (rows - i)
        print(" " * space, end="")

        for j in range(i, 0, -1):
            print(j, end="")

        print()


rows = int(input("Enter the number of rows : "))
pattern(rows)
