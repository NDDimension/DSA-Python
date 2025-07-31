"""
A
A B
A B C
A B C D
A B C D E

"""


def pattern(rows):
    for i in range(rows + 1):
        ch = "A"
        for j in range(i):
            print(ch, end=" ")
            ch = chr(ord(ch) + 1)

        print()


rows = int(input("Enter the number of rows : "))
pattern(rows)
