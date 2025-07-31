def natural_numbers_rec(n):
    if n <= 0:
        return []
    return [n] + natural_numbers_rec(n - 1)


n = int(input("Enter a positive integer: "))
print(natural_numbers_rec(n))
