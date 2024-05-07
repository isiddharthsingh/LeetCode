class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # Initialize a dictionary to store LIP values for each cell

        def dfs(r, c, preVal):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                matrix[r][c] <= preVal):
                return 0  # Base case: invalid cell or non-increasing value
            if (r, c) in dp:
                return dp[(r, c)]  # Return the cached result if available

            # Explore all four directions and calculate the LIP value
            res = 1
            res = max(res,1 +  dfs(r + 1, c, matrix[r][c]))
            res = max(res,1 +  dfs(r - 1, c, matrix[r][c]))
            res = max(res,1 +  dfs(r, c + 1, matrix[r][c]))
            res = max(res,1 +  dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res  # Cache the result
            return res

        # Apply DFS to each cell to find the longest increasing path
        max_length = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_length = max(max_length, dfs(r, c, float('-inf')))

        return max_length  # Return the maximum LIP value
