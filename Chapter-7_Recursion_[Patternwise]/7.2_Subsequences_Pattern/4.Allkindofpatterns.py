"""
"All Sort of Patterns in Recursion"
"""

# Time Complexity : O(2^n)
# Problem
"""Printing Subsequences whose sum is K

=> We follow the concept of take | Not take.

Example : arr = [1,2,1] sum = 2 -> subsequences : [1,1] , [2] 
"""


def subSequenceSumK(i, ds, s, arr, n, summ):
    if i == n:
        if s == summ:
            print(ds)
        return

    # Take
    ds.append(arr[i])
    subSequenceSumK(i + 1, ds, s + arr[i], arr, n, summ)

    # Not take
    ds.pop()
    subSequenceSumK(i + 1, ds, s, arr, n, summ)


arr = [1, 2, 1]
n = len(arr)
summ = 2
subSequenceSumK(0, [], 0, arr, n, summ)

# Problem
"""Print any Subsequence whose sum is K

=> Technique to return one answer only:
    - In the base case if satisfies -> True else False
    - Then during function call check if true , return it .
"""


def subSequenceSumK_one(i, ds, s, arr, n, summ):
    if i == n:
        # Condition Satisfied
        if s == summ:
            print(ds)
            return True

        # Not satisfied
        else:
            return False

    # Take
    ds.append(arr[i])
    if subSequenceSumK_one(i + 1, ds, s + arr[i], arr, n, summ):
        return True

    # Not take
    ds.pop()
    if subSequenceSumK_one(i + 1, ds, s, arr, n, summ):
        return True

    return False


subSequenceSumK_one(0, [], 0, arr, n, summ)

# Problem
"""Count subsequences having sum K

=> Technique to return count:
    - base case satisfied -> ret 1 else 0
    - call left , right
    - return left + right
"""


def subSequenceSumK_count(i, s, arr, n, summ):
    if i == n:
        # Condition Satisfied
        if s == summ:
            return 1

        # Not satisfied
        else:
            return 0

    # Take
    l = subSequenceSumK_count(i + 1, s + arr[i], arr, n, summ)

    # Not take
    r = subSequenceSumK_count(i + 1, s, arr, n, summ)

    return l + r


subSequenceSumK_count(0, 0, arr, n, summ)
