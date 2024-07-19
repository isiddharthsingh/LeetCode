# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        beforeStart = dummy
        end = head
        i = 0

        while end:
            i += 1
            if i % k == 0:
                start = beforeStart.next
                temp = end.next
                self.reverse(start, end)
                beforeStart.next = end
                start.next = temp
                beforeStart = start
                end = temp
            else:
                end = end.next
        
        return dummy.next

    def reverse(self, start: ListNode, end: ListNode) -> None:
        prev = None
        current = start

        while prev != end:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node