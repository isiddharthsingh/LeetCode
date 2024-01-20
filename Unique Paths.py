class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """row = [1]*n

        for i in range(m-1):
            newRow = [1] * n
            #go to every column except the right most one 
            for j in range(n-2,-1,-1):
                # right value + down value (which is at current index j)
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]"""

        dp = [[1 for j in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]