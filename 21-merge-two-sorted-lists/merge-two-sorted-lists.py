# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """if l1 is None:
            return l2
        if l2 is None:
            return l1
    
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2"""
        dummy = ListNode()
        curr = dummy
        # while l1 and l2 are not None
        while l1 and l2:
            # if l1 is less than l2
            if l1.val < l2.val:
                # append l1 to curr
                curr.next = l1
                # move l1 to next
                l1 = l1.next
            else:
                # append l2 to curr
                curr.next = l2
                # move l2 to next
                l2 = l2.next
            # move curr to next
            curr = curr.next

        # if l1 is not None
        if l1:
            # append l1 to curr
            curr.next = l1
        # if l2 is not None
        if l2:
            # append l2 to curr
            curr.next = l2
        # return dummy.next
        return dummy.next

        