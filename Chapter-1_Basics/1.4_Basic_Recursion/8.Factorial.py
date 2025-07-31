class Factorial:
    def Para_fact(self, i, fact):
        if i == 0 or i == 1:
            return fact

        return self.Para_fact(i - 1, fact * i)

    def Funct_fact(self, n):
        if n == 0 or n == 1:
            return 1

        return n * self.Funct_fact(n - 1)


i = int(input("Enter N for parameterized version: "))
n = int(input("Enter N for functional version: "))

Parameter = Factorial()
print("Parameterized version factorial:", Parameter.Para_fact(i, 1))

Functional = Factorial()
print("Functional version sum:", Functional.Funct_fact(n))
