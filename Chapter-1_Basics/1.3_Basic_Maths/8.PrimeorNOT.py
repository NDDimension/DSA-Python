def Prime_Brute(N):
    if N <= 1:
        return False

    divisors = set()
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            divisors.add(i)
            divisors.add(N // i)

    return len(divisors) == 2


# Input
N = int(input("Enter Number: "))
if Prime_Brute(N):
    print(f"{N} is Prime ✅")
else:
    print(f"{N} is Not Prime ❌")
