# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # If the tree is empty, return an empty list
        if not root:
            return []

        # Initialize a queue for level order traversal (BFS)
        q = collections.deque([root])
        # Initialize a list to store the average of each level
        res = []

        # Continue the loop until there are no more nodes to process
        while q:
            level_count = 0  # Initialize count of nodes at the current level
            level_sum = 0     # Initialize sum of node values at the current level
            qLen = len(q)     # Number of nodes at the current level

            # Process each node in the current level
            for _ in range(qLen):
                node = q.popleft()  # Remove the node from the front of the queue

                if node:  # Check if the node is not None
                    level_sum += node.val    # Add the node's value to the level sum
                    level_count += 1         # Increment the count of nodes in this level
                    q.append(node.left)      # Add the left child to the queue
                    q.append(node.right)     # Add the right child to the queue

            # After processing all nodes in the level, calculate the average
            if level_count > 0:
                res.append(level_sum / level_count)  # Append the average to the result list

        # Return the list of averages for each level
        return res
