"""
"M - Coloring Problem"

=> Given an undirected graph and a number m, determine if the graph can be colored with at most
    m colors such that no two adjacent vertices of the graph are colored with the same color.

=> Example

Input:
N = 4
M = 3
E = 5
Edges[] = {
  (0, 1),
  (1, 2),
  (2, 3),
  (3, 0),
  (0, 2)
}

Output: 1

=> Time Complexity : O(N^m)
=> Space Complexity : O(N) + O(N)
"""


def isSafe(node, color, graph, n, col):
    """
    Check if its safe to assign color
    """
    for k in range(n):
        if k != node and graph[k][node] == 1 and color[k] == col:
            return False

    return True


def solve(node, color, m, n, graph):
    """
    Try to color graph
    """

    if node == n:
        return True

    for col in range(1, m + 1):
        if isSafe(node, color, graph, n, col):
            color[node] = col
            if solve(node + 1, color, m, n, graph):
                return True

            # backtrack
            color[node] = 0

    return False


def graphColoring(graph, m, n):
    """
    Determine if the graph can be colored with at most `m` colors such that
    no two adjacent vertices have the same color.
    """
    color = [0] * n
    return solve(0, color, m, n, graph)


N, m = 4, 3

# Initialize 101x101 adjacency matrix
graph = [[0 for _ in range(101)] for _ in range(101)]

# Add edges: (0-1), (1-2), (2-3), (3-0), (0-2)
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
for u, v in edges:
    graph[u][v] = 1
    graph[v][u] = 1  # Since the graph is undirected

# Output the result
print(1 if graphColoring(graph, m, N) else 0)
