# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Initialize two pointers, curr and nxt, to the root and its left child, respectively
        curr, nxt = root, root.left if root else None

        # Continue the loop until we have traversed all nodes
        while curr and nxt:
            # Connect the left child of the current node to its right child
            curr.left.next = curr.right
            # If the current node has a next node, connect the right child of the current node to the left child of the next node
            if curr.next:
                curr.right.next = curr.next.left
            
            # Move to the next node in the same level
            curr = curr.next

            # If we have traversed all nodes in the current level, move to the next level
            if not curr:
                curr = nxt
                nxt = curr.left
        
        # Return the root of the tree
        return root
