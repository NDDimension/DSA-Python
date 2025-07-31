"""
*****
****
***
**
*

Here rows are increasing and the content of rows is decreasing
by (total rows - row no. + 1).

1.  The outer loop look for the rows.
2.  The inner loop look for the columns = (total rows - row no. + 1).
"""


def pattern_using_nested_loop(rows):
    for i in range(rows):
        for j in range(rows - i):
            print("* ", end="")
        print()


def pattern_without_nested_loops(rows):
    for i in range(rows, 0, -1):  # going from rows -> 0 decrementing by 1
        print("* " * i)


rows = int(input("Enter the number of rows : "))
pattern_using_nested_loop(rows)

pattern_without_nested_loops(rows)
