"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

Here rows are increasing and the content of rows is same as
row number from 1 to row number  i.e. 1st row -> 1
                                                            2nd row -> 2 2
likewise.

1.  The outer loop look for the rows.
2.  The inner loop look for the columns = row no.= 1 to row no. as content.
3.  end="" for printing the content in single line "*****".
4.  This print is for the new line after each completed iteration of outer loop.

"""


def pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(i, end="")
        print()


rows = int(input("Enter the number of rows : "))
pattern(rows)
