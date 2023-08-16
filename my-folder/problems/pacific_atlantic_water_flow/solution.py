class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl, pac = set(), set()
        arr = []
        R, C = len(heights),len(heights[0])
        def dfs(r, c, visit, m):
            if (r,c) in visit or min(r,c)<0 or r==R or c==C or heights[r][c]<m:
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        for c in range(C):
            dfs(0, c, pac, heights[0][c])
            dfs(R-1, c, atl, heights[R-1][c])
        for r in range(R):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, C-1, atl, heights[r][C-1])
        for r in range(R):
            for c in range(C):
                if (r,c) in pac and (r,c) in atl:
                    arr.append([r,c])
        return arr