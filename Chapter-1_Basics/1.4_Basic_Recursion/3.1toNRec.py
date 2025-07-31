def natural_numbers_rec(n):
    if n <= 0:
        return []
    return natural_numbers_rec(n - 1) + [n]


n = int(input("Enter a positive integer: "))
print(natural_numbers_rec(n))
