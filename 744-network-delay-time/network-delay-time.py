class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create an adjacency dictionary where each node is connected to its neighbors
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]  # Initialize a min heap with (cost, node)
        visit = set()  # Initialize a set to track visited nodes
        t = 0  # Initialize the total time

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue  # Skip if the node is already visited
            visit.add(node)  # Mark the node as visited
            t = max(t, cost)  # Update the total time

            for next_node, next_cost in edges[node]:
                if next_node not in visit:
                    heapq.heappush(minHeap, (cost + next_cost, next_node))  # Add neighboring edges to the heap

        return t if len(visit) == n else -1  # Return the total time or -1 if not all nodes are visited
