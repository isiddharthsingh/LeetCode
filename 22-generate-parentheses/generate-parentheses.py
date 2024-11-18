class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Stack to store the current sequence of parentheses
        stack = []
        # Result list to store all valid combinations
        res = []

        # Backtracking function
        def backtrack(openP, closedP):
            # Base case: If we have used all open and close parentheses
            if openP == closedP == n:
                # Join the stack to form a valid combination and add to result
                res.append("".join(stack))
                return
            
            # If we can still add an open parenthesis
            if openP < n:
                stack.append("(")            # Add an open parenthesis
                backtrack(openP + 1, closedP) # Recurse with incremented open count
                stack.pop()                  # Backtrack: remove the last added parenthesis

            # If we can still add a close parenthesis without violating the rules
            if closedP < openP:
                stack.append(")")            # Add a close parenthesis
                backtrack(openP, closedP + 1) # Recurse with incremented close count
                stack.pop()                  # Backtrack: remove the last added parenthesis

        # Start the backtracking with 0 open and close parentheses
        backtrack(0, 0)
        return res
