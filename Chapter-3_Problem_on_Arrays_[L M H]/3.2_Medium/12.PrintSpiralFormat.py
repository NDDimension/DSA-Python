"""
" Return Matrix in Spiral Order "

=> Move Left -> Right -> Down -> Right -> Left -> Top

=> Time Complexity : O (n x m)
=> Space Complexity : O (n)

"""


def print_spiral(matrix):
    ans = []

    n = len(matrix)
    m = len(matrix[0])

    top, left, bottom, right = 0, 0, n - 1, m - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            ans.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])

            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])

            left += 1

    return ans


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print(print_spiral(matrix))
