"""
"Rearrange the elements in +ve , -ve format"

Constraint : positive == negative ( even sized array)

=> Brute Force :

    - Iterate and collect +ve and -ve in two lists.
    - Add elements alternatively i.e. even index +ve and odd i for -ve

=> Time Complexity => O(n) + O(n) = O(2n)
=> Space Complexity => O(n/2) + O(n/2) = O(n)


=> Optimal Approach :

    - Take an ans = []
    - Iterate and check if arr[i] is +ve or -ve
    - If +ve, append to ans[2i] else append to ans[2i + 1]

=> Time Complexity => O(n)
=> Space Complexity => O(n)



=> For variety 2 : Odd Length Array :

=> Time Complexity => O(n) + O(min(len(pos), len(neg))) + O(leftovers)
                               => O(n) + O(n) => O(2n)
=> Space Complexity => O(n)
"""


def rearrangeBrute(arr):
    pos = []
    neg = []

    for i in range(len(arr)):
        if arr[i] > 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])

    for i in range(len(pos)):
        arr[2 * i] = pos[i]

    for i in range(len(neg)):
        arr[2 * i + 1] = neg[i]

    return arr


def rearrangeOptimal(arr):
    ans = [0] * len(arr)

    posI, negI = 0, 1

    for i in range(len(arr)):
        if arr[i] > 0:
            ans[posI] = arr[i]
            posI += 2

        else:
            ans[negI] = arr[i]
            negI += 2

    return ans


def rearrangeOddLen(arr):
    pos, neg = [], []

    for i in range(len(arr)):
        if arr[i] > 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])

    if len(pos) > len(neg):
        for i in range(len(neg)):
            arr[i * 2] = pos[i]
            arr[i * 2 + 1] = neg[i]

        index = len(neg) * 2
        for i in range(len(neg), len(pos)):
            arr[index] = pos[i]
            index += 1

    else:
        for i in range(len(pos)):
            arr[i * 2] = pos[i]
            arr[i * 2 + 1] = neg[i]

        index = len(pos) * 2
        for i in range(len(pos), len(neg)):
            arr[index] = neg[i]
            index += 1

    return arr


# Test cases
print(rearrangeOddLen([1, -2, 3, -4, 5, 6, 8]))
print(rearrangeOddLen([-1, -2, -3, -4, 5, 6]))

arr = [-1, 2, -4, -5]
print(rearrangeOptimal(arr))
