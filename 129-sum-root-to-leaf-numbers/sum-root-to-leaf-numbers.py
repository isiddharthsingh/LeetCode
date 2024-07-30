# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Helper function to perform depth-first search
        def dfs(curr, num):
            # If the current node is None, return 0
            if not curr: return 0

            # Update the current number by appending the current node's value
            num = num * 10 + curr.val

            # If it's a leaf node, return the current number
            if not curr.left and not curr.right:
                return num

            # Recursively calculate the sum for the left and right subtrees
            return dfs(curr.left, num) + dfs(curr.right, num)
        
        # Start the DFS with the initial number 0
        return dfs(root, 0)
