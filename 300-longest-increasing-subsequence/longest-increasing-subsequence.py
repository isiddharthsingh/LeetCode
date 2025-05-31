class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize a list `lis` where lis[i] will store the length of the 
        # longest increasing subsequence starting at index i.
        lis = [1] * len(nums)  # Every element is at least an LIS of length 1 (itself)

        # Iterate the list from right to left (reverse order)
        for i in range(len(nums) - 1, -1, -1):
            # Check all elements to the right of nums[i]
            for j in range(i + 1, len(nums)):
                # If nums[i] is less than nums[j], we can extend the LIS at j
                if nums[i] < nums[j]:
                    # Update the LIS at i as the max of current value or 1 + LIS at j
                    lis[i] = max(lis[i], 1 + lis[j])

        # The result is the maximum value in the LIS array
        return max(lis)