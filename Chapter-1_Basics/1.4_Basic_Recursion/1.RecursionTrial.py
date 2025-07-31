"""
Recursion is a programming concept where a function calls itself.
Here in the first trial we have printed a function that calls itself.
But its a bad practice as its infinite loop.

"Infinite Recursion"

def recursion():
    print("Recursion")
    recursion()

a = recursion()
print(a)

Now to avoid such issues, we use "base case" or "stopping condition".
"""
# Base case


def recursion(count=0):
    if count == 5:
        return
    print("Recursion", count)
    recursion(count + 1)


recursion()
