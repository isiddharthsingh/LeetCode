# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # Initialize a stack to store the nodes
        self.stack = []
        # Push all the left children of the root onto the stack
        while root:
            self.stack.append(root)
            root = root.left 

    def next(self) -> int:
        # Pop the top node from the stack
        res = self.stack.pop()
        # If the popped node has a right child, push all its left children onto the stack
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        # Return the value of the popped node
        return res.val

    def hasNext(self) -> bool:
        # Return True if there are nodes in the stack, False otherwise
        return self.stack != []

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
