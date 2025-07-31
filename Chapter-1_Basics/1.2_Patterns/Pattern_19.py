"""
* * * * * * * * * *
* * * *      * * * *
* * *            * * *
* *                  * *
*                        *
*                        *
* *                  * *
* * *             * * *
* * * *       * * * *
* * * * * * * * * *
"""


def pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("8", end="")

        space = 4 * (rows - i)
        print(" " * space, end="")

        for j in range(i, 0, -1):
            print("8", end="")

        print()


def inverted_pattern(rows):
    for i in range(rows, 1, -1):
        for j in range(1, i + 1):
            print("8", end="")

        space = 4 * (rows - i)
        print(" " * space, end="")

        for j in range(i, 0, -1):
            print("8", end="")

        print()


rows = int(input("Enter the number of rows : "))
inverted_pattern(rows)
pattern(rows)
