class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the left pointer to the first element
        l = 0

        # Iterate over the array with the right pointer
        for r in range(1, len(nums)):
            # If the current element is different from the previous one,
            # it is a unique element
            if nums[r] != nums[l]:
                l += 1  # Move the left pointer to the next position
                nums[l] = nums[r]  # Update the value at the left pointer

        # Return the new length of the array
        return l + 1