class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the maximum profit and the starting price
        maxProfit = 0
        start = prices[0]
        
        # Iterate through the prices
        for i in range(0, len(prices)):
            # If the current price is greater than the starting price,
            # update the maximum profit by adding the difference
            if start < prices[i]:
                maxProfit += prices[i] - start
            # Update the starting price
            start = prices[i]
        
        # Return the final maximum profit
        return maxProfit
