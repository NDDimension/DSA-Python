"""
*****
*****
*****
*****
*****

Rows and content of column is same like in 0th row -> 5 stars and
rows are 5 each having same 5 stars.

1.  The outer loop look for the 5 rows.
2.  The inner loop look for the 5 columns and its content.
3.  end="" for printing the content in single line "*****".
4.  This print is for the new line after each completed iteration of outer loop.

"""


def pattern(rows):
    for i in range(rows):
        for j in range(rows):
            print("*", end="")
        print()


rows = int(input("Enter the number of rows : "))
pattern(rows)
