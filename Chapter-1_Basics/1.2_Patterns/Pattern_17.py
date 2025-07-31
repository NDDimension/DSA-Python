"""
            A
         A B A
      A B C B A
   A B C D C B A
A B C D E D C B A

"""


def pattern(rows):
    for i in range(rows):
        # Space
        print("   " * (rows - i - 1), end="")

        for j in range(i + 1):
            print(chr(ord("A") + j), end="")
            if j < i:
                print(" ", end="")

        for j in range(i - 1, -1, -1):
            print(" " + chr(ord("A") + j), end="")

        print()


rows = int(input("Enter the number of rows : "))
pattern(rows)
