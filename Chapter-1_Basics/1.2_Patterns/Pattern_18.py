"""
E
D E
C D E
B C D E
A B C D E
"""


def pattern(rows):
    for i in range(rows):
        start_char = chr(ord("E") - i)
        for j in range(i + 1):
            print(chr(ord(start_char) + j), end=" ")

        print()


rows = int(input("Enter the number of rows : "))
pattern(rows)
