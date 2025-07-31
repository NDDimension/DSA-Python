"""
A
B B
C C C
D D D D
E E E E E

"""


def pattern(rows):
    for i in range(rows + 1):
        ch = chr(ord("A") + i - 1)
        for j in range(i):
            print(ch, end=" ")

        print()


rows = int(input("Enter the number of rows : "))
pattern(rows)
