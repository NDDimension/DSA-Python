"""
12345
1234
123
12
1

Here rows are increasing and the content of rows is decreasing
by (total rows - row no. + 1).

1.  The outer loop look for the rows.
2.  The inner loop look for the columns = (total rows - row no. + 1).
"""


def pattern(rows):
    for i in range(rows):
        for j in range(rows - i):
            print(j + 1, end="")
        print()


rows = int(input("Enter the number of rows : "))
pattern(rows)
