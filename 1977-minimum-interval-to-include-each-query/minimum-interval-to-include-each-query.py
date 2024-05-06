class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()  # Sort intervals based on the start time

        minHeap = []  # Initialize a min heap to track interval lengths
        res, i = {}, 0  # Initialize a dictionary to store results and an index for intervals

        for q in sorted(queries):
            # Add intervals that start before or at the query time to the min heap
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))  # Store interval length and end time
                i += 1

            # Remove intervals from the min heap that end before the query time
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            # Update the result dictionary with the minimum interval length for the query
            res[q] = minHeap[0][0] if minHeap else -1

        # Return the results for all queries
        return [res[q] for q in queries]
