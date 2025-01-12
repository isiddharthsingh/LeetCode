class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []  # Max-heap for profits
        minCapital = [(c, p) for c, p in zip(capital, profits)]  # Min-heap for capital
        heapq.heapify(minCapital)  # Convert minCapital to a heap
        
        for i in range(k):
            # Push all projects we can afford into the maxProfit heap
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)  # Use negative to simulate max-heap
            
            # If there are no more projects we can afford, stop
            if not maxProfit:
                break
            
            # Execute the project with the maximum profit
            w += -heapq.heappop(maxProfit)
        
        return w