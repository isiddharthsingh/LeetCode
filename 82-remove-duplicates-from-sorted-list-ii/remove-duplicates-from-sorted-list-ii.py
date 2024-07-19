# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node that points to the head of the list.
        # This helps handle edge cases such as when the head node needs to be removed.
        dummy = ListNode(0, head)
        # Initialize a pointer 'curr' to track the last node in the list that is known to not be a duplicate.
        curr = dummy

        # Traverse the linked list.
        while head:
            # If the current node has a duplicate (i.e., the next node has the same value),
            # move head forward until the end of the sequence of duplicates.
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip all duplicates by pointing curr.next to the node after the duplicates.
                curr.next = head.next
            else:
                # If there is no duplicate, just move curr forward to the next node.
                curr = curr.next
            
            # Move head forward to continue the traversal.
            head = head.next
        
        # Return the new head of the modified list (which is the next node of the dummy).
        return dummy.next