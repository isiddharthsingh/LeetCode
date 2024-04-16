class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap= []
        
        for i in arr:
            heapq.heappush(maxHeap,(-(abs(i-x)),-i))
            #print(maxHeap)

            if len(maxHeap) >k:
                heapq.heappop(maxHeap)

        result= [-i for _, i in maxHeap]
        return sorted(result)