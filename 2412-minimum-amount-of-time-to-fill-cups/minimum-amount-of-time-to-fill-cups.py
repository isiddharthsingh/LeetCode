import heapq
from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        if sum(amount) == 0:
            return 0 
        amount = [-a for a in amount]
        heapq.heapify(amount)
        total_time = 0
        while len(amount) > 1:
            first = -heapq.heappop(amount)
            second = -heapq.heappop(amount)
            first -= 1
            second -= 1
            total_time += 1
            if first > 0:
                heapq.heappush(amount, -first)
            if second > 0:
                heapq.heappush(amount, -second)
        print(amount)
        if amount:
            total_time += -amount[0]
        return total_time