from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create an adjacency dictionary
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        # Sort the destinations in reverse lexical order
        for src in adj:
            adj[src].sort(reverse=True)

        res = []  # Initialize the result list

        def dfs(src):
            while adj[src]:
                # Explore the next destination
                next_dest = adj[src].pop()
                dfs(next_dest)
            res.append(src)  # Add the current airport to the result

        dfs("JFK")  # Start the DFS from JFK
        return res[::-1]  # Reverse the result to get the correct order
