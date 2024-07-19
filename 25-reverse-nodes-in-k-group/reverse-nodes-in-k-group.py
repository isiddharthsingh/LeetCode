# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Function to reverse the nodes from start to end
        def reverse(start: ListNode, end: ListNode) -> None:
            prev = None
            curr = start

            while prev != end:
                tempNext = curr.next
                curr.next = prev
                prev = curr
                curr = tempNext

        # Base cases: if the list is empty or k is 1 (no need to reverse)
        if not head or k == 1:
            return head
        
        # Initialize a dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        beforeStart = dummy  # Pointer to the node before the current k-group
        end = head  # Pointer to traverse the list

        i = 0  # Counter to track nodes processed

        while end:
            i += 1
            # When we reach the end of the k-group
            if i % k == 0:
                start = beforeStart.next  # The first node of the current k-group
                temp = end.next  # Node right after the current k-group
                reverse(start, end)  # Reverse the current k-group
                beforeStart.next = end  # Connect the reversed k-group to the previous part of the list
                start.next = temp  # Connect the end of the reversed k-group to the next part of the list

                beforeStart = start  # Move beforeStart to the end of the reversed k-group
                end = temp  # Move end to the next node to start the next k-group
            else:
                end = end.next  # Move end to the next node if we haven't reached the end of a k-group
        
        # Return the new head of the modified list
        return dummy.next
        
        
        
        
        
        
        """dummy = ListNode(0,head)
        groupPrev = dummy 

        while True:
            kth = self.getKth(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next

            #reverse Group
            prev,curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp 

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp 
        return dummy.next

    
    def getKth(self,curr,k):
        while curr and k > 0:
            curr = curr.next
            k-=1
        return curr"""