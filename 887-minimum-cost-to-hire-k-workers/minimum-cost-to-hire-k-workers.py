import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Create a list of pairs (ratio, quality) for each worker
        pairs = [(wage[i] / quality[i], quality[i]) for i in range(len(quality))]
        pairs.sort(key=lambda p: p[0])  # Sort by ratio (ascending order)

        maxHeap = []  # Max heap to store negative quality values
        total_quality = 0  # Total quality of selected workers
        res = float("inf")  # Initialize the result

        for rate, q in pairs:
            heapq.heappush(maxHeap, -q)  # Push negative quality to the max heap
            total_quality += q  # Add quality to the total

            if len(maxHeap) > k:
                total_quality += heapq.heappop(maxHeap)  # Remove the largest quality

            if len(maxHeap) == k:
                # Update the result by considering the current rate
                res = min(res, total_quality * rate)

        return res
