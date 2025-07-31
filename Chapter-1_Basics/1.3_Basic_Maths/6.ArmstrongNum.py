"""
Armstrong Number

Logic => Extract digits
             sum of the (extracted digits)^lengthofNumber
             if sum == given no. ? Armstrong else NOT
"""


def Armstrong(N):
    original_no = N
    no_of_digits = len(str(N))
    summation = 0

    while N > 0:
        ld = N % 10
        summation = summation + (ld**no_of_digits)
        N = N // 10

    return summation == original_no


N = int(input("Enter Number: "))
print(f"Armstrong {N} ? => {Armstrong(N)}")
