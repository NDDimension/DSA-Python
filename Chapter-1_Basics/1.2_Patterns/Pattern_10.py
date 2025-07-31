"""
*
**
***
****
*****
****
***
**
*

Here we are going to work smart and we will be calling both pyraminds one after another.
"""


def pattern1(rows):
    for i in range(rows + 1):
        for j in range(i):
            print("*", end="")

        print()


def inverted_pattern1(rows):
    for i in range(rows - 1, 0, -1):
        for j in range(i):
            print("*", end="")

        print()


rows = int(input("Enter the number of rows : "))
pattern1(rows)
inverted_pattern1(rows)
