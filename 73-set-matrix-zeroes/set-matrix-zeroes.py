from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowZero = False
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # Determine if the first row needs to be zeroed
        for c in range(COLS):
            if matrix[0][c] == 0:
                rowZero = True
                break

        # Determine if the first column needs to be zeroed
        for r in range(ROWS):
            if matrix[r][0] == 0:
                matrix[0][0] = 0
                break

        # Use the first row and column to mark zeros
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        # Zero out cells based on marks in the first row and column
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Zero out the first column if needed
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Zero out the first row if needed
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

