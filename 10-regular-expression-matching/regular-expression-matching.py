class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}  # Dictionary to store computed results

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]  # Return precomputed result
            if i >= len(s) and j >= len(p):
                return True  # Base case: both strings are empty
            if j >= len(p):
                return False  # Pattern string is exhausted
            
            # Check if characters match or if pattern has a wildcard "."
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] == "*":
                # Handle the case when pattern has a "*"
                cache[(i, j)] = (dfs(i, j + 2) or  # Don't use the "*"
                                match and dfs(i + 1, j))  # Use the "*"
                return cache[(i, j)]
            
            if match:
                # Characters match, move to the next position in both strings
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False
        
        # Start the recursion from the beginning of both strings
        return dfs(0, 0)
