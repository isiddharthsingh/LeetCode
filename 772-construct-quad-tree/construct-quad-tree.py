"""# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val  # Value of the node (0 or 1)
        self.isLeaf = isLeaf  # Boolean indicating if the node is a leaf
        self.topLeft = topLeft  # Top-left child of the node
        self.topRight = topRight  # Top-right child of the node
        self.bottomLeft = bottomLeft  # Bottom-left child of the node
        self.bottomRight = bottomRight  # Bottom-right child of the node"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # Helper function to recursively construct the QuadTree
        def dfs(n, r, c):
            # Check if all elements in the current grid section are the same
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r + i][c + j] != grid[r][c]:  # Compare with the top-left element
                        allSame = False
                        break
                if not allSame:
                    break

            # If all elements are the same, create a leaf node
            if allSame:
                return Node(grid[r][c], True)

            # Otherwise, divide the grid into 4 quadrants and recursively construct the tree
            n = n // 2  # Half the size for the quadrants
            topLeft = dfs(n, r, c)  # Top-left quadrant
            topRight = dfs(n, r, c + n)  # Top-right quadrant
            bottomLeft = dfs(n, r + n, c)  # Bottom-left quadrant
            bottomRight = dfs(n, r + n, c + n)  # Bottom-right quadrant

            # Return a parent node with the 4 quadrants as children
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        # Start the DFS with the entire grid
        return dfs(len(grid), 0, 0)
