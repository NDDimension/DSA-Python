# Time Complexity => O(N)
def Give_all_Divisors(N):
    divisors = []
    for divisor in range(1, N + 1):
        if N % divisor == 0:
            divisors.append(divisor)

    return divisors


# Time Complexity => O(sqrt(N)) even faster
def Give_all_DivisorsFast(N):
    divisors = set()

    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            divisors.add(i)
            divisors.add(N // i)

    return sorted(divisors)


N = int(input("Enter Number : "))
print(f"Divisors of {N} => {Give_all_Divisors(N)}")
print(f"Divisors of {N} with faster method => {Give_all_DivisorsFast(N)}")
