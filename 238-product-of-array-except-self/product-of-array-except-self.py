class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize a result list with all 1s (same length as nums)
        res = [1] * len(nums)

        # Calculate the prefix product for each element
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix  # Store the prefix product
            prefix *= nums[i]  # Update the prefix product

        # Calculate the postfix product for each element
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix  # Multiply by the postfix product
            postfix *= nums[i]  # Update the postfix product

        return res
