"""
Online Stock Span

Design an algorithm that collects daily stock prices and returns the span
of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days
(starting from today and going backward) for which the price of the stock was less than
or equal to today's price.

Implement the StockSpanner class:
    - StockSpanner() Initializes the object of the class.
    - int next(int price) Returns the span of the stock's price given that today's price is `price`.

Example:
    Input:
        ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
        [[], [100], [80], [60], [70], [60], [75], [85]]

    Output:
        [null, 1, 1, 1, 2, 1, 4, 6]

    Explanation:
        StockSpanner stockSpanner = new StockSpanner();
        stockSpanner.next(100); // return 1
        stockSpanner.next(80);  // return 1
        stockSpanner.next(60);  // return 1
        stockSpanner.next(70);  // return 2
        stockSpanner.next(60);  // return 1
        stockSpanner.next(75);  // return 4
        stockSpanner.next(85);  // return 6

Constraints:
    - 1 <= price <= 10^5
    - At most 10^4 calls to next() will be made.

Optimal Approach:
    Use a monotonic decreasing stack that stores pairs (price, span).
    - For each new price, pop from the stack while the price at the top is less than or equal to current.
    - Accumulate the span by adding the popped spans.
    - Push (price, span) onto the stack and return the span.

Time Complexity:
    - Amortized O(1) per `next` call (each element is pushed and popped at most once)

Space Complexity:
    - O(n) where n is the number of calls to `next()`, for the stack storage
"""

"""Brute Force
-> TC : O(no. of days)
-> SC : O(total no. of next calls)"""


class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)
        span = 1
        i = len(self.prices) - 2
        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1

        return span


sp = StockSpanner()
print([sp.next(p) for p in [100, 80, 60, 70, 60, 75, 85]])
# Output: [1, 1, 1, 2, 1, 4, 6]

"""Optimal Approach
TC : O(2n)
SC : O(n)"""


class SS:
    def __init__(self):
        self.stack = []

    def next(self, price):
            span = 1
            while self.stack and self.stack[-1][0] <= price:
                _, prev_span = self.stack.pop()
                span += prev_span

            self.stack.append((price, span))
            return span


sp = SS()
print([sp.next(p) for p in [100, 80, 60, 70, 60, 75, 85]])
