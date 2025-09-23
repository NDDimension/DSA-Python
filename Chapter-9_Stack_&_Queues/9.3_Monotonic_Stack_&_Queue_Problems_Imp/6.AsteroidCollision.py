"""
Asteroid Collision

Simulates asteroid collisions and returns the state of asteroids after all collisions.

Asteroids are represented by integers where the absolute value indicates the size and the sign indicates the direction:
- A positive integer means the asteroid is moving to the right.
- A negative integer means the asteroid is moving to the left.

When two asteroids collide (i.e., one moves right and the other moves left), the larger asteroid survives. If both asteroids are of the same size, both are destroyed.

The function processes the list of asteroids and determines the final state of the asteroids after all collisions.

Approach:
1. Use a stack to simulate the movement and collision of asteroids.
2. Iterate over each asteroid in the list:
   - If the asteroid is moving to the right (positive), push it onto the stack.
   - If the asteroid is moving to the left (negative), check for collisions:
     - If the top of the stack is a right-moving asteroid (positive), compare their sizes.
     - If the left asteroid is larger, pop the right asteroid off the stack (it gets destroyed).
     - If the right asteroid is larger or the same size, pop the left asteroid off the stack (it gets destroyed).
     - If no collision occurs, add the asteroid to the stack.
3. The stack will contain the final state of the asteroids after all collisions have been processed.

Time Complexity:
- O(n), where n is the number of asteroids. Each asteroid is processed at most twice (once when added and possibly once when removed from the stack).

Space Complexity:
- O(n), in the worst case where no collisions occur and all asteroids remain in the stack.

Parameters:
asteroids (List[int]): A list of integers representing the asteroids.

Returns:
List[int]: A list representing the asteroids that remain after all collisions.

Example:
Input:
asteroids = [5, 10, -5]

Output:
[5, 10]

Explanation:
- The first asteroid (5) moves to the right, so it is added to the stack.
- The second asteroid (10) moves to the right, so it is also added to the stack.
- The third asteroid (-5) moves to the left. It collides with the asteroid 10, and since 10 is larger, -5 is destroyed.
- The stack contains [5, 10] after the collisions, which is the final result.
"""


# TC : O(2n)
# SC : O(n)
def AsteroidCollision(arr):
    st = []
    for a in arr:
        while st and a < 0 < st[-1]:
            if st[-1] < -a:
                st.pop()
                continue
            elif st[-1] == -a:
                st.pop()
            break
        else:
            st.append(a)
    return st


AsteroidCollision([5, 10, -5])
