class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Initialize pointers for the binary search on rows
        top, bot = 0, ROWS - 1

        # Binary search to find the potential row that may contain the target
        while top <= bot:
            # Find the middle row
            row = (top + bot) // 2
            
            # If the target is greater than the last element of the current row,
            # the target must be in a row below
            if target > matrix[row][-1]:
                top = row + 1
            
            # If the target is less than the first element of the current row,
            # the target must be in a row above
            elif target < matrix[row][0]:
                bot = row - 1
            
            # The target is within the range of the current row
            else:
                break
        
        # If no valid row was found, return False
        if not (top <= bot): 
            return False

        # Narrow down to the row where the target could be
        row = (top + bot) // 2
        
        # Initialize pointers for the binary search on the columns
        l, r = 0, COLS - 1
        
        # Binary search within the identified row
        while l <= r:
            # Find the middle column
            m = l + (r - l) // 2
            
            # If the target is greater than the middle element, search the right half
            if target > matrix[row][m]:
                l = m + 1
            
            # If the target is less than the middle element, search the left half
            elif target < matrix[row][m]:
                r = m - 1
            
            # If the target matches the middle element, return True
            else:
                return True
        
        # If the target is not found in the matrix, return False
        return False