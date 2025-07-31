"""
Reverse a Number :

Logic => Do the extraction
             reverse_num = (reverse_num x 10) + last_digit
"""


def Reverse_Number(N):
    rev_no = 0

    if N == 0:
        return 0
    while N > 0:
        ld = N % 10
        rev_no = (rev_no * 10) + ld
        N = N // 10

    return rev_no


N = int(input("Enter Number"))
print(f"Reverse of {N} = {Reverse_Number(N)}")
