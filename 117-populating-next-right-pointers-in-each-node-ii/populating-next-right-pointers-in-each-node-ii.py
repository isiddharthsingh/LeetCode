# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        # Node constructor
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # If the root is None, return None
        if not root: return None

        # Start with the root node
        curr_level = root

        # Traverse each level of the tree
        while curr_level:
            # Create a dummy node
            dummy = Node(0)
            # Temp node to keep track of the next node at the current level
            temp = dummy

            # Current node at the current level
            curr = curr_level
            while curr:
                # If the current node has a left child, connect it to the next node
                if curr.left:
                    temp.next = curr.left
                    temp = temp.next
                # If the current node has a right child, connect it to the next node
                if curr.right:
                    temp.next = curr.right
                    temp = temp.next 
                # Move to the next node at the current level
                curr = curr.next

            # Move to the next level
            curr_level=dummy.next
        # Return the root of the tree
        return root 
