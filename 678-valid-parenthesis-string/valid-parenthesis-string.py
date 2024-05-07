class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0  # Initialize counters for minimum and maximum open parentheses

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1  # Increment both counters
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1  # Decrement both counters
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1  # Treat '*' as both '(' and ')'

            if leftMax < 0:
                return False  # If there are more closing parentheses than opening ones, it's invalid
            if leftMin < 0:
                leftMin = 0  # Reset the minimum counter to zero (cannot have negative open parentheses)

        return leftMin == 0  # Check if all open parentheses are closed
