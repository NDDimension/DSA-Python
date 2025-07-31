"""
"Find the Missing and Repeating Number from the array"

=> Given an array find out which number is missing and which number is repeating.

Example -> [1,1,2,3,4,6]
Repeating -> 1
Missing -> 5
"""

"""
=> Brute Force:
    - Iterate and find out both.

=> Time Complexity : O(n^2)
=> Space Complexity : O(1)     
"""


def findMissingRepeating(arr):
    n = len(arr)
    miss = rep = -1

    for i in range(1, n + 1):
        count = 0
        for j in range(n):
            if arr[j] == i:
                count += 1
        if count == 2:
            rep = i
        elif count == 0:
            miss = i

        if miss != -1 and rep != -1:
            break

    return miss, rep


arr = [1, 1, 2, 3, 4, 6]
miss, rep = findMissingRepeating(arr)
print(f"Missing -> {miss}\nRepeating -> {rep}")

"""
=> Better Approach :
    - using hashing

=> Time Complexity : O(2n)
=> Space Complexity : O(n)     
"""


def findMissingRepeatingBetter(arr):
    n = len(arr)
    miss = rep = -1
    hashh = [0] * (n + 1)

    for i in range(n):
        hashh[arr[i]] += 1

    for i in range(1, n + 1):
        if hashh[i] == 2:
            rep = i
        elif hashh[i] == 0:
            miss = i

        if miss != -1 and rep != -1:
            break

    return miss, rep


arr = [1, 1, 2, 3, 4, 6]
miss, rep = findMissingRepeatingBetter(arr)
print(f"Missing -> {miss}\nRepeating -> {rep}")

"""
=> Optimal Approach :

    - using MATHS
    - find difference between sum and natural sum 
    - find the difference between sum of squares and natural sum of squares
    - take two equations and find their answers 
    - its our missing and repeating number

=> Time Complexity : O(n)
=> Space Complexity : O(1)     

    - using XOR method

=> Time Complexity : O(n)
=> Space Complexity : O(1)     
"""


def findMissingRepeatingOptimal(arr):
    n = len(arr)

    # Sum and Sum of Squares of Natural Numbers
    Sn = (n * (n + 1)) // 2
    Sn2 = (n * (n + 1) * (2 * n + 1)) // 6

    # Sum and Sum of Squares of Given Array
    S1 = sum(arr)
    S2 = sum([x * x for x in arr])

    eq1 = Sn - S1
    eq2 = Sn2 - S2

    val = eq2 // eq1

    miss = (val + eq1) // 2
    rep = val - miss

    return miss, rep


arr = [1, 1, 2, 3, 4, 6]
miss, rep = findMissingRepeatingOptimal(arr)
print(f"Missing -> {miss}\nRepeating -> {rep}")


def findMissingRepeatingOptimal2(arr):
    n = len(arr)

    xr = 0
    for i in range(n):
        xr ^= arr[i]
        xr ^= i + 1

    number = xr & ~(xr - 1)

    zero, one = 0, 0
    for i in range(n):
        if (arr[i] & number) != 0:
            one = one ^ arr[i]
        else:
            zero = zero ^ arr[i]

    for i in range(1, n + 1):
        if (i & number) != 0:
            one = one ^ i
        else:
            zero = zero ^ i

    cnt = 0
    for i in range(n):
        if arr[i] == zero:
            cnt += 1

    if cnt == 2:
        return [one, zero]
    return [zero, one]


arr = [1, 1, 2, 3, 4, 6]
miss, rep = findMissingRepeatingOptimal2(arr)
print(f"Missing -> {miss}\nRepeating -> {rep}")
