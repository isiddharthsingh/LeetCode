class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates in sorted array allowing at most two occurrences of each element.
        Modifies the array in-place and returns the new length.
        """
        # Initialize two pointers, l (left) and r (right), both starting at the beginning of the array
        l, r = 0, 0 

        # Iterate through the array with the right pointer
        while r < len(nums):
            # Initialize count for the current element
            count = 1
            # Count occurrences of the current element
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1
            
            # Allow at most two occurrences of the current element
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            # Move to the next distinct element
            r += 1
        
        # Return the new length of the array
        return l
