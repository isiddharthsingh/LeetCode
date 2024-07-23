# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If the list is empty, return the empty list
        if not head:
            return head
        
        # Initialize the length of the list to 1 and tail to head
        length, tail = 1, head
        # Traverse the list to find the tail and the length of the list
        while tail.next:
            tail = tail.next
            length += 1 

        # Compute the effective number of rotations needed
        k = k % length
        # If no rotation is needed, return the original list
        if k == 0:
            return head
        
        # Initialize curr to head
        curr = head
        # Traverse the list to find the (length-k-1)th node
        for i in range(length - k - 1):
            curr = curr.next
        # The next node is the new head after rotation
        newHead = curr.next
        # Disconnect the current node from the rest of the list
        curr.next = None
        # Connect the tail of the list to the old head
        tail.next = head

        # Return the new head of the list
        return newHead
