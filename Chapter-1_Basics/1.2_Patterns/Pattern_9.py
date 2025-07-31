"""
     *
    * *
   * * *
 * * * *
* * * * *
* * * * *
  * * * *
   * * *
    * *
     *

Here we are going to work smart and we will be calling both pyraminds one after another.
"""


def pyramind(rows):
    for i in range(rows):
        # Space
        for j in range(rows - i - 1):
            print(" ", end="")

        # Star
        for j in range(i + 1):
            print("*", end=" ")

        print()


def inverted_pyramind(rows):
    for i in range(rows):
        # Space
        for j in range(i):
            print(" ", end="")

        # Star
        for j in range(rows - i):
            print("*", end=" ")

        print()


rows = int(input("Enter the number of rows : "))
pyramind(rows)
inverted_pyramind(rows)
