class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c, visit, sz):
            R, C = len(grid), len(grid[0])
            if min(r,c)<0 or r==R or c==C or (r,c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r,c))
            count = 1
            count+= dfs(r+1, c, visit, count)
            count+= dfs(r-1, c, visit, count)
            count+= dfs(r, c+1, visit, count)
            count+= dfs(r, c-1, visit, count)
            return count
        visit = set()
        mx = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r,c) not in visit:
                    mx = max(mx, dfs(r, c, visit, 0))
        return mx