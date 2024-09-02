# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize the result list to store the final zigzag level order traversal
        res = []

        # Initialize the queue with the root node if it exists; otherwise, initialize it empty
        q = collections.deque([root] if root else [])

        # Continue processing nodes while the queue is not empty
        while q:
            # Initialize the list to store the current level's node values
            level = []

            # Process all nodes at the current level
            for _ in range(len(q)):
                # Pop the leftmost node from the queue
                node = q.popleft()
                # Append its value to the current level list
                level.append(node.val)
                
                # If the node has a left child, append it to the queue for the next level
                if node.left:
                    q.append(node.left)
                # If the node has a right child, append it to the queue for the next level
                if node.right:
                    q.append(node.right)

            # If the current level index is odd (i.e., the length of res is odd), reverse the level list
            # This is because the zigzag pattern requires reversing every other level
            level = reversed(level) if len(res) % 2 else level

            # Add the processed level to the result list
            res.append(level)

        # Return the final zigzag level order traversal result
        return res
