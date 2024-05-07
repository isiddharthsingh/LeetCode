class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)  # Size of the grid

        # Initialize a set to track visited cells and a min heap with (time, row, column)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]

        # Possible directions: right, left, down, up
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))  # Mark the starting cell as visited
        while minHeap:
            time, row, col = heapq.heappop(minHeap)
            if row == N - 1 and col == N - 1:
                return time  # If we reach the target cell, return the total time
            for dr, dc in directions:
                neiR, neiC = row + dr, col + dc
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visit):
                    continue  # Skip invalid or already visited cells
                visit.add((neiR, neiC))
                heapq.heappush(minHeap, [max(time, grid[neiR][neiC]), neiR, neiC])

        # If we cannot reach the target cell, return -1
        return -1
