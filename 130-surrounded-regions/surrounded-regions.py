class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board),len(board[0])

        def capture(r,c):
            if (r<0 or c<0 or r==ROWS or c==COLS or board[r][c]!="O"):
                return 
            board[r][c] = "B"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)


        # (DFS) Capture sunsurrounded region i.e border region (O-->B)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c]=="O" and (r in [0,ROWS-1]) or (c in [0,COLS-1])):
                    capture(r,c)
        

        # Capture surrounded region 
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # uncapture surrounded regions 
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "B":
                    board[r][c] = "O"