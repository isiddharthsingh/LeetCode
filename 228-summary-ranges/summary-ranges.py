class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Initialize an empty list to store the ranges
        ans = []
        # Initialize a pointer to the current number
        i = 0 

        # Iterate over the list of numbers
        while i < len(nums):
            # Remember the start of the current range
            start = nums[i]

            # Keep moving the pointer as long as the next number is consecutive
            while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
                i += 1  # This should be 'i += 1' instead of 'i+1' to actually increment i
            # If the start of the range is different from the current number, we have a range
            if start != nums[i]:
                ans.append(str(start) + "->" + str(nums[i]))
            else:  # If the start of the range is the same as the current number, we have a single number
                ans.append(str(nums[i]))
            i += 1  # This should be 'i += 1' instead of 'i+1' to actually increment i
        # Return the list of ranges
        return ans
