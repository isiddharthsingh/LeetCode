class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Get number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])

        # Step 1: Create a padded DP table `res` of size (ROWS+1) x (COLS+1)
        # Initialize all values to infinity (represents unreachable path)
        res = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]

        # Step 2: Set base case
        # This is a trick: place a 0 just "outside" the destination cell
        res[ROWS - 1][COLS] = 0

        # Step 3: Fill the DP table from bottom-right to top-left
        for r in range(ROWS - 1, -1, -1):  # from ROWS-1 down to 0
            for c in range(COLS - 1, -1, -1):  # from COLS-1 down to 0
                # Take current grid value plus min of right and down neighbors
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])

        # Step 4: Return the value at the top-left corner
        return res[0][0]