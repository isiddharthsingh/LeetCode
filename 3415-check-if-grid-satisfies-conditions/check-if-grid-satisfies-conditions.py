class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        if not grid:
            return True

        m, n = len(grid), len(grid[0])
    
        for i in range(m):
            for j in range(n):
                # Check vertical condition if not on the last row
                if i < m - 1 and grid[i][j] != grid[i + 1][j]:
                    return False
                
                # Check horizontal condition if not on the last column
                if j < n - 1 and grid[i][j] == grid[i][j + 1]:
                    return False

        return True
