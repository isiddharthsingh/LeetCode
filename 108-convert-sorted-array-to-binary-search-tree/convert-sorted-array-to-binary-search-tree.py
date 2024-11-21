# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # Helper function to recursively build the BST
        def helper(l, r):
            # Base case: If the left index exceeds the right, return None
            if l > r:
                return None
            
            # Find the middle element of the current subarray
            mid = (l + r) // 2
            
            # Create a new tree node with the middle element as its value
            root = TreeNode(nums[mid])
            
            # Recursively build the left subtree using the left half of the array
            root.left = helper(l, mid - 1)
            
            # Recursively build the right subtree using the right half of the array
            root.right = helper(mid + 1, r)
            
            # Return the root node of the subtree
            return root
        
        # Call the helper function with the full range of the array
        return helper(0, len(nums) - 1)
