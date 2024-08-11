# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # If the root is None, return 0
        if not root:
            return 0
        
        # Recursively count the nodes in the left and right subtrees and add 1 for the current node
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
