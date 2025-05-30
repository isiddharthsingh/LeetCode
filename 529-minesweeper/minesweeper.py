from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])

        # All 8 directions around a cell (like a compass)
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]

        def count_mines(x, y):
            """Count how many mines surround board[x][y]"""
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check bounds and count if it's a mine
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                    count += 1
            return count

        def dfs(x, y):
            """Reveal the cell and expand if no surrounding mines"""
            # Skip if not unrevealed
            if board[x][y] != 'E':
                return

            # Count adjacent mines
            mines = count_mines(x, y)

            if mines > 0:
                # Set to the number if there are mines nearby
                board[x][y] = str(mines)
            else:
                # No adjacent mines — mark as 'B' and reveal neighbors
                board[x][y] = 'B'
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # Check bounds
                    if 0 <= nx < m and 0 <= ny < n:
                        dfs(nx, ny)

        # Start from the clicked position
        x, y = click
        if board[x][y] == 'M':
            # Game over — clicked a mine
            board[x][y] = 'X'
        else:
            # Explore the board from this point
            dfs(x, y)

        return board