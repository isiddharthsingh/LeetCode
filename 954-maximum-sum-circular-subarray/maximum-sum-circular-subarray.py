class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Initialize variables to store the maximum subarray sum (globalMax),
        # minimum subarray sum (globalMin), current max and min sums (currMax, currMin),
        # and the total sum of the array (total).
        globalMax, globalMin = nums[0], nums[0]  # Start with the first element
        currMax, currMin = 0, 0  # Initialize current max/min subarray sums
        total = 0  # Total sum of all elements in the array

        # Iterate through each number in the array
        for n in nums:
            # Update the total sum of the array
            total += n
            
            # Update the current max subarray sum including the current element
            currMax = max(currMax + n, n)
            
            # Update the current min subarray sum including the current element
            currMin = min(currMin + n, n)
            
            # Update the global max subarray sum
            globalMax = max(globalMax, currMax)
            
            # Update the global min subarray sum
            globalMin = min(globalMin, currMin)
        
        # If all numbers are negative, the maximum circular subarray sum is the largest single element
        if globalMax < 0:
            return globalMax

        # Otherwise, return the maximum of:
        # 1. The maximum subarray sum (globalMax).
        # 2. The maximum circular subarray sum, calculated as (total - globalMin).
        return max(globalMax, total - globalMin)
