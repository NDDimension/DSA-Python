"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""


def pattern(rows):
    start = 1
    for i in range(rows):
        if i % 2 == 0:
            start = 1
        else:
            start = 0

        for j in range(i + 1):
            print(start, end="")
            start = 1 - start

        print()


rows = int(input("Enter the number of rows : "))
pattern(rows)
