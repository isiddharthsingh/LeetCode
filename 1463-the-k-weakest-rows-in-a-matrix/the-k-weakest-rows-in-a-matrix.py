class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        minHeap=[]
        for i,row in enumerate(mat):
            strength = sum(row)
            heapq.heappush(minHeap,(-strength,-i))
            # print (strength)

            if len(minHeap)>k:
                heapq.heappop(minHeap)
            # print (minHeap)

        result = []
        for i in range(len(minHeap)):
            result.append(-heapq.heappop(minHeap)[1])
        result.reverse()
        return result