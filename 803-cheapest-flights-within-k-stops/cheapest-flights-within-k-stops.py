class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize an array to store minimum prices for each node
        prices = [float("inf")] * n
        prices[src] = 0  # Set the price of the source node to 0

        for i in range(k + 1):
            tmpPrices = prices[:]  # Create a copy of the current prices

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue  # Skip if the source node has not been visited
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p  # Update the minimum price for the destination

            prices = tmpPrices  # Update the prices array

        # Return the minimum price for the destination node (or -1 if unreachable)
        return -1 if prices[dst] == float("inf") else prices[dst]
