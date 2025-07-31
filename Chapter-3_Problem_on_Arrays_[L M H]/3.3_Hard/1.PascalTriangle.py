"""
"Pascal Triangle Problem"

=> 3 Types

1. Given Row and Column => print the element residing there
2. Given the row no. => Print the whole row
3. Given n =>  Print the whole pascal

"""

"""
"Type 1"

-> Given row => find R-1 and Colum => C - 1

Perform (R-1) C (C-1) =  (R - 1) ! / (C - 1) ! x (R - C) !

=> Trick !! 

Given 'r' take the "c" upto that much count only 
like if 10C3 is given then r = 3 therefore run c = 10 till 10 x 9 x 8

=> Time Complexity = O(R)
=> Space Complexity = O(1) 
"""


def nCr(n, r):
    res = 1

    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)

    return res


def pascalTriangle(r, c):
    element = nCr(r - 1, c - 1)
    return element


"""
"Type 2"

=> Given row no use our nCr strategy to run the calculation
till row no.

=> Time Complexity = O(R)
=> Space Complexity = O(1) [ if not using list] 

"""


def pascalRow(r):
    for i in range(1, r + 1):
        print(nCr(r - 1, i - 1), end=" ")
    print()


import math


def pascalRowusingLib(r):
    return [math.comb(r - 1, i) for i in range(r)]


def pascalRowOptimized(r):
    ans = 1
    row = [ans]
    r = r - 1
    for i in range(r):
        ans = ans * (r - i)
        ans = ans // (i + 1)
        row.append(ans)
    return row


"""
"Type 3"

=> Using the nCr store all results in list and print it 

=> Time Complexity = O(R^3)
=> Space Complexity = O(1)

=> Using row generator and then triangle also can be done

=> Time Complexity = O(R^2)
=> Space Complexity = O(1)


"""


def pascalTriangleFull(n):
    ans = []

    for r in range(1, n + 1):
        temo = []
        for c in range(1, r + 1):
            temo.append(nCr(r - 1, c - 1))
        ans.append(temo)
    return ans


def pascalTriangleOpt(n):
    ans = []

    for i in range(1, n + 1):
        ans.append(pascalRowOptimized(i))

    return ans


def print_triangle(ans):
    for i in ans:
        print(" ".join(map(str, i)))


r, c = 5, 3
print_triangle(pascalTriangleOpt(r))
