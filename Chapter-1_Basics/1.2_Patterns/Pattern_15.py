"""
A B C D E
A B C D
A B C
A B
A

"""


def pattern(rows):
    for i in range(rows, 0, -1):
        ch = "A"
        for j in range(i):
            print(ch, end=" ")
            ch = chr(ord(ch) + 1)

        print()


rows = int(input("Enter the number of rows : "))
pattern(rows)
