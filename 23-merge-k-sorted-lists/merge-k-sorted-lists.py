# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If the input list is empty or None, return None
        if not lists or len(lists) == 0:
            return None
        
        # Continue merging lists in pairs until only one list remains
        while len(lists) > 1:
            mergedLists = []  # Temporary list to store merged results
            
            # Iterate through the lists in pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]  # First list in the pair
                l2 = lists[i + 1] if (i + 1) < len(lists) else None  # Second list in the pair (if exists)
                # Merge the two lists and append the result to mergedLists
                mergedLists.append(self.mergeList(l1, l2))
            
            # Update lists with the newly merged lists
            lists = mergedLists
        
        # The last remaining list is the fully merged list
        return lists[0]

    def mergeList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode()
        curr = dummy  # Pointer to the current position in the merged list
        
        # Merge the two lists until one of them is fully traversed
        while l1 and l2:
            if l1.val < l2.val:
                # Add the smaller node from l1
                curr.next = l1
                l1 = l1.next
            else:
                # Add the smaller node from l2
                curr.next = l2
                l2 = l2.next
            curr = curr.next  # Move to the next position in the merged list
        
        # If there are remaining nodes in l1, append them
        if l1:
            curr.next = l1
        
        # If there are remaining nodes in l2, append them
        if l2:
            curr.next = l2
        
        # Return the merged list, starting from the node after dummy
        return dummy.next