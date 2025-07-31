"""
Palindrome :

Logic => Do the extraction
             reverse_num = (reverse_num x 10) + last_digit
             check number = reverse_number if "True" then "palindrome"
"""


def Palindrome(N):
    original_no = N
    rev_no = 0

    if N == 0:
        return 0
    while N > 0:
        ld = N % 10
        rev_no = (rev_no * 10) + ld
        N = N // 10

    return original_no == rev_no


N = int(input("Enter Number"))
print(f"Palindrome {N} ? => {Palindrome(N)}")
