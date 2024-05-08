class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}  # Initialize a dictionary to store results for (i, j) pairs

        def dfs(i, j):
            if j == len(t):
                return 1  # Base case: t is fully matched
            if i == len(s):
                return 0  # Base case: s is exhausted
            if (i, j) in cache:
                return cache[(i, j)]  # Return the cached result if available
            
            # If s[i] matches t[j], consider both including and excluding s[i]
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)  # Exclude s[i]
            return cache[(i, j)]

        return dfs(0, 0)  # Start the recursion from index 0 for both s and t
