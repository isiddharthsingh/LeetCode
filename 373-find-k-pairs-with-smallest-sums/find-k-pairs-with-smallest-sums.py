import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Result list to store the k smallest pairs
        res = []
        
        # Edge case: If either array is empty or k is zero, return an empty list
        if not nums1 or not nums2 or not k:
            return res
        
        # Min-heap to store pairs along with their sums
        heap = []
        # Set to keep track of visited indices (i, j) to avoid duplicates
        visited = set()
        
        # Start by pushing the pair consisting of the first elements of nums1 and nums2
        # Push tuple (sum, i, j), where sum = nums1[0] + nums2[0], and (i, j) are indices
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))  # Mark this pair as visited
        
        # While we still need to find k pairs and the heap is not empty
        while k > 0 and heap:
            # Pop the smallest sum pair from the heap
            currSum, i, j = heapq.heappop(heap)
            # Add the corresponding pair to the result
            res.append([nums1[i], nums2[j]])
            
            # Check if we can move to the next element in nums1 (increment i)
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                # Push the new pair (nums1[i+1], nums2[j]) into the heap
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))  # Mark as visited
            
            # Check if we can move to the next element in nums2 (increment j)
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                # Push the new pair (nums1[i], nums2[j+1]) into the heap
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))  # Mark as visited
            
            # Decrement k as we've found one of the k pairs
            k -= 1
        
        # Return the result containing the k smallest pairs
        return res