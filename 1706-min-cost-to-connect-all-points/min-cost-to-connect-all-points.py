class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)  # Number of points

        # Create an adjacency dictionary where each point is connected to its neighbors
        adj = {i: [] for i in range(N)}

        # Calculate the Manhattan distance between each pair of points and populate the adjacency dictionary
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's Algorithm
        res = 0  # Initialize the result (total cost)
        visit = set()  # Initialize a set to track visited points
        minHeap = [[0, 0]]  # Initialize a min heap with [cost, point]

        while len(visit) < N:
            cost, point = heapq.heappop(minHeap)  # Get the minimum cost edge
            if point in visit:
                continue  # Skip if the point is already visited
            res += cost  # Add the cost to the result
            visit.add(point)  # Mark the point as visited
            for neiCost, nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])  # Add neighboring edges to the heap

        return res  # Return the total minimum cost
