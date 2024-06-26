class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize the left pointer and the total sum
        l, total = 0, 0
        # Initialize the result to infinity
        result = float("inf")

        # Iterate over the nums list with the right pointer
        for r in range(len(nums)):
            # Add the current number to the total sum
            total += nums[r]
            # While the total sum is greater than or equal to the target
            while total >= target:
                # Update the result with the minimum length of the subarray
                result = min(result, r - l + 1)
                # Subtract the number at the left pointer from the total sum
                total -= nums[l]
                # Move the left pointer to the right
                l += 1

        # If the result is still infinity, return 0
        # Otherwise, return the result
        return 0 if result == float("inf") else result
