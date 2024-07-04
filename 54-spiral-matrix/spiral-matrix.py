class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Initialize an empty list to store the elements in spiral order
        res = []

        # Define the boundaries of the matrix
        left, right = 0, len(matrix[0])  # Horizontal boundaries
        top, bottom = 0, len(matrix)  # Vertical boundaries

        # Continue the loop until the defined boundaries are valid
        while left < right and top < bottom:
            # Traverse from left to right in the topmost row which is not included in the spiral
            for i in range(left, right):
                res.append(matrix[top][i])
            # Move the top boundary one step downwards
            top += 1

            # Traverse from top to bottom in the rightmost column which is not included in the spiral
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            # Move the right boundary one step to the left
            right -= 1

            # If the updated boundaries are invalid, break the loop
            if not (left < right and top < bottom):
                break

            # Traverse from right to left in the bottommost row which is not included in the spiral
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            # Move the bottom boundary one step upwards
            bottom -= 1

            # Traverse from bottom to top in the leftmost column which is not included in the spiral
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            # Move the left boundary one step to the right
            left += 1

        # Return the elements in spiral order
        return res
