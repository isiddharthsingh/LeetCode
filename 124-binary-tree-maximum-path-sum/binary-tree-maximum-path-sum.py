class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize res with the smallest possible integer value
        res = [float('-inf')]

        # Helper function to compute max path sum
        def dfs(root):
            if not root:
                return 0
            
            # Compute max path sum for left and right children, ignoring negative sums
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            # Update the result if the current node forms a path with a greater sum
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return the maximum path sum without splitting
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
