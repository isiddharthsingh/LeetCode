class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize the search space
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle index
            if nums[mid] == target:
                # Target found, return its index
                return mid
            elif nums[mid] < target:
                # Target is larger, search in the right half
                left = mid + 1
            else:
                # Target is smaller, search in the left half
                right = mid - 1
        
        # If the target is not found, 'left' will be the insertion position
        return left
