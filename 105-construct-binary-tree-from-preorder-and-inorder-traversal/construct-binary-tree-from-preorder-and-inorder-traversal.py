# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # If the preorder or inorder list is empty, return None
        if not preorder or not inorder: return None

        # The first element of the preorder list is the root of the tree
        root = TreeNode(preorder[0])
        # Find the index of the root in the inorder list
        mid = inorder.index(preorder[0])
        # The elements before 'mid' in the inorder list form the left subtree,
        # and those after 'mid' form the right subtree
        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        # Return the root of the tree
        return root
