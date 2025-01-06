class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap using the first k elements of the array
        heap = nums[:k]
        
        # Convert the list into a valid min-heap
        heapq.heapify(heap)

        # Process the remaining elements in the array
        for num in nums[k:]:
            # If the current element is greater than the smallest element in the heap (heap[0]),
            # remove the smallest element and add the current element to the heap
            if num > heap[0]:
                heapq.heappop(heap)  # Remove the smallest element in the heap
                heapq.heappush(heap, num)  # Add the current element to the heap

        # The root of the heap (heap[0]) now holds the k-th largest element
        return heap[0]
