# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If the tree is empty, it is symmetric
        if not root:
            return True
        
        # Check if the left and right subtrees are mirror images of each other
        return self.isMirror(root.left, root.right)

    def isMirror(self, root1, root2):
        # If both subtrees are empty, they are mirror images
        if root1 is None and root2 is None:
            return True
        # If only one of the subtrees is empty, they are not mirror images
        if root1 is None or root2 is None:
            return False
        # If the values of the roots are different, the trees are not mirror images
        if root1.val != root2.val:
            return False
        
        # Recursively check if the left subtree of the first tree is a mirror image of the right subtree of the second tree
        # and if the right subtree of the first tree is a mirror image of the left subtree of the second tree
        return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
