"""
* * * * *
  * * * *
   * * *
    * *
     *

Here rows are increasing and the content of rows is decreasing
by (space, * , space):
where ;
    space = rowno =>   0th row -> 0 spaces
    star = rows - rowno         =>   5 - 0 = 5 star

Hence here 3 loops will be needed inside the outer loop
for space -> star -> space
"""


def pattern(rows):
    for i in range(rows):
        # Space
        for j in range(i):
            print(" ", end="")

        # Star
        for j in range(rows - i):
            print("*", end=" ")

        print()


rows = int(input("Enter the number of rows : "))
pattern(rows)
