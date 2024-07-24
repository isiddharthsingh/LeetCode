# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Initialize two dummy nodes for the left and right partitions
        left, right = ListNode(), ListNode()
        # Initialize two pointers to keep track of the tails of the left and right partitions
        ltail, rtail = left, right

        # Iterate over the linked list
        while head:
            # If the current node's value is less than x, append it to the left partition
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:  # If the current node's value is greater than or equal to x, append it to the right partition
                rtail.next = head
                rtail = rtail.next
            # Move to the next node
            head = head.next

        # Connect the left and right partitions
        ltail.next = right.next
        # Make sure the last node of the right partition points to None
        rtail.next = None

        # Return the head of the partitioned list
        return left.next
