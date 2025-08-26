"""
"Rat In the Maze"

=> Consider a rat placed at (0, 0) in a square matrix of order N * N.
    It has to reach the destination at (N - 1, N - 1).
    Find all possible paths that the rat can take to reach from source to destination.
    The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right).
    Value 0 at a cell in the matrix represents that it is blocked and the rat cannot move to
    it while value 1 at a cell in the matrix represents that rat can travel through it.

=> Note: In a path, no cell can be visited more than one time.

=> Example:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
        {1, 1, 0, 1},
        {1, 1, 0, 0},
        {0, 1, 1, 1}}

Output: DDRDRR DRDDRR

Time Complexity : O(4^(n x m))
Space Complexity : O(m x n)
"""


# Recursive function to explore the maze
def solve(i, j, maze, n, path, move, visited, di, dj):
    # If we've reached the destination (bottom-right corner)
    if i == n - 1 and j == n - 1:
        path.append(move)  # Store the current path
        return

    directions = "DLRU"  # D = Down, L = Left, R = Right, U = Up

    # Try all 4 directions one by one
    for index in range(4):
        next_i = i + di[index]  # Row index for next move
        next_j = j + dj[index]  # Column index for next move

        # Check if next cell is within bounds, not visited, and not blocked (i.e., cell == 1)
        if (
            0 <= next_i < n
            and 0 <= next_j < n
            and not visited[next_i][next_j]
            and maze[next_i][next_j] == 1
        ):
            visited[i][j] = 1  # Mark current cell as visited
            # Recur with updated position and path
            solve(
                next_i, next_j, maze, n, path, move + directions[index], visited, di, dj
            )
            visited[i][j] = 0  # Backtrack: unmark the cell for other paths


# Main function to initiate path finding
def find_path(maze, n):
    path = []  # List to store all valid paths
    visited = [[0] * n for _ in range(n)]  # Visited matrix initialized to 0

    # Movement vectors: Down, Left, Right, Up
    di = [1, 0, 0, -1]  # Row movement
    dj = [0, -1, 1, 0]  # Column movement

    # Only start if the starting cell is not blocked
    if maze[0][0] == 1:
        solve(0, 0, maze, n, path, "", visited, di, dj)

    return path  # Return all found paths


# Main program
if __name__ == "__main__":
    n = 4  # Size of the maze (n x n)

    # Maze grid: 1 = path, 0 = blocked
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]

    # Find all valid paths from (0, 0) to (n-1, n-1)
    result = find_path(maze, n)

    # If no path found, print -1
    if not result:
        print(-1)
    else:
        # Print all found paths separated by space
        for path in result:
            print(path, end=" ")
    print()  # Print newline at the end
