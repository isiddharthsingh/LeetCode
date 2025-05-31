# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)

            self.max_dia = max(self.max_dia,left_height+right_height)
            return 1+ max(left_height,right_height)
        height(root)
        return self.max_dia

        """res = [0]

        def dfs(root):
            if not root:
                return -1 
            
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0],2+left+right)

            return 1+max(left,right)
        
        dfs(root)
        return res[0]"""