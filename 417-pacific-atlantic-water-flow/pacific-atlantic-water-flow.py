class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, alt = set(),set()

        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or r < 0 or c < 0 or r==rows or c==cols or heights[r][c] < prevHeight):
                return
            
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        
        for c in range(cols):
            #start from the top row
            dfs(0,c,pac,heights[0][c])
            #start from bottom row
            dfs(rows-1,c,alt, heights[rows-1][c])

        for r in range(rows):
            #start from left row
            dfs(r,0,pac,heights[r][0])
            #start from right row
            dfs(r,cols-1,alt,heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in alt:
                    res.append([r,c])
        return res