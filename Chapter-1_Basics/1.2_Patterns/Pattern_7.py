"""
     *
    * *
   * * *
  * * * *
 * * * * *

Here rows are increasing and the content of rows is decreasing
by (space, * , space):
where ;
    space = rows - rowno. + 1 =>   0th row -> 5 - 0 + 1 = 4 spaces
    star = 2 x rowno + 1         =>   2 x 0 + 1 = 1 star

Hence here 3 loops will be needed inside the outer loop
for space -> star -> space
"""


def pattern(rows):
    for i in range(rows):
        # Space
        for j in range(rows - i + 1):
            print(" ", end="")

        # Star
        for j in range(i + 1):
            print("*", end=" ")

        print()


rows = int(input("Enter the number of rows : "))
pattern(rows)
