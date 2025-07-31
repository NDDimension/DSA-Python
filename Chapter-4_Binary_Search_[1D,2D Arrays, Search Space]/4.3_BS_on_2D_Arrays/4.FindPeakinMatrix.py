"""
"Find Peak element in the Matrix"

=> Given a matrix we need to find its peak -> element greater than top , bottom , right and left.
"""


# Brute : Stand at each pos and check for all 4 directions
# TC : O(4NM)
# SC : O(1)
def findPeak_Brute(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (
                (i == 0 or matrix[i][j] > matrix[i - 1][j])
                and (i == len(matrix) - 1 or matrix[i][j] > matrix[i + 1][j])
                and (j == 0 or matrix[i][j] > matrix[i][j - 1])
                and (j == len(matrix[0]) - 1 or matrix[i][j] > matrix[i][j + 1])
            ):
                return matrix[i][j]
    return -1


# Brute Optimized a bit : return the largest
# TC : O(NM)
# SC : O(1)
def findPeak_Brute_OP(matrix):
    return max(max(row) for row in matrix)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(findPeak_Brute(matrix))
print(findPeak_Brute_OP(matrix))


# Optimal Approach : Using Binary Search
# TC : O(N log M)
# SC : O(1)


def findPeak_BS(matrix):
    n, m = len(matrix), len(matrix[0])
    low, high = 0, m - 1

    while low <= high:
        mid = (low + high) // 2
        row = max(range(n), key=lambda x: matrix[x][mid])
        left = matrix[row][mid - 1] if mid - 1 >= 0 else float("-inf")
        right = matrix[row][mid + 1] if mid + 1 < m else float("-inf")

        if matrix[row][mid] > left and matrix[row][mid] > right:
            return matrix[row][mid]
        elif matrix[row][mid] < left:
            high = mid - 1
        else:
            low = mid + 1

    return -1


print(findPeak_BS(matrix))
