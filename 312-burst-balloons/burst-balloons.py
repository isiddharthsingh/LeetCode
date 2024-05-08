class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Extend the nums list with 1 at both ends
        nums = [1] + nums + [1]
        dp = {}  # Dictionary to store computed results

        def dfs(l, r):
            if l > r:
                return 0  # Base case: no balloons left
            if (l, r) in dp:
                return dp[(l, r)]  # Return precomputed result

            dp[(l, r)] = 0
            for i in range(l, r + 1):
                # Calculate coins obtained by bursting balloon i
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                # Recurse on left and right subproblems
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)  # Update maximum coins

            return dp[(l, r)]  # Return the maximum coins for this subproblem

        # Start the recursion from the first to second-to-last balloon
        return dfs(1, len(nums) - 2)
