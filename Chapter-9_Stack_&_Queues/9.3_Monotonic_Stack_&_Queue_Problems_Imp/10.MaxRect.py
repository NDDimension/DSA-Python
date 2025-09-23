"""
Given a 2D binary matrix filled with '0's and '1's, find the largest rectangle
containing only 1's and return its area.

This problem is a 2D extension of the "Largest Rectangle in Histogram" problem.
The idea is to treat each row as the base of a histogram and update the height
of each column as you iterate through the rows. Then, for each row, use the
Largest Rectangle in Histogram algorithm to compute the maximal area.

Parameters:
-----------
matrix : List[List[str]]
    A 2D list of strings where each element is either '0' or '1'.

Returns:
--------
int
    The area of the largest rectangle containing only '1's in the matrix.

Constraints:
-----------
- m == len(matrix)
- n == len(matrix[0]) if matrix is not empty
- 1 <= m, n <= 200
- matrix[i][j] is '0' or '1'

Example:
--------
>>> maximalRectangle([
...   ["1","0","1","0","0"],
...   ["1","0","1","1","1"],
...   ["1","1","1","1","1"],
...   ["1","0","0","1","0"]
... ])
6
Explanation:
The maximal rectangle of 1s has area 6, formed between row 2 and row 3, columns 1 to 4.

Optimal Approach:
-----------------
- Use a height array to represent a histogram for each row.
- For each row, update the histogram: if current cell is '1', increment height;
  if '0', reset height to 0.
- For each updated row, apply the Largest Rectangle in Histogram (using a monotonic stack)
  to find the maximal rectangle for that histogram.
- This results in an O(m * n) time solution, where m is the number of rows and n is the number of columns.
"""


# TC : O(m x n) + O(n x 2m)
# SC : O(n x m) + O(n)
def largestHist(arr):
    st = []
    maxArea = 0
    for i in range(len(arr)):
        while st and arr[st[-1]] > arr[i]:
            height = arr[st.pop()]
            width = i if not st else i - st[-1] - 1
            maxArea = max(maxArea, height * width)
        st.append(i)

    n = len(arr)
    while st:
        height = arr[st.pop()]
        width = n if not st else n - st[-1] - 1
        maxArea = max(maxArea, height * width)

    return maxArea


def MaximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix)
    m = len(matrix[0])
    maxArea = 0

    # Initialize histogram heights
    height = [0] * m

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                height[j] += 1
            else:
                height[j] = 0

        # Apply Largest Rectangle in Histogram on current row's histogram
        maxArea = max(maxArea, largestHist(height))

    return maxArea


print(
    MaximalRectangle(
        [
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0],
        ]
    )
)  # Output: 6 ✅
