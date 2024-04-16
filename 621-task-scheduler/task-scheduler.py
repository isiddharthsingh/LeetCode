class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0 
        q = deque() #pair of [-cnt,idletime]

        while maxHeap or q:
            time +=1
            if maxHeap:
                cnt = 1+heapq.heappop(maxHeap) #1 beacuse the values are negative
                if cnt:
                    q.append([cnt,time+n])
            
            if q and q[0][1] == time: #if q and q's idle time == time 
                heapq.heappush(maxHeap,q.popleft()[0])#only send the cnt 
        return time