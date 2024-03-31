# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth, result):
            if not node:
                return
            # If this is the first time we're at this depth, add the node value.
            if depth == len(result):
                result.append(node.val)
            # Prefer right nodes first, then left nodes.
            dfs(node.right, depth + 1, result)
            dfs(node.left, depth + 1, result)

        result = []
        dfs(root, 0, result)
        return result