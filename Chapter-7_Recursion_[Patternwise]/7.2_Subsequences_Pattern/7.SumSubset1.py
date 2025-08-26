"""
"Subset Sum 1"

=> Given an array print all the sum of the subset generated from it, in the increasing order.

=> Example :

n = 3
arr = [3 , 1 , 2]

O/P = [0 , 1 , 2 , 3 , 4 , 5 , 6]

Time Complexity : O(2^n log(2^n))
Space Complexity : O(2^n)
"""


def subsetSum1(arr, n, idx, current_sum, ans):
    if ans is None:
        ans = []

    if idx == n:
        ans.append(current_sum)
        return ans

    # Include current element
    subsetSum1(arr, n, idx + 1, current_sum + arr[idx], ans)

    # Exclude current element
    subsetSum1(arr, n, idx + 1, current_sum, ans)

    return ans


arr = [3, 1, 2]
n = 3
ans = subsetSum1(arr, n, 0, 0, [])
ans.sort()
for s in ans:
    print(s, end=" ")
print()
