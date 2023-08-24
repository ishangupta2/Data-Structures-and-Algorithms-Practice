class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        grid = {}
        R, C = len(matrix), len(matrix[0])
        def dfs(r, c, prev):
            if min(r,c)<0 or r==R or c==C or matrix[r][c] <= prev:
                return 0
            if (r,c) in grid:
                return grid[(r,c)]
            res = 1
            res = max(res, 1+ dfs(r, c+1, matrix[r][c]))
            res = max(res, 1+ dfs(r, c-1, matrix[r][c]))
            res = max(res, 1+ dfs(r+1,c, matrix[r][c]))
            res = max(res, 1+ dfs(r-1, c, matrix[r][c]))
            grid[(r,c)] = res
            return res
        mx = 1
        for r in range(R):
            for c in range(C):
                mx = max(mx, dfs(r, c, -1))
        return mx


            