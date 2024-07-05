class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows,cols = len(board),len(board[0])
        
        # all eight possible directions
        directions = [(-1,-1),(-1,0),(-1,1),
                      (0,-1),        (0,1),
                      (1,-1),(1,0),(1,1)]
        
        # Use intermediate states:
        # 0 -> 0: dead remains dead
        # 1 -> 1: live remains live
        # 1 -> 0: live becomes dead (mark as 2)
        # 0 -> 1: dead becomes live (mark as 3)

        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0

                #count live neighbors
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (board[nr][nc] == 1 or board[nr][nc] == 2):
                        live_neighbors += 1

                # Apply the Game of Life rules using intermediate states
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2   # live cell dies 
                else:
                    if live_neighbors == 3:
                        board[r][c] = 3 # dead cell becomes live  

        # update the board to the final states
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1