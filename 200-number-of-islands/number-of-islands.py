class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is empty
        if not grid:
            return 0
        
        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        # Set to keep track of visited cells
        visit = set()
        # Counter for the number of islands
        island = 0

        def bfs(r, c):
            # Queue for BFS traversal
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                # Define the four directions: right, left, down, up
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # Check if the new cell is within bounds, is land ('1'), and not visited
                    if (r in range(rows) and
                        c in range(cols) and 
                        grid[r][c] == "1" and 
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land ('1') and not visited, start BFS
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    # Increment island count after exploring connected land
                    island += 1
        
        # Return the total number of islands
        return island