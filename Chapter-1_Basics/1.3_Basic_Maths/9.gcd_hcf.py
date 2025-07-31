# Time Complexity => O(min(n1,n2))
def gcd_hcf(n1, n2):
    gcd = 1
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i

    return gcd


# Time Complexity => O(log_phi min(a,b))
def Euclidean_Algo(n1, n2):
    gcd = 1
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1

        if n1 == 0:
            gcd = n2
        else:
            gcd = n1

    return gcd


n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
print(f"GCD({n1},{n2}) => {gcd_hcf(n1, n2)}")
print(f"Eucledian GCD({n1},{n2}) => {Euclidean_Algo(n1, n2)}")

"""
More cleaner version of Euclidean:

def gcd_hcf(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return abs(n1)

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
print(f"GCD({n1}, {n2}) => {gcd_hcf(n1, n2)}")

"""
