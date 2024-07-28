# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # If the inorder or postorder list is empty, return None
        if not inorder or not postorder:
            return None
        
        # The last element of the postorder list is the root of the tree
        root = TreeNode(postorder[-1])
        # Find the index of the root in the inorder list
        mid = inorder.index(postorder[-1])

        # The elements before 'mid' in the inorder list form the left subtree,
        # and those after 'mid' form the right subtree
        # Recursively build the left and right subtrees
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])

        # Return the root of the tree
        return root
