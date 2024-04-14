import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            ans = x**2+y**2
            minHeap.append([ans,x,y])

        heapq.heapify(minHeap)
        res  = []

        while k>0:
            ans, x,y = heapq.heappop(minHeap)
            res.append([x,y])
            
            k-=1
        return res