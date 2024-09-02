# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize an empty list to store the result
        res = []

        # Initialize a queue for level order traversal (BFS)
        q = collections.deque([root])

        # Continue the loop until there are no more nodes to process
        while q:
            # Get the number of nodes at the current level
            qLen = len(q)
            print(qLen)  # This print statement is for debugging purposes to show the number of nodes at each level

            # Initialize an empty list to store the values of the current level
            level = []

            # Process each node in the current level
            for i in range(qLen):
                node = q.popleft()  # Remove the node from the front of the queue

                if node:  # Check if the node is not None
                    level.append(node.val)  # Append the node's value to the current level list
                    q.append(node.left)     # Add the left child to the queue for the next level
                    q.append(node.right)    # Add the right child to the queue for the next level

            # After processing all nodes in the current level, add the level list to the result
            if level:
                res.append(level)

        # Return the list of levels, where each level is a list of node values
        return res
