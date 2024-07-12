# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node as the head of the result list
        dummy = ListNode()
        # Initialize a pointer to the current node
        curr = dummy 
        # Initialize the carry to 0
        carry = 0

        # Continue the loop until both lists are exhausted and there is no carry
        while l1 or l2 or carry:
            # Get the values of the current nodes, or 0 if the list is exhausted
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 

            # Calculate the new digit and the carry
            val = v1 + v2 + carry 
            carry = val // 10
            val = val % 10
            # Add the new digit to the result list
            curr.next = ListNode(val)

            # Move the pointers to the next nodes
            curr = curr.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the result list, excluding the dummy head
        return dummy.next
