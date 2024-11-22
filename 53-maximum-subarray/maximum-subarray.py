class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize the current sum (currSum) to 0 and the maximum subarray sum (maxSub) to the first element.
        currSum = 0
        maxSub = nums[0]  # Assume the first element is the largest sum initially
        
        # Iterate through each number in the array
        for i in nums:
            # If the current sum is negative, reset it to 0 as it can't contribute to a larger sum
            if currSum < 0:
                currSum = 0
            
            # Add the current number to the running sum
            currSum += i
            
            # Update the maximum subarray sum if the current sum is greater
            maxSub = max(currSum, maxSub)
        
        # Return the maximum subarray sum found
        return maxSub