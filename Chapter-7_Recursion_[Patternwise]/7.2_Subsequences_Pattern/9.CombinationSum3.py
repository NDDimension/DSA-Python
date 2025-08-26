"""
"Combination Sum 3"

=> Given n and k value we need to return the combination that sums to k using only n integers from 1 to 9.

=> Example:

n = 3 , k = 7

O/P => [1 , 2,  4]

Time Complexity : O(C(9,k) * k)
Space Complexity : O(C(9,k) * k) + O(k)
"""


def combinationSum3(n, k):
    ans = []

    def helper(start, path, target):
        if len(path) == k:
            if target == 0:
                ans.append(path[:])
            return

        for i in range(start, 10):
            if i > target:
                break

            path.append(i)
            helper(i + 1, path, target - i)
            path.pop()

    helper(1, [], n)
    return ans


result = combinationSum3(7, 3)
for comb in result:
    print(comb)
