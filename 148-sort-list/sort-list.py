# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If the list is empty or has only one node, it's already sorted
        if not head or not head.next:
            return head

        # Helper function to split the list into two halves
        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None  # Break the list into two halves
            return head, mid

        # Helper function to merge two sorted linked lists
        def merge(list1, list2):
            dummy = ListNode(0)  # Dummy node to simplify edge cases
            tail = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            tail.next = list1 if list1 else list2  # Append the remaining nodes
            return dummy.next

        # Split the list into two halves
        left, right = split(head)

        # Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)

        # Merge the sorted halves
        return merge(left, right)
