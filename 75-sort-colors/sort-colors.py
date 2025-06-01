class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        curr = 0
        r = len(nums) - 1

        # Loop until current crosses right pointer
        while curr <= r:
            if nums[curr] == 0:
                # If current number is 0, swap it with left pointer
                nums[l], nums[curr] = nums[curr], nums[l]
                l += 1      # Move left pointer forward (0 placed)
                curr += 1   # Move to next element
            elif nums[curr] == 2:
                # If current number is 2, swap it with right pointer
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1      # Move right pointer left (2 placed)
                # Do NOT move curr here because the new number at curr needs checking
            else:
                # If current number is 1, it’s in the right place; just move on
                curr += 1