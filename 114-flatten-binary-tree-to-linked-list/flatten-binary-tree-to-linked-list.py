# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Start with the root node
        curr = root 

        # Traverse the tree
        while curr:
            # If the current node has a left child
            if curr.left:
                # Find the rightmost node of the left subtree
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right 

                # Connect the right subtree of the current node to the rightmost node of the left subtree
                predecessor.right = curr.right

                # Move the left subtree to the right
                curr.right = curr.left
                curr.left = None

            # Move to the next node on the right
            curr = curr.right
