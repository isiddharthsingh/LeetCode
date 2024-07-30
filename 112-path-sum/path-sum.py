# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Helper function to perform depth-first search
        def dfs(root, currSum):
            # If the current node is None, return False
            if not root: return False

            # Add the current node's value to the current sum
            currSum += root.val

            # If it's a leaf node, check if the current sum equals the target sum
            if not root.left and not root.right:
                return currSum == targetSum
            
            # Recursively check the left and right subtrees
            return (dfs(root.left, currSum) or dfs(root.right, currSum))
        
        # Start the DFS with the initial sum of 0
        return dfs(root, 0)
