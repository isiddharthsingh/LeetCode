from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        # Reverse the board to make it easier to work with
        board.reverse()

        def intToPos(square):
            # Convert a square number to board coordinates
            r = (square-1)//length
            c = (square-1)%length
            if r%2:
                c = length-1-c
            return [r,c]
        
        q = deque()
        # Start from square 1 with 0 moves
        q.append([1,0]) #[square,moves]
        visit = set()
        
        while q:
            square, moves = q.popleft()
            # Try all possible moves from 1 to 6
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                # If there's a snake or ladder, move to the destination square
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                # If we reach the last square, return the number of moves
                if nextSquare == length**2:
                    return moves + 1
                # If the square hasn't been visited, add it to the queue
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        
        # If we can't reach the last square, return -1
        return -1