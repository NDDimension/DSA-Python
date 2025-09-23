"""
Find the Celebrity (The Celebrity Problem)

A celebrity is defined as someone who is known by everyone else but knows no one.

You are given a helper function `knows(a, b)` that returns:
    - True if person `a` knows person `b`, and
    - False otherwise.

You must find the **celebrity** among `n` people at a party (labeled from 0 to n - 1), or return -1 if there is no celebrity.

Your task is to implement the function `findCelebrity(n)` which returns the index of the celebrity, or -1 if none exists.

Function Signature:
def findCelebrity(n: int) -> int:

Helper Function:
def knows(a: int, b: int) -> bool:
    # Provided by the problem environment. Returns True if a knows b, else False.

Constraints:
- 1 <= n <= 100
- There is exactly one celebrity or no celebrity at all.
- A person does not know themselves.

Optimal Approach:
- Time Complexity: O(n)
- Space Complexity: O(1)

We can solve this problem optimally in **O(n)** time using the following two-pass strategy:

1. **Candidate Identification (First Pass)**:
    - Start by assuming person 0 is a celebrity candidate.
    - Iterate through people from 1 to n-1.
    - If the current candidate knows person `i`, then the candidate cannot be a celebrity (since a celebrity knows no one).
    - In this case, update the candidate to `i`.

2. **Verification (Second Pass)**:
    - After the first pass, we have a candidate who might be a celebrity.
    - We verify the candidate by checking:
        - The candidate does **not** know anyone else.
        - Everyone else **knows** the candidate.
    - If either condition fails for any person, return -1.

Example:
Input: n = 3
Matrix (knows):
    0 1 2
0 [F T F]
1 [F F F]
2 [F T F]

Person 1 is the celebrity:
- 0 knows 1 ✅
- 2 knows 1 ✅
- 1 knows no one ✅

Output: 1
"""

"""Brute Force
TC : O(n^2) + O(n)
SC : O(2n)"""


def cp(matrix):
    n = len(matrix)
    iknow = [0] * n  # How many people i knows
    knowme = [0] * n  # How many people know i

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                iknow[i] += 1
                knowme[j] += 1

    for i in range(n):
        if iknow[i] == 0 and knowme[i] == n - 1:
            return i

    return -1


print(cp([[0, 1, 0], [0, 0, 0], [0, 1, 0]]))

"""Optimal Approach
TC : O(n)
SC : O(1 )"""


def CelebProb(matrix):
    n = len(matrix)
    candidate = 0

    # Step 1: Find the potential candidate
    for i in range(1, n):
        if matrix[candidate][i] == 1:
            # candidate knows i → can't be a celebrity
            candidate = i
        # else, i can't be a celebrity, so we keep candidate

    # Step 2: Verify the candidate
    for i in range(n):
        if i == candidate:
            continue
        if matrix[candidate][i] == 1 or matrix[i][candidate] == 0:
            return -1

    return candidate


print(CelebProb([[0, 1, 0], [0, 0, 0], [0, 1, 0]]))
