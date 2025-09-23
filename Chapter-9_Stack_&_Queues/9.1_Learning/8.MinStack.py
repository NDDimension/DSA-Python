"""
"Min Stack"

Problem Statement: Implement Min Stack | O(2N) and O(N) Space Complexity.
                                Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Examples:

Input Format:["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
[
[ ], [-2], [0], [-3], [ ], [ ], [ ], [ ]
]

Result: [null, null, null, null, -3, null, 0, -2]
Explanation:
stack < long long > st
st.push(-2); Push element in stack
st.push(0); Push element in stack
st.push(-3); Push element in stack
st.getMin(); Get minimum element fromstack
st.pop(); Pop the topmost element
st.top(); Top element is 0
st.getMin(); Minimum element is -2

"""


# Using Two Stacks
# TC : O(1)
# SC : O(n)
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):
        if not self.stack:
            return
        val = self.stack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def getMin(self):
        if not self.minStack:
            raise IndexError("Stack is empty")
        return self.minStack[-1]


s = MinStack()
s.push(3)
s.push(5)
print(s.getMin())
s.push(2)
s.push(2)
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin())


# Using Single Stack
# TC : O(1)
# SC : O(n)
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))  # (value, current_min)
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack[-1][1]


"""
✅ Concept: Space-Optimized Min Stack Using Encoding

The idea is:

Maintain a single stack and a variable minVal to track the current minimum.

When pushing a new value:

If the new value is greater than or equal to minVal, push it normally.

If it's less than minVal, you push an encoded value:
encoded = 2 * val - minVal
And update minVal = val.

On popping:

If the top is greater than or equal to minVal, it's a normal value.

If the top is less than minVal, it means it's an encoded value → we decode the previous minimum using:
previousMin = 2 * minVal - encoded

This saves space because we don’t store the minimums explicitly for each value.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.minVal = val

        elif val >= self.minVal:
            self.stack.append(val)

        else:
            # Encode
            enc = 2 * val - self.minVal
            self.stack.append(enc)
            self.minVal = val

    def pop(self):
        if not self.stack:
            return
        top = self.stack.pop()
        if top < self.minVal:
            # Decode
            self.minVal = 2 * self.minVal - top

    def top(self):
        if not self.stack:
            raise IndexError("Stack is Empty")
        top = self.stack[-1]
        if top >= self.minVal:
            return top
        else:
            # Encode Actual top
            return self.minVal

    def getMin(self):
        if self.minVal is None:
            raise IndexError("Stack is empty")
        return self.minVal


s = MinStack()
s.push(5)
s.push(3)
print(s.getMin())  # Output: 3
s.push(2)
print(s.getMin())  # Output: 2
s.pop()
print(s.getMin())  # Output: 3
print(s.top())  # Output: 3
s.pop()
print(s.top())  # Output: 5
