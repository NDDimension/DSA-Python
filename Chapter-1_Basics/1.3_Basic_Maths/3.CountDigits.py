"""
Count Digits

Concept is same as ExtractDigits

Time Complexity => O(log_10(N)) as division by 10

Note : "As an when there is something division and time complexity is depended on it
            then in Time Complexity "Log" will be present"
"""

import math


def step_method(N):
    digits = []
    while N > 0:
        last_digit = N % 10
        N = N // 10
        digits.append(last_digit)
    return digits[::-1]  # Return in original order


def no_last_digit_method(N):
    if N == 0:
        return 1
    count = 0
    while N > 0:
        count += 1
        N = N // 10
    return count


def log_method(N):
    if N == 0:
        return 1  # log10(0) is undefined
    return int(math.log10(N)) + 1


# Main code
N = int(input("Enter Number: "))

# Step Method
digits = step_method(N)
print("Step Method:")
print(f"Digits = {digits}")
print(f"Number of digits = {len(digits)}\n")

# Direct Method
print("Direct Method:")
print(f"Number of digits = {no_last_digit_method(N)}\n")

# Log Method
print("Log Method:")
print(f"Number of digits = {log_method(N)}")
