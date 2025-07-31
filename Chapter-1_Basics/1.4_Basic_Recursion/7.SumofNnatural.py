class Sum_of_First_N_natural:
    # Parameterized Version
    def sum_of_N(self, i, summ):
        if i < 1:
            return summ
        return self.sum_of_N(i - 1, summ + i)

    # Functional Version
    def summm(self, n):
        if n == 0:
            return 0
        return n + self.summm(n - 1)


i = int(input("Enter N for parameterized version: "))
n = int(input("Enter N for functional version: "))

Parameter = Sum_of_First_N_natural()
print("Parameterized version sum:", Parameter.sum_of_N(i, 0))

Functional = Sum_of_First_N_natural()
print("Functional version sum:", Functional.summm(n))
