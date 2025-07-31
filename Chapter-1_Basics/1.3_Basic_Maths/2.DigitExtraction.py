"""
Digit Extraction

7789 -> 7,7,8,9

Logic => 1. (number % 10)
             2. (number // 10)

Note : Perform "integer division //" not "float division /"

"""

N = int(input("Enter Number : "))
digits = []

while N > 0:
    last_digit = N % 10
    N = N // 10
    digits.append(last_digit)

print(digits[::-1])
