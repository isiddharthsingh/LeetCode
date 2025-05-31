class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a 2D DP table with an extra row and column for the base case (empty string)
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # Fill the DP table from bottom-right to top-left
        for i in range(len(text1) - 1, -1, -1):  # Go from second-last row to first
            for j in range(len(text2) - 1, -1, -1):  # Go from second-last column to first
                # If characters match, take 1 + diagonal value (dp[i+1][j+1])
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # If characters don't match, take the max from right or down cell
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # The top-left cell contains the length of the LCS
        return dp[0][0]