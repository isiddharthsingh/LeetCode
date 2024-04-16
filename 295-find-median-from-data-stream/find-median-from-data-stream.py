class MedianFinder:

    def __init__(self):
        #two heaps: large , small = minHeap, maxHeap
        self.small,self.large = [], []        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)

        #make sure the every num in small is <= every num in large
        if (self.small and self.large and
            (-self.small[0]) > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        #uneven size
        if len(self.small) > len(self.large)+1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        
        if len(self.large) > len(self.small)+1:
            val = -heapq.heappop(self.large)
            heapq.heappush(self.small,val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-self.small[0]+self.large[0])/2
        
"""
class MedianFinder:

    def __init__(self):

        #initialize your data structure here.
     
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
"""

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()