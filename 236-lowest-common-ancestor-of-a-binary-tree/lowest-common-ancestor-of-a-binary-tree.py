# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If the root is None, return None
        if not root:
            return None
        
        # If the root is either p or q, then the root is the LCA
        if root == q or root == p:
            return root 
        
        # Recursively find the LCA in the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        # Recursively find the LCA in the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are not None, then root is the LCA
        if left and right:
            return root 
        
        # Otherwise, return the non-None value
        return left if left else right
