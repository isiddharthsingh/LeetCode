class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all instances of val in nums in-place. The relative order of the elements may be changed.
        Returns the new length of nums after the removal.
        """
        # Pointer for the next position to place a non-val element
        k = 0

        # Iterate over each element in the list
        for i in range(len(nums)):
            if nums[i] != val:
                # If the element is not equal to val, place it at index k and increment k
                nums[k] = nums[i]
                k += 1

        # Return the new length of the array
        return k
