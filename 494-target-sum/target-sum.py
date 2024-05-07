class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # Initialize a dictionary to store results for (i, total) pairs

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0  # Base case: check if the target is reached
            if (i, total) in dp:
                return dp[(i, total)]  # Return the cached result if available

            # Recurse by adding or subtracting the current number
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                              backtrack(i + 1, total - nums[i]))

            return dp[(i, total)]  # Return the computed result

        return backtrack(0, 0)  # Start the recursion from index 0 with total 0
