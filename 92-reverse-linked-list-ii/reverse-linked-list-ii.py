# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node to act as the prev of the head node of the linked list
        dummy = ListNode(0, head)
        # Initialize two pointers, leftPrev and curr, at the dummy node
        leftPrev, curr = dummy, head
        # Move the two pointers to their respective positions
        for i in range(left - 1):
            leftPrev, curr = curr, curr.next

        # Initialize prev to None
        prev = None
        # Reverse the nodes of the linked list from position left to right
        for i in range(right - left + 1):
            tempNext = curr.next
            curr.next = prev
            prev, curr = curr, tempNext

        # Connect the first part of the linked list
        leftPrev.next.next = curr
        # Connect the last part of the linked list
        leftPrev.next = prev 

        # Return the new head node
        return dummy.next
